# vla-wam-robustness 综述

- 快照日期：2026-11-20
- 引用：论文用简称，元数据见 [papers.md](papers.md)；"P§x" 指 papers.md 的节号，"§x" 指本文的节号。论文内部的章节和表格写在简称后面，例如"FTM Table 3"。
- 数字默认是成功率（%）；"个点"表示绝对差。"未适应"指没有做任何针对漂移的适应或校正。

## 0. 定义与范围

核心问题：VLA 和 WAM 在部署时遇到 setup 漂移会退化多少、为什么退化；在冻结或基本冻结主干的前提下，现有方法在哪个位置、用什么监督来校正。

- **setup 漂移**：部署时以下条件与训练时不同：
  - 相机位姿，包括外部相机和腕部相机的安装位置与朝向；
  - 光照；
  - 桌面、墙面、地面的纹理，以及背景；
  - 模糊、雾和传感器噪声。
  - 相机故障（置黑、冻结）作为传感器一侧的相邻情形列出（Blackout-Freeze）。
- **不在范围内**：策略层面的漂移，即新物体、新任务、新指令、目标物体位置变化。基准论文通常同时测这些维度，本文只在说明基准口径时提到（LIBERO-PRO、INT-ACT、Eva-VLA）。
- **VLA**：以预训练 VLM 为骨干，输入图像与语言，输出动作的策略，例如 π0、π0.5、OpenVLA、GR00T N1（P§6.1）。
- **WAM（world action model）**：联合预测未来观测（视频，或编辑后的图像）与动作，或以视频 / 图像生成模型为骨干的策略，例如 Cosmos Policy、Fast-WAM、ImageWAM、DreamZero（P§6.2）。
- **四个分支**：
  - 鲁棒性基准，以及"为什么不鲁棒"的分析（§2，P§1–3）；
  - FTM 谱系：冻结或少参数的视觉域适应，以锚点论文 FTM 为中心（§3，P§4）；
  - 无标签测试时适应（§4，P§5）；
  - 条件注入结构与干预位置（§5，P§6）。

不包含：

- sim2real 的训练配方，见 [sim-real-cotraining](../sim-real-cotraining/README.md)；
- 训练数据的分布形状与泛化，见 [data-distribution-generalization](../data-distribution-generalization/README.md)。COLOSSEUM、Factor World、Shortcut-OXE、LIBERO-Plus、LIBERO-PRO 在两个方向都有列出，本方向只取其中与视觉 setup 漂移有关的部分。

检索以 arxiv.org 的 abs、HTML 和 listing 页面为主。已知的召回缺口和未核实的元数据见根目录 `issues.md` → ISSUE-007。

## 1. 分类框架

五个正交的轴。

- **轴 1：漂移类型**
  - 外部相机位姿或视角：LIBERO-Plus、RoboTwin 2.0-Plus（WAM-vs-VLA）、FTM 的 S/M/L 三档、AnyCamVLA、Homeward、CoRe-VLA
  - 腕部相机的安装偏移：WARP-VLA
  - 光照：VLATest、VLA-Arena、LIBERO-Plus、WAM-TTT、Juno-TTT、Robotic Steering
  - 纹理与背景：LIBERO-Plus、COLOSSEUM、Factor World
  - 模糊、雾与传感器噪声：LIBERO-Plus、SALT、CRT、StableVLA
  - 相机故障：Blackout-Freeze
  - 组合扰动：COLOSSEUM、RoboTwin 2.0 的 Hard 设置、VLA-Arena 的逐级叠加
- **轴 2：校正的位置**
  - 输入图像：AnyCamVLA、GS-VLA、Homeward、CoRe-VLA、WACO 的图像变形部分、VistaBot、CRT
  - 视觉 token 或编码器：FTM 论文中的 FTM 与 FLA、WARP-VLA、StableVLA、VLA-Retain、Not All Layers
  - 前缀 KV、提示或其他条件接口：TempoFit（前缀 K/V）、T³VF（query tokens）、TTT-VLA 与 VANE（latent prompt）
  - 动作头：SALT（动作专家交叉注意力 key 投影的奇异值尺度）、VLA-ZO（动作专家 LoRA）、COAST（动作专家残差流）、RL²-VLA（速度场合成）、CamVLA（输出相机系动作）
  - 全模型或大块权重：Cross-View AC、SCVC、DART、WACO 的全参微调、Adapt3R 与 GeoAware-VLA 的重训、TT-VLA 的 LoRA
  - 不改参数，只改采样或选择：BID、RTC、VLS、V-GPS、RoboMonkey
- **轴 3：监督**
  - 无标签：SALT、T³VF、VANE、TTT-VLA、WAM-TTT（用无标签的人类视频）、PAD、ILA、MoVie
  - 几何先验：
    - AnyCamVLA 需要测试相机和训练相机的内外参；
    - GS-VLA 需要度量深度和位姿；
    - Homeward 需要训练视角参考图、原相机外参和 URDF；
    - CoRe-VLA 需要 RGB-D 和已知刚体变换；
    - WACO 需要单帧 RGB-D、正运动学和标定包；
    - KYC 需要相机外参。
  - 多视角图像：WARP-VLA（重渲染的腕部视角）、AnyCamVLA 的 LVSM 微调（491 个多视角场景，不含动作）、VISTA、InfiNoVA
  - 新域演示：FTM（每任务 1 条）、DART 与 VLA-ZO（每场景 1 条）、Robotic Steering（每任务 20 条）、Not All Layers（每任务约 20 条）
  - 成对数据：Cross-View AC（338,575 对）、SCVC（583,648 对）、CRT（48,660 对干净 / 腐蚀帧）、GS-VLA（5 万对扰动 / 规范图像）
  - 介于两者之间的弱监督：进度估计器（TT-VLA、EVOLVE-VLA）、回合级结果反馈（PDF）、"已验证成功"的执行（Juno-TTT 阶段 2）
- **轴 4：是否冻结主干**
  - 冻结：FTM 与 FLA、图像侧方法（AnyCamVLA、GS-VLA、Homeward、CoRe-VLA、CRT）、WARP-VLA、SALT、T³VF、TTT-VLA、VANE、PDF、WAM-TTT、TempoFit，以及只改采样的 BID、VLS、V-GPS
  - 不冻结：Cross-View AC、SCVC、DART、一次全参微调基线、WACO、Adapt3R、GeoAware-VLA、TT-VLA
- **轴 5：条件注入形式**（详见 §5）
  - 逐层联合注意力，即动作模块第 l 层读条件模块第 l 层的前缀 KV：π0、π0.5、π0.5+KI、ImageWAM、Fast-WAM、LingBot-VA、Motus、VLAFlow
    - 层映射可配或可学的变体：NEO-VLA、Faster-WAM、DeepVision-VLA
  - 交叉注意力：GR00T N1 / N1.5 / N1.6、SmolVLA、RDT-1B、DP 的 Transformer 版、VLA-Adapter、GE-Act、VPP、mimic-video、DiT4DiT、ABot-M0
  - adaLN 或 FiLM：
    - 注入观测或语言：DP 的 CNN 版、ScaleDP、DexVLA、OpenVLA-OFT 的 OFT+；
    - 注入时间步：π0.5 的 adaptive RMSNorm，以及 GR00T N1、mimic-video、DiT4DiT、Motus、Cosmos Policy、ImageWAM 的动作 DiT。
  - 动作 token 放在 LLM 序列里：OpenVLA、FAST、OpenVLA-OFT（并行解码）
  - 同一扩散序列里联合去噪：Cosmos Policy、DreamZero、UWM、UVA
  - 另外两种：in-context 拼接（Dita、CogACT）；多层特征汇成全局向量（Video Policy）

## 2. 鲁棒性基准与"为什么不鲁棒"（P§1–3）

### 2.1 问题

VLA 在 LIBERO 等标准基准上的成功率接近饱和。这一支回答三件事：这些分数能不能反映对部署条件变化的鲁棒性；扰动维度和幅度怎样定义；退化来自什么机制。

### 2.2 演进

- **2023–2024**：
  - Factor World 按 11 个变化因素给难度排序，真机用 RT-1；
  - COLOSSEUM 设 14 个扰动轴；
  - VLATest 对 RT-1、Octo、OpenVLA 测光照、相机、干扰物和未见物体。
- **2025**：
  - LIBERO-Plus 由 40 个 LIBERO 任务生成 10,030 个任务，覆盖 7 个维度；
  - LIBERO-PRO 用替换物体、位置和指令揭示记忆；
  - RoboTwin 2.0 提供强域随机化的双臂基准；
  - Eva-VLA 加入最坏情况搜索；
  - VLA-Arena 把视觉扰动逐级叠加；
  - INT-ACT 测意图与执行之间的落差。
- **2026**：
  - Colosseum V2；
  - WAM-vs-VLA 自建 RoboTwin 2.0-Plus，专门比较 WAM 与 VLA；
  - 之后的 WAM 论文（ImageWAM、JAM、ZimaBlue、Phoenix、Faster-WAM）大多用 LIBERO-Plus 报告鲁棒性。

### 2.3 设计轴

- **移动哪台相机**：
  - LIBERO-Plus 及其衍生基准的相机维度只移动第三人称相机；
  - RoboTwin 2.0-Plus 的相机扰动只作用于头部相机（WAM-vs-VLA App. A.3）；
  - FTM 只移动 agentview 相机，腕部相机不变；
  - WARP-VLA 单独扰动腕部相机的安装。
- **幅度怎样报告**：
  - 给出物理幅度：
    - LIBERO-Plus：沿光轴把距离拉到 1.01–2.00×，方位角和俯仰角在 15°–75° 的锥内扰动，yaw / pitch / roll 各 2°–10°（App. A.4）；
    - VLATest：每轴旋转 ±5°，平移 0–5 cm；
    - RoboTwin 2.0-Plus：默认启用的是朝向扰动 C3（各轴 0–5°），球面位置扰动 C2（±10°、±10% 距离）默认关闭；
    - COLOSSEUM：前相机 ±0.1、肩部相机 ±0.05，单位没写；
    - VLA-Arena：每轴 U(−0.105, 0.105)，单位没写。
  - 用难度档：LIBERO-Plus 的 L1–L5 按 4 个参考模型中有几个能解出该任务来定档（App. C.3），不是物理幅度。
  - 不给数值：Colosseum V2 正文没有幅度；Eva-VLA 没有给数值范围；FTM 的 S/M/L 原文也没有数值（§3.1）。
- **单维还是组合**：LIBERO-Plus Table 1 是单维扰动；COLOSSEUM 和 RoboTwin 2.0 的 Hard 设置是组合；VLA-Arena 是逐级叠加。
- **随机还是最坏情况**：Eva-VLA 同时报告随机采样和 CMA-ES 最坏情况搜索。
- **有没有真机对照**：Factor World（RT-1）、VLA-Arena（Table 6）、COLOSSEUM（PerAct）、Colosseum V2（仿真与真机的 R²=0.49）。

### 2.4 代表数字

- **LIBERO-Plus Table 1**（原始 → 扰动后）：
  - OpenVLA：76.5 → Camera 1.1 / Robot 4.1 / Light 4.4；
  - OpenVLA-OFT：97.1 → 59.7 / 37.2 / 85.8；只用第三视角的 OFT_w：95.3 → Camera 16.8；
  - π0：94.2 → 15.8 / 6.6 / 79.6；π0-FAST：85.5 → Camera 66.4 / Robot 24.8；
  - UniVLA：95.2 → Camera 4.3；WorldVLA：79.1 → Camera 0.3。
  - Table 2 的总分：OpenVLA 15.6，OpenVLA-OFT 69.6，π0 53.6，π0-FAST 61.6，UniVLA 42.9，WorldVLA 25.0。
- **相机在多数基准中最难，或接近最难**：
  - Factor World 真机：背景 88.9，光照 83.3，干扰物 80.6，桌面纹理 52.8，相机 45.8；Fig. 1 图注原文为 "New camera positions are the hardest"。
  - VLATest：光照变化后保留 61.3% 的原成功案例（Table 4），相机变化后只保留 34.0%（Table 5）；原文称模型对相机外参 "very sensitive"（§5.4）。
  - VLA-Arena（逐级叠加，Table 3）：平均降幅为光照 13.5%、加物体颜色 24.0%、加相机 30.5%、加噪声 50.5%；真机 60.0 → 37.0（加光照）→ 20.0（再加相机）（Table 6）。
  - RoboTwin 2.0-Plus（WAM-vs-VLA Table 3）：相机一列在 5 个模型中的 4 个是最低的；π0.5 的 Robot（27.6）低于它的 Camera（45.6）。
- **反例与例外**：
  - COLOSSEUM：伤害最大的是干扰物数量、目标颜色和光照；3D 模型（RVT、PerAct）对相机位姿鲁棒。
  - Eva-VLA：最坏情况下的 3D 物体变换比光照更致命。π0.5 的失败率（随机 → 最坏）在 3D 变换下是 35.0 → 86.0，在光照下是 5.0 → 12.0。这张表的列对应关系是推断的，见 ISSUE-007。
- **预训练对视觉鲁棒性的帮助**：
  - Colosseum V2：π0.5 在视觉扰动下平均降 7.73% / 9.86%（单臂 / 双臂），ACT 降 28.57% / 29.06%；但 π0.5 对语言改写更敏感，降 19.16% / 24.0%（§V-A、§V-B）。
  - RoboTwin 2.0 Table 5（Easy → Hard）：ACT 29.7 → 1.7，DP3 55.2 → 5.0，π0 46.4 → 16.3。
- **相机故障**（Blackout-Freeze Table 5，顺序为 干净 / 场景置黑 / 腕部置黑 / 场景冻结 / 腕部冻结）：
  - π0.5（有本体感知）：93.1 / 28.9 / 13.1 / 5.8 / 3.6；
  - GR00T N1.7（有本体感知）：98.7 / 51.6 / 12.2 / 9.3 / 0.0。
  - 冻结比置黑更伤。

### 2.5 WAM 与 VLA 的比较

- **WAM-vs-VLA 是本轮唯一专门比较两类模型鲁棒性的研究**：
  - LIBERO-Plus（Table 4，原始 → 总分，括号内为 Camera）：Cosmos Policy 98.5 → 82.2（75.8）；GE-Act 94.4 → 80.3（60.7）；Fast-WAM 97.6 → 51.5（16.4）；π0.5 96.9 → 85.7（75.4）；X-VLA 98.1 → 71.4（23.4）。
  - RoboTwin 2.0-Plus（Table 3，原始 / Camera / 总分）：π0.5 78.4 / 45.6 / 58.6；X-VLA 65.6 / 23.2 / 53.1；MOTUS 87.0 / 21.6 / 71.5；LingBot-VA 92.1 / 28.9 / 74.2；Fast-WAM 91.2 / 30.4 / 72.7。WAM 与带视频生成部分的 MOTUS 总分更高，但 45.6 是 5 个模型中最高的 Camera。
  - 推理时延（Table 5）：π0.5 63 ms，Cosmos Policy 390 ms，MOTUS 1175 ms。
  - 结论原文：视频先验 "necessary but not sufficient"；"camera viewpoint and robot initial-state perturbations remain challenging for WAMs"。π0.5 靠多样数据也能达到相近的鲁棒性。
  - 口径：RoboTwin 2.0-Plus 是作者自建的基准，π0.5 是作者自己微调的（§3.2）。
- **模型族内部的差距大于两族之间的差距**：
  - LIBERO-Plus 总分（括号内为 Camera）：Fast-WAM 51.5（16.4）；Faster-WAM 78.3（Faster-WAM Table 3）；ImageWAM 的 FLUX.2 4B 版 83.1（80.8），9B 版 85.2（79.8）（ImageWAM Table 3、Table 7）；Phoenix 94.8（89.9）、InternW0-Δ 92.8（90.6）、VLA Qwen-RobotManip-Context 91.4（89.9）、π0.5 85.7（75.8）（Phoenix Table 1）。
  - JAM（1,506 任务子集，Table 6）：以 Wan 为骨干的 JAM 为 Camera 25.4、Background 46.2，Fast-WAM 为 Camera 24.2；以 Qwen3.5-2B 或 Ovis-U1 为骨干的 JAM，Camera 为 80.8 / 83.8。作者提醒："the cross-backbone comparison does not isolate the effect of pretraining alone"。
  - ZimaBlue 零样本平均 86.7，但 Camera 只有 58.1；π0.5 为 85.2（78.4）。在 LIBERO-Plus 训练集上 SFT 后，ZimaBlue 的 Camera 升到 95.4（Table 5）。
- **训练数据与模型族同样重要**：
  - 同一个 Fast-WAM，用多样化数据训练时在 RoboTwin 2.0-Plus 上总分 72.7，只用干净 LIBERO 数据训练时在 LIBERO-Plus 上总分 51.5（WAM-vs-VLA §3.3 RQ2）。
  - RoboTwin 2.0 Clean2Random 一列（Phoenix Table 1）：Fast-WAM 1.9，π0 16.3，π0.5 46.0，Phoenix 72.4。Clean2Random 的定义按名称理解为干净数据训练、随机化测试，正文中没有读到确认。
- **clean 到 randomized 的小降幅不等于对部署漂移鲁棒**：Fast-WAM Table 1 的训练数据含 25,000 条强随机化示教；WAM 从 clean 到 randomized 只掉 0.1–1.6 个点，π0 和 π0.5 掉 6–7.5 个点。这测的是训练分布内的随机化，Fast-WAM 论文本身也没有讨论鲁棒性。
- **原论文缺少因子化评测**：
  - DreamZero 在未见环境和物体上测试：AgiBot 未见任务的平均进度为 39.5%，预训练 VLA 为 16.3%（§5.1）；没有分开测相机、光照、背景。
  - Cosmos Policy、GE-Act、UVA 的原论文摘要都没有鲁棒性评测；前两者的数字来自 WAM-vs-VLA。

### 2.6 为什么不鲁棒

- **捷径与记忆**：
  - Shortcut-OXE：子数据集内部多样性低、子数据集之间差异大，都会诱发捷径；原文称策略 "learned to associate the viewpoint with the action"。每个任务配不同视角、视角多样性从 2 增加到 10 时，MiniVLA 的 OOD 成功率降为 0（Fig. 7）；原文 "Diversity does not always help"（§3.3）。
  - LIBERO-PRO：初始位置偏移约 0.2 单位时 OpenVLA 和 π0 就失败，π0.5 能撑到约 0.4（§2.3）；Pos 一栏中 OpenVLA 和 π0 在所有 suite 上都是 0.00；指令换成乱码后轨迹几乎不变。
  - LIBERO-Plus：Finding 5 为 "positional bias rather than genuine semantic understanding"，Finding 8 为 "rely more on fixed vision–action mappings"；OpenVLA-OFT 在 object suite 上去掉指令后成功率 "largely unchanged"（§4.1）。
- **视觉到动作的集中通路**：
  - VLA-Trace：π0.5 "is dominated by a concentrated visual-to-action routing pathway"；遮挡目标物体（替换成背景）后 π0.5 平均降 76.45 个点（Table 4）；生成阶段切断动作对图像的注意力后，LIBERO-10 从 93.5 降到 0.0。
  - INT-ACT：π0 finetune 的意图正确率 84.5，成功率只有 30.4（Table 1）。
- **相机鲁棒性多半是腕部相机带来的**：
  - SCVC §VI-B：Cosmos Policy 在 LIBERO-Plus 的相机扰动任务上，不遮挡时 80.5%，场景相机置黑 66.6%，腕部相机置黑 0.2%（Fig. 3）；作者训练的只用场景相机的对照，ID 93.2 → Camera 26.0（Table I）。原文："Published wrist-enabled camera robustness therefore conflates scene-view invariance with wrist stability"。
  - LIBERO-Plus：带腕部相机的 OpenVLA-OFT 为 59.7，只用第三视角的 OFT_w 为 16.8。
  - Cross-View AC 为排除这条捷径而全程遮蔽腕部相机；CoRe-VLA 报告外部相机移位后策略过度依赖腕部视图。
- **视觉表征错位，动作侧仍可用**：
  - FTM 的诊断是退化来自 "misalignment in Spatial Modeling, rather than Physical Modeling"；
  - Not All Layers 在五个架构上都发现，外观漂移（色调、暗角、对比度、去饱和、噪声）的适应代价集中在视觉编码器（Fig. 4）。
- **注意力分配错了，至多是部分原因**：Blackout-Freeze 把注意力重加权到本体感知，成功率只从 22.0% 提到 26.7%，而训练过的参考策略是 94.7%（§4.1）；原文："increasing attention to proprioception does not recover performance"。

### 2.7 局限

- **"幅度—成功率"关系的直接证据有限**：
  - VLATest：光照强度超过 8× 时约剩 40% 的成功案例，α<0.2 时约 60%，增强比减弱更伤；
  - Eva-VLA：把最坏扰动的分布放大 10 倍后，失败率反而从 98% 降到 18%，失败集中在特定构型，不是"幅度越大越坏"；
  - LIBERO-Plus 的 L1–L5 不是幅度（§2.3）。
- **数字照搬与口径不一**：不少 WAM 论文直接照搬 LIBERO-Plus 原表里的 VLA 数字（ImageWAM Table 3、JAM）；不同论文对同一模型报告的数字差别很大（§6 第 1 条）。
- **评测基础设施的缺口**：INT-ACT 因 SimplerEnv 的绿幕合成没有覆盖光照和相机。
- **综述层面**：两篇 WAM 综述都没有引用 WAM 与 VLA 的鲁棒性正面对比（§8）。

## 3. FTM 谱系：冻结或少参数的视觉域适应（P§4）

下文"FTM"既指锚点论文，也指其中的逐通道仿射方法；"FLA"指同一篇论文里的 ViT LoRA 方法。

### 3.1 锚点：FTM 与 FLA

精读笔记见 [notes/2025-ftm.md](notes/2025-ftm.md)。

- **论点**：把 VLA 分成 Spatial Modeling（视觉编码器）和 Physical Modeling（VLM 加动作专家）两部分；视角漂移主要扭曲视觉嵌入，动作侧仍然可用，所以只做视觉侧适应就够了。
- **方法**：
  - FTM：F̂ = (1+γ)⊙F + β，γ、β ∈ R^2048 是不随输入变化的全局参数，共约 4K 参数，主干全部冻结；
  - FLA：在 SigLIP ViT 的线性层上加 LoRA，rank 16 时为 4.7M 参数，语言模型和动作专家冻结。
- **评测口径**：
  - LIBERO 四个套件，新视角下每个任务测 50 次；只移动第三人称 agentview 相机，腕部相机不变。
  - S/M/L 三档：原文只写"固定平移 Δp 加特定四元数旋转"，沿用 Adapt3R，没有给数值。
  - **推断**：各档幅度就是 Adapt3R App. C.1 的平移偏移（Small (0.0, +0.3, −0.1) m 到 Large (−1.2, +1.0, −0.2) m）加上 DART Table 12 的旋转角（Small 18.5–33.2°，Medium 45.1–69.7°，Large 106.9–126.6°）。依据是 DART 在这套协议下复现 FLA 得到 91.6，锚点报告 90.8（DART Table 10）。
  - "一次演示"指每个任务一条新域演示（LIBERO 共 40 条），适应后在同一批任务上测试。
- **代表数字**（FTM Table 1、3、4）：
  - π0.5 零样本 48.5 → FTM 87.1 / FLA 90.8；整模 LoRA（约 467M 参数）90.3；
  - 提示学习基线（0.131M 参数）在 Libero-V 上的平均为 75.1；
  - Libero-V 中，π0.5 零样本在光照、纹理、噪声子集上已经有 96.2 / 96.0 / 93.5，FTM 之后是 96.0 / 96.0 / 93.6。
- **局限**：
  - 论文没有局限一节；真机只有定性结果；
  - Table 3 中 FTM 一行写的平均（90.5）与四列均值（约 93.2）对不上，见 ISSUE-007。

### 3.2 改视觉 token 或编码器的少参数适应

- **问题**：只改视觉侧，用很少的参数恢复视角或外观漂移下的性能。
- **演进**：
  - FTM / FLA：逐通道仿射、ViT LoRA；
  - WARP-VLA：在编码器和策略之间加 MoE 特征变换，面向腕部相机；
  - StableVLA：训练期在视觉到 LLM 的投影处加信息瓶颈适配器；
  - 诊断与评测类工作：Not All Layers、VLA-Retain；
  - 免训练的视觉 token 剪枝加注意力偏置：T3R（仅核实摘要）。
- **设计轴**：改哪一层（投影后的 token、ViT 权重、connector）；参数量（4K、4.7M、不到 10M）；监督（新域演示、多视角重渲染、不用额外数据）。
- **代表数字**：
  - WARP-VLA（Table I）：腕部相机 S/M/L 为 2 cm 3° / 4 cm 6° / 6 cm 9°；π0.5 39.2 → 78.3（Large 6.1 → 58.8），同表 AnyCamVLA 72.3、KYC 62.3；真机 36.7 → 48.7。
  - StableVLA（Table 1）：ImageNet-C 类腐蚀、Long 套件、严重度 5，VLA-Adapter 26.2 → 45.3，同表 OpenPI-0.5 为 47.7。
  - Not All Layers（Table IV）：组合漂移下，OpenVLA-OFT 预算 16M 时为 73.4，均匀分配的 LoRA 为 62.4。
  - VLA-Retain（Table 3）：在 LIBERO-Plus 相机或噪声子集上调视觉骨干与 connector，10 个配置中 8 个的"非目标扰动维度平均增益"为负；X-VLA 做相机调优后，目标维度 +69.4，非目标维度 −4.6。
  - 提示学习：VLA 上唯一的数据点是 FTM Table 4 的提示学习基线（0.131M 参数，75.1）。CAPO 的提示池用在 CLIP 加 RL 的策略上，不是 VLA。
- **局限**：
  - FLA 的优势依赖"每任务一条、测同一批任务"的协议：DART 改成每场景一条（共 5 条）、测 40 个任务后，FLA 为 74.3（§3.5）。
  - VLA-ZO 在同样的 S/M/L、5 条演示下，动作侧适应（58.2）略好于视觉侧（56.6）（Fig. 2b），与"漂移主要发生在视觉表征"不完全一致。
  - FTM 与 FLA 没有报告跨维度的副作用，而 VLA-Retain 显示视觉调优会让其他扰动维度变差。

### 3.3 在图像一侧变回训练视角，或复原画面

- **问题**：策略完全冻结、不用演示，在输入端把测试画面变回训练视角，或者把腐蚀的画面复原。
- **演进**：
  - 生成式新视角合成：AnyCamVLA（171M 的 LVSM，前馈重渲染）、VistaBot（4D 几何加视频扩散视角合成的潜变量）；
  - 显式 3D：GS-VLA（4.05M 参数的 U-Net 预测逐像素 3D 高斯）、CoRe-VLA（RGB-D 点云渲染加 NAFNet 修补，另加推理端动作块对齐 ETCA）；
  - 估计几何加运动学渲染：Homeward（场景用 VGGT 估计，机械臂按 URDF 和关节角渲染）；
  - 以机械臂为标定靶：WACO（按估计的位移变形第三人称图像，并规范化状态与动作坐标系；π0.5 需要全参微调）；
  - 腐蚀复原：CRT（Transformer 复原网络，用 48,660 对干净 / 腐蚀帧训练）。
- **设计轴**：需要哪些几何输入；要不要训练额外的网络；延迟；怎样处理腕部视图（CoRe-VLA 恢复外部视角后让腕部与外部视图重新协调）。
- **代表数字**：
  - AnyCamVLA（Table I，自定义 S/M/L，最大 15 cm、60°）：π0.5 69.9 → 94.5，OpenVLA-OFT 62.1 → 85.6；视角增广微调的 π0.5* 为 87.2，GeoAware-VLA 为 86.1；两个视角约 36.55 ms。腕部相机扰动下 Long 套件 28.6 → 88.6（Table II）。
  - GS-VLA（Table 1b，εt = 100 cm）：π0.5 spatial 42.6 → 86.8，libero_10 9.3 → 72.1；XVLA 1.4 → 81.0（Table 1a）。
  - Homeward（Table 3，LIBERO-Plus 相机维度，1,599 个变体）：π0.5 76.5 → 95.1，π0 68.0 → 91.2，OpenVLA-OFT 62.5 → 77.6；用真值参数的 AnyCamVLA 在 π0.5 上为 85.1（Table 5）；约 0.21 s / 查询。
  - CoRe-VLA：真机外部相机位移 1.6 m，π0.5 13.3 → 83.3（Table 2）；LIBERO 上 0.9 m，13.8 → 71.5；LIBERO-Plus 相机维度 72.0 → 89.1（Table 3）；延迟 244 → 478 ms。
  - WACO：LIBERO-PoseShift L1–L3（相机 ≤2 / 5 / 10 cm、±3 / 5 / 10°，基座 yaw ±3 / 8 / 15°）74.0 → 87.2，真值 oracle 88.7（Table VI）；LIBERO-Plus 相机维度 62.5 → 93.7（Table VII，含微调）；UR5e 43.3 → 80.0（Table IX）。
  - CRT（Table II，LIBERO-10，π0.5 干净时 90%）：横线 0.5 时 2% → 87%，水滴 68% → 87%，高斯噪声 87% → 79%（反而下降）；SmolVLA 的干净性能 43 → 33。
- **局限**：
  - 几何估计不准时会崩：GS-VLA 换成 DepthAnything V2 估计的深度后，从 86.8 降到 44.5（Table 16）；Homeward 只用 VGGT 恢复、不加机器人渲染层时为 72.8，低于不校正的 79.7（Table 2）。
  - 大视角下新暴露的区域无法恢复（GS-VLA §6、AnyCamVLA §V、CoRe-VLA §6）。
  - 策略已经掌握该视角时，启用校正反而有害：Homeward 在 OFT+ 上把成功率从 95.7 降到 91.1（Table 6）。
  - 本轮没有找到在同一协议下比较图像侧方法与 FTM 的论文：WACO 和 Homeward 只在相关工作里提到 FTM / FLA，DART 和 VLA-ZO 比较的是 FLA，而且换了协议。

### 3.4 训练时让策略对相机鲁棒

- **问题**：在训练阶段就让策略对相机变化不敏感。这些方法都要动策略的训练，可以当作冻结方法的上界参照。
- **四条路线**：
  1. 换成 3D 或几何骨干：Adapt3R（标定 RGB-D 点云加 2D 语义特征）、GeoAware-VLA（冻结 VGGT 加可训练投影）。两者都只在 BAKU、VQ-BeT 等非 VLA 策略上验证过，需要重训。
  2. 成对视角加一致性约束：Cross-View AC 约束两个视角下的动作流速度场一致；SCVC 在 Cosmos Policy 上只对动作、未来本体状态、价值这些视角不变的块加一致性。
  3. 显式提供相机信息，或输出相机系动作：KYC（Plücker 射线图）、CamVLA（输出相机系动作和手眼矩阵）、OVOA-VLA、PAIR、VersaCamVLA。
  4. 数据增广：VISTA（单图新视角合成）、InfiNoVA（4D 高斯渲染）、RageVLA。
  - 另有两篇只核实了摘要：View Collapse 研究多视角 VLA 的对抗训练与视角坍缩，LIT 在训练时打破视觉到动作的捷径。
- **代表数字**：
  - Adapt3R（Table 9）：LIBERO-90 换相机 S/M/L，BAKU+Adapt3R 为 0.847 / 0.829 / 0.829，BAKU+RGB 为 0.141 / 0.061 / 0.043；真机未见视角 79.4，RGB 为 27.8（Table 11）。
  - GeoAware-VLA（Table I）：三个未见视角的均值，GeoAware BAKU 82.6、GeoAware VQ-BeT 77.9；原版 BAKU 37.9、VQ-BeT 41.4，OpenVLA-OFT 50.2。
  - Cross-View AC（Table 1）：LIBERO-Plus 相机维度 87.2±0.4；用同样的数据但只训流匹配损失为 79.8，混合相机 SFT 为 74.7，只用名义数据为 16.8，打乱配对为 25.8；真机未见相机 53.3 → 74.4（Table 7）。
  - SCVC（Table II，seed 1）：方位外推 63.8 → 76.0，仰角外推 54.9 → 63.7，方位内插 86.3 → 85.1，ID 92.3 → 91.7；对未来画面加一致性约束有害（收缩到 1/(1+4λ)）。
  - KYC（Table I）：随机场景的 Lift 任务上 SmolVLA 19.6 → 54.4。
  - CamVLA：RLBench 未见视角 π0 33.2 → 51.4；真机 15° 下 16.0 → 29.3。
  - 上界参照：用 2 万条扰动轨迹训练的 OpenVLA-OFT+ 在 LIBERO-Plus 相机维度上为 92.8（WACO Table VII）；ZimaBlue 在 LIBERO-Plus 训练集上 SFT 后 Camera 为 95.4。
- **局限**：
  - 配对数据难获得：Cross-View AC 需要动作等价的视角对（§5、App. I）；SCVC 指出同一状态下的视角对在真机上难采集，WAM 上也没有真机证据。
  - 配对是否动作等价是关键：Cross-View AC 打乱配对后只剩 25.8。
  - Cross-View AC 只在流匹配动作头上验证；SCVC 只扰动场景相机（§VIII）。

### 3.5 少样本或一次演示适应

- **问题**：用一条或少量新域演示做适应。
- **代表方法**：
  - DART：域向量 = 目标域增量 − 源域增量，经 SVD 子空间过滤和缩放后加回；每个场景 1 条新域演示（LIBERO 共 5 条），加源域同任务 1 条。
  - VLA-ZO：只用前向传播的零阶优化，更新动作专家的 q/v LoRA（约 1.25M 参数）。
  - Robotic Steering：按可解释性选出 20 个 LLM 注意力头做 LoRA，每个任务 20 条演示。
  - Not All Layers：先用 10 张无标注目标观测诊断，再按区域分配 LoRA rank；每个任务约 20 条演示。
  - RAGu：检索 DROID 演示并做几何标定（仅核实摘要）。
- **代表数字**：
  - DART Table 1（π0.5，LIBERO S/M/L）：零样本 54.5，一次全参微调 31.5，RETAIN 69.6，FLA 74.3（Large 54.3），DART 79.1；UR10e 真机 43.3 → 81.7，FLA 为 55.0（Table 5）。
  - VLA-ZO（同一套 S/M/L）：48.27 → 58.17（q=16）/ 63.58（q=64）；用零阶优化重实现的 FLA 为 56.56。
  - Robotic Steering（Table 2）：光照漂移下，普通 LoRA 25%，选头 LoRA 47.5%；没有测相机漂移。
- **协议差异**：FTM 里一次 LoRA 是 90.3，DART 里一次全参微调是 31.5。两者的协议差在两点：演示覆盖每个任务还是每个场景；测试任务在适应时有没有见过。
- **局限**：
  - Large 视角（旋转超过 100°）下，所有一次演示方法都明显退化（DART §7）。
  - DART 的缩放系数 α 需要小范围搜索。
  - Not All Layers 指出，源域 Fisher 在域差大时会估错。

### 3.6 跨论文口径：π0.5 在相机漂移下的未适应成功率

- **LIBERO 四套件，Adapt3R 式 S/M/L，双相机**：48.5（FTM Table 3）；54.5（DART Table 1，S/M/L 为 88.3 / 63.9 / 11.3）；48.27（VLA-ZO Table 1）。
- **AnyCamVLA 自定义 S/M/L（≤15 cm、≤60°）**：69.9（92.4 / 72.2 / 45.0）。
- **GS-VLA，εt = 100 cm**：spatial 42.6，libero_10 9.3。
- **LIBERO-Plus 相机维度**：62.5（WACO Table VII，公开权重）、72.0（CoRe-VLA Table 3）、75.4（WAM-vs-VLA Table 4）、75.8（Phoenix Table 1）、76.5（Homeward Table 3）、78.4（ZimaBlue Table 5）。遮蔽腕部、只用名义数据微调时为 16.8（Cross-View AC Table 1）。
- **LIBERO 腕部相机扰动 S/M/L（2–6 cm、3–9°）**：39.2（WARP-VLA Table I）。
- WACO 指出，LIBERO-Plus 发布的协议会把扰动变体的参数泄漏进提示词（§IV-A）。这是否解释了同一维度上数字的分散，原文没有检验。

## 4. 无标签测试时适应（P§5）

### 4.1 问题

部署时没有动作标签，也没有奖励，只用策略自己能拿到的信号在线校正，例如自监督辅助任务、未来观测、动作块的时间一致性、特征统计量。本节重点是冻结或基本冻结的策略，以及视觉 setup 漂移。

### 4.2 视觉控制策略上的经典 TTA

- **PAD**：
  - 训练时编码器同时服务 RL 头和逆动力学自监督头；部署时只保留自监督损失，在线更新共享的卷积编码器。
  - 随机颜色下 Walker-walk 406 → 468（Table 1）；真机 Push(cloth) 64% → 88%（Table 5）；摘要称 36 个环境中 31 个有提升。
  - 辅助任务必须与控制相关：旋转预测不如逆动力学（Sec. 4.2）。
- **ILA**：
  - 在潜空间做对抗式分布对齐，加冻结的前向 / 逆动力学一致性约束，只更新编码器。
  - DrQ-v2（Table II）：背景 228 → 602，颜色 234 → 536，相机位姿 345 → 417。
  - 相机位姿下（Table III）：零样本 319，PAD 326，ILA 412；真机 reach 15% → 约 90%。
- **MoVie**：
  - 在编码器前两层卷积前插入 STN，以冻结潜动力学模型的预测损失为信号，适应相机变化。
  - Table 1：DMC 492.71 → 656.43，xArm 28 → 52，Adroit 21 → 53；只有仿真。
- **TEMPO**：
  - 用冻结的分布式 critic 的 Q 值作为无奖励的性能代理，更新 actor。
  - 只测了运动控制下的地形与负载，没有视觉漂移；真机 Go2 小腿负载 89.8 → 98.7（Table 1）。
- **共同前提**：策略里有一个干净可分的"编码器加头"，在线数据较多（几十个回合或上千步）。ILA 中相机位姿的增益明显小于背景和颜色。

### 4.3 VLA 上的无标签测试时训练

- **演进**：这一类集中出现在 2026 年，主流做法是把可更新的部分压到很小：
  - 奇异值尺度：SALT（SmolVLA 2,560 个，GR00T N1.7 24,576 个）；
  - query tokens：T³VF；
  - latent prompt：TTT-VLA，以及 VANE（形状 [8,16,1024]，约 13.1 万个标量）；
  - 更大的更新：Juno-TTT（世界模型全参数，加 LoRA 与动作头）、TT-VLA（LoRA）。
- **信号**：
  - 自己生成的动作目标：SALT 把上一个动作块中还没执行的剩余段当作时间对齐的目标，代入掩码 flow-matching 损失；门控统计量是相邻两次重规划之间接口 token 的余弦变化。
  - 未来视觉预测：
    - T³VF 用预测的未来图像对比 n=4 步之后的真实观测，并只在 K=5 次动作采样的方差低于近期分位数时更新；
    - VANE 预测冻结 V-JEPA 2 对 k=8 步之后观测的表征；更新先在影子副本上做，未来 4 对证据中至少 3 对支持才提交，否则回滚。
  - 部署时可以拿到的状态：TTT-VLA 用流匹配预测末端位置和夹爪状态。
  - 学到的进度或置信度，属于弱监督：TT-VLA（VLAC 进度估计器作为稠密奖励）、EVOLVE-VLA、T²VLA；PDF 另外需要回合级结果反馈；Juno-TTT 阶段 2 需要"已验证成功"的执行，验证方式文中没写。
- **代表数字**：
  - SALT（LIBERO-10，五种腐蚀、严重度 5 的平均，Table 1）：
    - SmolVLA 43.9 → 53.2，同表 ActMAD 44.5、BID 46.0、self-training 42.9；
    - GR00T N1.7 58.7 → 66.0，同表 ActMAD 60.4、BID 63.1；
    - 对最强基线 BID 分别领先 7.2 和 2.9 个点；
    - 真机 task progress：数字扰动 0.46 → 0.61，物理扰动 0.51 → 0.62；
    - 每次重规划 134.8 ms，带更新时 559.3 ms（Table 9）。
  - T³VF（Table 1）：
    - 在 LIBERO-Plus 上微调过的模型（w/ Perturbed Train）：平均 49.3 → 52.1，Camera 50.5 → 55.3，Light 67.8 → 72.4；
    - 没有在扰动数据上训练的模型（w/o Perturbed Train）：平均 39.8 → 40.3，Camera 39.2 → 41.5，Light 62.5 → 62.3；
    - 开销约 1.3×（Fig. 3）。
  - TTT-VLA（WidowX，Table 2）：π0.5 从 51.1 到 63.5，来自训练时加入的潜提示和状态定位代理任务（SG-LP）；63.5 → 67.4 才是测试时训练这一步的增量。Google Robot（Table 3）：VM 68.9 → 72.4，VA 58.6 → 60.1。800 对 episode 中，145 个由失败变成功，114 个由成功变失败（Table 7）。
  - VANE：WidowX 上同条件的 TTT 基线 68.0 → VANE 71.2，不做 TTT 时为 70.7，TTT-VLA 为 67.4（Table 3、6）；Google Robot 三个任务 73.6 → 72.4，反而下降（Table 4）。
  - Juno-TTT：真机噪声 40% → 65%（8/20 → 13/20），光照 55% → 70%；SimplerEnv 68.5 → 72.7。
  - TT-VLA（Table 1 总平均）：Nora 29.92 → 33.75，OpenVLA 39.83 → 41.93。
  - PDF（Table 1）：LIBERO 平均 0.77，OpenVLA 复现值 0.69、报告值 0.75。
- **稳定性**：
  - TTT-VLA 的逐 episode 在线更新（batch 1）不稳定；
  - VANE 为此引入影子副本和回滚；
  - T³VF 用多样本方差决定何时更新；
  - SALT 用门控决定何时启动适应。
- **局限**：
  - SALT 没有测相机位姿漂移。漂移从第一次重规划就存在时，它几乎无效（App. I；SmolVLA 32.5 对 32.9，这组数字没有逐字核对，见 ISSUE-007）。改变任务本身的扰动、渐变式的漂移，它也处理不了（App. J）。
  - TTT-VLA 的代理专家在测试时也要用；训练时同时优化动作目标与代理目标；只在仿真里测（Limitations）。
  - T³VF 只测了一个模型（Mantis，先预测未来图像再出动作），只在仿真。
  - 这些工作都没有拿 TENT、LN 仿射或 BN-adapt 这类经典基线做数值对比；SALT、T³VF、TTT-VLA、PDF 只是引用了 TENT。
  - Dune 的损失里用到目标动作，来源没写，无法确认是否无标签；它在 LIBERO 上的均值 61.4 低于 AdamW 的 78.3（Table 1），零阶优化比 Adam 慢数倍（Sec. 6）。

### 4.4 冻结策略的推理期引导与选择

- 这一类不改权重，代价转到推理计算和外部打分器上：
  - VLS：VLM 写出的可微奖励在每个去噪步做梯度引导，加 RBF 斥力和 Feynman–Kac 重采样；LIBERO-PRO 上 π0.5 23.69 → 36.81（Table I）。
  - V-GPS：离线 RL 训练的 Q 函数给 K 个候选动作重排；真机 Octo-small-1.5 0.24 → 0.44（Table 1）；K=50 时推理慢 1.59×。
  - RoboMonkey：采样、加扰动、投票，再由 VLM 验证器挑动作；摘要称 OOD 上绝对提升 25%。
  - TACO：用伪计数验证动作块。
  - Retrieve-then-Steer：把环境验证过的成功片段存入记忆，按状态检索后注入采样的中间状态。
  - Infer-Diagnose-Refine：比较真实视觉输入与零填充视觉输入下的动作差，做门控残差融合。
  - ShadowVLA：用规范场景下的成功 rollout 做参考，经 RGB-D 配准做分段刚体映射；LIBERO-Goal 3/59 → 51/59，针对的是物体位移。
- **局限**：这些方法针对的多是物体、位置和语义偏移，基本没有测相机或光照这类 setup 漂移。

### 4.5 WAM 与世界模型

- 世界模型自带一个无标签信号：预测的未来与实际看到的未来之差。
- **WAM-TTT**：
  - WAM（LDA-1B）冻结，只更新视频侧的 TTT 快权重；信号是无标签人类视频上的视频预测损失，加 KV 记忆重建。
  - 新家庭场景中光照、桌高、物体同时变化，9 个任务的平均进度 32.5 → 46.2，WAM-ICL 为 7.1（Table 1）。
  - Deliver Drink 任务：光照扰动 54.0 → 66.0，空间扰动 28.0 → 56.0（Sec. 4.4）。
  - 需要目标域的人类视频，还要事先用成对的人-机数据做元训练。
- **T2-z**：冻结世界模型，只优化环境潜变量，对应摩擦、质量、人定规则等不可观测因素；摘要报告动作成功率 33.73% → 72.96%。
- **Self-Correcting Planning**：冻结的潜世界模型，用反向预测残差中可由偏移解释的部分诊断执行器偏移；摘要报告 PushT 0.650 → 0.862。
- **WorldAgen**：测试时用探索动作采集真实转移，轻量更新世界模型（只读了 listing 摘要）。
- T³VF 和 Juno-TTT 用的也是这类信号（§4.3）。这些工作都没有测相机位姿漂移。

### 4.6 扩散与流匹配策略特有的信号

- **动作块的重叠段**：
  - BID：候选块与上一块在重叠段上的 L2 距离（后向一致性），加上与强、弱 checkpoint 的对比，从 16 个样本中选一个；7 个仿真任务相对提升约 32%，加 EMA 后约 46%；VQ-BeT 在 Push-T 各噪声下的平均 38.9 → 43.8（Table 4）；推理时间约 2×。
  - RTC：冻结一定会执行的前 d 步，其余部分用引导做 inpainting；延迟 π0.5 76 ms，RTC 97 ms，BID（N=16）223 ms（App. A.3）。
  - Sentinel：相邻两次推理在重叠段上动作分布的 MMD 或 KL 作为 OOD 监测量，阈值用成功 rollout 做保形校准；Close Box 上 STAC-MMD 的 TPR 100%、TNR 94%（Table 1）。
  - Self-GAD 把 BID 的一致性改成每个去噪步上的引导。
  - SALT 把重叠段当作梯度更新的目标（§4.3）。
- **去噪过程的不确定度**：
  - DVAC：最后几个去噪步中干净动作估计的方差，只执行低方差的前缀；摘要报告 LIBERO 94.75 → 98.00，重规划次数减少 43.0%。
  - GeCO：优化后动作处的场范数，作为免训练的 OOD 检测器。
  - τ0-WM：按重去噪一致性给候选动作排序。
  - FAIL-Detect：只用成功示范学到的不确定度，配合保形预测。
  - T³VF 用 K 次采样的方差决定何时更新。
- **去噪误差作为监督**：Diffusion-TTA 以判别模型的输出为条件计算去噪误差，再反传给判别模型；ImageNet-C 高斯噪声的在线设置下，ConvNext-Tiny 16.4 → 47.4，TENT 只有 2.7（Table 2）。本轮没有找到把它用在策略上的实例。

### 4.7 通用 TTA 代表作

- **归一化统计与仿射**：
  - BN-adapt 只替换 BN 统计：ResNet-50 的 mCE 76.7 → 62.2；
  - TENT 用熵最小化更新 BN 统计和通道仿射：ImageNet-C 误差 source 59.5% / BN 49.9% / Tent 44.0%。
- **Transformer 与 LN**：
  - SAR：BN 是 TTA 不稳定的主因；GN / LN 模型更稳定，但熵最小化仍会塌缩成单一类别；做法是只更新归一化层的仿射参数，ViT-LN 冻结 blocks 9–11。
  - CFA：在 ViT 上按类条件和整体两个层面对齐隐藏表征的分布；比较了 LN、CLS token、特征提取器、全部参数四种更新对象，称损失合适时不必限制可调参数。
  - FOA：只用前向传播，用 CMA-ES 优化新增的输入 prompt，并做激活平移；8-bit ViT 上优于 32-bit 的 TENT。
- **自监督辅助任务**：TTT（旋转预测）；TTT-MAE（MAE 重建，冻不冻解码器差别可以忽略）。
- **多视图一致性与提示**：MEMO（多个增广上的边际熵，单个测试点即可）；TPT（CLIP 的文本 prompt，零样本 top-1 平均 +3.6%）；TDA（KV 缓存加正负伪标签，不反传）。
- **特征统计对齐**：ActMAD 对齐多层逐特征的激活统计，摘要报告 KITTI-Fog 检测 +15.4%；在 SALT 中作为 VLA 基线时只有 43.9 → 44.5（SmolVLA）和 58.7 → 60.4（GR00T N1.7）。

### 4.8 信号与更新对象的对应

- **自监督辅助任务**：TTT（共享特征提取器）、PAD 与 TTT-MAE（编码器）、TTT-VLA（latent prompt）
- **未来观测或表征预测**：Juno-TTT 阶段 1（世界模型）、T³VF（query tokens）、VANE（prompt bank）、WAM-TTT（快权重）
- **特征分布或统计对齐**：ILA（编码器）、BN-adapt（归一化统计）、CFA（表征对齐）、ActMAD、FOA（prompt 加激活平移）
- **冻结动力学或世界模型的一致性**：ILA、MoVie（编码器）、T2-z（环境潜变量）、Self-Correcting Planning（不更新模型）
- **critic 或价值**：TEMPO（整个 actor）、V-GPS（只重排序）
- **熵或置信度**：MEMO（全部参数）、TENT 与 SAR（仿射）、TPT（文本 prompt）、T²VLA（策略）
- **动作块重叠段的时间一致性**：SALT（奇异值尺度）；BID、Self-GAD、RTC、Sentinel 不更新参数
- **多样本一致性、投票或方差**：PDF（扰动头）、T³VF（决定何时更新）、RoboMonkey、DVAC
- **去噪误差、去噪方差或场范数**：Diffusion-TTA、DVAC、GeCO、τ0-WM
- **VLM 奖励或验证器**：VLS、RoboMonkey
- **学到的进度估计器或成功记忆**：EVOLVE-VLA、TT-VLA（LoRA）、Retrieve-then-Steer（非参数记忆）
- 按这张对应表，"只更新归一化统计或仿射"这一类在 VLA 上本轮没有找到实测；策略侧"只改输入"的方法只有视角合成类（§3.3）。

### 4.9 与"冻结 VLA、无标签、setup 漂移"的对照

- 本轮没有一项工作同时满足以下四点：
  - 完全冻结，或只改极少参数；
  - 不用标签，也不用结果反馈；
  - 针对相机位姿这类从一开始就存在的 setup 漂移；
  - 有真机验证。
- 按接近程度：
  1. SALT：主干和视觉编码器冻结，信号完全无标签，真机上测了关灯和顶部相机罩网；但没有相机位姿漂移，漂移从第一次重规划就存在时几乎无效。
  2. T³VF：只更新 query tokens，在 LIBERO-Plus 的 Camera 维度上给出了数字（50.5 → 55.3，只在 LIBERO-Plus 上微调过的模型上；未微调的模型 39.2 → 41.5）；一个模型，只在仿真。
  3. WAM-TTT：WAM 冻结，真机光照下有增益；需要目标域人类视频和成对数据的元训练。
  4. VANE 与 TTT-VLA：只更新 prompt，在 SimplerEnv 的视觉变体上增益 +1.5 到 +3.9；VANE 在 Google Robot 的部分设置上反而下降。
  5. Juno-TTT：真机噪声和光照上增益明显，但更新 LoRA 和动作头，并需要"已验证成功"的样本。
  6. Infer-Diagnose-Refine：免训练的反事实视觉诊断，摘要没有数字，也没说明针对哪类视觉漂移。
- 相机位姿：T³VF 是本轮唯一在 VLA 上对相机维度给出无标签 TTA 数字的工作；在不预测未来图像的常规 VLA 上，本轮没有找到。离它最近的是非 VLA 的 ILA、MoVie，以及需要几何输入的图像侧方法（§3.3）。

## 5. 条件注入结构与干预位置（P§6）

### 5.1 问题

图像、语言、状态这些条件以什么形式进入动作生成模块，决定了校正能放在哪里：前缀 KV、交叉注意力的 key / value、调制参数、LLM 序列，或者联合去噪序列的残差流。

### 5.2 VLA 的注入形式

- **逐层联合注意力（Mixture-of-Transformers）**：
  - π0：动作专家第 l 层读 PaliGemma 前缀第 l 层的 KV（共 18 层）；三段 blockwise causal mask，依次为图像加语言、状态、噪声动作；专家只通过自注意力与前缀交互。流匹配，动作块长度 50，10 步 Euler；专家约 300M（§IV，App. A-B、A-D）。
  - π0.5：同样逐层；原文 "information flows unidirectionally from the VLM to the action expert"；时间步经单独 MLP 投影后由 adaptive RMSNorm 注入；状态离散成文本 token 放进前缀；动作专家不看 FAST token（App. A-E，§IV-A）。
  - π0.5+KI：正向通路不变，用 stop-gradient 切断动作专家流回预训练权重的梯度（§5.2）。
  - NEO-VLA：专家第 j 层读骨干第 m_j 层的 KV，层映射可以配置。VLAFlow 和 Should-AE-Train 沿用逐层 KV 接口。
- **单层特征加交叉注意力**：
  - GR00T N1：Eagle-2 LLM 第 12 层（中间层）的特征，由交替做交叉注意力和自注意力的 DiT 读取，时间步经 adaLN 注入。正文称中间层比最后层推理更快、下游成功率更高（§2.1，没给数字）。
  - GR00T N1.5：VLM 冻结，DiT 对 VL embedding 做 "cross-attended"（官方页面）。
  - GR00T N1.6（`n1d6` 分支代码）：`select_layer=16`，LLM 截到前 16 层；`AlternateVLDiT` 共 32 层，奇数块做自注意力，偶数块做交叉注意力，并在"非图像 token"和"图像 token"之间轮换。
  - SmolVLA：只用 LLM 前一半层；交叉注意力与自注意力交替为 85.5，纯交叉注意力 79.0，纯自注意力 74.5（Table 6）。
  - RDT-1B：每个 DiT block 做交叉注意力，图像和文本逐层交替（ACI），理由是图像 token 太多会 "overshadow" 文本（§4.1）。
  - VLA-Adapter：policy 第 l 层读 VLM 第 l 层（Bridge Attention），属于逐层交叉注意力。
  - ABot-M0：默认读 Qwen3-VL 的最后一层。
- **动作 token 放在 LLM 序列里**：
  - OpenVLA：每维动作 256 个 bin，覆盖 Llama 词表中最不常用的 256 个 token；
  - FAST：DCT 后接 BPE，自回归预测；
  - OpenVLA-OFT：改为输入空动作 embedding，用双向掩码并行解码，接 MLP 做 L1 回归；LIBERO 上 L1 为 95.3，扩散头为 95.4。
- **adaLN 与 FiLM**：
  - DP 的 CNN 版在每个卷积层逐通道做 FiLM；Transformer 版每个 decoder block 做交叉注意力，时间步作为第一个 token。
  - ScaleDP 把观测 embedding 分解成多个仿射层。
  - DexVLA 把 reasoning token 经 FiLM 注入。
  - OpenVLA-OFT 的 OFT+ 用 FiLM 把语言注入视觉编码器的每个 block；不用 FiLM 时，ALOHA 上语言跟随约 33%，接近随机。
- **in-context 拼接**：CogACT 把条件压成一个 cognition token，与噪声动作一起输入 DiT；Dita 把图像特征、语言 token 和时间步 embedding 拼在因果 Transformer 序列前部，不用 adaLN，也不用交叉注意力。

### 5.3 WAM 的注入形式

- **逐层 KV 与 MoT**：
  - Fast-WAM：基于 Wan2.2-5B 视频 DiT；动作 token 只看干净的首帧 token，不看未来帧；文本经交叉注意力注入所有 token。
  - LingBot-VA：每层各模态用独立 QKV 做联合自注意力，视频与动作交错排列、时间上因果。
  - Motus：理解、视频、动作三个专家的自注意力拼接。
  - ImageWAM：见 §5.4。
  - Faster-WAM 打破了层对齐：每个动作层、每个 head 对所有视频层的 KV 学一组 softmax 权重，动作专家只剩 1 层；LIBERO-Plus 上 78.3，Fast-WAM 为 51.5（Table 3）；动作生成约 6 ms，Fast-WAM 约 150 ms。它同时改了很多其他东西。
- **逐层交叉注意力**：GE-Act 的第 i 个动作 block 读第 i 个视觉 block 的输出（§3.1）。
- **视频特征加交叉注意力，或汇成全局向量**：
  - VPP：聚合 SVD U-Net 各上采样层的特征，在 DiT 中做交叉注意力；
  - mimic-video：Cosmos-Predict2 第 19 层；
  - DiT4DiT：Cosmos-Predict2.5-2B 第 18 层；
  - Video Policy：SVD 第 9 / 14 / 17 / 20 / 23 层汇成一个全局向量，动作损失不回传到视频网络。
- **同一扩散序列里联合去噪**：
  - Cosmos Policy 把动作、本体感受和价值复制后写成新的 latent 帧，插入视频序列，不改结构；
  - DreamZero 视频与动作联合去噪、共享时间步；
  - UWM 两者各有独立的时间步；
  - UVA 用联合 latent 加两个轻量扩散头。
  - 这类结构没有独立的前缀 KV 接口。
- **测试时生成未来帧的作用**：Fast-WAM 去掉测试时的视频生成后，RoboTwin / LIBERO 为 91.8 / 97.6，与联合去噪（90.6 / 98.5）和先视频后动作（91.3 / 98.0）相当；去掉训练时的视频共训则降到 83.8 / 93.5。作者称测试时想象的作用 "comparatively limited"（§4）。

### 5.4 ImageWAM 的注入方式，以及与 π0 / π0.5 的异同

下面关于代码的结论只基于官方仓库的 main 分支（2026-11-20 读取），没有核对其他分支或发布版本。

- **论文的描述**（§3.2、App. §5.1.1、Fig. 2）：
  - 编辑模型默认是 OmniGen2，另有 Ovis-U1 和 FLUX.2 两个版本；LLM / VLM 冻结，只训练扩散分支和动作专家。
  - 缓存取全部层 𝒞={(K_ℓ,V_ℓ)}，ℓ=1..L（Eq. 5）。
  - 动作专家与编辑模型 "same architecture"，hidden 1024。
  - Fig. 2 图注称动作专家 "integrates the intermediate KV features from this generation process via joint attention"。
  - 推理时在固定的 τ⋆ 上只跑一次编辑前向，不解码图像；正文没给 τ⋆ 的值。
  - 论文没有关于注入形式、层或 τ⋆ 的消融。
- **main 分支代码**：
  - `mot.py::prefill_flux2_video_cache` 逐层缓存编辑 DiT 的 K/V（FLUX.2-klein-4B 有 5 个 double-stream 块和 20 个 single-stream 块）。
  - `forward_flux2_action_with_video_cache` 在动作第 l 块里把 `cache[l].k` 与动作自己的 K 拼接，V 同理，再用动作的 query 做注意力。配置 `num_layers_double: 5, num_layers_single: 20` 与编辑模型一一对应。OmniGen2 和 Ovis-U1 两条路径结构相同。
  - 掩码 `_build_mot_attention_mask_flux2` 的注释为 "Stable text/ref prefix cannot attend to noisy target/action tokens" 和 "Action uses stable prefix and action self-context, not target/noisy image"。动作 token 只看文本（加本体感受）和参考图像（当前观测），不看噪声目标帧 token。这与 App. §5.1.1 的 "attend to the other tokens" 不一致。
  - 推理函数 `infer_action_flux2` 中目标 token 数为 0，编辑分支的时间步设为 `zeros`。按其调度器 x=(1−σ)x₀+σε、timestep=σ·1000，这对应 σ=0，即干净端。训练时这个时间步随机采样，通过编辑 DiT 的 adaLN 调制影响前缀 KV。
  - 动作 DiT 的时间步经 `time_in` MLP 和 FLUX 的 `Modulation`（shift / scale / gate）注入，属于 adaLN 式调制；本体感受接在文本之后；训练损失权重 λ_video=0.5、λ_action=1.0。
- **与 π0 / π0.5 相同的地方**：
  - 前缀只计算一次，存成各层 KV；
  - 前缀不看后缀；
  - 动作专家第 l 层把自己的 K/V 拼到前缀第 l 层的 K/V 后面做注意力；
  - 时间步用 adaptive norm 注入动作专家；
  - 动作只读条件 token。
  - 也就是说，两者都是逐层联合注意力，不是交叉注意力。
- **不同的地方**：
  1. **前缀编码器**：π0.5 的前缀由 PaliGemma 自己逐层处理图像和文本。ImageWAM 的前缀由图像编辑 DiT（双流块加单流块）处理，冻结的 LLM / VLM 只把最后层隐状态作为文本 token 交给 DiT，所以动作专家读到的是编辑 DiT 的逐层 KV，读不到 LLM 的逐层 KV。
  2. **前缀 KV 依赖扩散时间步**：编辑 DiT 的 adaLN 让前缀 KV 随 σ 变化（训练时随机，推理代码固定为 0）；π0.5 的前缀没有时间步。
  3. **世界模型损失只在训练期起作用**：训练时编辑分支用流匹配预测目标帧，这塑造了前缀表征；推理时不计算目标 token，动作也从不读目标 token。这与 Fast-WAM 的结论一致。
  4. **其他细节**：状态的注入方式不同（π0.5 是离散文本，ImageWAM 是接在文本后的 embedding）；动作去噪 3 步，π0.5 为 10 步；ImageWAM 的动作 DiT 有 double-stream 和 single-stream 两种块。
- **鲁棒性数字**：ImageWAM Table 3 中，FLUX.2-4B 版在 LIBERO-Plus 相机维度上为 80.8，π0 为 13.8（照搬自 LIBERO-Plus），Fast-WAM 为 16.4。两者训练配方不同，不能把差异归因于注入方式。ImageWAM §4.4 Q3 报告相机、光照、噪声维度不随编辑骨干的规模单调提升，作者归因于缓存与扰动类型是否对齐。

### 5.5 读哪一层

- **VLA**：
  - GR00T N1：中间层优于最后层（§2.1，没给数字）。
  - SmolVLA（Table 8）：读前 N=8 / 16 / 24 / 32 层，分别为 75.0 / 78.5 / 79.5 / 80.3。
  - ABot-M0（LIBERO-Plus，Table 8）：最后层 71.0，中间层 69.0，后 16 层 67.4，与 GR00T N1 的"中间层更好"相反。
  - NEO-VLA（Table 4）：骨干冻结时，只读前 28 层 94.9，跳层读 28 层 90.9，只读后 28 层 86.7；微调后跳层读法最好（95.3）。
  - VLA-Adapter：全部层带门控融合最好（§3）。
  - Layer Mystery（摘要）：54 种融合配置中 47 种不如最好的单层；最优层随骨干和基准变化；用 InfoNCE 选层的 regret 为 3.71 个点，固定选最深层为 17.89 个点。
- **WAM 的视频特征**：
  - VPP（CALVIN）：只用最后层 3.60，多层聚合 4.33；Layer-3 / 6 / 9 / 12 分别为 3.72 / 3.88 / 4.29 / 4.05；两步去噪 4.19，不如单步。
  - mimic-video：第 19 层最好。正文默认 τv=1（一次前向），但重建扫描显示 τv≈0.4 最优，Fig. 6 图注与正文矛盾。
  - DiT4DiT：第 2–8 层差，第 18 层最好，第 24–28 层崩（Fig. 8a）；单步去噪最好（Fig. 8b）。

### 5.6 干预的位置

- **改前缀 KV**：
  - KV steering（LLM 上的工作）：
    - prefill 之后，对最后一个 prompt token 位置的 K、V 各加一次差均值向量，各层都改；实际上主要改的是 V（c^k≈0，c^v 取 1–10）。
    - Llama-3.2-3B 的 ARC-c 74.32 → 79.27，激活引导为 74.23。
    - 每 token 10 ms，与基线相同；激活引导为 15 ms。
  - TempoFit（冻结的 π0.5 与 QwenGR00T，不训练）：
    - 在线性投影之后、RoPE 之前改前缀 K/V，只改部分中间层，K 和 V 都改；用 K-to-K 检索历史 KV，残差注入后做范数保持。
    - LIBERO-Long 上 π0.5 92.6 → 96.6；延迟为 1.04 倍。
    - Table IV：只在中间层启用 96.6，全部层（0–17）74.2，直接拼接（Concatenation）0.8，去掉范数保持 90.2。同表还有 "bottom 9–17" 59.8、"top 0–8" 89.4，标签照原文。正文没给具体层号。
- **激活引导**：
  - MI-Steering：把 VLM 的 FFN value vector 投影到 token 空间、按语义聚类后上调权重。OpenVLA 在 LIBERO 上，fast 簇比 slow 簇的位移平均大 27.73%；只改早层 μ=0.007，只改晚层 0.086，全部改 0.098。
  - CTRL-STEER：选 10 个 Llama-2 FFN 神经元，多数在后半段层；静态引导会让成功率崩溃（如 Long 58 → 10），用 PID 或 RL 动态调整则能保持（RL 57.0）。
  - COAST：在动作专家某一层（如 π0.5 第 11 层）的残差流上乘一个 conceptor 门；LIBERO-10 上 π0.5 0.43 → 0.80。"action expert 是瓶颈"在文中只是假设，没有与 VLM 层直接对比。
  - RL²-VLA：在动作专家 latent 上训练离线 RL 策略，把它的速度场与 VLA 的合成，只在预测会失败时启用；摘要称 OOD 上最多 +17.3%。
- **机理分析**：
  - VLA-Trace：生成阶段不让动作看图像时，π0.5 在 LIBERO-10 上从 93.5 降到 0.0；不让看文本时为 39.0，而 Goal、Spatial、Object 三个套件仍有 96.5–99。存在一段窄的"视觉→动作"瓶颈层，最脆弱的层上只剩 4%。
  - Present-not-Remembered：Octo 在 L6 之后动作不再依赖历史；在 L4 注入对动作的影响是在 L8 注入的 7–9 倍，但与注入内容无关，修复不了遮挡。
  - DeepVision-VLA：在深层遮掉 ROI 视觉 token 几乎不影响动作；把 DINOv3 后 16 层的 QKV 并入 VLA 的后 16 层得到 88%，均匀并入 16 层 85%，并入前 16 层 61.5%（基线 65.5）。
  - Knowing When to Stop：读动作专家对观测的注意力熵；预测越远，熵越高，误差越大，据此截断动作块。
  - StairVLA（摘要）：早期去噪偏重语言加视觉，后期偏重当前视觉；LIBERO 96.5 → 97.8。
- **WAM 上的干预**：
  - WA-LQR：在 DiT block 的残差流上，每个去噪步和每个 chunk 做 ActAdd 或 WA-LQR。Cosmos Policy 相机朝向扰动 46.0 → 59.3（LQR），相机噪声 26.7 → 67.3（ActAdd）；LingBot-VA 上几乎线性不可分，ActAdd 反而有害（48 → 41）。
  - SteerTrace（摘要）：对抗扰动主要经未来 token 或当前帧 token 进入动作专家。恢复未来 token 可消除 61–94% 的攻击效果；攻击约束未来帧不变时，恢复当前帧 token 可消除 87–99%；恢复视频专家第 10–29 层中 0.36% 的 FFN 神经元可消除 72–96%。

### 5.7 局限

- 改前缀 KV 与改动作专家残差流（COAST、RL²-VLA）没有在同一模型、同一扰动下比较过。
- 改前缀 KV 的 VLA 工作（TempoFit）针对的是长时程记忆，不是视觉漂移；WAM 上唯一面向鲁棒性的引导工作是 WA-LQR，改的是残差流。
- 读哪一层的结论随骨干和基准变化（Layer Mystery）；VLA-Adapter 与 ABot-M0 的结论相反。
- knockout 只检验必要性，不检验充分性（VLA-Trace Limitations）。
- 同一种干预在不同 WAM 上效果相差很大（WA-LQR §7）。

## 6. 横向趋势

1. **同一模型的未适应相机数字，在不同论文之间不可比**：
   - π0.5：Adapt3R 式 S/M/L 下有 48.5（FTM）、54.5（DART）、48.27（VLA-ZO）三个值；LIBERO-Plus 相机维度上有 62.5（WACO）、72.0（CoRe-VLA）、75.4（WAM-vs-VLA）、75.8（Phoenix）、76.5（Homeward）、78.4（ZimaBlue）六个值（§3.6）。
   - π0：LIBERO-Plus Table 1 中 Camera 为 15.8，ImageWAM Table 3 照搬 LIBERO-Plus 写作 13.8，WAM-vs-VLA 用 JAX 重跑后为 61.0（Table 4）。
   - Cosmos Policy 在 LIBERO-Plus 相机维度上：WAM-vs-VLA 报告 75.8；SCVC 报告发布 checkpoint 为 79.5（Table I），遮挡实验中不遮挡时为 80.5%（Fig. 3）。
   - Fast-WAM 在 LIBERO-Plus 全集上为 51.5，在 JAM 使用的 1,506 任务子集上为 55.3。
2. **腕部相机是混杂因素**：
   - LIBERO-Plus 的相机维度只动第三人称相机，RoboTwin 2.0-Plus 只动头部相机，FTM 只动 agentview 相机；
   - 遮掉腕部后，Cosmos Policy 的相机维度只剩 0.2%（SCVC）；OFT_w 只有 16.8，OpenVLA-OFT 为 59.7（LIBERO-Plus）；
   - Cross-View AC 为此遮蔽腕部；CoRe-VLA 报告策略过度依赖腕部；
   - 腕部相机本身出问题时影响更大：腕部冻结下 π0.5 只剩 3.6，GR00T N1.7 为 0.0（Blackout-Freeze）；腕部安装偏移是 WARP-VLA 单独处理的问题。
3. **图像侧方法依赖几何信息，几何不准就会崩**：GS-VLA 换成估计深度后从 86.8 降到 44.5；Homeward 只用 VGGT 恢复时比不校正还差（72.8 对 79.7）；CoRe-VLA 自述依赖深度精度；AnyCamVLA 需要已知的内外参（§3.3）。
4. **视觉侧少参数适应的增益依赖评测协议**：
   - FLA 在"每任务一条、测同一批任务"下为 90.8，在"每场景一条、测 40 个任务"下为 74.3（FTM、DART）；
   - Libero-V 的平均分主要由相机一列决定，非相机扰动下零样本已有 93.5–96.2（FTM）；
   - 在相机数据上调视觉模块会让其他扰动维度变差（VLA-Retain）。
5. **VLA 上特征统计对齐的增益很小**：ActMAD 作为 SALT 的基线，SmolVLA 上只有 +0.6（43.9 → 44.5），GR00T N1.7 上 +1.7（58.7 → 60.4）（SALT Table 1）。
6. **以上一动作块剩余段为目标的 TTA，对从一开始就存在的漂移几乎无效**：SALT 的信号依赖扰动出现之前的干净计划；漂移从第一次重规划就存在时几乎没有增益（App. I、App. J）。
7. **VLA 上的无标签测试时训练增益普遍不大，稳定性是共同难题**：
   - 测试时这一步的增益：T³VF 平均 +2.8，VANE +3.2，TTT-VLA 在 WidowX 上 +3.9、Google Robot VA 上 +1.5；SALT 相对不适应提升 9.3 和 7.3 个点，相对最强基线 BID 只领先 7.2 和 2.9 个点。
   - 稳定性：TTT-VLA 的在线版本会塌缩，VANE 需要回滚，T³VF 和 SALT 都要门控（§4.3）。
8. **VLA 上还没有"只调 LN / RMSNorm 仿射，加无标签信号"的报告**：SALT、T³VF、TTT-VLA、PDF 都只引用了 TENT，没有拿它做数值对比；"只调归一化仿射"的经验（TENT、SAR）来自视觉分类模型。
9. **"相机位姿漂移、冻结 VLA、无标签"这个组合，本轮没有找到严格满足的工作**：唯一接近的 T³VF 是先预测未来图像的 VLA（Mantis），在 LIBERO-Plus 相机维度上增益 +4.8（在扰动数据上微调过的模型）或 +2.3（未微调的模型），只在仿真；最近的其他工作要么不是 VLA（ILA、MoVie），要么需要几何输入（AnyCamVLA、Homeward 等）（§4.9）。
10. **"读哪层、改哪层"的证据互相不完全一致**：
    - 改哪层：TempoFit 只改中间层最好（96.6），改全部层为 74.2；MI-Steering 只改早层几乎无效；DeepVision-VLA 注入深层（88%）好于浅层（61.5%）；VLA-Trace 显示 π0.5 有一段窄的视觉→动作瓶颈层；Present-not-Remembered 中 Octo 在 L6 之后不再使用历史。
    - 读哪层：GR00T N1 认为中间层更好，ABot-M0 认为最后层更好；骨干冻结时 NEO-VLA 读前段层最好；VLA-Adapter 认为全部层融合最好，Layer Mystery 发现融合多半不如最好的单层、最优层随骨干和基准变化；视频特征上 VPP、mimic-video、DiT4DiT 都是中间偏深的层最好。
    - 这些结论来自不同的模型、任务和指标，没有一项工作在同一设置下同时比较"读"和"改"。
11. **没有证据支持 WAM 普遍比 VLA 更鲁棒**：
    - LIBERO-Plus 上最好的 WAM（Cosmos Policy，82.2）与 π0.5（85.7）相当；RoboTwin 2.0-Plus 上 WAM 总分更高，但相机一维是 π0.5 最高（WAM-vs-VLA）；
    - WAM 内部从 51.5 到 94.8 的差距大于两族之间的差距（Phoenix）；
    - 以视频生成器为骨干本身不带来视角鲁棒性（JAM）；
    - ZimaBlue 自述相机视角变化是关键瓶颈；
    - 两篇 WAM 综述都没有引用鲁棒性正面对比（WAM-Survey、WAM-Tutorial）。
12. **训练数据的影响与模型族同量级**：同一 Fast-WAM 在两种训练数据下总分为 72.7 与 51.5（WAM-vs-VLA）；Clean2Random 下 Fast-WAM 只有 1.9（Phoenix）；在 LIBERO-Plus 数据上 SFT 后相机维度可到 92–96（ZimaBlue、WACO 表中的 OpenVLA-OFT+）。
13. **WAM 的收益集中在训练期**：Fast-WAM 去掉测试时视频生成后性能基本不变，去掉训练时的视频共训才明显下降；ImageWAM 的代码在推理时不计算目标 token，动作也不读目标 token（§5.3、§5.4）。

## 7. 文献自述的开放问题

- 极端视角下所有一次演示方法都明显退化（DART §7）
- 剩余失败集中在最宽的轨道上，那里超过一半的画面落在原视野之外（WACO §IV-B）
- 单视角无法恢复看不见的内容，包括大视角下新暴露的区域、远目标视角和大遮挡（GS-VLA §6、AnyCamVLA §V、CoRe-VLA §6、WARP-VLA）
- 需要外部度量深度，真机复现是 "natural follow-up"（GS-VLA §5、§6）
- 依赖深度精度（CoRe-VLA §6）
- 真机上 URDF 与真实外观有差距，机械臂前方有遮挡，接触时夹爪的渲染是难点（Homeward §5）
- 训练相机在不同演示之间不一致时，目标视角怎么选还没有解决（AnyCamVLA §V）
- 视觉调优的目标增益不能预测保留程度，副作用不能用源域遗忘解释，更宽的数据不能消除回退，补救策略的效果因模型而异（VLA-Retain Table 3、Table 4、Fig. 4、Fig. 5）
- 动作等价的视角对难以获得（Cross-View AC §5、App. I）；同状态视角对在真机上难采集，WAM 上没有真机证据（SCVC）
- 只在流匹配动作头上验证，离散 token 的 VLA 列为未来工作（Cross-View AC）
- 校正什么时候该启用：策略已掌握该视角时校正会降分（Homeward Table 6）；只在检测到腐蚀时才启用复原（CRT §5）
- 源域 Fisher 在大域差下会估错，适应仍要约 20 条有标注演示（Not All Layers）
- 缩放系数需要搜索，按层自适应、免超参的缩放留作未来工作（DART）
- 泛化不可分解，组合扰动带来的差距一致为负（LIBERO-Plus §5、Finding 9）
- 自动生成的轨迹不可靠，所以训练数据里排除了位姿扰动（LIBERO-Plus App. D.1）
- 缺少标准化的鲁棒评测框架，模型应能承受 "reasonable and practically necessary perturbations"（LIBERO-PRO §6–7）
- 相机视角和机器人初始状态扰动对 WAM 仍然难；推理时延是 "major limitation"；如何更高效地利用世界模型骨干的动态先验（WAM-vs-VLA 结论、§1）
- 同时追求所有因素的泛化不可行；分析没有定位具体的伪相关；方案只在数据侧，没有在完整 OXE 规模上验证（Shortcut-OXE §5–6）
- 需要扩充光照与相机的多样性，加入相机内参和分辨率这类变异算子，以及不确定性估计与安全监控（VLATest §6）
- 只扰动场景相机，腕部相机位姿扰动不在范围内；对失败或恢复状态下的视角鲁棒性没有声明；仰角轴只有一个外推点（SCVC §VIII）
- 腕部冻结仍很难处理；能否把注意力的转移变成可靠的恢复尚未解决；用平均 embedding 替换的收益不稳定（Blackout-Freeze §4.1–4.2）
- knockout 只是必要性探针，不是自然 OOD 失败的模型；分析没有扩展到 LIBERO-Plus、LIBERO-PRO 或 RoboTwin；activation patching 和表征恢复留作后续（VLA-Trace Limitations）
- 只模拟刚体；仿真与真机的绝对成功率迁移不佳，R²=0.49（Colosseum V2 §VI）
- SimplerEnv 的绿幕合成难以做光照与相机扰动（INT-ACT §3、§5）
- 生成一致的多视角预测仍然难；短时预测准确不保证长时行为鲁棒；生成指标不足以反映动作 grounding（WAM-Survey §III-E1、§I、§V-A）
- 视频表征要同时可预测、可执行，并兼顾训练稳定性（WAM-Survey §III-D1）
- 特征条件化的接口可能只是在利用与任务相关的特征，而不是有意义的未来信息；准确的视觉预测不一定带来更好的控制（WAM-Tutorial §3）
- 失败主要来自视频生成错误；评测的 rollout 次数少；推理只有约 7 Hz（DreamZero §5.1、§6）
- 真机结果只有定性描述，扰动参数的范围没有完整给出（Eva-VLA）
- 最优层依赖骨干和基准，多层融合多半不如最好的单层（Layer Mystery）
- 全部层一起改会引入历史与当前的干扰；层子集、缓存大小、衰减斜率都是固定的；记忆里有无关帧时性能下降（TempoFit §I、§V）
- WAM 的可引导性强烈依赖结构，跨任务、跨模型的迁移有限；需要既可引导、又保留基础模型表征的 WAM（WA-LQR §7）
- "action expert 是瓶颈"仍是假设（COAST 引言）
- 微调对可引导性的影响不清楚，引导向量的语义会随任务和时间漂移（MI-Steering limitations）
- 测试时生成未来帧的作用 "comparatively limited"，价值主要在训练期（Fast-WAM §4）
- 相机、光照、噪声维度不随编辑骨干规模单调提升（ImageWAM §4.4 Q3）
- 视频特征取自哪个噪声水平，正文与图注的结论矛盾（mimic-video）
- 注入层的历史能改变动作，但与内容无关，修复不了遮挡（Present-not-Remembered App. G）
- KV 隔离是否有益取决于动作监督和训练日程（Should-AE-Train §5）
- 自监督辅助任务必须与控制相关，如何自动选择留作未来工作（PAD Sec. 4.2）
- 无监督更新不保证单调提升；测试时采集的数据要与源 buffer 分布相近；需要更好的潜特征对齐方法（ILA Sec. VI）
- 没有真机实验（MoVie Conclusion）
- 只在仿真里测，也没有与已有 TTT 方法直接对比；小批量在线更新会让 prompt 塌缩；收益集中在少数关键决策点（TTT-VLA Limitations）
- 增益依任务和本体而定，没有报告 wall-clock 时间（VANE）
- critic 在漂移下必须仍有信息量，否则适应会变差；有额外的内存和计算开销（TEMPO App. C、B.8）
- 漂移从第一次重规划就存在时没有干净的计划可学；改变任务本身的扰动修不了；门控会漏掉渐变式漂移；每次更新都要额外的梯度步和重新生成动作块（SALT App. I、App. J）
- 增益相对推理开销偏小，训练不含扰动时增益更小（T³VF）
- 元训练要求人-机成对数据的技能阶段对齐；快权重的表达能力边界还没刻画；只用了 RGB（WAM-TTT）
- BN 在小批量和混合漂移下不稳定，LN / GN 模型的熵最小化会塌缩（SAR）
- 批采样、MCMC 和 Feynman–Kac 重采样的开销高（VLS）
- 在低成本、高频的机器人上计算昂贵，只适用短上下文策略（BID）
- 要反传去噪步，只适用于扩散或流策略（RTC Sec. 6）
- 策略必须能随机采样，价值函数的泛化受限于训练所用的两种本体（V-GPS）
- 只保证误报率，需要成功 rollout 做校准，只能在失败发生时检测（Sentinel）
- 零阶优化比 Adam 慢数倍（Dune Sec. 6）

## 8. 现有综述的分类对照

- **WAM-Survey（2609.16074）**：
  - 分类：end-to-end 与 dual systems（§III-C），joint 与 IDM（§III-B）。
  - 条件注入：把 π0 / π0.5 归入 "cross-attention conditioning"（§III-C2）；把 ImageWAM 单独列为 "KV-cache transfer"，与 MoT（Fast-WAM）和 "cross-attention"（π0）并列。
  - 鲁棒性：没有引用任何 WAM 与 VLA 的鲁棒性正面对比；唯一相关的说法是引述 DWAM 的 "enhanced robustness"，以及 "richer vision-language and video representations generally improve action generalization and robustness"（§III-C1）。提到了 LIBERO-Plus 但没有描述，没有提到 LIBERO-PRO。
  - 读到的正文在 §VI 处被截断。
- **WAM-Tutorial（2607.00836）**：
  - 分类：imagine-then-execute、video-feature-conditioned、joint、auxiliary 四类（§3）。
  - 没有鲁棒性评测或对比。§2.2 指出，在观测空间做预测的模型必须处理 "background changes, illumination, texture, or sensor noise"；§3 提醒 "accurate visual prediction does not necessarily lead to better control"。
- **与本文轴 5 的对照**：
  - π0 / π0.5：WAM-Survey 归为交叉注意力；按本文的分类属于逐层联合注意力。
  - ImageWAM：WAM-Survey 归为 KV-cache transfer；本文同样归为逐层联合注意力。
  - Fast-WAM：WAM-Survey 归为 MoT；本文同样归为逐层联合注意力。
  - 依据：
    - π0 §IV 与 App. A-D：动作专家第 l 层读前缀第 l 层的 KV，与前缀共享自注意力，blockwise causal mask 不让前缀看后缀；
    - π0.5 App. A-E："information flows unidirectionally from the VLM to the action expert"；
    - Fast-WAM Fig. 2：MoT 逐层共享注意力（具体层对应原文没写）；
    - ImageWAM main 分支代码：`forward_flux2_action_with_video_cache` 把 `cache[l].k` 与动作的 K 拼接后做注意力，掩码不让前缀看动作 token（§5.4）。
  - 由此看，三者在注入层面属于同一类，WAM-Survey 把 π0 归为交叉注意力不准确。π0 一侧的依据是论文正文和附录，本轮没有读 π0 的代码。
  - 真正的交叉注意力接口见 GR00T N1（DiT 交替交叉注意力与自注意力，读第 12 层特征）和 GE-Act（逐层交叉注意力）。

## 9. 入门阅读顺序

1. LIBERO-Plus（Table 1、App. A.4、App. C.3）：7 个扰动维度的定义与幅度，以及 L1–L5 的定档方式。
2. SCVC §VI-B：读 LIBERO-Plus 相机分数之前，先看腕部相机审计。
3. WAM-vs-VLA：唯一专门比较 WAM 与 VLA 鲁棒性的研究，含 RoboTwin 2.0-Plus 的相机口径和推理时延。
4. Shortcut-OXE 与 LIBERO-PRO：捷径学习和记忆。
5. FTM（配合 [notes/2025-ftm.md](notes/2025-ftm.md)）：锚点，FTM / FLA 的定义和"漂移主要在视觉侧"的假设。
6. Adapt3R App. C.1 与 DART（Table 1、Table 10、Table 12）：视角协议的数值、FLA 的独立复现、更严的一次演示协议。
7. AnyCamVLA，接着读 Homeward：冻结策略加图像侧重渲染的代表，以及它们的失败模式和"免训练"的边界。
8. Cross-View AC：训练侧鲁棒性的严谨对照，包括同数据对照、打乱配对和腕部遮蔽。
9. VLA-Retain：视觉调优在其他扰动维度上的副作用。
10. PAD 与 ILA：策略侧 TTA 的起点；ILA 直接测了相机位姿，可以看到相机漂移比颜色和背景难得多。
11. TENT 与 SAR：只调归一化仿射加熵最小化的范式，以及 LN 模型为什么会塌缩。
12. BID，接着读 SALT：动作块重叠段这一信号，从样本选择到梯度更新；SALT App. I / J 说明了它的盲区。
13. T³VF 与 WAM-TTT：VLA 上相机维度的无标签 TTA 数字，以及 WAM 侧的视频预测信号。
14. π0（§IV、App. A）与 π0.5 App. A-E，再读 GR00T N1：两种主流的条件注入接口。
15. VLA-Adapter 与 Layer Mystery：读哪一层，两种相反的结论。
16. Fast-WAM 与 ImageWAM（配合代码 `mot.py`）：π0 式 MoT 怎样搬到视频或编辑 DiT 上，以及"测试时不生成"的证据。
17. TempoFit：在冻结的 π0.5 上改前缀 KV，层位置消融最清楚，范数保持等实现细节也写全了。
18. VLA-Trace 与 WA-LQR：π0.5 的视觉→动作通路，以及 WAM 上面向鲁棒性的残差流引导。
