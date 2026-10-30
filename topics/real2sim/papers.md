# real2sim 论文目录

- 快照日期：2026-10-30
- 年份：论文首次出现在 arXiv 的年份。
- 会议/期刊：已确认的发表处；"预印本" 表示检索时未找到发表处。标 † 的条目来源存疑，见根目录 `issues.md` → ISSUE-001。
- 每条的标题、年份、arXiv 编号均经检索命中核实。
- 分节对应 [survey.md](survey.md) 的分类。

## 1. 真实场景 → 可仿真环境（操作）

- **RialTo** · 2024 · RSS 2024 · [arXiv 2403.03949](https://arxiv.org/abs/2403.03949) · [项目](https://real-to-sim-to-real.github.io/RialTo)
  - Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation
  - 手机扫描 + GUI 手工加关节建孪生；"inverse distillation" 把真实示教迁入孪生后做 RL 微调
- **CASHER** · 2024 · RSS 2025 · [arXiv 2412.01770](https://arxiv.org/abs/2412.01770) · [项目](https://casher-robot-learning.github.io/CASHER)
  - Robot Learning with Super-Linear Scaling
  - 众包手机扫描大量孪生，通用策略逐步替代人工示教
- **DRAWER** · 2025 · CVPR 2025 · [arXiv 2504.15278](https://arxiv.org/abs/2504.15278) · [项目](https://xiahongchi.github.io/DRAWER)
  - DRAWER: Digital Reconstruction and Articulation with Environment Realism
  - 无交互视频 → SDF 几何 + 网格锚定高斯外观，自动推断抽屉/门关节
- **HoloScene** · 2025 · NeurIPS 2025 · [arXiv 2510.05560](https://arxiv.org/abs/2510.05560) · [项目](https://xiahongchi.github.io/HoloScene)
  - HoloScene: Simulation-Ready Interactive 3D Worlds from a Single Video
  - 单视频 → 含刚体参数与支撑关系的交互场景图，基于能量的联合优化
- **RoboSnap** · 2026 · 预印本 · [arXiv 2607.06699](https://arxiv.org/abs/2607.06699) · [项目](https://robosnap.github.io)
  - RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation
  - 单张 RGB → SAM 3D 前景网格 + GS 背景；构建 DROID-Sim（564 场景）
- **SceneRig** · 2026 · CoRL 2026 Agentic Robotics Workshop · [arXiv 2610.28585](https://arxiv.org/abs/2610.28585) · [项目](https://red-fairy.github.io/SceneRig)
  - SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images
  - VLM 智能体在仿真器中"编辑—验证"循环；逐 episode 与真实一致率 69% vs SimFoundry 54%
- **DEXTERA** · 2026 · 预印本 · [arXiv 2609.21045](https://arxiv.org/abs/2609.21045) · [项目](https://dextera-project.github.io)
  - DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real
  - 单图 → Hunyuan3D 物体 + Particulate 关节 + VLM 物理默认值；仿真—真实联合训练 29.2% → 61.9%

## 2. 数字表亲与生成式场景分布

- **URDFormer** · 2024 · RSS 2024 · [arXiv 2405.11656](https://arxiv.org/abs/2405.11656) · [项目](https://urdformer.github.io)
  - URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images
  - 渲染仿真资产 → 扩散模型真实化 → 学习 图像→URDF 逆映射
- **ACDC** · 2024 · CoRL 2024 · [arXiv 2410.07408](https://arxiv.org/abs/2410.07408) · [项目](https://digital-cousins.github.io)
  - Automated Creation of Digital Cousins for Robust Policy Learning
  - 匹配多个语义/几何相似资产（表亲）代替精确孪生；零样本 sim-to-real 90% vs 孪生 25%
- **GRS** · 2024 · CVPR 2025 Workshops · [arXiv 2410.15536](https://arxiv.org/abs/2410.15536)
  - GRS: Generating Robotic Simulation Tasks from Real-World Images
  - 单张 RGB-D → 检索资产 + LLM 生成任务与测试，迭代修复直到可解
- **Video2Policy** · 2025 · 预印本 · [arXiv 2502.09886](https://arxiv.org/abs/2502.09886) · [项目](https://yewr.github.io/video2policy)
  - Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos
  - 互联网视频 → 物体网格与 6D 轨迹 → LLM 写奖励做 RL；仿真 72% / 真实 47%
- **RoboTwin** · 2025 · CVPR 2025 Highlight · [arXiv 2504.13059](https://arxiv.org/abs/2504.13059) · [项目](https://robotwin-benchmark.github.io)
  - RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins
  - 图生 3D 孪生 + LLM 生成专家代码的双臂基准
- **SimFoundry** · 2026 · 预印本 · [arXiv 2606.28276](https://arxiv.org/abs/2606.28276) · [项目](https://research.nvidia.com/labs/gear/simfoundry)
  - SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation
  - 单视频 → 孪生 → 物体/场景/任务三轴表亲；评测平均 Pearson 0.911
- **Seeing2Sim** · 2026 · 预印本 · [arXiv 2604.15805](https://arxiv.org/abs/2604.15805)
  - From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation
  - 全景图 → 生成式仿真场景 → 编辑得表亲，拼接多房间环境
- **AssetFidelity-Eval** · 2026 · 预印本 · [arXiv 2610.00731](https://arxiv.org/abs/2610.00731) · [代码](https://github.com/Kaedim/yam-sim-harness-oss)
  - Measuring Asset and Scene Reconstruction Effects in Real-to-Sim Robot Evaluation
  - 两种重建流程对照：度量几何 + 人工物理 r=0.90，默认单图流程 r=0.51

## 3. 铰接物体重建（从观测）

- **PARIS** · 2023 · ICCV 2023 · [arXiv 2308.07391](https://arxiv.org/abs/2308.07391) · [项目](https://3dlg-hcvc.github.io/paris)
  - PARIS: Part-level Reconstruction and Motion Analysis for Articulated Objects
  - 两个关节状态的多视图 → 自监督分离静止/运动部件与关节参数
- **DigitalTwinArt** · 2024 · CVPR 2024 · [arXiv 2404.01440](https://arxiv.org/abs/2404.01440) · [代码](https://github.com/NVlabs/DigitalTwinArt)
  - Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects
  - 两状态 RGB-D → 先重建各状态，再求连接它们的关节；支持多运动部件
- **ArtGS** · 2025 · ICLR 2025 · [arXiv 2502.19459](https://arxiv.org/abs/2502.19459) · [项目](https://articulate-gs.github.io)
  - Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting
  - 规范高斯融合多状态信息，处理复杂多部件物体
- **VideoArtGS** · 2025 · 预印本 · [arXiv 2509.17647](https://arxiv.org/abs/2509.17647) · [项目](https://videoartgs.github.io)
  - VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video
  - 单目视频 + 预训练跟踪器运动先验 → 关节；可导出 URDF
- **Articulat3D** · 2026 · ECCV 2026 · [arXiv 2603.11606](https://arxiv.org/abs/2603.11606) · [项目](https://maxwell-zhao.github.io/Articulat3D)
  - Articulat3D: Reconstructing Articulated Digital Twins From Monocular Videos with Geometric and Motion Constraints
  - 3D 点轨迹 + 运动基 → 软刚体分组 → 运动学精化

## 4. 铰接资产推断/生成 → URDF/MJCF

- **Real2Code** · 2024 · ICLR 2025 · [arXiv 2406.08474](https://arxiv.org/abs/2406.08474) · [代码](https://github.com/MandiZhao/real2code)
  - Real2Code: Reconstruct Articulated Objects via Code Generation
  - OBB 抽象上用微调 CodeLlama 生成 MJCF 关节
- **Articulate-Anything** · 2024 · ICLR 2025 · [arXiv 2410.13882](https://arxiv.org/abs/2410.13882) · [项目](https://articulate-anything.github.io)
  - Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model
  - VLM actor–critic 写 URDF 代码，网格从 PartNet-Mobility 检索
- **SINGAPO** · 2024 · ICLR 2025 · [arXiv 2410.16499](https://arxiv.org/abs/2410.16499) · [项目](https://3dlg-hcvc.github.io/singapo)
  - SINGAPO: Single Image Controlled Generation of Articulated Parts in Objects
  - 图引导扩散生成部件属性 + 检索部件网格
- **Articulate AnyMesh** · 2025 · CoRL 2025 · [arXiv 2502.02590](https://arxiv.org/abs/2502.02590) · [项目](https://articulate-anymesh.github.io)
  - Articulate AnyMesh: Open-Vocabulary 3D Articulated Objects Modeling
  - 对任意刚体网格做开放词汇部件分割与功能关节
- **URDF-Anything** · 2025 · NeurIPS 2025 · [arXiv 2511.00940](https://arxiv.org/abs/2511.00940) · [项目](https://lzvsdy.github.io/URDF-Anything)
  - URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model
  - 3D MLLM 用分割 token 联合预测部件与运动学
- **SPARK** · 2025 · CVPR 2026 Oral† · [arXiv 2512.01629](https://arxiv.org/abs/2512.01629)
  - SPARK: Sim-ready Part-level Articulated Reconstruction with VLM Knowledge
  - VLM 粗 URDF → 可微 FK + 渲染精化关节
- **Particulate** · 2025 · CVPR 2026 · [arXiv 2512.11798](https://arxiv.org/abs/2512.11798) · [项目](https://ruiningli.com/particulate)
  - Particulate: Feed-Forward 3D Object Articulation
  - 前馈 Transformer 数秒内给静态网格加部件、运动学树和运动参数
- **PhysX-Anything** · 2025 · CVPR 2026† · [arXiv 2511.13648](https://arxiv.org/abs/2511.13648) · [项目](https://physx-anything.github.io)
  - PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
  - 单图 → 几何 + 关节 + 尺度/材料/可供性 → URDF/XML
- **URDF-Anything+** · 2026 · NeurIPS 2026† · [arXiv 2603.14010](https://arxiv.org/abs/2603.14010) · [项目](https://urdf-anything-plus.github.io)
  - URDF-Anything+: End-to-End Generation for Simulation-Ready Articulated Assets
  - 端到端自回归扩散逐部件生成，替代多阶段流程与资产检索

## 5. 资产来源与物理有效性

- **SAM 3D Objects** · 2025 · 预印本 · [arXiv 2511.16624](https://arxiv.org/abs/2511.16624) · [Hugging Face](https://huggingface.co/facebook/sam-3d-objects)
  - SAM 3D: 3Dfy Anything in Images
  - 单图 + 掩码 → 物体形状、纹理与布局；2026 年多条 real2sim 流程的默认资产源
- **SVMR-Bench** · 2025 · BMVC 2026 · [arXiv 2505.17966](https://arxiv.org/abs/2505.17966)
  - Is Single-View Mesh Reconstruction Ready for Robotics?
  - 用机器人标准评测 13 个单视图重建模型，无一满足
- **SimuScene** · 2026 · 预印本 · [arXiv 2606.03994](https://arxiv.org/abs/2606.03994) · [项目](https://snuvclab.github.io/SimuScene)
  - SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image
  - 重建过程中把物理引擎当诊断信号修正形状和布局
- **Picasso** · 2026 · RSS 2026 · [arXiv 2602.08058](https://arxiv.org/abs/2602.08058) · [代码](https://github.com/MIT-SPARK/Picasso)
  - Picasso: Holistic Scene Reconstruction with Physics-Constrained Sampling
  - 接触图引导的全场景拒绝采样，保证无穿透与稳定
- **PhysConsistent-R2S** · 2026 · 预印本 · [arXiv 2602.12633](https://arxiv.org/abs/2602.12633) · [项目](https://physics-constrained-real2sim.github.io)
  - Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning
  - 接触图上用可微刚体仿真优化位姿、质心、质量、摩擦
- **Scalable Real2Sim** · 2025 · IROS 2025† · [arXiv 2503.00370](https://arxiv.org/abs/2503.00370) · [代码](https://github.com/nepfaff/scalable-real2sim)
  - Scalable Real2Sim: Physics-Aware Asset Generation Via Robotic Pick-and-Place Setups
  - 机器人抓取—扫描—激励物体，用关节力矩做带可行性约束的 SDP 惯性辨识

## 6. 渲染耦合仿真：策略训练与数据生成

- **Embodied Gaussians** · 2024 · CoRL 2024 · [arXiv 2406.10788](https://arxiv.org/abs/2406.10788) · [项目](https://embodied-gaussians.github.io)
  - Physically Embodied Gaussian Splatting: A Visually Learnt and Physically Grounded 3D Representation for Robotics
  - 高斯绑在 PBD 粒子上，光度误差变成修正仿真状态的"视觉力"
- **SplatSim** · 2024 · ICRA 2025 · [arXiv 2409.10161](https://arxiv.org/abs/2409.10161) · [代码](https://github.com/qureshinomaan/SplatSim)
  - SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting
  - 机器人连杆高斯随 FK 运动、物体高斯随仿真位姿运动；零样本真实 86.25%
- **RL-GSBridge** · 2024 · ICRA 2025 · [arXiv 2409.20291](https://arxiv.org/abs/2409.20291) · [代码](https://github.com/IRMV-Manipulation-Group/RL-GSBridge)
  - RL-GSBridge: 3D Gaussian Splatting Based Real2Sim2Real Method for Robotic Manipulation Learning
  - 网格绑定高斯随物理同步编辑，供视觉 RL
- **RoboGSim** · 2024 · 预印本 · [arXiv 2411.11839](https://arxiv.org/abs/2411.11839) · [项目](https://robogsim.github.io)
  - RoboGSim: A Real2Sim2Real Robotic Gaussian Splatting Simulator
  - 重建、孪生构建、场景组合、交互引擎四模块的 GS 仿真器
- **DreMa** · 2024 · ICLR 2025 · [arXiv 2412.14957](https://arxiv.org/abs/2412.14957) · [项目](https://leobarcellona.github.io/DreamToManipulate)
  - Dream to Manipulate: Compositional World Models Empowering Robot Imitation Learning with Imagination
  - 以物体为中心的高斯 + 物理仿真，等变变换少量真实示教生成新示教
- **Re3Sim** · 2025 · 预印本 · [arXiv 2502.08645](https://arxiv.org/abs/2502.08645) · [项目](https://xshenhan.github.io/Re3Sim)
  - Re³Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation
  - GS 背景 + 光追网格前景的混合渲染，特权规划器生成示教
- **DISCOVERSE** · 2025 · IROS 2025 · [arXiv 2507.21981](https://arxiv.org/abs/2507.21981) · [项目](https://air-discoverse.github.io)
  - DISCOVERSE: Efficient Robot Simulation in Complex High-Fidelity Environments
  - 3DGS + MuJoCo 统一框架，5 路 RGB-D 约 650 FPS
- **X-Sim** · 2025 · CoRL 2025 Oral · [arXiv 2505.07096](https://arxiv.org/abs/2505.07096) · [项目](https://portal-cornell.github.io/X-Sim)
  - X-Sim: Cross-Embodiment Learning via Real-to-Sim-to-Real
  - 人类视频中物体运动 → 逼真孪生中物体中心奖励 RL → 蒸馏图像策略
- **RoboSimGS** · 2025 · IEEE RA-L 2026 · [arXiv 2510.10637](https://arxiv.org/abs/2510.10637) · [项目](https://robosimgs.github.io)
  - High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic Manipulation Learning with Gaussian Splatting
  - MLLM 推断物理基元的密度、刚度和关节，高斯负责外观
- **TwinAligner** · 2025 · 预印本 · [arXiv 2512.19390](https://arxiv.org/abs/2512.19390) · [项目](https://twin-aligner.github.io)
  - TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation
  - 像素级视觉对齐 + 交互轨迹刚体动力学辨识
- **DREAM** · 2026 · 预印本 · [arXiv 2608.29078](https://arxiv.org/abs/2608.29078)
  - DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation
  - 部署现场重建 → LLM 生成目标与成功判定 → TAMP 生成示教微调 VLA

## 7. 无闭环动力学的逼真数据生成

- **RoboSplat** · 2025 · RSS 2025 · [arXiv 2504.13175](https://arxiv.org/abs/2504.13175) · [代码](https://github.com/InternRobotics/RoboSplat)
  - Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation
  - 直接编辑单条示教的高斯，沿 6 个泛化轴增广
- **R2R2R** · 2025 · CoRL 2025 · [arXiv 2505.09601](https://arxiv.org/abs/2505.09601) · [项目](https://real2render2real.com)
  - Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware
  - 关闭动力学，IsaacLab 只当渲染器，运动学重定向人类示教
- **ReBot** · 2025 · IROS 2025 · [arXiv 2503.14526](https://arxiv.org/abs/2503.14526) · [项目](https://yuffish.github.io/rebot)
  - ReBot: Scaling Robot Learning with Real-to-Sim-to-Real Robotic Video Synthesis
  - 仿真中回放真实轨迹换新物体，合成到修复后的真实视频背景上
- **RoLA** · 2025 · CoRL 2025 · [arXiv 2509.22970](https://arxiv.org/abs/2509.22970) · [项目](https://rola-2025.github.io)
  - Robot Learning from Any Images
  - 单张野外图像 → 物理场景 → 仿真轨迹混合回原照片

## 8. real2sim 策略评测

- **SIMPLER** · 2024 · CoRL 2024 · [arXiv 2405.05941](https://arxiv.org/abs/2405.05941) · [项目](https://simpler-env.github.io)
  - Evaluating Real-World Robot Manipulation Policies in Simulation
  - 绿幕 visual matching + 系统辨识；提出 MMRV，Google Robot 上 r=0.924
- **Real-is-Sim** · 2025 · 预印本 · [arXiv 2504.03597](https://arxiv.org/abs/2504.03597) · [项目](https://realissim.rai-inst.com)
  - Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin
  - 策略始终作用于与现实 60 Hz 同步的孪生，真机跟随孪生
- **GSWorld** · 2025 · 预印本 · [arXiv 2510.20813](https://arxiv.org/abs/2510.20813) · [项目](https://3dgsworld.github.io)
  - GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic Manipulation
  - GSDF 高斯-网格资产，同一孪生用于训练、评测、失败回放和 DAgger 标注
- **RobotArena∞** · 2025 · ICLR 2026 · [arXiv 2510.23571](https://arxiv.org/abs/2510.23571) · [项目](https://robotarenainf.github.io)
  - RobotArena ∞: Scalable Robot Benchmarking via Real-to-Sim Translation
  - 把数据集视频转成孪生，用 VLM 与众包偏好打分
- **Real2Sim-Eval** · 2025 · ICRA 2026 · [arXiv 2511.04665](https://arxiv.org/abs/2511.04665) · [项目](https://real2sim-eval.github.io)
  - Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions
  - GS 渲染 + PhysTwin 软体，3 个任务 r 0.90–0.94
- **PolaRiS** · 2025 · RSS 2026 · [arXiv 2512.16881](https://arxiv.org/abs/2512.16881) · [项目](https://polaris-evals.github.io)
  - PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies
  - GS 评测场景 + 短暂仿真联合训练使通用策略可评测；6 场景平均 r=0.90，与 RoboArena r=0.98
- **ReVeal** · 2026 · 预印本 · [arXiv 2609.23910](https://arxiv.org/abs/2609.23910)
  - ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation
  - 重建级指标判断孪生是否够用；r 随重建质量从 0.773 升到 0.960
- **YUBI-Real2Sim** · 2026 · 预印本 · [arXiv 2610.17521](https://arxiv.org/abs/2610.17521) · [项目](https://yubi-real2sim.airoa.io)
  - YUBI-Real2Sim: 3DGS Scene Verification for Reliable Policy Evaluation
  - 鱼眼腕部相机场景验证；新视角质量分数不能可靠预测排序可靠性

## 9. 学习型世界模型作为仿真器（对照范式）

- **UniSim (WM)** · 2023 · ICLR 2024 Outstanding Paper · [arXiv 2310.06114](https://arxiv.org/abs/2310.06114) · [项目](https://universal-simulator.github.io)
  - Learning Interactive Real-World Simulators
  - 动作/语言条件视频模拟器，纯在其中训练的策略零样本迁移
- **WorldEval** · 2025 · 预印本 · [arXiv 2505.19017](https://arxiv.org/abs/2505.19017) · [项目](https://worldeval.github.io)
  - WorldEval: World Model as Real-World Robot Policies Evaluator
  - 以被评策略的潜动作（Policy2Vec）条件化视频模型；3 任务 r=0.942
- **WorldGym** · 2025 · ICLR 2026 · [arXiv 2506.00613](https://arxiv.org/abs/2506.00613)
  - WorldGym: World Model as An Environment for Policy Evaluation
  - 世界模型中蒙特卡洛 rollout + GPT-4o 判定成功；17 个 Bridge 任务 r=0.78
- **DreamGen** · 2025 · CoRL 2025 · [arXiv 2505.12705](https://arxiv.org/abs/2505.12705) · [代码](https://github.com/NVIDIA/GR00T-Dreams)
  - DreamGen: Unlocking Generalization in Robot Learning through Video World Models
  - 视频世界模型生成"神经轨迹"，伪标注动作训练策略
- **Genie Envisioner** · 2025 · 预印本 · [arXiv 2508.05635](https://arxiv.org/abs/2508.05635) · [项目](https://genie-envisioner.github.io)
  - Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation
  - 视频 DiT 同时作为策略、仿真器与基准
- **Ctrl-World** · 2025 · ICLR 2026 · [arXiv 2510.10125](https://arxiv.org/abs/2510.10125)
  - Ctrl-World: A Controllable Generative World Model for Robot Manipulation
  - 多视图可控世界模型做闭环想象评测；排序大体一致，绝对成功率偏低
- **Veo-WS** · 2025 · 预印本 · [arXiv 2512.10675](https://arxiv.org/abs/2512.10675)
  - Evaluating Gemini Robotics Policies in a Veo World Simulator
  - 位姿条件多视图 Veo；1600+ 真实评测，OOD r=0.86
- **WEAVER** · 2026 · 预印本 · [arXiv 2606.13672](https://arxiv.org/abs/2606.13672) · [项目](https://arnavkj1995.github.io/WEAVER)
  - WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation
  - 潜空间 flow matching 世界模型，ρ=0.870
- **Mem-World** · 2026 · CoRL 2026 · [arXiv 2606.18960](https://arxiv.org/abs/2606.18960)
  - Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation
  - 面元索引的腕部视角 4D 记忆，缓解遮挡下遗忘与幻觉
- **PhysCanvas** · 2026 · 预印本 · [arXiv 2610.28613](https://arxiv.org/abs/2610.28613) · [项目](https://zebinx.github.io/PhysCanvas_HomePage)
  - Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning
  - 视触觉世界模型 + 真实结果一致性奖励后训练；r 0.602 → 0.885

## 10. 视觉 gap 与逼真度研究

- **Sim2Real-VLA study** · 2026 · 预印本 · [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
  - Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models
  - >10k 真实试验；逼真度提升真实成功率，但超过中等光追后饱和
- **WorldArena** · 2026 · 预印本 · [arXiv 2602.08971](https://arxiv.org/abs/2602.08971) · [项目](https://worldarena.ai)
  - WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models
  - 视频质量不能可靠预测具身功能效用（"perception–functionality gap"）

## 11. 刚体系统辨识与仿真参数推断

- **SimOpt** · 2018 · ICRA 2019 · [arXiv 1810.05687](https://arxiv.org/abs/1810.05687) · [项目](https://sites.google.com/view/simopt)
  - Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience
  - 用少量真实 rollout 以 REPS 调整域随机化分布，而非点估计
- **BayesSim** · 2019 · RSS 2019 · [arXiv 1906.01728](https://arxiv.org/abs/1906.01728) · [代码](https://github.com/rafaelpossas/bayes_sim)
  - BayesSim: adaptive domain randomization via probabilistic inference for robotics simulators
  - 黑盒仿真器上学习摊销后验 p(θ | 轨迹统计量)；RSS 版无真机实验
- **gradSim** · 2021 · ICLR 2021 · [arXiv 2104.02646](https://arxiv.org/abs/2104.02646) · [项目](https://gradsim.github.io)
  - gradSim: Differentiable simulation for system identification and visuomotor control
  - 可微多物理 + 可微渲染，从像素端到端求物理参数梯度
- **DROPO** · 2022 · Robotics and Autonomous Systems 2023 · [arXiv 2201.08434](https://arxiv.org/abs/2201.08434)
  - DROPO: Sim-to-Real Transfer with Offline Domain Randomization
  - 离线真实转移上用 CMA-ES 拟合随机化分布的均值与方差
- **AdaptSim** · 2023 · CoRL 2023 · [arXiv 2302.04903](https://arxiv.org/abs/2302.04903) · [项目](https://irom-lab.github.io/AdaptSim)
  - AdaptSim: Task-Driven Simulation Adaptation for Sim-to-Real Transfer
  - 以任务表现而非动力学匹配为目标调整仿真参数
- **ASID** · 2024 · ICLR 2024 · [arXiv 2404.12308](https://arxiv.org/abs/2404.12308) · [项目](https://weirdlabuw.github.io/asid)
  - ASID: Active Exploration for System Identification in Robotic Manipulation
  - 用不完美仿真规划最大化 Fisher 信息的真实探索，再标定
- **Phys2Real** · 2025 · ICRA 2026 · [arXiv 2510.11689](https://arxiv.org/abs/2510.11689) · [项目](https://phys2real.github.io)
  - Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation
  - VLM 物理先验与在线辨识按逆方差融合
- **VLM-BT Real2Sim** · 2026 · 预印本 · [arXiv 2601.08454](https://arxiv.org/abs/2601.08454)
  - Real2Sim via Active Perception with Behavior Trees Automatically Generated by VLMs
  - VLM 决定测哪些参数，生成行为树执行探测
- **RigPI** · 2026 · 预印本† · [arXiv 2606.25212](https://arxiv.org/abs/2606.25212)
  - RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation
  - VLM 初始化并限定搜索空间，再在 NVIDIA Newton 中两阶段梯度精化

## 12. 可变形 / 颗粒 / 流体物理孪生

- **PAC-NeRF** · 2023 · ICLR 2023 · [arXiv 2303.05512](https://arxiv.org/abs/2303.05512) · [项目](https://xuan-li.github.io/PAC-NeRF)
  - PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification
  - 可微 MPM + NeRF，联合辨识几何与弹性/塑性/颗粒/流体参数
- **PhysGaussian** · 2023 · CVPR 2024 · [arXiv 2311.12198](https://arxiv.org/abs/2311.12198) · [代码](https://github.com/XPandora/PhysGaussian)
  - PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics
  - MPM 直接作用于高斯核，"所见即所仿"
- **Spring-Gaus** · 2024 · ECCV 2024 · [arXiv 2403.09434](https://arxiv.org/abs/2403.09434) · [项目](https://zlicheng.com/spring_gaus)
  - Reconstruction and Simulation of Elastic Objects with Spring-Mass 3D Gaussians
  - 弹簧-质点模型锚定 3DGS，物理学习与外观解耦
- **PhysDreamer** · 2024 · ECCV 2024 Oral · [arXiv 2404.13026](https://arxiv.org/abs/2404.13026) · [项目](https://physdreamer.github.io)
  - PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation
  - 把视频生成模型的运动先验蒸馏为材料场
- **GIC** · 2024 · NeurIPS 2024 · [arXiv 2406.14927](https://arxiv.org/abs/2406.14927) · [项目](https://jukgei.github.io/project/gic)
  - GIC: Gaussian-Informed Continuum for Physical Property Identification and Simulation
  - 高斯几何为物性辨识提供显式形状监督
- **NeuMA** · 2024 · NeurIPS 2024 · [arXiv 2410.08257](https://arxiv.org/abs/2410.08257) · [项目](https://xjay18.github.io/projects/neuma.html)
  - Neural Material Adaptor for Visual Grounding of Intrinsic Dynamics
  - 预训练神经本构律 + LoRA 低秩残差
- **OmniPhysGS** · 2025 · ICLR 2025 · [arXiv 2501.18982](https://arxiv.org/abs/2501.18982) · [项目](https://wgsxm.github.io/projects/omniphysgs)
  - OmniPhysGS: 3D Constitutive Gaussians for General Physics-Based Dynamics Generation
  - 每个高斯学习 12 种本构模型的混合权重
- **PhysTwin** · 2025 · ICCV 2025 · [arXiv 2503.17973](https://arxiv.org/abs/2503.17973) · [项目](https://jianghanxiao.github.io/phystwin-web)
  - PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos
  - 三视角 RGB-D 交互视频 → 零阶 + 一阶两阶段逆物理 → 可实时仿真的形变孪生
- **DPSI** · 2024 · IJRR 2025 · [arXiv 2411.00554](https://arxiv.org/abs/2411.00554) · [项目](https://ianyangchina.github.io/SI4RP-data)
  - Differentiable Physics-based System Identification for Robotic Manipulation of Elastoplastic Materials
  - 一次按压/推移交互即可辨识可解释的弹塑性参数
- **PGND** · 2025 · RSS 2025 · [arXiv 2506.15680](https://arxiv.org/abs/2506.15680) · [项目](https://kywind.github.io/pgnd)
  - Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos
  - 完全学习的粒子-网格神经动力学，用于 MPC
- **Pixie** · 2025 · 预印本 · [arXiv 2508.17437](https://arxiv.org/abs/2508.17437) · [项目](https://pixie-3d.github.io)
  - Pixie: Fast and Generalizable Supervised Learning of 3D Physics from Pixels
  - 前馈预测材料类别与 E、ν、密度场，数秒得到可仿真高斯场景
- **MOSIV** · 2026 · ICLR 2026 · [arXiv 2603.06022](https://arxiv.org/abs/2603.06022)
  - Multi-Object System Identification from Videos
  - 多物体逐物体连续材料参数辨识（仅合成数据）
- **EgoPhys** · 2026 · 预印本 · [arXiv 2606.16202](https://arxiv.org/abs/2606.16202) · [项目](https://hjhyunjinkim.github.io/EgoPhys)
  - EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video
  - 单段第一人称视频 → 摊销的稠密弹簧刚度
- **FORM** · 2026 · 预印本 · [arXiv 2609.38105](https://arxiv.org/abs/2609.38105) · [项目](https://form-robots.github.io)
  - FORM: Robot Manipulation through Direct Material Law Identification
  - 弱形式动量平衡化为线性最小二乘，辨识从 10–25 min 降到 2–5 s

## 13. 机器人侧动力学对齐

- **ActuatorNet** · 2019 · Science Robotics 2019 · [arXiv 1901.08652](https://arxiv.org/abs/1901.08652)
  - Learning agile and dynamic motor skills for legged robots
  - 用真实执行器数据训练执行器网络替代理想模型
- **ASAP** · 2025 · RSS 2025 · [arXiv 2502.01143](https://arxiv.org/abs/2502.01143)
  - ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  - 残差动作模型 Δa(s,a) 让仿真复现真实转移，再在增强仿真中微调
- **UAN** · 2025 · ICLR 2025 Workshop (WRL) · [arXiv 2502.10894](https://arxiv.org/abs/2502.10894) · [项目](https://uan.csail.mit.edu)
  - Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
  - 无力矩传感器，用 RL 训练修正力矩的执行器网络
- **SPI-Active** · 2025 · CoRL 2025 · [arXiv 2505.14266](https://arxiv.org/abs/2505.14266) · [代码](https://github.com/LeCAR-Lab/SPI-Active)
  - Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
  - 大规模并行 CMA-ES 轨迹匹配 + 按 Fisher 信息设计指令
- **Dao & Fern 2026** · 2026 · 预印本 · [arXiv 2604.11090](https://arxiv.org/abs/2604.11090)
  - Simulator Adaptation for Sim-to-Real Learning of Legged Locomotion via Proprioceptive Distribution Matching
  - 匹配本体感知分布而非时间对齐轨迹，无需动捕
- **NeuralActuator** · 2026 · RSS 2026 · [arXiv 2607.11734](https://arxiv.org/abs/2607.11734) · [项目](https://frank-zy-dou.github.io/projects/NeuralActuator)
  - NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception
  - 通过可微仿真从位姿轨迹学习舵机力矩代理模型
- **HumanoidNDM** · 2026 · CoRL 2026 · [arXiv 2610.34126](https://arxiv.org/abs/2610.34126)
  - HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model
  - 真机数据训练人形神经动力学模型，经模型反传梯度在线微调跟踪策略，免动捕；主归属 [humanoid-motion-tracking](../humanoid-motion-tracking/papers.md)
- **IDTD** · 2026 · 预印本 · [arXiv 2610.10905](https://arxiv.org/abs/2610.10905) · [代码](https://github.com/jsw7460/IDTD)
  - Informationally Decoupled Trajectory Design for Sim-to-Real System Identification
  - 轨迹分段各自隔离一组参数，打破参数耦合

## 14. 残差物理与混合仿真

- **TossingBot** · 2019 · RSS 2019 · [arXiv 1903.11239](https://arxiv.org/abs/1903.11239) · [项目](https://tossingbot.cs.princeton.edu)
  - TossingBot: Learning to Throw Arbitrary Objects with Residual Physics
  - 网络修正弹道控制器输出的释放速度
- **NeuralSim** · 2020 · ICRA 2021 · [arXiv 2011.04217](https://arxiv.org/abs/2011.04217) · [项目](https://sites.google.com/usc.edu/neuralsim)
  - NeuralSim: Augmenting Differentiable Simulators with Neural Networks
  - 把神经模块嵌入可微刚体引擎内部
- **NeRD** · 2025 · CoRL 2025 · [arXiv 2508.15755](https://arxiv.org/abs/2508.15755) · [代码](https://github.com/NVlabs/neural-robot-dynamics)
  - Neural Robot Dynamics
  - 学习的机器人中心动力学替代求解器，可用真实数据微调
- **CLASH** · 2026 · 预印本 · [arXiv 2602.18707](https://arxiv.org/abs/2602.18707)
  - CLASH: Collision Learning via Augmented Sim-to-real Hybridization to Bridge the Reality Gap
  - gap 拆为辨识的接触参数 + 早停的小残差，约 10 次真实碰撞
- **RAFL** · 2026 · 预印本 · [arXiv 2603.22039](https://arxiv.org/abs/2603.22039)
  - RAFL: Generalizable Sim-to-Real of Soft Robots with Residual Acceleration Field Learning
  - 局部、拓扑无关的残差加速度场，可跨形态迁移

## 15. 足式运动与导航

- **LucidSim** · 2024 · CoRL 2024 · [arXiv 2411.00083](https://arxiv.org/abs/2411.00083) · [项目](https://lucidsim.github.io)
  - Learning Visual Parkour from Generated Images
  - 对照：不重建真实场景，生成图像训练 RGB 跑酷
- **Vid2Sim** · 2025 · CVPR 2025 · [arXiv 2501.06693](https://arxiv.org/abs/2501.06693) · [项目](https://metadriverse.github.io/vid2sim)
  - Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation
  - 单目网络视频 → 3DGS + TSDF 碰撞网格 → RL 导航
- **VR-Robo** · 2025 · IEEE RA-L 2025 · [arXiv 2502.01536](https://arxiv.org/abs/2502.01536) · [项目](https://vr-robo.github.io)
  - VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion
  - GS 渲染 + 网格物理混合，Go2 仅 RGB 上楼梯找目标
- **EmbodiedSplat** · 2025 · ICCV 2025 · [arXiv 2509.17430](https://arxiv.org/abs/2509.17430) · [项目](https://gchhablani.github.io/embodied-splat)
  - EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device
  - iPhone RGB-D → Habitat-Sim，针对部署地点微调导航策略
- **GaussGym** · 2025 · 预印本 · [arXiv 2510.15352](https://arxiv.org/abs/2510.15352) · [项目](https://escontrela.me/gauss_gym)
  - GaussGym: An open-source real-to-sim framework for learning locomotion from pixels
  - 多源输入 → VGGT → 3DGS + NKSR 网格，>100k steps/s 视觉 RL
- **UrbanVerse** · 2025 · ICLR 2026 · [arXiv 2510.15018](https://arxiv.org/abs/2510.15018) · [项目](https://urbanverseproject.github.io)
  - UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos
  - 城市漫游视频 → 布局 + 检索资产（不重建）
- **S2E** · 2025 · ICLR 2026 · [arXiv 2507.22028](https://arxiv.org/abs/2507.22028) · [项目](https://vail-ucla.github.io/S2E)
  - From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning
  - 带物理的 GS 场景中对视频预训练导航模型做 RL 后训练
- **Wanderland** · 2025 · CVPR 2026 · [arXiv 2511.20620](https://arxiv.org/abs/2511.20620) · [项目](https://ai4ce.github.io/wanderland)
  - Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI
  - LiDAR 度量重建基准；指出纯视频 real2sim 度量上不可靠
- **ReaDy-Go** · 2026 · IEEE RA-L 2026 · [arXiv 2602.11575](https://arxiv.org/abs/2602.11575) · [项目](https://syeon-yoo.github.io/ready-go-site)
  - ReaDy-Go: Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation with Moving Obstacles
  - 静态 GS 场景 + 可动画 GS 人体，在行人中导航
- **QuadVerse** · 2026 · 预印本 · [arXiv 2606.07118](https://arxiv.org/abs/2606.07118) · [项目](https://quad-verse.github.io)
  - QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation
  - 视频 → 3DGS + 网格 + 摩擦后验 + 残差动力学，视觉与物理同时对齐
- **VLK** · 2026 · 预印本 · [arXiv 2606.30645](https://arxiv.org/abs/2606.30645) · [项目](https://vision-language-kinematics.github.io)
  - VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes
  - 度量 3DGS 室内场景合成 48k 轨迹，G1 导航与搬箱
- **LEGS** · 2026 · 预印本 · [arXiv 2606.01458](https://arxiv.org/abs/2606.01458) · [项目](https://hojjunekim.github.io/legs)
  - LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World
  - GS 背景 + 网格前景，免遥操作微调 G1 移动操作 VLA

## 16. 自动驾驶闭环仿真

- **UniSim (driving)** · 2023 · CVPR 2023 Highlight · [arXiv 2308.01898](https://arxiv.org/abs/2308.01898)
  - UniSim: A Neural Closed-Loop Sensor Simulator
  - 驾驶日志 → 神经特征网格，可编辑闭环多传感器仿真
- **NeuRAD** · 2023 · CVPR 2024 · [arXiv 2311.15260](https://arxiv.org/abs/2311.15260) · [代码](https://github.com/georghess/NeuRAD)
  - NeuRAD: Neural Rendering for Autonomous Driving
  - 带精细传感器模型的 NeRF
- **OmniRe** · 2024 · ICLR 2025 Spotlight · [arXiv 2408.16760](https://arxiv.org/abs/2408.16760) · [代码](https://github.com/ziyc/drivestudio)
  - OmniRe: Omni Urban Scene Reconstruction
  - 高斯场景图覆盖所有动态参与者，包括 SMPL 行人
- **HUGSIM** · 2024 · IEEE TPAMI · [arXiv 2412.01718](https://arxiv.org/abs/2412.01718)
  - HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving
  - 实时 3DGS 闭环基准
- **RAD** · 2025 · NeurIPS 2025 · [arXiv 2502.13144](https://arxiv.org/abs/2502.13144) · [代码](https://github.com/hustvl/RAD)
  - RAD: Training an End-to-End Driving Policy via Large-Scale 3DGS-based Reinforcement Learning
  - 4,305 段逐段 3DGS 场景中 RL 后训练端到端规划器
- **NAVSIM v2** · 2025 · CoRL 2025 · [arXiv 2506.04218](https://arxiv.org/abs/2506.04218) · [代码](https://github.com/autonomousvision/navsim)
  - Pseudo-Simulation for Autonomous Driving
  - 预渲染 3DGS 反事实视角做伪仿真评测；与闭环 R²=0.8
- **SimScale** · 2025 · CVPR 2026 Oral · [arXiv 2511.23369](https://arxiv.org/abs/2511.23369) · [代码](https://github.com/OpenDriveLab/SimScale)
  - SimScale: Learning to Drive via Real-World Simulation at Scale
  - 仿真—真实联合训练，收益随仿真数据量持续增长
- **REAP** · 2026 · 预印本 · [arXiv 2605.08713](https://arxiv.org/abs/2605.08713)
  - REAP: Reinforcement-Learning End-to-End Autonomous Parking with Gaussian Splatting Simulator for Real2Sim2Real Transfer
  - 3DGS 停车场场景 RL 泊车，实车迁移

## 17. 人类视频 → 仿真

- **VideoMimic** · 2025 · CoRL 2025 · [arXiv 2505.03729](https://arxiv.org/abs/2505.03729) · [项目](https://videomimic.net)
  - Visual Imitation Enables Contextual Humanoid Control
  - 手机视频 → 度量 4D 人体 + 场景 → RL 跟踪，G1 上楼梯、坐下
- **HDMI** · 2025 · 预印本 · [arXiv 2509.16757](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io)
  - HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos
  - 视频 → 人体与物体轨迹 → G1 人–物交互；部署需动捕
- **CRISP** · 2025 · ICLR 2026 · [arXiv 2512.14696](https://arxiv.org/abs/2512.14696) · [项目](https://crisp-real2sim.github.io/CRISP-Real2Sim)
  - CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives
  - 接触引导的平面基元场景，物理合理的人形跟踪
- **Real2Sim-HOI** · 2026 · 预印本 · [arXiv 2605.14462](https://arxiv.org/abs/2605.14462) · [项目](https://knoxzhao.github.io/real2sim_in_HOI)
  - Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos
  - 视频 → 4D 人–物交互，作为物理 rollout 的教师轨迹（仅仿真）
- **Human2Sim2Robot** · 2025 · CoRL 2025 · [arXiv 2504.12609](https://arxiv.org/abs/2504.12609) · [论文集](https://proceedings.mlr.press/v305/lum25a.html)
  - Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL using One Human Demonstration
  - 物体轨迹 + 预抓取位姿作物体中心 RL 奖励，Allegro 手零样本上真机
- **Video2Sim2Real** · 2026 · 预印本 · [arXiv 2606.08828](https://arxiv.org/abs/2606.08828) · [项目](https://video2sim2real.github.io)
  - Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video
  - 单视频 → 孪生 + 运动先验 → 模仿学习 + 残差 RL 灵巧操作

## 18. 综述、框架与工具

- **RealityGap-Survey** · 2025 · Annual Review of Control, Robotics, and Autonomous Systems 2026 · [arXiv 2510.20808](https://arxiv.org/abs/2510.20808)
  - The Reality Gap in Robotics: Challenges, Solutions, and Best Practices
  - 把 real2sim 放在"改进仿真"之下，拆为几何、运动学/动力学、渲染三个逆问题
- **3DGen4Robot-Survey** · 2026 · 预印本 · [arXiv 2604.26509](https://arxiv.org/abs/2604.26509) · [项目](https://3dgen4robot.github.io)
  - 3D Generation for Embodied AI and Robotic Simulation: A Survey
  - 3D 生成的三种角色：数据生成器、仿真环境、Sim2Real 桥
- **3DGS-Robotics-Survey** · 2024 · 预印本 · [arXiv 2410.12262](https://arxiv.org/abs/2410.12262)
  - 3D Gaussian Splatting in Robotics: A Survey
  - 按场景理解 / 交互组织 3DGS 应用
- **NeuralFields-Survey** · 2024 · 预印本 · [arXiv 2410.20220](https://arxiv.org/abs/2410.20220) · [项目](https://robonerf.github.io)
  - Neural Fields in Robotics: A Survey
  - 4 种表示 × 5 个领域
- **DT2EAI-Review** · 2025 · Intelligence & Robotics 2025 · [DOI](https://doi.org/10.20517/ir.2025.11)
  - Digital twins to embodied artificial intelligence: review and perspective
  - 数字孪生与具身 AI 的三种协同
- **RoboVerse** · 2025 · RSS 2025 · [arXiv 2504.18904](https://arxiv.org/abs/2504.18904) · [项目](https://roboverseorg.github.io)
  - RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning
  - 多仿真器平台，含 GS 与网格重建 → URDF 的 Real2Sim 工具集
- **Isaac Lab** · 2025 · 预印本 · [arXiv 2511.04831](https://arxiv.org/abs/2511.04831) · [代码](https://github.com/isaac-sim/IsaacLab)
  - Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning
  - 可在物理资产旁渲染 NuRec 3DGS/3DGUT 场景
- **3DGUT** · 2024 · CVPR 2025 · [arXiv 2412.12507](https://arxiv.org/abs/2412.12507) · [代码](https://github.com/nv-tlabs/3dgrut)
  - 3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting
  - NVIDIA NuRec 渲染背后的高斯渲染引擎

## 补充（已核实，只列编号）

- 场景与资产：MotionAnymesh (2603.12936)，Kinematify (2511.01294)，Infinite Mobility (2503.13424)，ArtiPoint (2509.01708, CoRL 2025)，EmbodiedGen (2506.10600)，PhysWorld-video (2511.07416)，OP-Gen (2509.06191)，RecGen (2604.27106)，LiteReality (2507.02861, NeurIPS 2025)，ForceTwin (2609.21751)，Subsecond 3D Mesh Generation (2512.24428)
- 渲染与评测：Robo-GS (2408.14873, ICRA 2025)，RoboPearls (2506.22756, ICCV 2025)，EnerVerse-AC (2505.09723)，IRASim (2406.14540)，GASE (2606.17520)，ManiSplat (2606.10645)，EmbodieDreamer (2507.05198)，Prompting with the Future (2506.13761, RSS 2025)，World-in-World (2510.18135, ICLR 2026)，Robot Policy Evaluation for Sim-to-Real Transfer (2508.11117)，Cosmos-Surg-dVRK (2510.16240)，MolmoSpaces (2602.11337)
- 物理与动力学：NPDR (CoRL 2021, PMLR v164)，ASBI (2510.15331)，Neural Fidelity Calibration (2504.08604)，Kamaras et al. (2510.26656)，Agentic Real2Sim (2607.19190)，AdaptiGraph (2407.07889, RSS 2024)，PhysFlow (2411.14423, CVPR 2025)，VisionLaw (2508.13792, ICLR 2026)，VoMP (2510.22975)，PhysWorld-MPM (2510.21447)，EMPM (2601.17251)，BendTwin (2608.06164)，KnockGS (2608.27365)，DDBot (2510.17335, T-RO 2026)，Ru et al. fabric study (2503.16310)，Gao et al. soft robot residual (2402.01086, RA-L 2024)，HALO (2603.15084)，Kovalev et al. (2604.10351)，Bjelonic et al. (2509.06342, IJRR 2026)，FADA (2606.28476)
- 场景与人类：DexMachina (2505.24853, ICML 2026)，SPIDER (2511.09484)，OmniRetarget (2509.26633)，Dex-One2Many (2610.12470)，RAD-2 (2604.15308)，Cosmos-Drive-Dreams (2506.09042)，RL sim-to-real survey (2502.13187)，ACM CSUR physics-simulator survey (2505.01458)，position paper "Robots Need More than VLA and World Models" (2606.06556)
