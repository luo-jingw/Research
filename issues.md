# ISSUE-001

Status: open

Area: real2sim

## Observation

第一轮 real2sim 综述（`topics/real2sim/papers.md`）中，部分论文的发表处或数值只来自二手来源，或在一手来源中自相矛盾。

## Impact

在引用这些论文的发表处或数值前，需要回到一手来源确认。`papers.md` 中这些条目的发表处标有 †。

## Evidence

- **RigPI (2606.25212)**：arXiv Comments 字段写 "Accepted to … IROS 2027"
- **Scalable Real2Sim (2503.00370)**：IROS 2025 只出现在作者 GitHub 仓库，arXiv 页面未列发表处
- **SPARK (2512.01629)、PhysX-Anything (2511.13648)**：CVPR 2026 来自 cvpr.thecvf.com 虚拟会场页面，未在论文页面确认
- **URDF-Anything+ (2603.14010)**：NeurIPS 2026 来自 neurips.cc 海报页面，未在论文页面确认
- **SIMPLER (2405.05941)**：物理后端（SAPIEN/ManiSkill2）未从论文正文确认
- **Mem-World (2606.18960)**：摘要只给出 "Pearson 比 Ctrl-World 高 14.5%"；r=0.97 vs 0.85 只见于搜索摘要
- **Cosmos-Surg-dVRK (2510.16240)**：r > 0.92 只见于二手总结
- **MolmoSpaces (2602.11337)**：发表处未确认
- **GaussGym (2510.15352)**：论文一处写 IsaacGym，另一处写 IsaacSim
- **BayesSim (1906.01728)**：RSS 2019 版的"真实"数据由仿真器生成，没有真机实验
- **"Contact-UAN"、"MatPhys" (2605.19386)**：只见于索引列表或参考文献，未找到论文页面
- **Awesome-Real2Sim2Real GitHub 列表**：至少两处发表处错误：EmbodiedSplat 应为 ICCV 2025，CRISP 应为 ICLR 2026

## Hypotheses

- RigPI 的 "IROS 2027" 可能是 "IROS 2026" 的笔误。

## Next Experiment

引用任一条目前，打开该论文的 arXiv 最新版本、会议论文集或项目页核对；Awesome 类列表只用于发现论文，不作为发表处来源。

## Resolution

# ISSUE-002

Status: open

Area: humanoid-motion-tracking

## Observation

第一轮 humanoid-motion-tracking 综述（`topics/humanoid-motion-tracking/papers.md`）中，部分发表处只来自其他论文的引用或二手页面，部分方法细节未从一手来源确认；检索预算在 2025–2026 世界模型分支上提前耗尽。

## Impact

引用标 † 的发表处或下列细节前需回到一手来源确认。可微世界模型分支（papers.md §7–§10）的 2025–2026 覆盖可能不完整。

## Evidence

- **H2O、OmniH2O、HumanPlus、ExBody、TWIST、UniTracker、LATENT、PHUMA**：发表处只来自其他论文的引用
- **BeyondMimic、SONIC**：Science Robotics 11(117) 来自 SuperMimic 参考文献，未打开期刊页面
- **GMR**：ICRA 2026 只见于一处引用
- **QWM、FADA**：CoRL 2026 来自作者或实验室页面，arXiv 页面未列发表处
- **FADA**：一个检索来源未找到 arXiv；另一个检索来源给出 arXiv 2606.28476
- **SuperDyno**：只读了摘要，策略梯度估计器的具体形式未确认
- **BONES-SEED**：数据集页面未打开，规模数字来自 SONIC 与 SuperMimic 的引用
- **GMT、ExBody2**：发表处未确认
- **GigaBrain-WBC-0.5 (2608.18234)**：arXiv 元数据中名称为 "InterTrack"
- **可微世界模型分支**：2025–2026 只覆盖了检索时打开过页面的课题组：ETH RSL、UCSD Hansen、NVIDIA、Georgiev、Y. Song、PKU Libin Liu、CMU LeCAR

## Hypotheses

## Next Experiment

- 引用前打开对应论文的 arXiv 最新版本或会议论文集核对。
- 补检 2025–2026 年"经学习动力学反传梯度训练腿足/人形策略"的工作，核对 survey.md §3 的覆盖。

## Resolution

# ISSUE-003

Status: open

Area: vla-fast-control

## Observation

第一轮 vla-fast-control 综述（`topics/vla-fast-control/papers.md`）中，部分发表处未在一手来源确认，部分条目缺少 arXiv 或关键细节；各论文的延迟测量口径不统一。

## Impact

引用标 † 的发表处或下列细节前需回到一手来源确认；延迟数字只能在同一论文内比较。

## Evidence

- **ACT (2304.13705)、HIL-SERL (2410.21845)、ConRFT (2502.05450)、UMI (2402.10329)**：发表处（RSS 2023 / Science Robotics 2025 / RSS 2025 / RSS 2024）不在 arXiv comment 中，未在论文集确认
- **DemoSpeedup (2506.05064)**：CoRL 2025 只来自 mlanthology 索引
- **SpeedTuning (2608.09138)**：arXiv v1 为 2026-08，但 comment 写 ICRA 2025
- **RACE**：无 arXiv，只在项目页与 OpenReview 确认
- **Helix**：无论文，数字来自 Figure 博客（2025-02-20）
- **MiniVLA**：未找到 arXiv，博客未打开
- **MetaGenSim**：所用预训练 VLA 的身份未确认
- **RLDG、PA-RL、RLT**：基模型（RLDG）、示教条数（PA-RL、RLT）未确认
- **RL-Co (2602.12628)**：正文原话是 200 条纯真实示教的基线 "lower than or comparable to" 20 条示教的 RL-Co（Open Drawer，π0.5），不是明确超过
- **延迟数字**：各论文是否包含图像编码、网络传输、去噪步数不同，跨论文不可直接比较

## Hypotheses

## Next Experiment

引用前打开对应论文的 arXiv 最新版本或会议论文集核对；需要跨模型比较延迟时，在同一硬件与同一口径下自测。

## Resolution

# ISSUE-004

Status: open

Area: sim-real-cotraining

## Observation

第一轮 sim-real-cotraining 综述（`topics/sim-real-cotraining/papers.md`）中，部分发表处只见于索引或二手来源，部分论文原文内部数字不一致，部分数字只来自摘要，引用扫描有缺口。

## Impact

引用标 † 的发表处或下列数字前需回到一手来源确认；检索缺口可能漏掉 2026 年的后续工作。

## Evidence

- **发表处只见于索引或二手来源**：
  - DataMIL (2505.09603)：ICLR 2026 只见于 TUCO 的参考文献
  - Re-Mix (2408.14037)：CoRL 2024 只见于二手来源
  - EgoMimic (2410.24221)：ICRA 2025 只见于二手来源
  - AnchorDream (2512.11797)、SimLauncher (2507.04452)：ICRA 2026 / IROS 2025 只见于 OpenAlex 的 DOI 记录
  - simDP：无 arXiv，Sensors 2026 元数据来自 OpenAlex；与 ICML 2026 论文 "Encoder-Adapted Sim-to-Real Transfer of Simulation-Trained Diffusion Policies for Robot Manipulation" 作者部分重合，关系未核实
  - MimicLabs (2506.13536)：Semantic Scholar 标为 ICLR，未确认
  - Sim&Real Co-Train (2503.24361)：部分来源称 RSS 2025，arXiv comment 未写
- **原文内部不一致**：
  - Mechanistic Co-Train：正文称最佳方法约 74%，Table 2 的 21/30 为 70%；附录 D.5 搜索区间中 N、M 的命名与正文定义似乎相反
  - RoboCousin：Table 3 表注写每个策略 1,000 条仿真轨迹，正文写 400 条
  - Humanoid Dex Sim2Real：引言称新物体上提升 80~100%，表中没有对应拆分
- **只核实了摘要的数字**：RoboRender、PhyVisGen、GaussianFactory、DiscoDemo、EmbodiRSI、TANDEM、F4R、RoboCurate、Real2Edit2Real
- **引用扫描缺口**：Semantic Scholar 多次返回 429，GR00T N1、RoboCasa、DreamGen、RoboTwin 2.0、DP3、EgoBridge、PLD 的被引列表未扫描或未扫完
- **发现但未纳入的候选**：EVA (2603.17808)、World Action Verifier (2604.01985)、DreamZero (2602.15922)、TC-IDM (2601.18323)、VERA、AutoTrialGen、"Physically-Grounded Data Generation via Video Diffusion Models"、"Gotta Scoop 'Em All"（Semantic Scholar 标 ICRA 2026）、ProMix、AlphaNIST (2610.13354，comment 只写 ICRA)

## Hypotheses

## Next Experiment

引用前打开对应论文的 arXiv 最新版本或论文集核对；第二轮检索时补扫上述论文的被引列表。

## Resolution

# ISSUE-005

Status: open

Area: data-distribution-generalization

## Observation

第一轮 data-distribution-generalization 综述（`topics/data-distribution-generalization/papers.md`）中，部分发表处只见于索引或二手来源，部分数字在原文内部不一致或缺少口径，几组论文的结论相互冲突。

## Impact

引用标 † 的发表处或下列数字前需回到一手来源确认；冲突的结论在综述中只陈述各自原文，尚无对照实验解释。

## Evidence

- **发表处只见于索引或二手来源**：
  - Power Law CR (2604.22951)：ICML 2026 只见于 OpenReview 与 PDF 页脚，arXiv abs 页没有 comment
  - Uniform Cluster Prior (2210.07277)：ICLR 2023 未在一手页面确认
  - CLEVR-CoGenT (1612.06890)、TMN (1905.05908)：CVPR 2017 / ICCV 2019 未在 CVF 页面确认（访问被拦截）
  - Category-Viewpoint OOD (2007.08032)：Nature Machine Intelligence 2022 未确认
  - Env Drivers (1910.00571)、Zipfian Env (2203.08222)：ICLR 2020 / CoLLAs 2022 只见于 OpenReview、dblp
  - Factor World (2307.03659)、PVR-Robust (2312.12444)：未找到发表处，不在 CoRL 2023 的 PMLR 卷中
- **原文内部不一致或缺口径**：
  - MOSAIC (2605.00273)：组合实验的数据集规模，正文写 10k / 50k / 100k，Table 1 写 10k / 20k / 100k；偏斜实验的具体偏斜比例没有在正文给出数字
  - SSL Curation (2405.15613)：幂律重采样 ImageNet（82.7 → 57.0）时，原文没有说明各 α 下的总样本量是否相同
  - Perfect-Demo (2606.15587)：摘要数字与 HTML v2 的 Table 1 不一致，综述取表中数字
  - Infant Lumpy (2510.15060)：主效应 D = 3.83 的单位在正文中没有写明；v1 标题为 "...found in everyday infant experiences"
- **结论冲突**：
  - 因素组合的难度是否叠加：Factor World 称多数因素对不叠加难度；LIBERO-Plus 报告成对扰动有一致的负组合性 gap（"non-decomposable"）
  - 重复的利弊：Repeated Data 中 0.1% 数据重复 100 次显著损害预训练；Repeated Examples 与 Long-CoT Repetition 中小数据多次重复优于大数据单次。设定不同（通用预训练、算术任务、长 CoT SFT），没有同设定对照
  - 视觉数据整理：SSL Curation 主张 SSL 数据应 "large, diverse and balanced"；DataComp 在固定训练所见样本数时，更小、过滤更严（重复更多）的子集更好
- **结论未核实**：Wonnacott 2012 (DOI 10.1016/j.jml.2011.11.004) 只核实了元数据，未取得摘要，其关于偏斜与均衡输入的结论未知
- **简称冲突**：CRAFT (2610.00524) 与 2602.12532 同名；ACT-VLA (2607.00351) 易与 ACT（Action Chunking Transformer）混淆
- **发现但未纳入的候选**：AC-VLA (2607.15714)、ReGuide (2609.38616)、ACG-Bench (2610.06184)、VIMA (2210.03094)、Policy Architectures for Compositional Generalization in Control (2203.05960)、Adversarial Data Collection (2503.11646)、Simple-to-Complex Structured Demonstrations (2607.04591)、DROPO (2201.08434)、Understanding Domain Randomization for Sim-to-real Transfer (2110.03239)、WARP-RM (2606.28320)、SCIZOR (2505.22626)、PSD (2605.01544)、From 12 to 200 Demonstrations (2610.37170)、CIFT (2509.24797)

## Hypotheses

- 因素难度是否叠加的冲突，可能来自策略规模与评测任务的差异：Factor World 用 RT-1 类策略和拾取任务，LIBERO-Plus 用大型 VLA 和 LIBERO 任务。

## Next Experiment

引用前打开对应论文的 arXiv 最新版本、论文集或期刊页核对；第二轮检索时精读 Wonnacott 2012 与 MOSAIC 附录，补齐缺失的口径。

## Resolution
