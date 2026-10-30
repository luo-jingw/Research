# real2sim 综述

- 快照日期：2026-10-30
- 覆盖：2018–2026 年机器人方向的 real2sim 工作，重点是 2024–2026。
- 引用格式：方法简称，元数据见 [papers.md](papers.md)，节号写作 `P§n`。
- 本文只写可溯源到文献的内容。基于这些文献提出的研究设想记录在根目录 `opportunities.md`（`Area: real2sim`）。

## 0. 定义

real2sim 指从真实观测（扫描、视频、单张图像、交互轨迹、关节力矩）反求仿真器的状态与参数，使仿真在下游任务关心的维度上复现现实。重建结果通常交给 RL 微调、示教生成或策略评测使用，形成 real-to-sim-to-real 闭环。

RealityGap-Survey 把 sim-to-real 的方法分为"缩小 gap"（改进仿真、选择模态、设计选择）与"克服 gap"（域泛化与适应、数据选择、策略结构）两类。real2sim 归在"改进仿真"之下，与系统辨识、学习残差并列，并被表述为三个逆问题：几何、运动学/动力学（含铰接）、渲染。

## 1. 分类框架

本综述用三个正交轴组织文献。

**轴一：重建什么**

| 对象 | 内容 | 主要章节 |
|---|---|---|
| 几何与布局 | 可碰撞网格、物体位姿、支撑关系、尺度 | §2 |
| 铰接与运动学 | 部件分割、关节类型/轴/范围、URDF/MJCF | §3 |
| 外观 | 策略相机看到的像素 | §4 |
| 物体物理参数 | 质量、惯性、摩擦、刚度、本构律 | §5 |
| 机器人侧动力学 | 执行器、延迟、质心、残差动作 | §6 |

**轴二：拿来做什么**

| 用途 | 对孪生的要求 | 代表 |
|---|---|---|
| 策略训练（RL 微调） | 可闭环交互、接触大致正确 | RialTo, CASHER, X-Sim, VR-Robo |
| 数据生成（IL / VLA 示教） | 像素逼真，接触可近似甚至关闭 | Re3Sim, DREAM, R2R2R, RoboSplat |
| 策略评测 | 仿真结果与真实结果相关（Pearson r、MMRV） | SIMPLER, PolaRiS, ReVeal |
| 规划 / MPC | 动力学预测准确、速度快 | PhysTwin, PGND, Picasso |

**轴三：保真度目标**

| 目标 | 含义 | 代表 |
|---|---|---|
| 数字孪生（twin） | 精确复现一个真实场景 | RialTo, DRAWER, PolaRiS |
| 数字表亲（cousin） | 与真实场景语义/几何相似的一组变体 | ACDC, SimFoundry, Seeing2Sim |
| 生成式分布 | 从真实输入出发生成大量任务与场景 | GRS, Video2Policy, RoboTwin |
| 学习型世界模型 | 不显式重建，直接从数据学习动作条件的视频模型 | Ctrl-World, Veo-WS, WorldGym |

一个典型的 2025–2026 流水线：

```
真实输入（扫描 / 视频 / 单图 / 交互）
  ├─ 几何：图生 3D（SAM 3D, Hunyuan3D, TRELLIS）+ 度量布局（MoGe, VGGT）+ 凸分解碰撞（V-HACD, CoACD）
  ├─ 铰接：检索（PartNet-Mobility）或前馈推断（Particulate）→ URDF
  ├─ 外观：3DGS 背景 + 网格前景
  ├─ 物理：VLM 先验 / 交互辨识 / 可微仿真
  └─ 组装进 Isaac Sim / IsaacLab / MuJoCo / ManiSkill / Genesis
        → 训练 / 数据生成 / 评测 → 真机
```

RoboSnap、DEXTERA、SimFoundry、SceneRig 都是这种结构的实例。

## 2. 几何、布局与资产（P§1, P§2, P§5）

### 2.1 场景 → 可仿真环境

- **起点**：RialTo 证明手机扫描 + 在 GUI 中手工加几分钟关节，得到的孪生足以针对准静态任务做 RL 微调；"inverse distillation" 把少量真实示教迁移进孪生。CASHER 用众包扫描摊销每个场景的人力，并让通用策略逐步替代人工示教。
- **去掉人工环节**：DRAWER 从无交互视频自动推断抽屉/门关节，表示上用 SDF 几何 + 网格锚定的高斯外观；HoloScene 把整个场景优化成带刚体参数和支撑关系的场景图，物理仿真在优化循环内。
- **单图起点（2026）**：RoboSnap、SceneRig、DEXTERA 从一张图出发，用基础模型拼装场景：SAM 3D 或 Hunyuan3D 出物体，MoGe/VGGT 出度量布局，VLM 给质量与摩擦，Particulate 或检索给关节。RoboSnap 和 DEXTERA 只对交互区域保留网格，背景只用高斯渲染。
- **设计轴**：输入成本（扫描 / 视频 / 单图）、碰撞几何由观测决定的程度、渲染与物理如何切分。单图最便宜，但被遮挡的几何、物理参数和关节都只能靠先验。

### 2.2 孪生、表亲与生成式分布

- **是否需要精确孪生**：ACDC 用多个匹配资产组成的"表亲"分布训练，零样本 sim-to-real 成功率 90%，精确孪生为 25%。URDFormer 学习图像 → URDF 的逆映射，从真实图像生成铰接场景。
- **生成式扩展**：GRS、Video2Policy、RoboTwin 用检索或生成的资产 + LLM 写的任务、奖励或专家代码换取数据规模。Video2Policy 报告仿真 72%、真实 47%。
- **2026 年两条线合流**：SimFoundry 从单视频建孪生，再沿物体/场景/任务三个轴生成表亲，分别带来约 17%/21%/40% 的真实成功率提升；同时报告评测相关性（7 个任务 × 5 个策略，平均 Pearson 0.911）。Seeing2Sim 从全景图做同样的事。
- **保真度对评测的影响已有定量结果**：
  - AssetFidelity-Eval：度量几何 + 人工设定物理的孪生 r=0.90，默认单图流程 r=0.51；平均分数误差 6.97 vs 17.54 个百分点。论文自述两套流程同时改变了多个因素，无法归因到单一因素。
  - SceneRig：逐 episode 与真实一致率 69%，SimFoundry 为 54%。

### 2.3 资产来源与物理有效性

- **图生 3D 成为默认资产源**：SAM 3D Objects、TRELLIS/TRELLIS.2、Hunyuan3D 2.1–3.1、InstantMesh、Rodin 出现在上述大部分流水线中。
- **开箱即用不够**：SVMR-Bench 用机器人标准（5 mm 精度、初始无碰撞、静止位姿稳定、遮挡鲁棒、2 s 内出场景）评测 13 个模型，无一满足。
- **物理从后处理变为重建约束（2026）**：SimuScene 把重力下的失稳当作修正信号；Picasso 做接触图引导的拒绝采样；PhysConsistent-R2S 在接触图上用可微刚体仿真优化位姿、质心、质量和摩擦。
- **碰撞几何**几乎都用凸分解（V-HACD、CoACD）；AssetFidelity-Eval 指出凸分解对凹物体拟合最差。
- **质量与惯性**：多数流水线问 VLM（SimFoundry、RoboSnap、DEXTERA、AssetFidelity-Eval）。Scalable Real2Sim 是实测路线：机器人抓取物体后做激励轨迹，用关节力矩以带物理可行性约束的 SDP 辨识，质量误差约 1%，但转动惯量误差在基准上为 42%，端到端测试中为 359%。

## 3. 铰接与运动学（P§3, P§4）

- **从观测重建**：PARIS、DigitalTwinArt 从两个关节状态的多视图逐物体优化，不依赖类别先验；ArtGS 改用高斯处理复杂多部件物体；VideoArtGS、Articulat3D 借预训练点跟踪器的运动先验，把输入放宽到一段随手拍的单目视频。趋势是采集更便宜、部件更多；代价是逐物体优化，且物体必须在镜头前被动过。这些方法都不估计关节限位、摩擦或阻尼，其中只有 VideoArtGS 提供 URDF/USD 导出。
- **从先验推断/生成**：目标是用最少输入得到可加载的仿真文件。
  - 代码生成：Real2Code 在 OBB 抽象上用 LLM 写 MJCF；Articulate-Anything 用 VLM actor–critic 写 URDF，网格从 PartNet-Mobility 检索，PartNet-Mobility 上成功率 75%，基线为 8.7–12.2%。
  - 生成模型：SINGAPO、URDFormer 在部件模板上做生成或逆建模。
  - 任意网格加关节：Articulate AnyMesh、Particulate、MotionAnymesh，与图生 3D 天然配合；DEXTERA 即用 Particulate 给 Hunyuan3D 物体加关节。
  - 端到端（2025–2026）：URDF-Anything、SPARK、PhysX-Anything、URDF-Anything+ 从图像或点云直接到 URDF，以"物理可执行性"评价。PhysX-Anything 还预测尺度、材料和可供性。
- **设计轴**：检索还是生成（检索的网格干净但覆盖有限）、多阶段还是端到端、是否涉及物理（只有 PhysX-Anything 预测物理属性；MotionAnymesh、SPARK 优化无碰撞运动）。

## 4. 外观：渲染耦合仿真（P§6, P§7）

### 4.1 高斯/NeRF + 物理仿真

- **问题**：在网格渲染仿真器中训练的 RGB 策略到真实相机上失效。
- **2024：把高斯挂到刚体上**：SplatSim、RL-GSBridge 在 PyBullet 中让机器人连杆的高斯随 FK 运动、物体高斯随仿真位姿运动。Embodied Gaussians 把高斯绑定到 PBD 粒子上，用渲染误差反过来修正物理状态。
- **2025：混合表示与框架化**，网格负责接触、高斯负责像素：Re3Sim（GS 背景 + 光追网格前景）、RoboSimGS（GS + MLLM 推断的物理/运动学基元）、GSWorld（GSDF 高斯-网格资产）、DISCOVERSE（GS + MuJoCo，约 650 FPS）、TwinAligner（视觉对齐之上加动力学辨识）。
- **示教从哪来**：仿真遥操作（SplatSim）、特权规划器或 TAMP（Re3Sim、DREAM）、对少量真实示教做等变变换（DreMa）、从人类视频做 RL（X-Sim）。
- **逼真渲染的作用**：DISCOVERSE 的对比表中，GS 类仿真零样本真实成功率 44–55%（ACT，无增广），网格仿真为 6–14.5%；该表由作者自己跑。
- **剩余差距**：零样本成功率通常仍低于真实数据训练：SplatSim 86.25% vs 97.5%；TwinAligner 多数设置低于真实数据训练。

### 4.2 不做闭环动力学的数据生成

- R2R2R 关闭动力学，IsaacLab 只作渲染器，运动学重定向人类示教；1 段人类示教训练的策略与 150 条遥操作示教相当。
- RoboSplat 直接编辑单条示教的高斯，沿 6 个泛化轴增广，单示教真实成功率 87.8%，数百条真实示教 + 2D 增广为 57.2%。
- ReBot、RoLA 把仿真渲染合成到修复后的真实背景或照片上。RoLA 的消融：混合回原照片 85.4%，直接网格渲染 11.7%。
- 代价：接触不经物理检验，不能用于闭环评测。

## 5. 物体物理参数（P§11, P§12, P§14）

### 5.1 刚体系统辨识与仿真参数推断

- **黑盒闭环**：SimOpt 定义了 real2sim 闭环：仿真器视为黑盒，用少量真实 rollout 以 REPS 调整域随机化分布。BayesSim、NPDR 换成 likelihood-free 后验；DROPO 把仿真重置到记录的真实状态，离线最大化下一状态的高斯近似似然。
- **梯度路线**：gradSim（可微仿真 + 可微渲染，从像素求梯度）、RigPI（NVIDIA Newton 中梯度精化）。代价是局部极小和对可微接触的要求。
- **采什么数据成为独立设计轴（2023 起）**：ASID 用 Fisher 信息规划探索，SPI-Active、IDTD 设计解耦的激励轨迹，ASBI 按信息增益选动作。
- **匹配什么**：AdaptSim 以任务表现而非动力学匹配为目标。
- **基础模型先验（2025–2026）**：Phys2Real 按逆方差融合 VLM 估计与在线估计；RigPI 用 VLM 初始化并限定梯度搜索范围；VLM-BT Real2Sim 让 VLM 决定探测哪些参数、怎么探测。

### 5.2 可变形、颗粒与流体物理孪生

- **起点**：PAC-NeRF 把可微 MPM 与神经渲染耦合，从多视角视频辨识几何与材料参数。之后 3DGS 成为默认表示：PhysGaussian 作为前向仿真载体，GIC、Spring-Gaus 用于辨识。
- **物理模型轴**：
  - 弹簧-质点（Spring-Gaus、PhysTwin、EgoPhys）：快，适合绳、布、毛绒，可有稠密刚度，但只能表达弹性。
  - MPM（PAC-NeRF、GIC、DPSI、MOSIV、FORM）：覆盖塑性、颗粒和流体，但慢且数值刚性；DPSI 必须给杨氏模量设上限才能稳定。
- **监督来源轴**：真实多视角视频（PAC-NeRF、GIC、Spring-Gaus）；机器人交互 + 点云或力（DPSI、FORM、PhysTwin）；生成视频先验（PhysDreamer、OmniPhysGS）。
- **本构律轴**：固定律少量参数 → 空间变化场（PhysDreamer、PhysTwin）→ 学习修正（NeuMA）→ 专家混合（OmniPhysGS）→ LLM 提出符号本构律（VisionLaw）。PGND 完全学习动力学，以可解释性换跨材料精度。
- **2025–2026 趋势**：前馈/摊销估计（Pixie、VoMP、EgoPhys）、多物体场景（MOSIV）、非迭代辨识（FORM，2–5 s vs 迭代基线 10–25 min）、用孪生为世界模型生成数据（PhysWorld-MPM）。
- **面向机器人的代表**：PhysTwin 用三视角 RGB-D 交互视频，先零阶采样再一阶梯度，得到可实时仿真、可用于模型规划的形变孪生；Real2Sim-Eval 把它用作软体评测后端（§7）。

### 5.3 残差物理与混合仿真

- **残差放在哪里**：控制输出（TossingBot 修正释放速度）、引擎内部（NeuralSim）、力（Gao et al. 在 FEM 上学残差力）、本构律（NeuMA）、整个求解器（NeRD 用学习的机器人中心模型替代求解器，可用真实数据微调；真实抛方块数据上位置误差从 0.036 m 降到 0.018 m）。
- **约束残差以保泛化（2026）**：CLASH 把 gap 拆成辨识的接触参数 + 早停的小残差，只用约 10 次真实碰撞；RAFL 让残差成为局部、拓扑无关的场，以跨形态迁移；Neural Fidelity Calibration 同时推断参数和残差的后验。
- **权衡**：残差越有表达力，训练数据拟合越好，外推越差；局部化和正则化是目前的应对。

## 6. 机器人侧动力学对齐（P§13）

- **学习执行器**：ActuatorNet 指出执行器动力学主导足式 sim2real gap，并用真实力矩数据监督学习执行器网络。
- **无力矩传感器**：UAN（修正力矩）与 ASAP（整机残差动作 Δa(s,a)）用 RL 训练修正量，让仿真复现真实编码器或动捕轨迹；NeuralActuator、Kovalev et al. 通过可微仿真从位姿轨迹反传。
- **参数化辨识并行发展**：SPI-Active（基座惯性与电机增益 + 主动激励）、IDTD（打破参数耦合）、HALO（可微仿真中辨识负载）、Bjelonic et al.（从执行器到整机自底向上辨识，策略迁移不再需要动力学随机化）。
- **同一目标下的对比**：Dao & Fern 在不需动捕、不需时间对齐的本体感知分布匹配目标下，比较参数辨识、残差动作、残差执行器三种模型，回应了 ASAP 自述的动捕依赖。
- **权衡**：残差/增量模型能吸收未建模效应，但不透明且数据需求大，ASAP 称完整 23 自由度残差模型不现实；参数化辨识可解释、数据高效，但受模型类和激励充分性限制。
- **与人形动作跟踪的交点**：ASAP、VideoMimic 同时是人形全身控制谱系的节点；SuperMimic 把"用真机数据细化学习型世界模型并利用其可微性做系统辨识"列为未来工作；同期的 HumanoidNDM（CoRL 2026）在真机数据上训练人形神经动力学模型，经模型反传梯度在线微调跟踪策略，不需要动捕。见 [humanoid-motion-tracking](../humanoid-motion-tracking/README.md)。

## 7. 策略评测（P§8, P§9, P§10）

### 7.1 物理仿真评测

- **协议**：SIMPLER 确立了配对评测协议：同一组策略在仿真和真实中各跑一遍，用 MMRV 和 Pearson r 衡量排序一致性。绿幕 + 纹理匹配的 visual matching（Google Robot 平均 r=0.924，MMRV 0.056）优于 variant aggregation（r=0.778，MMRV 0.143）。绿幕要求固定相机，无法评测腕部相机策略。
- **高斯评测器**：
  - Real-is-Sim 在线保持与现实同步的孪生；离线评测即关闭跟随器。
  - GSWorld、Real2Sim-Eval 把 GS 渲染与 ManiSkill 或 PhysTwin 配对。Real2Sim-Eval 三个任务（玩具装箱、绳、push-T）r 为 0.901–0.944；同任务 IsaacLab 基线 r 为 0.237（绳）和 0.649（push-T）。
  - PolaRiS 加入短暂仿真联合训练（90/10 真实/仿真混合，约 1k 步），使 DROID 通用策略在新场景中可评测；6 个场景平均 r=0.90（最差 0.81），与 RoboArena 分数 r=0.98。
  - RobotArena∞ 走另一条扩展路线：把已有数据集视频转成生成网格孪生，用 VLM 与众包偏好替代配对真实评测。
- **何时够用（2026）**：
  - ReVeal：重建质量决定一致性，2DGS → PGSR → PGSR-D 的 r 为 0.773 → 0.850 → 0.960。
  - YUBI-Real2Sim：9 个场景–任务组合中 8 个复现了真实排序，但新视角质量分数不能作为场景验收规则。
  - AssetFidelity-Eval、SceneRig、SimFoundry 的结果见 §2.2。
- **典型验证规模**：2–8 个策略 × 3–8 个任务，每格 10–60 次真实试验。

### 7.2 学习型世界模型作为评测器

- **思路**：不建资产、不跑物理，从机器人日志学动作条件视频模型，在其中 rollout 策略，用人或 VLM 判定成功。
- **演进**：可信度展示（UniSim）→ 显式验证评测器（WorldEval 3 任务 r=0.942；WorldGym 17 任务 r=0.78；Ctrl-World；Veo-WS 1600+ 次真实评测，OOD r=0.86）→ 针对已知失效模式（Mem-World 解决遮挡下的记忆，WEAVER 解决速度与时长，PhysCanvas 用触觉与结果奖励后训练）。
- **反复出现的验证结论**：排序常能保持，但绝对成功率偏低（Ctrl-World 中 π0.5 Close-Laptop 真实 0.70、世界模型 0.05；Veo-WS 同样偏低）；失败集中在接触密集与小物体交互。
- **唯一的正面对比**：PolaRiS 测得 Ctrl-World 的 MMRV 为 0.22，并把错排归因于幻觉。
- **额外能力**：同一模型可兼作数据引擎（DreamGen、Genie Envisioner、Ctrl-World / WEAVER 后训练），物理评测器没有这一用途。

### 7.3 视觉 gap 指标

- 检索范围内没有论文验证过图像级指标（PSNR、FID、嵌入距离）能预测策略迁移。实际使用的都是结果级指标：MMRV、Pearson r、成功率绝对差。
- 受控证据：逼真度提升真实成功率，但超过中等光追（4 spp）后饱和（Sim2Real-VLA study）；评测相关性上 GS 渲染优于光追或贴图网格（PolaRiS 消融）；几何重建质量决定一致性（ReVeal）。
- 反面证据：新视角质量分数不能可靠预测排序可靠性（YUBI-Real2Sim）；复杂任务上 FID 相关性差（WorldEval）；视频质量 ≠ 功能效用（WorldArena、World-in-World）。

## 8. 场景扩展（P§15, P§16, P§17）

### 8.1 足式运动与导航

- **标准配方**：几乎都是 3DGS 负责渲染、单独的碰撞网格负责物理。网格来自融合渲染深度（Vid2Sim、VR-Robo）、NKSR（GaussGym）或 LiDAR（Wanderland）；训练在 Isaac Sim/Gym、Unity 或 Habitat 中进行。
- **从单场景到规模化**：从每个部署点一个场景（VR-Robo、EmbodiedSplat），到多源前馈重建（GaussGym）、网络视频语料（Vid2Sim → S2E）、检索资产代替重建（UrbanVerse）。
- **设计轴**：采集设备（手机 / RGB-D / LiDAR）；重建、检索还是生成（VR-Robo / UrbanVerse / LucidSim）；静态还是动态场景（ReaDy-Go 加入行人）；只对齐视觉还是也对齐物理（QuadVerse 加入摩擦后验与执行器残差）。
- **度量可靠性**：Wanderland 测得纯视频重建有米级轨迹误差和碎片化网格，在 Vid2Sim 场景中做 RL 微调反而损害策略。
- **向人形迁移（2026）**：VLK、LEGS 用 GS 场景合成训练数据并微调 VLA，而不是做 RL。

### 8.2 自动驾驶

- **演进**：UniSim（从日志做神经闭环仿真）→ NeuRAD（传感器物理）→ OmniRe（全部动态参与者含行人）→ HUGSIM（实时 3DGS 闭环基准）→ RAD（逐段 3DGS 场景中大规模 RL，碰撞率降为 1/3）。
- **评测与数据规模**：NAVSIM v2 用预渲染视角替代序列仿真（与闭环 R²=0.8）；SimScale 显示规划器收益随仿真数据量持续增长；REAP 用于泊车。
- **核心权衡**：自车偏离记录轨迹后图像质量下降，回放的其他车辆不会对自车做出反应。
- **分化**：RAD-2 改用 BEV 特征扭曲仿真器，Cosmos-Drive-Dreams 改用生成式世界模型，均不再显式重建。

### 8.3 人类视频 → 仿真

- **人形分支**：VideoMimic 从单段视频重建度量人体 + 场景，用 RL 跟踪；CRISP 用接触引导的平面基元得到更干净的场景几何；HDMI、Real2Sim-HOI 加入物体交互。
- **灵巧手分支**：重建物体而非场景，人类只提供奖励和初始化，不作为动作标签：Human2Sim2Robot、Video2Policy、Video2Sim2Real、Dex-One2Many。
- **设计轴**：重建什么（人 + 场景 / 只有物体）；物理如何修正运动学（RL 跟踪、SPIDER 的采样、DexMachina 的虚拟物体控制器）；场景表示（单一刚体网格 / 基元）；部署时的感知（本体 + 高度图 / 动捕）。

## 9. 2025–2026 横向趋势

每条均可由所列论文直接观察到。

1. **单图 + 基础模型拼装**取代扫描：RoboSnap、SceneRig、DEXTERA、SimuScene、RoLA。
2. **"GS 渲染 + 网格物理"成为默认分工**：VR-Robo、Re3Sim、RoboSnap、DREAM、GaussGym、Isaac Lab（NuRec）、RoboVerse、DISCOVERSE。NVIDIA 文档说明 NuRec 体积只用于渲染，没有物理属性。
3. **VLM 成为物理参数的默认来源**：SimFoundry、RoboSnap、DEXTERA、RoboSimGS、Phys2Real、RigPI。DEXTERA 自述 VLM 推断的物理参数不精确，影响多步任务。
4. **物理约束进入重建过程**：SimuScene、Picasso、PhysConsistent-R2S、HoloScene。
5. **前馈化与摊销化**：Particulate（关节）、Pixie、VoMP（材料场）、EgoPhys（刚度）、FORM（非迭代辨识）。
6. **评测成为主要用途，"孪生何时够用"成为核心问题**：PolaRiS、ReVeal、YUBI-Real2Sim、AssetFidelity-Eval、SceneRig、SimFoundry。
7. **学习型世界模型成为并行范式**，且已有与物理评测器的直接对比：Ctrl-World、Veo-WS、WEAVER、Mem-World、PolaRiS。
8. **向人形与移动操作扩展**：VideoMimic、ASAP、VLK、LEGS、GaussGym（T1 人形）。

## 10. 文献自述的开放问题

| 问题 | 陈述来源 |
|---|---|
| 只支持刚体，无法处理布、液体、植物、颗粒 | SplatSim, RoboGSim, Re3Sim, X-Sim, DREAM, TwinAligner, SIMPLER, RoboSnap, CASHER, GaussGym |
| 关节推断只有转动/平移，缺关节限位、摩擦、阻尼；多自由度与闭链未解决 | URDFormer, Real2Code, SPARK；RealityGap-Survey 称关节推断仍有"considerable gap" |
| 物理参数靠手设或 VLM 猜测 | Re3Sim, X-Sim, PolaRiS, ReVeal, RoboSnap, DEXTERA, GRS |
| 接触参数未辨识；转动惯量难辨识 | Scalable Real2Sim, ASID |
| 光照烘焙，插入物体与场景光照不一致 | RoboGSim, DISCOVERSE, RL-GSBridge, DRAWER；PolaRiS 认为 GS 可能需要让位于基于扩散的渲染 |
| 重建与人工成本仍是瓶颈 | RoboSimGS, DISCOVERSE, TwinAligner, SIMPLER, Real2Sim-Eval, VR-Robo, Vid2Sim |
| 单视图重建不满足机器人要求，几何指标好不等于任务成功 | SVMR-Bench |
| 可观测性：遮挡下视觉修正失效，需要完整观测 | Real-is-Sim, DreMa |
| 评测覆盖与统计量不足；尚无可靠的场景验收规则 | Real-is-Sim, Real2Sim-Eval, PolaRiS, RobotArena∞, YUBI-Real2Sim；RealityGap-Survey 称让仿真评测对齐真实表现仍是开放问题 |
| 视频重建度量不可靠 | Wanderland, VideoMimic（"monocular 4D human–scene recovery is still brittle in the wild"） |
| 动态场景、非刚性行人、偏离记录视角后质量下降 | RAD, HUGSIM, GaussGym, Wanderland |
| 辨识病态、多解与局部极小 | DPSI, PhysConsistent-R2S, DROPO, SPI-Active；RealityGap-Survey 称基于仿真的推断是病态的 |
| 机器人侧对齐依赖动捕、损耗硬件、高维残差模型数据需求大 | ASAP, SPI-Active, UAN |
| 世界模型评测器：幻觉、接触与小物体失真、绝对成功率偏低、依赖人工打分 | WorldEval, WorldGym, Ctrl-World, Veo-WS, PhysCanvas |

## 11. 现有综述与本分类的对照

检索范围内没有专门以 real2sim 为主题的综述；它作为一类方法出现在 sim-to-real 综述中，或作为 3D 生成的一种用途出现。

| 综述 | 组织方式 | real2sim 的位置 |
|---|---|---|
| RealityGap-Survey | gap 成因：动力学、感知、执行、系统设计；方法：缩小 vs 克服 | "Real-to-Sim First" 归在改进仿真下，拆成几何、运动学/动力学、渲染三个逆问题 |
| 3DGen4Robot-Survey | 3D 生成的三种角色：数据生成器、仿真环境、Sim2Real 桥 | 桥内再分场景重建、运动学重建、物理/视觉–动力学对齐；不含室外与驾驶 |
| 3DGS-Robotics-Survey | 场景理解 vs 交互；技术进展分适应性与效率 | 只作为未来方向出现 |
| NeuralFields-Survey | 4 种表示 × 5 个领域 | 分散在各领域中 |
| DT2EAI-Review | 无正式分类；孪生中训练、人体孪生、大规模环境孪生三种协同 | 孪生中训练 |

本综述的三轴框架（重建对象 × 用途 × 保真度目标）与 RealityGap-Survey 的三个逆问题对应，并把机器人侧动力学单列，把评测作为一种用途显式区分。

## 12. 入门阅读顺序

| 顺序 | 论文 | 理由 |
|---|---|---|
| 1 | RealityGap-Survey | 交代 real2sim 在 sim-to-real 方法中的位置，以及为什么几何、动力学、渲染是三个独立的逆问题 |
| 2 | RialTo | 现代操作 real-to-sim-to-real 闭环的定义，说明一个可用孪生最少需要什么 |
| 3 | ACDC | 提出数字表亲，引出贯穿后续文献的孪生 vs 表亲问题 |
| 4 | SplatSim | 在刚体仿真上叠加 GS 渲染做零样本 RGB 策略迁移的最小配方 |
| 5 | SIMPLER | 配对仿真/真实评测协议与 MMRV、Pearson 指标的来源 |
| 6 | PolaRiS | 当前 GS 评测通用 VLA 的参考，含渲染与联合训练消融和对世界模型评测器的直接对比 |
| 7 | SimOpt → ASID | 黑盒参数分布闭环，以及"采什么真实数据"如何决定辨识质量 |
| 8 | PhysTwin | 面向机器人的形变物理孪生，零阶 + 梯度两阶段逆物理 |
| 9 | ASAP（配合 SPI-Active） | 机器人侧对齐的残差动作路线与参数化路线 |
| 10 | SimFoundry（配合 SceneRig、AssetFidelity-Eval） | 2026 年端到端流水线及保真度对评测影响的定量证据 |
| 11 | VR-Robo → GaussGym → Wanderland | 运动/导航中"GS 渲染 + 网格物理"的配方、规模化版本与度量可靠性反证 |
| 12 | Ctrl-World（配合 Veo-WS） | 学习型仿真器评测的代表，及其与现实分歧之处 |
