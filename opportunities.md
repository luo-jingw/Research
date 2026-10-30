# OPT-001

Status: open

Area: real2sim

## Observation

- ReVeal：重建质量决定评测一致性，2DGS → PGSR → PGSR-D 的 Pearson r 为 0.773 → 0.850 → 0.960。
- YUBI-Real2Sim：新视角合成质量分数不能作为场景验收规则。
- AssetFidelity-Eval：两套重建流程 r 为 0.90 vs 0.51，但论文自述两者同时改变了多个因素，无法归因。
- 检索范围内没有论文验证过图像级指标（PSNR、FID、嵌入距离）能预测策略迁移（`topics/real2sim/survey.md` §7.3）。

## Opportunity

一个在跑真实评测之前就能判断"这个孪生能否保持策略排序"的验收指标。

## Expected Mechanism

假设：策略排序错误主要来自任务相关区域（接触面、目标物体位姿、交互动力学）的误差，而非全局渲染质量；按交互区域或策略注意力加权的几何/外观/物理误差，与 MMRV 的相关性应高于全局 PSNR 或新视角质量。

## Required Evidence

- 一组"孪生变体 × 策略 × 任务"的配对仿真/真实评测结果；
- 每次只改变一个因素（几何、外观、物理）的受控消融，补上 AssetFidelity-Eval 的混杂因素问题。

## Promotion Condition

能获得公开的配对仿真/真实评测数据，或有可做配对评测的真机平台与至少 3 个策略。

# OPT-002

Status: open

Area: real2sim

## Observation

- 多数高斯渲染仿真的物理参数靠手设或 VLM 给出：Re3Sim、X-Sim、PolaRiS、ReVeal、RoboSnap、DEXTERA。
- 物理辨识方向（`survey.md` §5）的工作很少用逼真渲染下的视觉策略做评测；例外有 TwinAligner、QuadVerse、Real2Sim-Eval、PhysConsistent-R2S。
- Real2Sim-Eval 在绳任务上，PhysTwin 孪生 r=0.901，IsaacLab 基线 r=0.237。
- 刚体桌面任务上，外观的影响很大：RoLA 混合渲染 85.4% vs 直接网格渲染 11.7%；RoboSplat 87.8% vs 57.2%。
- 训练侧 ACDC 表亲 90% vs 孪生 25%；评测侧 AssetFidelity-Eval、SceneRig 显示更高保真度带来更高一致性。

## Opportunity

按任务类型对 real2sim 的保真度因素做归因，再只在任务需要的地方加入交互式物理辨识（如 ASID 式主动探索）。

## Expected Mechanism

假设：
- 刚体准静态任务中外观主导，接触密集与可变形任务中物理主导；
- 评测需要孪生级保真度，训练受益于表亲级多样性。

## Required Evidence

- 覆盖刚体准静态、接触密集、可变形三类任务的受控实验，分别替换外观、几何、物理参数；
- 同时报告训练侧（零样本真实成功率）与评测侧（Pearson r、MMRV）。

## Promotion Condition

OPT-001 的配对评测数据或平台可用；或选定一类任务作为研究课题时。

# OPT-003

Status: open

Area: humanoid-motion-tracking, real2sim

## Observation

- SuperMimic 的世界模型只从仿真转移学习，以仿真上下文 ξ（摩擦、标定偏置、躯干质心）为条件；论文把"用真机数据细化世界模型、利用其可微性做系统辨识"列为未来工作。
- HumanoidNDM 在真机数据上训练人形神经动力学模型，经模型反传梯度在线微调跟踪策略；其摘要未提及仿真预训练先验。
- RWM-U：约 1 h 真实数据混入有益，更多反而变差，因为真实日志缺少失败转移，仿真仍不可少。
- NeRD、PIA：仿真预训练的神经仿真器用少量真实数据微调即可显著降低误差。
- SPI-Active、ASAP：人形侧系统辨识与残差对齐目前用 CMA-ES 或 RL，不经可微模型。

## Opportunity

以 SuperMimic 式仿真预训练、ξ 条件化的可微世界模型为先验，用少量真机日志：
1. 对 ξ 做梯度式系统辨识；
2. 必要时在冻结主干上微调一个小残差；
3. 继续用 BPTT 更新策略。

## Expected Mechanism

假设：ξ 条件化的世界模型已经覆盖了域随机化范围内的动力学族，真机 gap 中可参数化的部分可以靠反求 ξ 吸收，剩余部分由小残差吸收；仿真先验提供真实日志中缺失的失败转移，避免 RWM-U 观察到的真实数据过多反而变差的问题。

## Required Evidence

- 用真机或作为替身的第二个仿真器（sim-to-sim）验证：反求出的 ξ 能否降低多步预测误差，并提升跟踪回报；
- 与 HumanoidNDM（纯真机数据模型）、ASAP（残差动作）、SPI-Active（采样式辨识）在相同数据量下对比。

## Promotion Condition

SuperMimic 官方代码发布，或某个非官方复现在全量 BONES-SEED 上达到论文水平；并有可用的人形真机或可信的 sim-to-sim 替身。

# OPT-004

Status: open

Area: humanoid-motion-tracking

## Observation

- RWM 报告 SHAC 式 BPTT 经其学习的腿足世界模型不收敛，因而改用模型内 PPO。
- SuperMimic 用同类 BPTT + critic 在人形跟踪上稳定收敛，且比同一世界模型上的 PPO 少约 64× 想象步数。
- 两者的差异包括：SuperMimic 的世界模型在训练中用自身策略的数据持续重拟合，RWM 用其他策略的轨迹预训练；SuperMimic 的模型是确定性的并以 ξ 为条件；跟踪奖励逐步稠密；终止用可微的软生存权重而非硬截断。
- 两篇论文都没有分析哪个差异决定了收敛性。

## Opportunity

确定"经学习世界模型做 BPTT"在腿足/人形控制中收敛的充分条件。

## Expected Mechanism

假设：上述差异中至少一项（在线重拟合以保持模型在当前策略分布上准确、稠密奖励、软终止）是收敛的必要条件。

## Required Evidence

在同一任务与世界模型结构上，逐一切换上述四个因素的受控实验，报告收敛与否、回报和梯度方差。

## Promotion Condition

有可运行的 SuperMimic 实现（官方或已验证的复现）与 RWM 开源代码（github.com/leggedrobotics/robotic_world_model）。

# OPT-005

Status: open

Area: vla-fast-control, real2sim

## Observation

- 加速失败的主要原因是控制器与机器人–物体动力学变化、推理延迟、精确阶段不耐加速（`topics/vla-fast-control/survey.md` §3.1）。SAIL 自述没有处理动力学变化，呼吁引入动力学模型或仿真数据。
- RACE、RoboPace 的重定时只考虑机器人运动学限幅；RoboPace 报告只考虑物理限幅的重定时在接触附近"largely fail"。
- 真机 RL 能同时提升成功率与节拍（HIL-SERL 1.8×、π*0.6 吞吐 >2×、RLT 关键阶段最多 3×），代价是人工奖励标注、干预与复位（π*0.6 自述）。
- 仿真 RL 已能零真实示教或少量示教提升真机成功率（SimpleVLA-RL、GenWorld-RL、RL-Co），GenWorld-RL 报告真机执行快 1.13×；这些工作的优化目标是成功率，不是节拍。
- Sim&Real Pushing：接触任务中物理 gap 比视觉 gap 更重要。
- 检索范围内没有同时做到"少量遥操作示教 + 动力学经辨识的仿真 + 以节拍为优化目标"的工作（survey.md §5）。

## Opportunity

从少量遥操作示教微调的 VLA 出发，在动力学经辨识、并注入实测推理延迟的仿真孪生中，用 RL 以节拍为目标训练速度头或残差，同时用真实示教做锚定，再零样本或少量真机 RL 部署。

## Expected Mechanism

假设：
- 加速失败中可由仿真复现的部分（机器人与物体的动力学变化、推理延迟导致的块错位）占主导；动力学经辨识（参照 real2sim 综述 §5–§6 的 ASID、SPI-Active、PhysTwin）后，仿真中学到的提速能迁移到真机；
- 仿真承担高速区域的探索，避免真机 RL 的人工复位与安全成本；真实锚定防止策略偏离示教的精确阶段。

## Required Evidence

在同一任务与机器人上对比：
1. 示教重定时（DemoSpeedup）；
2. 推理时重定时（RACE 或 SAIL）；
3. 默认物理参数仿真中的节拍 RL；
4. 辨识后物理参数仿真中的节拍 RL。

报告真机节拍、成功率，以及仿真与真机节拍之差，并分别消融动力学辨识与延迟注入。

## Promotion Condition

确定具体机器人与任务，有可用的仿真（IsaacLab / ManiSkill / MuJoCo）孪生，并能采集该任务的少量遥操作示教。
