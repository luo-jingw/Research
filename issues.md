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

# ISSUE-006

Status: open

Area: vla-drawing-writing

## Observation

第一轮 vla-drawing-writing 综述（`topics/vla-drawing-writing/papers.md`）中，部分发表处没有在一手页面确认，部分数字来自图表标签或原文内部不一致；在正文中使用 ManiSkill3 绘图任务的论文召回可能不完整。

## Impact

引用标 † 的发表处或下列数字前需回到一手来源确认。"交集只有 2 篇仿真论文"的结论依赖检索召回，可能偏低。

## Evidence

- **发表处只见于 PDF 页眉或二手来源**：
  - RDT-1B (2410.07864)：ICLR 2025 只见于 PDF 页眉，arXiv comment 为 "10 pages, conference"
  - DreamZero (2602.15922)：ICLR 2026 只见于检索结果摘要，未在 arXiv comment 或论文集确认，目录中按预印本列出
- **图表读数**：
  - DreamZero Fig. 9 的各柱数值是从 PDF 文本层的柱上标签按列位置对齐读出的；两个子方向与本地核对结果一致，但没有对照图像本身
  - BURGER §4.1 的数据规模结果只有曲线图，没有数值表
- **原文内部不一致或缺口径**：
  - FG-CLTP (2603.10871)：书写任务在 §V-B 写作"在白板上书写指定字符"，在 §V-B2 写作"画不间断的圆"；评测次数没有报告
  - BURGER (2610.40532)：Table 1 没有 π0 一行；仿真中的机器人型号正文未写；与 13,200 条仿真示教共训的 sim-to-real 只在 §1 提到，没有数值
- **召回缺口**：
  - 只在正文中使用 DrawTriangle-v1 / DrawSVG-v1 的论文只能靠全文检索发现（DAP 就是这种情况）；Semantic Scholar 全文片段检索因限流没有完成
  - ManiSkill3 软体任务中是否仍含 ManiSkill2 的 Write 未核实
  - LingBot-VA 没有找到一手页面，未筛查
- **发现但未纳入**：
  - HiFi-UMI (2607.25895)：用 UMI 重建手写轨迹，被评测的 VLA 不做书写
  - Gemini Robotics (2503.20020)、WALL-OSS (2509.11766)：字母相关任务是用积木拼词（子方向检索的全文扫描结果，未在本地复核）
  - MolmoAct (2508.07917)：用户画的轨迹只作为引导条件
- **agent 分支的元数据与口径**：
  - Wonderful Team (2407.19094)：TMLR 2025 只见于 PDF 页眉，arXiv comment 为 "aka Wonderful Team"
  - GeminiPainter (2608.00829)：arXiv abs 页的标题是一个描述性句子，HTML 全文标题为 "GeminiPainter: Real-Time AI-Guided Robotic Sketch Generation for Live Portraiture"；目录沿用 abs 页标题
  - RURL (2611.18562)：真机逐次记录（App. G）在 HTML 版中只有目录，《星夜》线稿的尝试次数无法核实
  - MOPS (2505.03725)：绘图域结果只有柱状图，没有数值表
  - Gym-Anything (2610.40565)：白板任务没有单独数值
- **agent 分支未找到 arXiv 版本的线索**："Embodied Generative AI Art for Enhanced Human Robot Interaction"（HRI 2025，只见于机构库页面）、"Demonstrating Artistic Drawing on Low-Cost Robot"（CoRL 2025 demo）
- **agent 分支发现但未纳入**：
  - RoboBench (2510.17801)：规划原语里有 draw(tool, character, target_object)，未核实评测题是否含写画
  - KPI (2609.36151)：人形机器人白板写 "NB"，但写字实验用脚本参考，不经 VLM
  - AnyBody (2606.29209)：人形机器人手腕空中写字，潜空间 RL，没有 LLM
  - HandwritingAgent (2606.18788)、LVGM (2511.11119)：生成手写或汉字矢量笔画，没有机器人
  - PainterBench (2609.34195)、AgentDrawBench (2610.19025)、TurtleAI (2606.03626)：数字画布绘图 agent 基准，没有机器人执行

## Hypotheses

- DAP 中 π0 在 DrawTriangle-v1 上只有 2.0%，可能部分来自训练不稳定（作者自述在该任务上另调过超参数），不完全反映任务难度。

## Next Experiment

引用前核对 ICLR 2025 / 2026 论文集；对照 DreamZero 原图复核 Fig. 9；第二轮检索时用全文检索补查 "DrawTriangle-v1"、"DrawSVG-v1"、"TableTopFreeDraw" 的使用者。

## Resolution

# ISSUE-007

Status: open

Area: vla-wam-robustness

## Observation

第一轮 vla-wam-robustness 综述（`topics/vla-wam-robustness/papers.md`、`survey.md`）中：部分发表处没能在一手页面确认，或与其他方向的 `papers.md` 不一致；部分数字只来自模型对 HTML 正文的摘录，没有逐字核对；若干论文原文内部前后不一致；检索召回有已知缺口，还有一些方法只在别人的表格中出现，arXiv 编号没有核实。

## Impact

引用标 † 的发表处、下列数字，或综述中"本轮没有找到"一类的结论之前，需要回到一手来源确认。"相机位姿漂移、冻结 VLA、无标签"组合缺失，以及"VLA 上没有只调 LN / RMSNorm 仿射的 TTA 报告"这两条结论依赖检索召回，可能偏强。

## Evidence

- **发表处没能在一手页面确认**：
  - LIBERO-Plus (2510.13626)：CVPR 2026 只见于 cvpr.thecvf.com 的虚拟会场 poster 页，CVF 论文集 PDF 返回 403，没有打开。会议版标题为 "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models"。目录写作 CVPR 2026†。
  - FOA (2404.01650)：comment 只写 "accepted by International Conference on Machine Learning"，没写年份；目录按 v1 年份写作 ICML 2024†。
  - Adapt3R (2503.04877)：comment 中没有发表处，DART 的参考文献写作 CoRL，属于二手信息；目录按预印本列出。
  - VLA-Arena (2512.22539)：页面上只有 ICML 模板的关键词，没有 comment；按预印本列出。
  - VPP (2412.14803)：关键词写 ICML，录用没有确认；按预印本列出。
  - PDF (2604.18107)：代码仓库名含 CVPR2026，comment 没列发表处；按预印本列出。
  - WorldAgen (2609.08162)：检索片段称 AAAI；按预印本列出。
  - DP (2303.04137)：没有读到 comment，正文自称是 RSS 会议论文的扩展版；按预印本列出。
  - VersaCamVLA (2610.12451)：NeurIPS 2026 只在摘要级核实中记录。
- **发表处与其他方向统一**：π0（RSS 2025）、π0.5（CoRL 2025）、OpenVLA（CoRL 2024）、OpenVLA-OFT（RSS 2025）、UVA（RSS 2025）、RDT-1B（ICLR 2025†）按 vla-drawing-writing、vla-fast-control 已有的记法写入本方向；本轮子方向只读到 arXiv comment 字段，没有重新核对这些发表处。
- **仍不一致的发表处**：
  - LIBERO-Plus (2510.13626)：data-distribution-generalization 记为预印本，本方向记为 CVPR 2026†
- **抽查后已按原文更正的转述**：
  - SALT (2610.07946)：几乎无效的条件是漂移"从第一次重规划就存在"，不是"从第一帧"；Table 1 中 BID 为 46.0 / 63.1，SALT 对最强基线的领先是 7.2 / 2.9 个点。
  - TTT-VLA (2606.03127)：51.1 → 63.5 来自训练时加入的潜提示与状态定位代理任务（SG-LP），63.5 → 67.4 才是测试时训练的增量；代理专家在测试时也要用；原文没有说代理头"必须"在训练时加入，只说训练时同时优化动作目标与代理目标。
  - TempoFit (2603.07647) Table IV：只在中间层启用 96.6，全部层（0–17）74.2，直接拼接 0.8，去掉范数保持 90.2。
  - T³VF (2605.08215)：Camera 50.5 → 55.3、Light 67.8 → 72.4 只属于 "w/ Perturbed Train" 一组（在 LIBERO-Plus 上微调过的模型）；"w/o Perturbed Train" 一组为 Camera 39.2 → 41.5、Light 62.5 → 62.3。
  - WAM-vs-VLA (2603.22078)：RoboTwin 2.0-Plus 的相机扰动只作用于头部相机；默认启用朝向扰动 C3（各轴 0–5°），球面位置扰动 C2（±10°、±10% 距离）默认关闭；Table 3 的相机一列只在 5 个模型中的 4 个最低，π0.5 的 Robot（27.6）低于其 Camera（45.6）。
  - FTM (2512.02902)：视角幅度原文没有数值，"各档幅度即 Adapt3R App. C.1 与 DART Table 12 的数值"是推断；"一次演示"是每个任务一条、在同一批任务上测试。
- **只来自模型摘录、没有逐字核对的数字**：
  - SALT App. I（SmolVLA 32.5 对 32.9）。
  - 基准与 WAM 比较一支（LIBERO-Plus、WAM-vs-VLA、ImageWAM、JAM、ZimaBlue、Phoenix、Colosseum V2、VLATest、Blackout-Freeze、VLA-Trace 等）的数字全部由 WebFetch 读 HTML 正文得到；只画在图里的数字没有读到数值，例如 Colosseum V2 的相机单项只在 Fig. 5 中。
  - FTM 谱系一支中，用 curl 抽取原文逐字核对过的只有 FTM、Adapt3R（App. C.1、§4.3、Table 9、Table 11）、AnyCamVLA（Table I–III）、Cross-View AC（Table 1）、DART（Table 1、10、12，App. 0.C.2、0.B.2，§7）。其余由 WebFetch 读取；GS-VLA、WACO、Homeward 的页面超过 10 万字符，只读了前 10 万字符。
  - Eva-VLA (2509.18953) Table 1：WebFetch 读到的表格是乱码，列对应关系是推断的。
  - 只核实了摘要的条目：Layer Mystery、UVA、UWM、ScaleDP、RL²-VLA、SteerTrace、StairVLA、Knowing When to Stop、EVOLVE-VLA、RoboMonkey、TACO、Retrieve-then-Steer、Infer-Diagnose-Refine、T2-z、Self-Correcting Planning、Self-GAD、FAIL-Detect、DVAC、GeCO、τ0-WM、VistaBot、InfiNoVA、CAPO、T3R、PAIR、OVOA-VLA、VersaCamVLA、View Collapse、LIT、RAGu；WorldAgen 只读了 listing 摘要，RageVLA 只核实了 listing 标题。
- **原文内部不一致**：
  - FTM (2512.02902)：FLA 的训练步数 §4.3 写 2000，Table 7 写 1,500（decay 2,000）；Table 3 中 FTM 一行的 Libero-V 平均写作 90.5，四列均值约为 93.2；Table 1 中 FTM 的平均 v1 为 87.2、v2 为 87.1；§3.1 把 π0.5 写成自回归输出离散动作 token，附录 §11 写成 flow matching 动作专家。
  - FTM (2512.02902)：Table 1 的 OpenVLA-OFT 行与 GeoAware-VLA Table I 的对应行逐项相同（均值 50.3 对 50.2），可能取自 GeoAware 但没有注明；Table 2 把 GeoAware 拆成 S/M/L，拆分来源没有说明。
  - Cross-View AC (2608.06965)：ID 成功率正文 Table 1 为 94.2±0.8，arXiv 摘要为 95.0±0.8。
  - GS-VLA (2608.19066)：参数量 4M 与正文中出现的 44M 不一致；Table 4 与 Table 1b 的零噪声行对不上。
  - CRT (2602.01158)：高斯噪声下成功率 87% → 79%，正文却称"恢复"。
  - TEMPO (2610.20318)：摘要称最高提升 80%，引言称 50%。
  - T³VF (2605.08215)：Table 1 中 Robot 维度的 Δ 写作 +1.8，与 29.0 → 31.8 不符。
  - VLA-Arena (2512.22539)：高斯噪声正文写方差 0.05，Table 14 写 σ²=0.085。
  - COAST (2605.17144)：正文与 Table 1 的 MetaWorld 数字不一致。
  - mimic-video (2512.15692)：正文默认 τv=1，Fig. 6 图注称中间噪声水平最好。
  - ImageWAM (2606.19531)：App. §5.1.1 称动作 token "attend to the other tokens"，main 分支代码的掩码不让动作 token 看噪声目标帧 token。
- **口径存疑或跨论文对不上**：
  - π0 在 LIBERO-Plus 相机维度上：LIBERO-Plus Table 1 为 15.8，ImageWAM Table 3 照搬 LIBERO-Plus 写作 13.8。
  - Homeward (2611.24455)：Table 3 中 π0.5 不校正为 76.5，Table 2 中"不校正"为 79.7，没有确认两表是否用同一模型、同一子集。
  - LIBERO-Plus §3：只遮第三视角时为 43.6 / 43.0 / 67.3，正文没说分别对应哪个模型。
  - WAM-vs-VLA：RoboTwin 2.0-Plus 的 C1（距离 0.85–1.0×）是否默认启用，没有确认；Table 3 中 "MOTUS" 是否就是 Motus (2512.13030)，没有确认。
  - Phoenix (2611.24938)：Clean2Random 的定义只按名称理解，正文没有读到。
  - TTT-VLA (2606.03127)：离线 buffer 约 800 / 800 / 2000，单位没标。
- **四个子方向文件之间的不一致**：
  - InfiNoVA (2609.27734)：一个子方向从 abs 页记为 "InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies"，另一个从检索结果记为 "InfiNoVA: ∞ Novel View Augmentation for Viewpoint Invariant Robot Policies"；目录用前者，原标题可能用的是 ∞ 符号。
  - VersaCamVLA (2610.12451)：做了摘要级核实的子方向只记了简称和 NeurIPS 2026；目录中的完整标题来自另一个子方向的检索结果（UNVERIFIED）。
  - SCALE：一个子方向记为 DART 表中的 ICML 2026 方法、编号未核实；另一个在 listing 中记了 2602.04208；没有确认是同一篇。
  - Self-Adaptive VLA (2609.30092)：一个子方向归为上下文或记忆式适应，另一个写作针对硬件漂移、训练时用预补偿的专家动作；两边都没有精读。
  - Robust-WAM：一个子方向称它只在 CoRe-VLA Table 3 中出现、编号未核实；另一个从检索结果记为 2608.05903（UNVERIFIED）。
  - "相机位姿漂移、冻结 VLA、无标签"组合：TTA 子方向一处称本轮没有找到，另一处称 T³VF 是唯一在 VLA 上对相机维度给出无标签 TTA 数字的工作。综述按后者写，并把"没有找到"限定在不预测未来图像的常规 VLA 上。
  - π0.5 相机零样本的跨度：FTM 谱系子方向的要点写"16.8 到 76.5"，但同一文件的口径表里还有 9.3（GS-VLA libero_10）和 11.3（DART Large），另一个子方向记了 78.4（ZimaBlue）；综述按协议逐项列出，不写总跨度。
  - VLA-Trace (2605.30117) 标题中 "through" 的大小写、MI-Steering (2509.00328) 标题的大小写，两个子方向的记录不同；目录分别取已核实的一方。
- **只在别人表格中出现、arXiv 编号没有核实，没有列入目录**：
  - RETAIN（DART 标为 ICLR 2026）、SCALE（DART 标为 ICML 2026）
  - Anchor-Align、GAM、AVA-VLA、SRPO、Robust-WAM（CoRe-VLA Table 3）
  - TBD-VLA、CycleVLA（WACO Table VII）
  - Spatial Forcing（WARP-VLA Table I）
  - Evo-0（GeoAware-VLA Table I）
  - 各文表格里被评测、本轮没有单独核实的模型：X-VLA、UniVLA、WorldVLA、NORA、RIPT-VLA、HoloBrain0-GD、VLA-JEPA、MOTUS、InternVLA-A1.5、ABot-M0.5、OpenWAM-α、InternW0-Δ、Qwen-RobotManip-Context、ACoT-VLA、GR00T N1.7、Mantis、LDA-1B、QwenPi / QwenWPI
- **发现但没有展开（只读了标题、listing 或摘要），没有列入目录**：
  - 基准：LIBERO-VPro (2609.24350)、RoboCasa-Shift (2610.27861)、LIBERO-Occ (2606.10862)
  - 子方向只核实了摘要、没有记完整标题：X-World (2610.34105，LIBERO-Plus 未适应 76.5)、MVUCF (2608.01826，GR00T-N1.6 上 LIBERO-Plus +22.4)、MAP-VLA (2511.09516，冻结 VLA 上用于记忆的软提示)
  - 训练侧（标题来自检索结果，UNVERIFIED）：SG-WAM (2608.01397)、E0 (2511.21542)、Flatness Preserves Instruction Following in Vision-Language-Action Models (2606.23641)、Stable Language Guidance for Vision–Language–Action Models (2601.04052)、Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations (2509.11417)、Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults (2606.10501)
  - 测试时与部署期适应：Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models (2611.26438)、Verify, Act, Distill (2610.14885)、RecastVLA (2609.32155)、Self-Adaptive VLA for Robust Robot Deployment (2609.30092)、Taming VLAs under Robot Execution Errors (2609.37334)、Scouting the Dynamics Gap (2609.36107)、AdaPower (2512.03538)、RA-VLA (2608.25585)、GUARD (2611.10343)、PriGo (2607.07076)、ADPro (2508.06266)、UMI-on-Air (2510.02614)、GPC (2502.00622)、VLA Knows Its Limits (2602.21445)、SCALE (2602.04208)、RoboHarness (2603.24060)
  - VLN 上的 TTA：Asking Less, Adapting Better (2610.30643)、Credit-Guided Policy Improvement for Test-time Adaptive VLN (2609.37591)
  - 注入与引导：VLA-Cache (2502.02175)、SR-VLA (2611.22356)、Learning What to Say to Your VLA (2606.12299)、Embodied Interpretability (2605.00321)、From Recovery to Drop-off (2608.08904)、CAC-VLA (2607.04816)
  - WAM 结构：AWAM (2610.23396)、Flex-π (2608.10860，标题已核实，内容未读)
  - 其他：FAVR (2611.20971)、RoVi-Aug (2409.03403)、X-Sim (2505.07096)
- **召回缺口**：
  - TTA 一支的 arXiv 站内检索按时间倒序，listing 被截断：`test-time adaptation vision-language-action` 共 97 条看了约 90 条，`test-time training robot policy` 共 332 条只看了前约 37 条。2023–2025 年的条目可能漏检。
  - WebSearch 额度有限，只用于发现论文；FTM 谱系、基准、TTA 三个子方向分别用了 4、6、3 次。
  - 只读了摘要的条目没有读正文，其中的结论和数字只到摘要层面。
  - ImageWAM 的代码结论只基于 main 分支（2026-11-20 读取）；π0 的结构结论来自论文正文与附录，没有读代码。

## Hypotheses

- LIBERO-Plus 相机维度上同一模型的数字分散，可能部分来自 WACO 指出的"扰动参数泄漏进提示词"（WACO §IV-A），以及各文是否用公开权重、是否重跑。
- InfiNoVA 的标题差异可能只是 ∞ 符号在 abs 页上的转写方式不同。

## Next Experiment

引用前打开 CVPR 2026 论文集确认 LIBERO-Plus 的发表处；用 curl 或 pdftotext 逐字核对 WebFetch 得到的关键数字，优先 WAM-vs-VLA Table 3 / 4、Homeward Table 2 / 3、SALT App. I、Eva-VLA Table 1；第二轮检索补查 2023–2025 年的策略侧 TTA，并核实只在别人表格中出现的方法的 arXiv 编号。

## Resolution
