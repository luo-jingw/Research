# 人形动作跟踪与可微世界模型综述

- 快照日期：2026-10-30
- 锚点论文：SuperMimic（arXiv:2610.28480，CoRL 2026 Oral），精读见 [notes/2026-supermimic.md](notes/2026-supermimic.md)。
- 引用格式：方法简称，元数据见 [papers.md](papers.md)，节号写作 `P§n`。
- 本文只写可溯源到文献的内容。基于这些文献提出的研究设想记录在根目录 `opportunities.md`（`Area: humanoid-motion-tracking`）。

## 0. 定义与范围

基于物理的动作跟踪（physics-based motion tracking / motion imitation）：在仿真中训练策略，让机器人跟踪重定向后的人体参考动作（动捕或视频），再部署到真机。跟踪器训练好之后，往往作为通用的底层全身控制器，由遥操作、速度指令、扩散引导、VLA token 等上层接口驱动。

SuperMimic 同时属于两条谱系：

1. **动作跟踪谱系**：DeepMimic → PHC → H2O → BeyondMimic → SONIC → SuperMimic。核心问题是怎样让一个策略覆盖越来越大的动作库，并迁移到真机。
2. **可微学习动力学谱系**：SuperTrack → ControlVAE → MoConVQ → SuperDyno → SuperMimic，旁边还有可微仿真（SHAC、AHAC）和世界模型（Dreamer、RWM）。核心问题是用解析梯度代替 model-free 的似然比梯度。

## 1. 分类框架

| 轴 | 取值 | 代表 |
|---|---|---|
| 训练范式 | 每动作专家 | DeepMimic, ASAP, KungfuBot, BeyondMimic |
| | 专家 → 蒸馏通用策略 | PULSE, OmniH2O, GMT, TWIST, UniTracker, BumbleBee, Humanoid-GPT, OmniXtreme |
| | 单个通用 PPO | PHC, SONIC, HoloMotion-1 |
| | 经学习模型的 MBRL | ControlVAE, MoConVQ, SuperMimic |
| 数据来源 | 动捕（AMASS、LAFAN1、BONES-SEED） | PHC, GMT, SONIC |
| | 视频重建 | ASAP, KungfuBot, VideoMimic, HoloMotion-1 |
| 上层接口 | 遥操作 | H2O, OmniH2O, TWIST, TWIST2 |
| | 速度 / 多模式指令 | ExBody, HOVER, SuperMimic |
| | 扩散引导 | BeyondMimic |
| | token / 潜动作 | SONIC, PULSE, LATENT |
| | 残差物体策略 | ResMimic, HDMI |
| | 提示 | BFM-Zero, METATRON |
| 环境交互 | 平地 | 大多数跟踪器, SuperMimic |
| | 地形 / 物体 / 场景 | SceneBot, PGMT, GigaBrain-WBC-0.5, VideoMimic, HDMI |

## 2. 动作跟踪谱系

### 2.1 图形学根源（P§1）

- DeepMimic 给出模板：模仿奖励 + 任务目标，每段动作训练一个 PPO 专家，可复现翻转、旋转等杂技。AMP 用对抗式运动先验替代逐帧跟踪奖励。
- PHC 证明一个跟踪器可以模仿 98.9% 的 AMASS，并带摔倒恢复。
- NPMP、PULSE、MaskedMimic 把跟踪器蒸馏成潜空间或掩码目标控制器，供下游复用。SuperMimic 的 Table 1 把这些方法统一描述为分阶段流水线：PPO/A2C 跟踪器 → DAgger/BC 潜空间 → PPO 或引导下游。

### 2.2 上真机（2024，P§2）

- H2O / OmniH2O 把这条线搬到 Unitree H1：SMPL 形状拟合重定向，用特权模仿器过滤不可行动作（"sim-to-data"），再从特权教师蒸馏到稀疏输入学生，用于遥操作。OmniH2O 把运动学位姿作为 VR、RGB、自主控制的统一接口。
- ExBody 让上身模仿动作、腿部只跟踪根速度；HumanPlus 用 RGB 影随采数据再学自主技能；HOVER 用一个掩码多模式学生覆盖运动学、关节、根指令三种模式。

### 2.3 2025 年的分化（P§3）

- **专家路线，追求敏捷**：ASAP（每动作专家 + 真机残差动作对齐）、KungfuBot（自适应跟踪容差课程）、BeyondMimic（一套 MDP 与超参数适用于任意动作，不需逐动作调参即可 sim-to-real）。
- **通用路线，追求覆盖**：GMT、TWIST、UniTracker、BumbleBee、Any2Track。几乎都是教师 → 学生 DAgger 蒸馏，学生用 MoE、CVAE 或聚类来对抗行为平均化。
- **蒸馏的代价**：UniTracker 指出蒸馏学生丢失多样性；ExBody2 报告通用性与保真度之间的权衡，在子集上微调会损害其他动作；OmniXtreme 把动作库变大时保真度崩塌称为 "generality barrier"。

### 2.4 规模化（2025–2026，P§4）

三种回应方式：

- **SONIC**
  - 做法：单个通用 PPO，模型 1.2M → 42M 参数，FSQ token 接口
  - 规模：611 h 数据，128 × L40 × 7 天（约 21,000 GPU-h）
- **HoloMotion-1**
  - 做法：稀疏 MoE Transformer 直接用 PPO 训练
  - 规模：>2,000 h，以视频为主，64 × RTX 5090
- **Humanoid-GPT**
  - 做法：约 300 个聚类专家 → 并行 DAgger 蒸馏进因果 GPT
  - 规模：20 亿帧；MLP、TCN 随数据量饱和，Transformer 继续提升

SuperMimic 走第四条路：不扩数据也不换结构，而是降低每单位数据的算力（§4）。

### 2.5 数据与重定向（P§6）

- GMR 显示重定向伪影对跟踪鲁棒性的限制往往大于奖励调参，且对动态和长序列影响最大。
- OmniRetarget 用交互网格 Laplacian 在重定向时保持接触。
- 语料：AMASS 是早期默认语料，GMT 指出其严重偏向步行；PHUMA 做物理筛选；BONES-SEED 是 SONIC 数据的公开部分（142,220 条、288 h），SuperMimic 用其过滤后的 129,514 条、264.56 h。

### 2.6 跟踪器成为接口（P§5）

- 遥操作：H2O、TWIST、TWIST2（免动捕 VR，15 min 采 100 条示教）、GigaBrain-WBC-0.5。
- 扩散引导：BeyondMimic 在潜状态–动作扩散上做 classifier guidance。
- token：SONIC 的 FSQ token 连接规划器、VR 遥操作与 VLA。
- 潜动作：PULSE → LATENT（网球对拉）。
- 残差物体策略：ResMimic、HDMI。
- 提示：BFM-Zero（Forward-Backward 无监督 RL）、METATRON（冻结的提示条件基础策略，技能由编码智能体写成代码）。

### 2.7 离开平地（2026，P§5）

SceneBot 以逐连杆接触标签为条件处理场景交互（搬箱上楼）；PGMT 加入地形感知（越过 37 cm 障碍）；GigaBrain-WBC-0.5 在约 2,200 h 数据上自动标注支撑几何，地形交互成功率 81.3%。VideoMimic 从视频同时重建人与场景，学习上楼梯、坐下等情境技能。

## 3. 可微学习动力学谱系

### 3.1 角色与人形的学习代理模型（P§7）

- **问题**：PPO 跟踪大动作库样本效率低，图形学仿真器又不可微。
- **SuperTrack** 是直接模板：在 8 帧窗口上拟合世界模型，在 32 帧窗口上通过它反传跟踪损失，没有 critic。论文自述的核心局限：前瞻被策略窗口限制，窗口加长又因自回归误差累积而不稳定；探索不如 PPO（摔倒恢复的迈步、足底滑动）。
- **ControlVAE、MuscleVAE、MoConVQ** 继续经学习模型训练，加入生成式技能潜空间，扩展到数十小时动作数据。**SuperDyno** 扩展到数万段动作。
- **DiffMimic** 改用真可微仿真器，需要 Demonstration Replay 稳定长视界梯度。
- 据 SuperMimic Table 1，这一支在 SuperMimic 之前没有真机部署。

### 3.2 可微仿真策略学习（P§8）

- **核心风险**：一阶梯度方差低，但穿过刚性接触时有偏或呈混沌（Suh et al.）。
- **四种应对**：
  - 缩短视界并用 critic 自举：SHAC；AHAC 在刚性接触前自适应截断。
  - 平滑接触物理：Schwarke et al. 用穿透深度的 sigmoid 缩放硬接触力。
  - 前向与反向用不同模型：Song et al. 在 IsaacGym 中高保真前向、在平滑单刚体代理上反传。
  - 熵正则：SAPO。
- **真机足式部署**：Song et al.（Mini Cheetah，2024）、Schwarke et al.（ANYmal D，2025）。代价：Schwarke 报告样本效率比 PPO 高 10× 以上，但单次迭代墙钟更慢；Song 指出奖励必须可微，终止与落脚点需人工设计。这些方法都要求一个自己掌控且可求导的仿真器。

### 3.3 世界模型用于机器人策略优化（P§9）

- **梯度估计器来回摆动**：
  - Dreamer、MAAC：经学习模型的路径梯度 + 终端价值。
  - DreamerV3：连续动作也改用 REINFORCE。
  - RWM：在想象 rollout 上跑 PPO；报告 SHAC 式 BPTT 经其腿足世界模型不收敛，Dreamer 落后。
  - TD-MPC2、Puppeteer：在潜空间做规划，不对策略目标求导。
  - PWM：重新采用一阶梯度，论点是正则化的学习模型比真实接触动力学更平滑；在 152 维 SNU 人形上仍不如 SHAC。
- **真机迁移的两种来源**：直接在硬件上学习（DayDreamer），或仿真预训练的神经仿真器零样本部署（RWM、QWM）。
- **主要风险是模型被利用**：RWM 指出从头训练不稳定，因为策略会利用模型误差，因此世界模型需要预训练。

### 3.4 在真实数据上拟合动力学（P§10）

- **微调仿真预训练的神经仿真器**
  - 代表：NeRD（抛方块位置误差减半）、PIA（<1 h 实车）
  - 策略更新方式：PPO / 规划
- **把真实数据混入模型训练**
  - 代表：RWM-U：约 1 h 真实数据有益，过多反而变差，因为真实日志缺少失败转移
  - 策略更新方式：不确定性惩罚的模型内 PPO
- **在解析仿真或模型上学残差**
  - 代表：ASAP、Ishihara et al.、FADA
  - 策略更新方式：RL 微调 / MPC
- **经可微仿真辨识物理参数**
  - 代表：PIN-WM
  - 策略更新方式：MBRL
- **真机数据训练神经动力学模型 + 经模型反传梯度**
  - 代表：HumanoidNDM
  - 策略更新方式：BPTT

HumanoidNDM（CoRL 2026，2026-10-25 上线）用低频参考扰动自适应采集真机数据，训练基于历史的本体神经动力学模型（借助可微正运动学在欧氏空间中建模），再经模型反传梯度在线微调跟踪策略，不需要动捕。

## 4. SuperMimic 的位置

**在动作跟踪谱系中**：

- 属于"一个通用策略覆盖整个数据集"的分支，与 SONIC 同一机器人（G1）、同一数据来源（BONES-SEED 是 SONIC 数据的公开部分），沿用 BeyondMimic 的跟踪 MDP 与奖励（去掉自碰撞惩罚）。
- 改变的是算力而不是数据或结构：用拟合仿真转移的可微世界模型 + BPTT 替代 model-free PPO。1 × H100 × 3 h 超过 SONIC 已发布 checkpoint 的归一化回报。
- 在 Table 1 的框架下，SuperMimic 把跟踪器、潜空间与下游速度接口放进同一个 MBRL 循环联合训练，避免分阶段蒸馏。
- 论文附录说明：129,514 条基准动作是两种方法的训练动作，失败数衡量覆盖而非泛化；SONIC 也用 SuperMimic 的终止条件判定失败。

**在可微学习动力学谱系中**：

- 配方与 SuperTrack 直接对应：世界模型在 k=8 步窗口上拟合、策略在 H=32 步想象上反传，与 SuperTrack 的 8 帧 / 32 帧窗口相同。SuperMimic 用 SHAC 式终端 critic 解决 SuperTrack 自述的"前瞻受限于窗口"问题；消融中无 critic 时 H≤16 训练失败，有 critic 的策略在推扰下 0.5–2.4 s 内恢复。
- 梯度估计器上属于路径梯度一侧（Dreamer v1、MAAC、PWM），与 DreamerV3、RWM、RWM-U 的模型内似然比梯度相反；报告达到同一世界模型上 PPO 最佳回报所需想象步数少约 64×。
- 接触处理上不去设计可微接触（Song、Schwarke、AHAC），而是对不可微的 MuJoCo Warp 学一个可微代理，与 PWM 的论点一致。
- 与 RWM 的结论相反：RWM 报告 SHAC 式 BPTT 经学习的腿足世界模型不收敛，SuperMimic 在人形跟踪上收敛且稳定。两篇论文都没有分析造成差异的条件。
- 与 RWM 相同，世界模型只用仿真数据，零样本部署到 G1；是 §3.1 这一支中第一个有真机部署的工作。

**与 real2sim 的交点**：SuperMimic 把"用真机数据细化世界模型、利用其可微性做系统辨识"列为未来工作。HumanoidNDM 已经在真机数据上训练神经动力学模型并经其反传梯度微调策略；其摘要把模型描述为真机数据训练，未提及以仿真预训练模型作为先验。见 [real2sim](../real2sim/README.md) §6。

## 5. SuperMimic 的社区复现

论文发布后 10 天内出现多个非官方复现（P§11），均为仓库作者自报结果：

- 只复现 LAFAN1 40 段受控实验的：supermimic_vibed（1.47 GPU-h、回报 0.829，论文为 1.2 h、0.82）、supermimic-mjlab（无域随机化评测，回报 0.895）。AlphaSignal 以"单 GPU 超过 Berkeley 的 H100 结果"为题报道前者，但两者 GPU 不同、GPU-h 更多、只有 40 段动作。
- 复现全量 BONES-SEED 的：realmimic（1 × RTX 4090 × 10.5 h，仅仿真）、SuperMimic-Repro-Sim2Real（严格设置下 LAFAN1 0.56，低于论文的 0.82；真机 G1 舞蹈在多次失败后成功两次）。
- 截至 2026-10-30，没有论文引用 SuperMimic；同期相关工作有 HumanoidNDM、SONIC-K1、METATRON、MimicAll。

## 6. 文献自述的开放问题

- 世界模型只从仿真学习；多接口联合训练研究不足；只在平地（SuperMimic）
- 长期部署缺少安全与能耗的形式化处理（SONIC）
- 扩散策略继承状态估计误差；0.64 s 视界过短；历史依赖导致重复模式，加大引导权重又在动作首尾绊倒（BeyondMimic）
- 缺少起身、翻滚等接触密集技能与地形；AMASS 偏向步行；机器人力矩达不到人体速度（GMT）
- 蒸馏导致行为平均化，MLP 学生泛化差（UniTracker）
- 动作库增大时保真度崩塌，高动态动作在真机上尤甚（OmniXtreme）
- MLP、TCN 跟踪器随数据饱和；大模型在小数据上过拟合（Humanoid-GPT）
- 重定向伪影损害动态与长序列（GMR）
- 需要动捕物体位姿，每个技能一个策略（HDMI）
- 单目 4D 重建脆弱（VideoMimic）
- 重定向中的足底滑动；视频或生成模型得到的动作缺乏物理一致性（SceneBot）
- 指令过滤器只能识别陌生指令，不能识别物理风险；只标注静态支撑（GigaBrain-WBC-0.5）
- 前瞻受限于窗口，长窗口不稳定；探索不如 PPO（SuperTrack）
- 刚性与不连续使一阶梯度有偏、混沌使其方差膨胀（Suh et al.）
- 奖励必须可微，终止惩罚无法优化，需领域特定设计（Song et al.）
- 单次迭代比 PPO 慢；全可微需要额外工作（Schwarke et al.）
- 需要大量已有数据、逐任务重训，人形上扩展性差（PWM）
- 从头训练会被策略利用模型误差；硬件在线学习需恢复策略、特权状态感知与安全约束（RWM）
- 受数据覆盖限制；真实数据缺少失败转移，仍需仿真（RWM-U）
- 未在 20–50 自由度人形上测试；真实微调假设全状态可观（NeRD）
- 硬件损耗（两台 G1 损坏）；依赖动捕；完整 23 自由度残差模型不现实（ASAP）

## 7. 入门阅读顺序

1. **DeepMimic**：模仿奖励与每动作 PPO 的模板
2. **PHC**：从专家到 AMASS 规模的单个跟踪器；其 SMPL 拟合与摔倒恢复被 H2O 线复用到硬件
3. **BeyondMimic**：机器人配方（MDP、奖励、sim-to-real 细节），GMR 用它评测，SuperMimic 直接沿用
4. **SONIC**：规模化参照与 SuperMimic 的直接基线；BONES-SEED 与 token 接口的来源
5. **GMR**：重定向质量常比奖励调参更限制鲁棒性
6. **SuperTrack**：SuperMimic 的直接配方模板，局限写得坦率
7. **SHAC → Suh et al.**：SuperMimic 采用的短视界 BPTT + critic 目标，以及一阶梯度穿过接触为何失效
8. **PWM**："学习模型比真实接触动力学给出更好的一阶梯度"这一论点
9. **RWM → RWM-U**：对照设计：模型内 PPO、不确定性惩罚，以及混入真实数据的证据
10. **SuperMimic**：两条谱系的交汇
11. **HumanoidNDM**：真机数据 + 经模型反传梯度的人形跟踪微调
