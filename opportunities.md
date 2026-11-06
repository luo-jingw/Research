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

# OPT-006

Status: open

Area: sim-real-cotraining

## Observation

- 共训练策略需要同时做到跨域对齐与域可分：只做 OT 或 ADDA 不比普通共训练好（14.3 vs 15.3/30），保留域标签再对齐的 CFG-ADDA 为 21/30（Mechanistic Co-Train）；MMD 特征最对齐但成功率最低（BEACON）。
- 精确孪生能为每个真实状态渲染出对应的仿真帧，配对几乎没有成本；已有的配对式方法只在小任务上有真实数字：BIFROST（Push-T 0.50 vs 0.33）、Invariance Co-training、SARI 的逐相机颜色校准（`topics/sim-real-cotraining/survey.md` §4.2）。
- BIFROST 自述接触不连续时配对片段结果分歧，训练信号有害。

## Opportunity

在部署场景孪生中，为每条真实遥操作示教渲染逐帧配对的仿真观测，把配对约束加到"域标签 + 对齐"的共训练目标里：配对样本只约束接近、搬运等无接触阶段的表征，接触阶段不加约束。在操作任务上与普通共训练、CFG-ADDA、OT Co-Train 对比。

## Expected Mechanism

假设：
- 配对约束提供逐样本的对齐信号，比分布级对齐（OT、MMD、ADDA）更精确，能在保留域标签的同时减少表征漂移；
- 无接触阶段的仿真与真实结果一致，配对约束有益；接触阶段的结果可能分歧，排除接触段可以避开 BIFROST 报告的有害信号。

## Required Evidence

同一任务、同一组真实示教（每任务 10–50 条）与同一批孪生数据下，比较：
1. 普通共训练（Sim&Real Co-Train 配方）；
2. CFG-ADDA；
3. 配对约束作用于全部阶段；
4. 配对约束只作用于无接触阶段。

报告真机成功率，以及 sim/real 表征的对齐程度与域可分性的探针结果。

## Promotion Condition

部署场景孪生可以按真实示教的机器人状态与物体位姿重新渲染，且能区分接触与无接触阶段。

# OPT-007

Status: open

Area: sim-real-cotraining

## Observation

- 仿真数据的价值取决于选什么：均匀生成的仿真数据可能低于只用真实数据（MetaGenSim 23/80 vs 26/80），全量仿真池不如精选子集（TUCO 25.8% vs 85.8%）。
- 在孪生中定位失败、只在失败处补数据有效：Real-is-Sim 补 30 条仿真示教 57% → 80%，与 60 条真实相当；EmbodiRSI、F4R 也是这一模式（`topics/sim-real-cotraining/survey.md` §3.5）。
- 部署后的策略在真实数据覆盖的状态模仿真实示教，在其他状态依赖仿真行为（R2S2R Grounding）；接触段需要真实数据（SARI）。
- 检索范围内没有论文用孪生事先决定该采哪些真实遥操作示教；只在真机上做的 Mulligan 把初始状态集中到失败处，提升 10–34 个百分点。

## Opportunity

用孪生决定真实遥操作采集计划：先用孪生数据 + 少量真实示教共训练，在孪生中大规模评测，找出孪生内仍失败的状态，以及孪生内成功、但在孪生与真实之间结果差异大的阶段（例如接触段）；只在这些状态采集真实遥操作，与均匀采集比较相同条数下的真机成功率。

## Expected Mechanism

假设：
- 共训练策略在仿真覆盖充分、物理可信的状态已经足够好，真实示教的边际价值集中在两类状态：孪生内仍失败的状态，和仿真物理不可信的接触阶段；
- 把真实示教定向到这两类状态，可以在相同条数下提高真机成功率，或在相同成功率下减少真实示教条数。

## Required Evidence

在同一任务上，固定真实示教总数（例如 20、50 条），比较：
1. 均匀采集真实示教；
2. 只按孪生失败状态定向采集；
3. 按失败状态加接触阶段定向采集。

报告真机成功率，以及达到同一成功率所需的真实示教条数。

## Promotion Condition

部署场景孪生可以批量评测策略并导出失败状态，真机遥操作可以从指定的初始状态开始采集。

# OPT-008

Status: open

Area: data-distribution-generalization

## Observation

- Infant Lumpy：图像总数与类别频率相同时，一个实例占类内 35% 且视角多变的训练集，对新实例的泛化优于均匀采样实例；作者自述实例频率偏斜与外观变化两者的贡献尚未拆开（`topics/data-distribution-generalization/survey.md` §2.2）。
- Bambach 2018、Tsutsui 2021：样本量相同时，"相似为主 + 多样长尾"的混合优于纯相似或纯多样。
- Physics LM 3.1：头部实体的多样改写让尾部实体的知识可提取（4.4% → 86.8%）；Scaling CG：少数热门模块无害，少数冷门模块有害。
- 机器人数据侧，Robot-Data-Comp、F-ACIL 研究了因素覆盖方式，检索范围内没有论文研究"同一物体实例的重复次数与外观变化"对新物体泛化的作用。

## Opportunity

在机器人抓放数据上复现 lumpy 对照：总示教数和物体类别相同，比较"一个锚点物体实例占 35%、其示教覆盖大量位姿与光照变化"与"所有实例均匀"两种训练集，在未见过的同类物体上评测；再加两个条件拆开作者未拆开的两个因素：锚点高频但变化少，以及锚点不高频但变化多。

## Expected Mechanism

假设：
- 锚点实例的多变示教让策略学到哪些变化不改变动作，这种不变性可以迁移到同类新实例；
- 收益主要来自锚点内部的变化，而不是频率偏斜本身。

## Required Evidence

在同一任务、同一模型、同一总示教数下，比较四种训练集：
1. 均匀；
2. 锚点 35% + 变化多；
3. 锚点 35% + 变化少；
4. 均匀 + 每个实例的变化多。

每个条件至少 3 个随机种子，报告未见实例上的成功率；从零训练的小策略与冻结视觉编码器的预训练策略分开报告。

## Promotion Condition

有可批量生成示教的仿真抓放环境，物体实例、位姿、光照可以独立参数化。

# OPT-009

Status: open

Area: data-distribution-generalization

## Observation

- 组合覆盖的条件已有较一致的结论：每个属性值都出现，每个值至少 2 个搭配伙伴，组合图连通，模型结构与组合方式匹配（CG First Principles、Modular Hyperteacher、SQOOP、Visual CG Scaling；`survey.md` §4.3–§4.4）。
- 频率方面只有间接证据：热门模块无害、冷门模块有害（Scaling CG）；低频概念组合更慢（Multiplicative Emergence）；组合推理上幂律训练优于均匀（Power Law CR）。
- MOSAIC 的组合留出实验刻意只用均匀分布；检索范围内没有论文在组合留出条件下直接比较偏斜与均匀的属性频率（`survey.md` §4.5）。
- 机器人侧的组合基准（CompoSuite、COLOSSEUM、MESA）都没有控制属性频率的形状。

## Opportunity

在仿真抓放任务上做"偏斜 × 组合留出"的交叉实验。物体按形状 × 颜色 × 尺寸参数化，留出若干"属性都见过、组合没见过"的物体作 OOD 测试，另留"属性值没见过"的物体作对照。两个因子交叉：
- 覆盖形状：十字（L 形）、十字 + 对角带、随机稀疏格；
- 属性频率：均匀，Zipf α = 0.5 / 1 / 1.5，以及每个属性值设最低出现次数的截头分布。

## Expected Mechanism

假设：
- 覆盖形状决定组合 OOD 的上限：十字覆盖对单体策略不够，加少量离轴组合后大幅改善；
- 在覆盖相同时，头部偏斜不伤组合泛化，低于某个下限的冷门属性值会被记忆而不是组合；
- 改变抓取运动的属性（形状、尺寸）比只改变外观的属性（颜色）需要更多组合覆盖。

## Required Evidence

在同一总示教数与同一模型下，跑完"覆盖形状 × 频率形状"网格，每格至少 3 个随机种子。报告：
- 已见组合、留出组合、未见属性值三类物体的成功率；
- 首次闭合时夹爪中心相对物体的偏差；
- 冷门属性值上的成功率随其出现次数的变化。

## Promotion Condition

仿真环境中物体的形状、颜色、尺寸可以独立参数化，并能为每种组合批量生成成功示教。

# OPT-010

Status: open

Area: data-distribution-generalization

## Observation

- 同一状态下动作要一致：IL Data Quality 的 action divergence；GO-1-Pro 中执行速度多模态有害，统一动作速率后平均分 +15%（`survey.md` §6.2）。
- 需要多种速度时，可以作为显式条件（MoMo、TempoVLA）；轨迹内的精确段不宜加速（Perfect-Demo、DemoSpeedup）。
- 因素与数据来源之间的相关会被策略当作捷径（Shortcut-OXE），共训练策略需要分辨样本来自哪个域（Sim&Real Pushing）。
- 检索范围内没有论文研究 sim + real 共训练中行程长度、速度剖面、抓取位姿分布的形状，以及 sim 与 real 在这些分布上的错配（`survey.md` §6.6）。

## Opportunity

在 sim + real 共训练中系统比较仿真数据的运动分布：
- 速度剖面：规划器固定剖面、重定时到真实遥操作的节奏、随机变速，以及随机变速 + 速度条件输入；
- 抓取位姿：与真实测试分布一致、比真实更宽的均匀分布、难点（工作区边缘、关节分支边界）加密；
- 桥接数据：少量在 sim 与 real 中都出现的位姿与物体组合。

## Expected Mechanism

假设：
- 仿真速度剖面与真实不一致、又没有速度条件时，速度成为同一状态下的动作歧义，或成为域标签，降低真机精度；重定时到真实节奏或加速度条件可以消除；
- 抓取位姿分布的支撑集比形状更重要，在支撑集覆盖测试范围后，难点加密优于均匀；
- 桥接数据减少策略把 sim 与 real 的系统差异当作区分行为的捷径。

## Required Evidence

固定真实示教（例如 50 条）与仿真示教总数，每次只改变一个分布因素，报告：
- 真机或高保真孪生中的成功率；
- 首次闭合时的位置偏差；
- 执行时间；
- sim 与 real 表征的域可分性探针。

## Promotion Condition

有部署场景的仿真孪生可以按指定的速度剖面与位姿分布生成示教，并有少量同任务的真实遥操作示教。
