# real2sim 论文目录

- 快照日期：2026-10-30
- 年份：论文首次出现在 arXiv 的年份。
- 会议/期刊：已确认的发表处；"arXiv" 表示检索时未找到发表处。标 † 的条目来源存疑，见根目录 `issues.md` → ISSUE-001。
- 每条的标题、年份、arXiv 编号均经检索命中核实。
- 分节对应 [survey.md](survey.md) 的分类。

## 1. 真实场景 → 可仿真环境（操作）

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RialTo | Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation | 2024 | RSS 2024 | 2403.03949 | real-to-sim-to-real.github.io/RialTo | 手机扫描 + GUI 手工加关节建孪生；"inverse distillation" 把真实示教迁入孪生后做 RL 微调 |
| CASHER | Robot Learning with Super-Linear Scaling | 2024 | RSS 2025 | 2412.01770 | casher-robot-learning.github.io/CASHER | 众包手机扫描大量孪生，通用策略逐步替代人工示教 |
| DRAWER | DRAWER: Digital Reconstruction and Articulation with Environment Realism | 2025 | CVPR 2025 | 2504.15278 | xiahongchi.github.io/DRAWER | 无交互视频 → SDF 几何 + 网格锚定高斯外观，自动推断抽屉/门关节 |
| HoloScene | HoloScene: Simulation-Ready Interactive 3D Worlds from a Single Video | 2025 | NeurIPS 2025 | 2510.05560 | xiahongchi.github.io/HoloScene | 单视频 → 含刚体参数与支撑关系的交互场景图，基于能量的联合优化 |
| RoboSnap | RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation | 2026 | arXiv | 2607.06699 | robosnap.github.io | 单张 RGB → SAM 3D 前景网格 + GS 背景；构建 DROID-Sim（564 场景） |
| SceneRig | SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images | 2026 | CoRL 2026 Agentic Robotics Workshop | 2610.28585 | red-fairy.github.io/SceneRig | VLM 智能体在仿真器中"编辑—验证"循环；逐 episode 与真实一致率 69% vs SimFoundry 54% |
| DEXTERA | DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real | 2026 | arXiv | 2609.21045 | dextera-project.github.io | 单图 → Hunyuan3D 物体 + Particulate 关节 + VLM 物理默认值；仿真—真实联合训练 29.2% → 61.9% |

## 2. 数字表亲与生成式场景分布

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| URDFormer | URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images | 2024 | RSS 2024 | 2405.11656 | urdformer.github.io | 渲染仿真资产 → 扩散模型真实化 → 学习 图像→URDF 逆映射 |
| ACDC | Automated Creation of Digital Cousins for Robust Policy Learning | 2024 | CoRL 2024 | 2410.07408 | digital-cousins.github.io | 匹配多个语义/几何相似资产（表亲）代替精确孪生；零样本 sim-to-real 90% vs 孪生 25% |
| GRS | GRS: Generating Robotic Simulation Tasks from Real-World Images | 2024 | CVPR 2025 Workshops | 2410.15536 | — | 单张 RGB-D → 检索资产 + LLM 生成任务与测试，迭代修复直到可解 |
| Video2Policy | Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos | 2025 | arXiv | 2502.09886 | yewr.github.io/video2policy | 互联网视频 → 物体网格与 6D 轨迹 → LLM 写奖励做 RL；仿真 72% / 真实 47% |
| RoboTwin | RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins | 2025 | CVPR 2025 Highlight | 2504.13059 | robotwin-benchmark.github.io | 图生 3D 孪生 + LLM 生成专家代码的双臂基准 |
| SimFoundry | SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation | 2026 | arXiv | 2606.28276 | research.nvidia.com/labs/gear/simfoundry | 单视频 → 孪生 → 物体/场景/任务三轴表亲；评测平均 Pearson 0.911 |
| Seeing2Sim | From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation | 2026 | arXiv | 2604.15805 | — | 全景图 → 生成式仿真场景 → 编辑得表亲，拼接多房间环境 |
| AssetFidelity-Eval | Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation | 2026 | arXiv | 2610.00731 | github.com/Kaedim/yam-sim-harness-oss | 两种重建流程对照：度量几何 + 人工物理 r=0.90，默认单图流程 r=0.51 |

## 3. 铰接物体重建（从观测）

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| PARIS | PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects | 2023 | ICCV 2023 | 2308.07391 | 3dlg-hcvc.github.io/paris | 两个关节状态的多视图 → 自监督分离静止/运动部件与关节参数 |
| DigitalTwinArt | Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects | 2024 | CVPR 2024 | 2404.01440 | github.com/NVlabs/DigitalTwinArt | 两状态 RGB-D → 先重建各状态，再求连接它们的关节；支持多运动部件 |
| ArtGS | Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting | 2025 | ICLR 2025 | 2502.19459 | articulate-gs.github.io | 规范高斯融合多状态信息，处理复杂多部件物体 |
| VideoArtGS | VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video | 2025 | arXiv | 2509.17647 | videoartgs.github.io | 单目视频 + 预训练跟踪器运动先验 → 关节；可导出 URDF |
| Articulat3D | Articulat3D: Reconstructing Articulated Digital Twins From Monocular Videos with Geometric and Motion Constraints | 2026 | ECCV 2026 | 2603.11606 | maxwell-zhao.github.io/Articulat3D | 3D 点轨迹 + 运动基 → 软刚体分组 → 运动学精化 |

## 4. 铰接资产推断/生成 → URDF/MJCF

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| Real2Code | Real2Code: Reconstruct Articulated Objects via Code Generation | 2024 | ICLR 2025 | 2406.08474 | github.com/MandiZhao/real2code | OBB 抽象上用微调 CodeLlama 生成 MJCF 关节 |
| Articulate-Anything | Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model | 2024 | ICLR 2025 | 2410.13882 | articulate-anything.github.io | VLM actor–critic 写 URDF 代码，网格从 PartNet-Mobility 检索 |
| SINGAPO | SINGAPO: Single Image Controlled Generation of Articulated Parts in Objects | 2024 | ICLR 2025 | 2410.16499 | 3dlg-hcvc.github.io/singapo | 图引导扩散生成部件属性 + 检索部件网格 |
| Articulate AnyMesh | Articulate AnyMesh: Open-Vocabulary 3D Articulated Objects Modeling | 2025 | CoRL 2025 | 2502.02590 | articulate-anymesh.github.io | 对任意刚体网格做开放词汇部件分割与功能关节 |
| URDF-Anything | URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model | 2025 | NeurIPS 2025 | 2511.00940 | lzvsdy.github.io/URDF-Anything | 3D MLLM 用分割 token 联合预测部件与运动学 |
| SPARK | SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge | 2025 | CVPR 2026 Oral† | 2512.01629 | — | VLM 粗 URDF → 可微 FK + 渲染精化关节 |
| Particulate | Particulate: Feed-Forward 3D Object Articulation | 2025 | CVPR 2026 | 2512.11798 | ruiningli.com/particulate | 前馈 Transformer 数秒内给静态网格加部件、运动学树和运动参数 |
| PhysX-Anything | PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image | 2025 | CVPR 2026† | 2511.13648 | physx-anything.github.io | 单图 → 几何 + 关节 + 尺度/材料/可供性 → URDF/XML |
| URDF-Anything+ | URDF-Anything+: End-to-End Generation for Simulation-Ready Articulated Assets | 2026 | NeurIPS 2026† | 2603.14010 | urdf-anything-plus.github.io | 端到端自回归扩散逐部件生成，替代多阶段流程与资产检索 |

## 5. 资产来源与物理有效性

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| SAM 3D Objects | SAM 3D: 3Dfy Anything in Images | 2025 | arXiv | 2511.16624 | huggingface.co/facebook/sam-3d-objects | 单图 + 掩码 → 物体形状、纹理与布局；2026 年多条 real2sim 流程的默认资产源 |
| SVMR-Bench | Is Single-View Mesh Reconstruction Ready for Robotics? | 2025 | BMVC 2026 | 2505.17966 | — | 用机器人标准评测 13 个单视图重建模型，无一满足 |
| SimuScene | SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image | 2026 | arXiv | 2606.03994 | snuvclab.github.io/SimuScene | 重建过程中把物理引擎当诊断信号修正形状和布局 |
| Picasso | Picasso: Holistic Scene Reconstruction with Physics-Constrained Sampling | 2026 | RSS 2026 | 2602.08058 | github.com/MIT-SPARK/Picasso | 接触图引导的全场景拒绝采样，保证无穿透与稳定 |
| PhysConsistent-R2S | Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning | 2026 | arXiv | 2602.12633 | physics-constrained-real2sim.github.io | 接触图上用可微刚体仿真优化位姿、质心、质量、摩擦 |
| Scalable Real2Sim | Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups | 2025 | IROS 2025† | 2503.00370 | github.com/nepfaff/scalable-real2sim | 机器人抓取—扫描—激励物体，用关节力矩做带可行性约束的 SDP 惯性辨识 |

## 6. 渲染耦合仿真：策略训练与数据生成

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| Embodied Gaussians | Physically Embodied Gaussian Splatting: A Visually Learnt and Physically Grounded 3D Representation for Robotics | 2024 | CoRL 2024 | 2406.10788 | embodied-gaussians.github.io | 高斯绑在 PBD 粒子上，光度误差变成修正仿真状态的"视觉力" |
| SplatSim | SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting | 2024 | ICRA 2025 | 2409.10161 | github.com/qureshinomaan/SplatSim | 机器人连杆高斯随 FK 运动、物体高斯随仿真位姿运动；零样本真实 86.25% |
| RL-GSBridge | RL-GSBridge: 3D Gaussian Splatting Based Real2Sim2Real Method for Robotic Manipulation Learning | 2024 | ICRA 2025 | 2409.20291 | github.com/IRMV-Manipulation-Group/RL-GSBridge | 网格绑定高斯随物理同步编辑，供视觉 RL |
| RoboGSim | RoboGSim: A Real2Sim2Real Robotic Gaussian Splatting Simulator | 2024 | arXiv | 2411.11839 | robogsim.github.io | 重建、孪生构建、场景组合、交互引擎四模块的 GS 仿真器 |
| DreMa | Dream to Manipulate: Compositional World Models Empowering Robot Imitation Learning with Imagination | 2024 | ICLR 2025 | 2412.14957 | leobarcellona.github.io/DreamToManipulate | 以物体为中心的高斯 + 物理仿真，等变变换少量真实示教生成新示教 |
| Re3Sim | Re³Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation | 2025 | arXiv | 2502.08645 | xshenhan.github.io/Re3Sim | GS 背景 + 光追网格前景的混合渲染，特权规划器生成示教 |
| DISCOVERSE | DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity Environments | 2025 | IROS 2025 | 2507.21981 | air-discoverse.github.io | 3DGS + MuJoCo 统一框架，5 路 RGB-D 约 650 FPS |
| X-Sim | X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real | 2025 | CoRL 2025 Oral | 2505.07096 | portal-cornell.github.io/X-Sim | 人类视频中物体运动 → 逼真孪生中物体中心奖励 RL → 蒸馏图像策略 |
| RoboSimGS | High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic Manipulation Learning with Gaussian Splatting | 2025 | IEEE RA-L 2026 | 2510.10637 | robosimgs.github.io | MLLM 推断物理基元的密度、刚度和关节，高斯负责外观 |
| TwinAligner | TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation | 2025 | arXiv | 2512.19390 | twin-aligner.github.io | 像素级视觉对齐 + 交互轨迹刚体动力学辨识 |
| DREAM | DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation | 2026 | arXiv | 2608.29078 | — | 部署现场重建 → LLM 生成目标与成功判定 → TAMP 生成示教微调 VLA |

## 7. 无闭环动力学的逼真数据生成

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RoboSplat | Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation | 2025 | RSS 2025 | 2504.13175 | github.com/InternRobotics/RoboSplat | 直接编辑单条示教的高斯，沿 6 个泛化轴增广 |
| R2R2R | Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware | 2025 | CoRL 2025 | 2505.09601 | real2render2real.com | 关闭动力学，IsaacLab 只当渲染器，运动学重定向人类示教 |
| ReBot | ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Robotic Video Synthesis | 2025 | IROS 2025 | 2503.14526 | yuffish.github.io/rebot | 仿真中回放真实轨迹换新物体，合成到修复后的真实视频背景上 |
| RoLA | Robot Learning from Any Images | 2025 | CoRL 2025 | 2509.22970 | rola-2025.github.io | 单张野外图像 → 物理场景 → 仿真轨迹混合回原照片 |

## 8. real2sim 策略评测

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| SIMPLER | Evaluating Real-World Robot Manipulation Policies in Simulation | 2024 | CoRL 2024 | 2405.05941 | simpler-env.github.io | 绿幕 visual matching + 系统辨识；提出 MMRV，Google Robot 上 r=0.924 |
| Real-is-Sim | Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin | 2025 | arXiv | 2504.03597 | realissim.rai-inst.com | 策略始终作用于与现实 60 Hz 同步的孪生，真机跟随孪生 |
| GSWorld | GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation | 2025 | arXiv | 2510.20813 | 3dgsworld.github.io | GSDF 高斯-网格资产，同一孪生用于训练、评测、失败回放和 DAgger 标注 |
| RobotArena∞ | RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation | 2025 | ICLR 2026 | 2510.23571 | robotarenainf.github.io | 把数据集视频转成孪生，用 VLM 与众包偏好打分 |
| Real2Sim-Eval | Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions | 2025 | ICRA 2026 | 2511.04665 | real2sim-eval.github.io | GS 渲染 + PhysTwin 软体，3 个任务 r 0.90–0.94 |
| PolaRiS | PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies | 2025 | RSS 2026 | 2512.16881 | polaris-evals.github.io | GS 评测场景 + 短暂仿真联合训练使通用策略可评测；6 场景平均 r=0.90，与 RoboArena r=0.98 |
| ReVeal | ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation | 2026 | arXiv | 2609.23910 | — | 重建级指标判断孪生是否够用；r 随重建质量从 0.773 升到 0.960 |
| YUBI-Real2Sim | YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation | 2026 | arXiv | 2610.17521 | yubi-real2sim.airoa.io | 鱼眼腕部相机场景验证；新视角质量分数不能可靠预测排序可靠性 |

## 9. 学习型世界模型作为仿真器（对照范式）

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| UniSim (WM) | Learning Interactive Real-World Simulators | 2023 | ICLR 2024 Outstanding Paper | 2310.06114 | universal-simulator.github.io | 动作/语言条件视频模拟器，纯在其中训练的策略零样本迁移 |
| WorldEval | WorldEval: World Model as Real-World Robot Policies Evaluator | 2025 | arXiv | 2505.19017 | worldeval.github.io | 以被评策略的潜动作（Policy2Vec）条件化视频模型；3 任务 r=0.942 |
| WorldGym | WorldGym: World Model as An Environment for Policy Evaluation | 2025 | ICLR 2026 | 2506.00613 | — | 世界模型中蒙特卡洛 rollout + GPT-4o 判定成功；17 个 Bridge 任务 r=0.78 |
| DreamGen | DreamGen: Unlocking Generalization in Robot Learning through Video World Models | 2025 | CoRL 2025 | 2505.12705 | github.com/NVIDIA/GR00T-Dreams | 视频世界模型生成"神经轨迹"，伪标注动作训练策略 |
| Genie Envisioner | Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation | 2025 | arXiv | 2508.05635 | genie-envisioner.github.io | 视频 DiT 同时作为策略、仿真器与基准 |
| Ctrl-World | Ctrl-World: A Controllable Generative World Model for Robot Manipulation | 2025 | ICLR 2026 | 2510.10125 | — | 多视图可控世界模型做闭环想象评测；排序大体一致，绝对成功率偏低 |
| Veo-WS | Evaluating Gemini Robotics Policies in a Veo World Simulator | 2025 | arXiv | 2512.10675 | — | 位姿条件多视图 Veo；1600+ 真实评测，OOD r=0.86 |
| WEAVER | WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation | 2026 | arXiv | 2606.13672 | arnavkj1995.github.io/WEAVER | 潜空间 flow matching 世界模型，ρ=0.870 |
| Mem-World | Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation | 2026 | CoRL 2026 | 2606.18960 | — | 面元索引的腕部视角 4D 记忆，缓解遮挡下遗忘与幻觉 |
| PhysCanvas | Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning | 2026 | arXiv | 2610.28613 | zebinx.github.io/PhysCanvas_HomePage | 视触觉世界模型 + 真实结果一致性奖励后训练；r 0.602 → 0.885 |

## 10. 视觉 gap 与逼真度研究

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| Sim2Real-VLA study | Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models | 2026 | arXiv | 2603.22876 | — | >10k 真实试验；逼真度提升真实成功率，但超过中等光追后饱和 |
| WorldArena | WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models | 2026 | arXiv | 2602.08971 | worldarena.ai | 视频质量不能可靠预测具身功能效用（"perception–functionality gap"） |

## 11. 刚体系统辨识与仿真参数推断

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| SimOpt | Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience | 2018 | ICRA 2019 | 1810.05687 | sites.google.com/view/simopt | 用少量真实 rollout 以 REPS 调整域随机化分布，而非点估计 |
| BayesSim | BayesSim: adaptive domain randomization via probabilistic inference for robotics simulators | 2019 | RSS 2019 | 1906.01728 | github.com/rafaelpossas/bayes_sim | 黑盒仿真器上学习摊销后验 p(θ \| 轨迹统计量)；RSS 版无真机实验 |
| gradSim | gradSim: Differentiable simulation for system identification and visuomotor control | 2021 | ICLR 2021 | 2104.02646 | gradsim.github.io | 可微多物理 + 可微渲染，从像素端到端求物理参数梯度 |
| DROPO | DROPO: Sim-to-Real Transfer with Offline Domain Randomization | 2022 | Robotics and Autonomous Systems 2023 | 2201.08434 | — | 离线真实转移上用 CMA-ES 拟合随机化分布的均值与方差 |
| AdaptSim | AdaptSim: Task-Driven Simulation Adaptation for Sim-to-Real Transfer | 2023 | CoRL 2023 | 2302.04903 | irom-lab.github.io/AdaptSim | 以任务表现而非动力学匹配为目标调整仿真参数 |
| ASID | ASID: Active Exploration for System Identification in Robotic Manipulation | 2024 | ICLR 2024 | 2404.12308 | weirdlabuw.github.io/asid | 用不完美仿真规划最大化 Fisher 信息的真实探索，再标定 |
| Phys2Real | Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation | 2025 | ICRA 2026 | 2510.11689 | phys2real.github.io | VLM 物理先验与在线辨识按逆方差融合 |
| VLM-BT Real2Sim | Real2Sim via Active Perception with Behavior Trees Automatically Generated by VLMs | 2026 | arXiv | 2601.08454 | — | VLM 决定测哪些参数，生成行为树执行探测 |
| RigPI | RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation | 2026 | arXiv† | 2606.25212 | — | VLM 初始化并限定搜索空间，再在 NVIDIA Newton 中两阶段梯度精化 |

## 12. 可变形 / 颗粒 / 流体物理孪生

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| PAC-NeRF | PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification | 2023 | ICLR 2023 | 2303.05512 | xuan-li.github.io/PAC-NeRF | 可微 MPM + NeRF，联合辨识几何与弹性/塑性/颗粒/流体参数 |
| PhysGaussian | PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics | 2023 | CVPR 2024 | 2311.12198 | github.com/XPandora/PhysGaussian | MPM 直接作用于高斯核，"所见即所仿" |
| Spring-Gaus | Reconstruction and Simulation of Elastic Objects with Spring-Mass 3D Gaussians | 2024 | ECCV 2024 | 2403.09434 | zlicheng.com/spring_gaus | 弹簧-质点模型锚定 3DGS，物理学习与外观解耦 |
| PhysDreamer | PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation | 2024 | ECCV 2024 Oral | 2404.13026 | physdreamer.github.io | 把视频生成模型的运动先验蒸馏为材料场 |
| GIC | GIC: Gaussian-Informed Continuum for Physical Property Identification and Simulation | 2024 | NeurIPS 2024 | 2406.14927 | jukgei.github.io/project/gic | 高斯几何为物性辨识提供显式形状监督 |
| NeuMA | Neural Material Adaptor for Visual Grounding of Intrinsic Dynamics | 2024 | NeurIPS 2024 | 2410.08257 | xjay18.github.io/projects/neuma.html | 预训练神经本构律 + LoRA 低秩残差 |
| OmniPhysGS | OmniPhysGS: 3D Constitutive Gaussians for General Physics-Based Dynamics Generation | 2025 | ICLR 2025 | 2501.18982 | wgsxm.github.io/projects/omniphysgs | 每个高斯学习 12 种本构模型的混合权重 |
| PhysTwin | PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos | 2025 | ICCV 2025 | 2503.17973 | jianghanxiao.github.io/phystwin-web | 三视角 RGB-D 交互视频 → 零阶 + 一阶两阶段逆物理 → 可实时仿真的形变孪生 |
| DPSI | Differentiable Physics-based System Identification for Robotic Manipulation of Elastoplastic Materials | 2024 | IJRR 2025 | 2411.00554 | ianyangchina.github.io/SI4RP-data | 一次按压/推移交互即可辨识可解释的弹塑性参数 |
| PGND | Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos | 2025 | RSS 2025 | 2506.15680 | kywind.github.io/pgnd | 完全学习的粒子-网格神经动力学，用于 MPC |
| Pixie | Pixie: Fast and Generalizable Supervised Learning of 3D Physics from Pixels | 2025 | arXiv | 2508.17437 | pixie-3d.github.io | 前馈预测材料类别与 E、ν、密度场，数秒得到可仿真高斯场景 |
| MOSIV | Multi-Object System Identification from Videos | 2026 | ICLR 2026 | 2603.06022 | — | 多物体逐物体连续材料参数辨识（仅合成数据） |
| EgoPhys | EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video | 2026 | arXiv | 2606.16202 | hjhyunjinkim.github.io/EgoPhys | 单段第一人称视频 → 摊销的稠密弹簧刚度 |
| FORM | FORM: Robot Manipulation through Direct Material Law Identification | 2026 | arXiv | 2609.38105 | form-robots.github.io | 弱形式动量平衡化为线性最小二乘，辨识从 10–25 min 降到 2–5 s |

## 13. 机器人侧动力学对齐

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| ActuatorNet | Learning agile and dynamic motor skills for legged robots | 2019 | Science Robotics 2019 | 1901.08652 | — | 用真实执行器数据训练执行器网络替代理想模型 |
| ASAP | ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | 2025 | RSS 2025 | 2502.01143 | — | 残差动作模型 Δa(s,a) 让仿真复现真实转移，再在增强仿真中微调 |
| UAN | Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation | 2025 | ICLR 2025 Workshop (WRL) | 2502.10894 | uan.csail.mit.edu | 无力矩传感器，用 RL 训练修正力矩的执行器网络 |
| SPI-Active | Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning | 2025 | CoRL 2025 | 2505.14266 | github.com/LeCAR-Lab/SPI-Active | 大规模并行 CMA-ES 轨迹匹配 + 按 Fisher 信息设计指令 |
| Dao & Fern 2026 | Simulator Adaptation for Sim-to-Real Learning of Legged Locomotion via Proprioceptive Distribution Matching | 2026 | arXiv | 2604.11090 | — | 匹配本体感知分布而非时间对齐轨迹，无需动捕 |
| NeuralActuator | NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception | 2026 | RSS 2026 | 2607.11734 | frank-zy-dou.github.io/projects/NeuralActuator | 通过可微仿真从位姿轨迹学习舵机力矩代理模型 |
| HumanoidNDM | HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model | 2026 | CoRL 2026 | 2610.34126 | — | 真机数据训练人形神经动力学模型，经模型反传梯度在线微调跟踪策略，免动捕；主归属 [humanoid-motion-tracking](../humanoid-motion-tracking/papers.md) |
| IDTD | Informationally Decoupled Trajectory Design for Sim-to-Real System Identification | 2026 | arXiv | 2610.10905 | github.com/jsw7460/IDTD | 轨迹分段各自隔离一组参数，打破参数耦合 |

## 14. 残差物理与混合仿真

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| TossingBot | TossingBot: Learning to Throw Arbitrary Objects with Residual Physics | 2019 | RSS 2019 | 1903.11239 | tossingbot.cs.princeton.edu | 网络修正弹道控制器输出的释放速度 |
| NeuralSim | NeuralSim: Augmenting Differentiable Simulators with Neural Networks | 2020 | ICRA 2021 | 2011.04217 | sites.google.com/usc.edu/neuralsim | 把神经模块嵌入可微刚体引擎内部 |
| NeRD | Neural Robot Dynamics | 2025 | CoRL 2025 | 2508.15755 | github.com/NVlabs/neural-robot-dynamics | 学习的机器人中心动力学替代求解器，可用真实数据微调 |
| CLASH | CLASH: Collision Learning via Augmented Sim-to-real Hybridization to Bridge the Reality Gap | 2026 | arXiv | 2602.18707 | — | gap 拆为辨识的接触参数 + 早停的小残差，约 10 次真实碰撞 |
| RAFL | RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning | 2026 | arXiv | 2603.22039 | — | 局部、拓扑无关的残差加速度场，可跨形态迁移 |

## 15. 足式运动与导航

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| LucidSim | Learning Visual Parkour from Generated Images | 2024 | CoRL 2024 | 2411.00083 | lucidsim.github.io | 对照：不重建真实场景，生成图像训练 RGB 跑酷 |
| Vid2Sim | Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation | 2025 | CVPR 2025 | 2501.06693 | metadriverse.github.io/vid2sim | 单目网络视频 → 3DGS + TSDF 碰撞网格 → RL 导航 |
| VR-Robo | VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion | 2025 | IEEE RA-L 2025 | 2502.01536 | vr-robo.github.io | GS 渲染 + 网格物理混合，Go2 仅 RGB 上楼梯找目标 |
| EmbodiedSplat | EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device | 2025 | ICCV 2025 | 2509.17430 | gchhablani.github.io/embodied-splat | iPhone RGB-D → Habitat-Sim，针对部署地点微调导航策略 |
| GaussGym | GaussGym: An open-source real-to-sim framework for learning locomotion from pixels | 2025 | arXiv | 2510.15352 | escontrela.me/gauss_gym | 多源输入 → VGGT → 3DGS + NKSR 网格，>100k steps/s 视觉 RL |
| UrbanVerse | UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos | 2025 | ICLR 2026 | 2510.15018 | urbanverseproject.github.io | 城市漫游视频 → 布局 + 检索资产（不重建） |
| S2E | From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning | 2025 | ICLR 2026 | 2507.22028 | vail-ucla.github.io/S2E | 带物理的 GS 场景中对视频预训练导航模型做 RL 后训练 |
| Wanderland | Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI | 2025 | CVPR 2026 | 2511.20620 | ai4ce.github.io/wanderland | LiDAR 度量重建基准；指出纯视频 real2sim 度量上不可靠 |
| ReaDy-Go | ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles | 2026 | IEEE RA-L 2026 | 2602.11575 | syeon-yoo.github.io/ready-go-site | 静态 GS 场景 + 可动画 GS 人体，在行人中导航 |
| QuadVerse | QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation | 2026 | arXiv | 2606.07118 | quad-verse.github.io | 视频 → 3DGS + 网格 + 摩擦后验 + 残差动力学，视觉与物理同时对齐 |
| VLK | VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes | 2026 | arXiv | 2606.30645 | vision-language-kinematics.github.io | 度量 3DGS 室内场景合成 48k 轨迹，G1 导航与搬箱 |
| LEGS | LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World | 2026 | arXiv | 2606.01458 | hojjunekim.github.io/legs | GS 背景 + 网格前景，免遥操作微调 G1 移动操作 VLA |

## 16. 自动驾驶闭环仿真

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| UniSim (driving) | UniSim: A Neural Closed-Loop Sensor Simulator | 2023 | CVPR 2023 Highlight | 2308.01898 | — | 驾驶日志 → 神经特征网格，可编辑闭环多传感器仿真 |
| NeuRAD | NeuRAD: Neural Rendering for Autonomous Driving | 2023 | CVPR 2024 | 2311.15260 | github.com/georghess/NeuRAD | 带精细传感器模型的 NeRF |
| OmniRe | OmniRe: Omni Urban Scene Reconstruction | 2024 | ICLR 2025 Spotlight | 2408.16760 | github.com/ziyc/drivestudio | 高斯场景图覆盖所有动态参与者，包括 SMPL 行人 |
| HUGSIM | HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving | 2024 | IEEE TPAMI | 2412.01718 | — | 实时 3DGS 闭环基准 |
| RAD | RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning | 2025 | NeurIPS 2025 | 2502.13144 | github.com/hustvl/RAD | 4,305 段逐段 3DGS 场景中 RL 后训练端到端规划器 |
| NAVSIM v2 | Pseudo-Simulation for Autonomous Driving | 2025 | CoRL 2025 | 2506.04218 | github.com/autonomousvision/navsim | 预渲染 3DGS 反事实视角做伪仿真评测；与闭环 R²=0.8 |
| SimScale | SimScale: Learning to Drive via Real-World Simulation at Scale | 2025 | CVPR 2026 Oral | 2511.23369 | github.com/OpenDriveLab/SimScale | 仿真—真实联合训练，收益随仿真数据量持续增长 |
| REAP | REAP: Reinforcement-Learning End-to-End Autonomous Parking with Gaussian Splatting Simulator for Real2Sim2Real Transfer | 2026 | arXiv | 2605.08713 | — | 3DGS 停车场场景 RL 泊车，实车迁移 |

## 17. 人类视频 → 仿真

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| VideoMimic | Visual Imitation Enables Contextual Humanoid Control | 2025 | CoRL 2025 | 2505.03729 | videomimic.net | 手机视频 → 度量 4D 人体 + 场景 → RL 跟踪，G1 上楼梯、坐下 |
| HDMI | HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos | 2025 | arXiv | 2509.16757 | hdmi-humanoid.github.io | 视频 → 人体与物体轨迹 → G1 人–物交互；部署需动捕 |
| CRISP | CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives | 2025 | ICLR 2026 | 2512.14696 | crisp-real2sim.github.io/CRISP-Real2Sim | 接触引导的平面基元场景，物理合理的人形跟踪 |
| Real2Sim-HOI | Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos | 2026 | arXiv | 2605.14462 | knoxzhao.github.io/real2sim_in_HOI | 视频 → 4D 人–物交互，作为物理 rollout 的教师轨迹（仅仿真） |
| Human2Sim2Robot | Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL using One Human Demonstration | 2025 | CoRL 2025 | 2504.12609 | proceedings.mlr.press/v305/lum25a.html | 物体轨迹 + 预抓取位姿作物体中心 RL 奖励，Allegro 手零样本上真机 |
| Video2Sim2Real | Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video | 2026 | arXiv | 2606.08828 | video2sim2real.github.io | 单视频 → 孪生 + 运动先验 → 模仿学习 + 残差 RL 灵巧操作 |

## 18. 综述、框架与工具

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RealityGap-Survey | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 2025 | Annual Review of Control, Robotics, and Autonomous Systems 2026 | 2510.20808 | — | 把 real2sim 放在"改进仿真"之下，拆为几何、运动学/动力学、渲染三个逆问题 |
| 3DGen4Robot-Survey | 3D Generation for Embodied AI and Robotic Simulation: A Survey | 2026 | arXiv | 2604.26509 | 3dgen4robot.github.io | 3D 生成的三种角色：数据生成器、仿真环境、Sim2Real 桥 |
| 3DGS-Robotics-Survey | 3D Gaussian Splatting in Robotics: A Survey | 2024 | arXiv | 2410.12262 | — | 按场景理解 / 交互组织 3DGS 应用 |
| NeuralFields-Survey | Neural Fields in Robotics: A Survey | 2024 | arXiv | 2410.20220 | robonerf.github.io | 4 种表示 × 5 个领域 |
| DT2EAI-Review | Digital twins to embodied artificial intelligence: review and perspective | 2025 | Intelligence & Robotics 2025 | doi 10.20517/ir.2025.11 | — | 数字孪生与具身 AI 的三种协同 |
| RoboVerse | RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning | 2025 | RSS 2025 | 2504.18904 | roboverseorg.github.io | 多仿真器平台，含 GS 与网格重建 → URDF 的 Real2Sim 工具集 |
| Isaac Lab | Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | 2025 | arXiv | 2511.04831 | github.com/isaac-sim/IsaacLab | 可在物理资产旁渲染 NuRec 3DGS/3DGUT 场景 |
| 3DGUT | 3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting | 2024 | CVPR 2025 | 2412.12507 | github.com/nv-tlabs/3dgrut | NVIDIA NuRec 渲染背后的高斯渲染引擎 |

## 补充（已核实，未列入主表）

- 场景与资产：MotionAnymesh (2603.12936)，Kinematify (2511.01294)，Infinite Mobility (2503.13424)，ArtiPoint (2509.01708, CoRL 2025)，EmbodiedGen (2506.10600)，PhysWorld-video (2511.07416)，OP-Gen (2509.06191)，RecGen (2604.27106)，LiteReality (2507.02861, NeurIPS 2025)，ForceTwin (2609.21751)，Subsecond 3D Mesh Generation (2512.24428)
- 渲染与评测：Robo-GS (2408.14873, ICRA 2025)，RoboPearls (2506.22756, ICCV 2025)，EnerVerse-AC (2505.09723)，IRASim (2406.14540)，GASE (2606.17520)，ManiSplat (2606.10645)，EmbodieDreamer (2507.05198)，Prompting with the Future (2506.13761, RSS 2025)，World-in-World (2510.18135, ICLR 2026)，Robot Policy Evaluation for Sim-to-Real Transfer (2508.11117)，Cosmos-Surg-dVRK (2510.16240)，MolmoSpaces (2602.11337)
- 物理与动力学：NPDR (CoRL 2021, PMLR v164)，ASBI (2510.15331)，Neural Fidelity Calibration (2504.08604)，Kamaras et al. (2510.26656)，Agentic Real2Sim (2607.19190)，AdaptiGraph (2407.07889, RSS 2024)，PhysFlow (2411.14423, CVPR 2025)，VisionLaw (2508.13792, ICLR 2026)，VoMP (2510.22975)，PhysWorld-MPM (2510.21447)，EMPM (2601.17251)，BendTwin (2608.06164)，KnockGS (2608.27365)，DDBot (2510.17335, T-RO 2026)，Ru et al. fabric study (2503.16310)，Gao et al. soft robot residual (2402.01086, RA-L 2024)，HALO (2603.15084)，Kovalev et al. (2604.10351)，Bjelonic et al. (2509.06342, IJRR 2026)，FADA (2606.28476)
- 场景与人类：DexMachina (2505.24853, ICML 2026)，SPIDER (2511.09484)，OmniRetarget (2509.26633)，Dex-One2Many (2610.12470)，RAD-2 (2604.15308)，Cosmos-Drive-Dreams (2506.09042)，RL sim-to-real survey (2502.13187)，ACM CSUR physics-simulator survey (2505.01458)，position paper "Robots Need More than VLA and World Models" (2606.06556)
