# sim-real-cotraining 论文目录

- 快照日期：2026-10-31
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment / journal-ref 字段或论文集确认的发表处；"预印本" 表示未找到发表处。标 † 的发表处只见于索引或二手来源，见根目录 `issues.md` → ISSUE-004。
- 每条的标题、年份、arXiv 编号均经 arxiv.org 页面核实；DUL 与 simDP 没有 arXiv，分别取自 CVF 论文集与 DOI 索引。
- 与其他方向重复的论文沿用其他方向 `papers.md` 中的简称与发表处。
- 分节对应 [survey.md](survey.md) 的分类；一篇论文只列在主归属的一节。

## 1. 数据组合：混合、分阶段与仿真数据的价值

### 1.1 联合共训练

- **Sim&Real Co-Train** · 2025 · 预印本 · [arXiv 2503.24361](https://arxiv.org/abs/2503.24361) · [项目](https://co-training.github.io)
  - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation
  - 仿真即使与真实有明显差异也有用；仿真量应比真实多出数量级，且比例需要调
- **Sim&Real Pushing** · 2025 · IROS 2025 · [arXiv 2503.22634](https://arxiv.org/abs/2503.22634) · [项目](https://sim-and-real-cotraining.github.io)
  - Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies for Planar Pushing from Pixels
  - 物理差距比视觉保真更关键。存在物理差距时，消除视觉差距反而降低性能，加 one-hot 域标签可以恢复
- **RoboCasa** · 2024 · RSS 2024 · [arXiv 2406.02523](https://arxiv.org/abs/2406.02523) · [项目](https://robocasa.ai)
  - RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots
  - 任务无关的大规模仿真也能帮助真实任务
- **R2S2R Grounding** · 2026 · 预印本 · [arXiv 2610.00821](https://arxiv.org/abs/2610.00821) · [项目](https://industrialnext.github.io/r2s2r-grounding)
  - Getting Out and Getting Back: World and Behavior Grounding in Real2Sim2Real Co-Training
  - 部署后的策略在真实数据覆盖的状态模仿真实示范，在其他状态依赖仿真行为
- **SARI** · 2026 · 预印本 · [arXiv 2610.02804](https://arxiv.org/abs/2610.02804) · [项目](https://icra27-sari.vercel.app)
  - SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation
  - 按"哪一段需要物理保真"来分配数据源
- **OpenViTac** · 2026 · 预印本 · [arXiv 2610.10384](https://arxiv.org/abs/2610.10384) · [项目](https://fvl-repo.github.io/OpenViTac)
  - OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework
  - 视触觉任务上 sim+real 有增益；跨域触觉信号差异限制了增益
- **Zero-HLM** · 2026 · 预印本 · [arXiv 2610.35075](https://arxiv.org/abs/2610.35075) · [项目](https://young-bit.github.io/zero-hlm)
  - Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data
  - 反例：残余视觉域差下，co-training 不一定优于纯仿真
- **Ambient DP** · 2026 · 预印本 · [arXiv 2606.12365](https://arxiv.org/abs/2606.12365) · [项目](https://ambient-diffusion-policy.github.io)
  - Ambient Diffusion Policy: Imitation Learning from Suboptimal Data in Robotics
  - 新增一个混合维度："按噪声水平决定用哪类数据"
- **LBM** · 2025 · 预印本 · [arXiv 2507.05331](https://arxiv.org/abs/2507.05331) · [项目](https://toyotaresearchinstitute.github.io/lbm1)
  - A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation
  - 大规模混合中仿真只占很小一部分

### 1.2 分阶段、数据金字塔与纯仿真预训练

- **GR00T N1** · 2025 · 预印本 · [arXiv 2503.14734](https://arxiv.org/abs/2503.14734) · [项目](https://developer.nvidia.com/isaac/gr00t)
  - GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
  - "数据金字塔"框架的代表
- **InternData-A1** · 2025 · 预印本 · [arXiv 2511.16651](https://arxiv.org/abs/2511.16651)
  - InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy
  - 首次证据：纯合成预训练可与最强真实预训练相当
- **InternVLA-A1** · 2026 · 预印本 · [arXiv 2601.02456](https://arxiv.org/abs/2601.02456) · [项目](https://internrobotics.github.io/internvla-a1.github.io)
  - InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation
  - 仿真约占 72% 采样权重，但预训练里加入真实数据对真实任务提升明显
- **GraspVLA** · 2025 · 预印本 · [arXiv 2505.03233](https://arxiv.org/abs/2505.03233) · [项目](https://pku-epic.github.io/GraspVLA-web)
  - GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data
  - 纯合成预训练让少样本后训练很高效
- **MolmoBot** · 2026 · 预印本 · [arXiv 2603.16861](https://arxiv.org/abs/2603.16861)
  - MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation
  - 零样本 sim2real，挑战"必须有真实数据"的观点
- **SimVLA** · 2026 · 预印本 · [arXiv 2610.11248](https://arxiv.org/abs/2610.11248) · [项目](https://kyounginbaik.github.io/simvla)
  - SimVLA: Zero-Shot Sim-to-Real VLA Learning for Mobile Manipulation
  - 仿真 VQA 与部署 rollout 数据是互补的监督
- **SMART** · 2026 · 预印本 · [arXiv 2610.07652](https://arxiv.org/abs/2610.07652)
  - SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining
  - 铰接物体的合成预训练
- **ZAP** · 2026 · 预印本 · [arXiv 2610.35817](https://arxiv.org/abs/2610.35817)
  - Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent
  - web 预训练加仿真两层，不用真实数据
- **SPD** · 2026 · 预印本 · [arXiv 2608.15917](https://arxiv.org/abs/2608.15917) · [项目](https://spd.bot)
  - Pre-training Visual Dexterity in Simulation
  - 仿真遥操作可作为灵巧手的预训练数据源
- **RoboCasa365** · 2026 · ICLR 2026 · [arXiv 2603.04356](https://arxiv.org/abs/2603.04356)
  - RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots
  - 两阶段训练，且微调期仍混入仿真
- **SimHum** · 2026 · CoRL 2026 · [arXiv 2601.19406](https://arxiv.org/abs/2601.19406) · [项目](https://kaipengfang.github.io/sim-and-human)
  - Sim-and-Human Co-training for Data-Efficient and Scene-Generalizable Bimanual Manipulation
  - 仿真与人类数据互补
- **Sim2Real-VLA Study** · 2026 · 预印本 · [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
  - Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models
  - 多样性与保真度的系统证据
- **Param Merging** · 2025 · ICLR 2026 · [arXiv 2512.08333](https://arxiv.org/abs/2512.08333)
  - Robust Finetuning of Vision-Language-Action Robot Policies via Parameter Merging
  - 遗忘对策的类比；未在仿真预训练上测试
- **Rethink VLA Scaling** · 2026 · 预印本 · [arXiv 2602.09722](https://arxiv.org/abs/2602.09722) · [项目](https://research.beingbeyond.com/rethink_vla)
  - Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization
  - 混合方式不对会产生负迁移

### 1.3 仿真数据的汇率

- **DUL** · 2026 · CVPR 2026 Findings · [CVF](https://openaccess.thecvf.com/content/CVPR2026F/html/Shi_Teleoperation_Simulation_or_Human_Video_Data_Utilization_Law_for_Robot_CVPRF_2026_paper.html)
  - Teleoperation, Simulation, or Human Video? Data Utilization Law for Robot Manipulation
  - 汇率随任务和评估分布而变，不是常数
- **SIM1** · 2026 · 预印本 · [arXiv 2604.08544](https://arxiv.org/abs/2604.08544) · [项目](https://internrobotics.github.io/sim1.github.io)
  - SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds
  - 可变形物体孪生；汇率取决于评估分布
- **R2R2R** · 2025 · CoRL 2025 · [arXiv 2505.09601](https://arxiv.org/abs/2505.09601) · [项目](https://real2render2real.com)
  - Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware
  - 汇率的一个上限数据点
- **SimScale** · 2025 · CVPR 2026 Oral · [arXiv 2511.23369](https://arxiv.org/abs/2511.23369) · [代码](https://github.com/OpenDriveLab/SimScale)
  - SimScale: Learning to Drive via Real-World Simulation at Scale
  - 驾驶域中"固定真实、只扩仿真"的缩放证据

### 1.4 数据筛选与加权

- **TUCO** · 2026 · 预印本 · [arXiv 2610.05407](https://arxiv.org/abs/2610.05407)
  - TUCO: Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training
  - 第一个针对 sim-to-real co-training 的数据筛选系统研究
- **BEACON** · 2026 · 预印本 · [arXiv 2605.08571](https://arxiv.org/abs/2605.08571)
  - BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation
  - 学到的样本权重优于固定混合比
- **CUPID** · 2025 · CoRL 2025 · [arXiv 2506.19121](https://arxiv.org/abs/2506.19121) · [项目](https://cupid-curation.github.io)
  - CUPID: Curating Data your Robot Loves with Influence Functions
  - 基于闭环影响函数的数据筛选
- **DataMIL** · 2025 · ICLR 2026† · [arXiv 2505.09603](https://arxiv.org/abs/2505.09603) · [项目](https://robin-lab.cs.utexas.edu/datamodels4imitation)
  - DataMIL: Selecting Data for Robot Imitation Learning with Datamodels
  - 端到端、以性能为目标的数据选择
- **Re-Mix** · 2024 · CoRL 2024† · [arXiv 2408.14037](https://arxiv.org/abs/2408.14037)
  - Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning
  - 域级混合权重优化
- **MimicLabs** · 2025 · 预印本 · [arXiv 2506.13536](https://arxiv.org/abs/2506.13536) · [项目](https://robo-mimiclabs.github.io)
  - What Matters in Learning from Large-Scale Datasets for Robot Manipulation
  - 把仿真当作研究数据组成的实验台
- **AutoScale** · 2026 · 预印本 · [arXiv 2605.21372](https://arxiv.org/abs/2605.21372)
  - Closed Loop Dynamic Driving Data Mixture for Real-Synthetic Co-Training
  - 动态的混合比例优化

### 1.5 跨域类比

- **EgoMimic** · 2024 · ICRA 2025† · [arXiv 2410.24221](https://arxiv.org/abs/2410.24221) · [项目](https://egomimic.github.io)
  - EgoMimic: Scaling Imitation Learning via Egocentric Video
  - 人类视频 co-training 的类比

## 2. 孪生内外的数据生成

### 2.1 真实示教播种的扩增

- **MimicGen** · 2023 · CoRL 2023 · [arXiv 2310.17596](https://arxiv.org/abs/2310.17596) · [项目](https://mimicgen.github.io)
  - MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations
  - 按物体中心子任务切分演示，经位姿变换重放并筛选成功轨迹；该族方法的原型
- **SkillMimicGen** · 2024 · 预印本 · [arXiv 2410.18907](https://arxiv.org/abs/2410.18907) · [项目](https://skillgen.github.io)
  - SkillMimicGen: Automated Demonstration Generation for Efficient Skill Learning and Deployment
  - 只对接触段做技能级适配，段间用运动规划衔接，更适合迁移到真实
- **DexMimicGen** · 2024 · ICRA 2025 · [arXiv 2410.24185](https://arxiv.org/abs/2410.24185) · [项目](https://dexmimicgen.github.io)
  - DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning
  - 真实演示先移植进孪生，孪生兼作安全过滤器，再在真机上产出真实数据
- **IntervenGen** · 2024 · 预印本 · [arXiv 2405.01472](https://arxiv.org/abs/2405.01472) · [项目](https://sites.google.com/view/intervengen2024)
  - IntervenGen: Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning
  - 扩增的对象是纠偏片段而不是完整演示，覆盖策略会出错的状态
- **MoMaGen** · 2025 · ICLR 2026 · [arXiv 2510.18316](https://arxiv.org/abs/2510.18316) · [项目](https://momagen.github.io)
  - MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation
  - 把 X-Gen 扩展到移动底座和主动相机
- **CP-Gen** · 2025 · CoRL 2025 · [arXiv 2508.03944](https://arxiv.org/abs/2508.03944) · [项目](https://cp-gen.github.io)
  - Constraint-Preserving Data Generation for Visuomotor Policy Learning
  - 用几何感知的数据生成覆盖新物体形状
- **PGDG** · 2026 · 预印本 · [arXiv 2605.21710](https://arxiv.org/abs/2605.21710) · [项目](https://cunxid.github.io/PGDG)
  - PGDG: Physically Grounded Data Generation for Robust Bimanual Policy Learning from a Single Demonstration
  - 扩增的重点是恢复行为，不是空间覆盖
- **DemoGen** · 2025 · 预印本 · [arXiv 2502.16932](https://arxiv.org/abs/2502.16932) · [项目](https://demo-generation.github.io)
  - DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning
  - 不经仿真、不经渲染的点云级合成
- **R2RGen** · 2025 · RSS 2026 · [arXiv 2510.08547](https://arxiv.org/abs/2510.08547) · [项目](https://r2rgen.github.io)
  - R2RGEN: Real-to-Real 3D Data Generation for Spatially Generalized Manipulation
  - DemoGen 的升级：支持多相机和移动底座
- **Real2Edit2Real** · 2025 · CVPR 2026 · [arXiv 2512.19402](https://arxiv.org/abs/2512.19402) · [项目](https://real2edit2real.github.io)
  - Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface
  - 三维编辑负责几何，视频生成负责外观
- **RoboSplat** · 2025 · RSS 2025 · [arXiv 2504.13175](https://arxiv.org/abs/2504.13175) · [代码](https://github.com/InternRobotics/RoboSplat)
  - Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation
  - 直接在 3DGS 场景里编辑演示
- **WANDA** · 2026 · 预印本 · [arXiv 2607.13154](https://arxiv.org/abs/2607.13154) · [项目](https://wanda.lecar-lab.org)
  - Worlds in One Demo: A Synthetic Data Engine for Learning Open-World Mobile Manipulation
  - 单条演示扩展到跨场景移动操作

### 2.2 无真实种子的示教来源

- **RoboTwin 2.0** · 2025 · 预印本 · [arXiv 2506.18088](https://arxiv.org/abs/2506.18088) · [项目](https://robotwin-platform.github.io)
  - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation
  - LLM 写专家代码，加强随机化
- **Splat2Act** · 2026 · 预印本 · [arXiv 2610.13945](https://arxiv.org/abs/2610.13945) · [项目](https://splat2act.github.io)
  - Splat2Act: From Captured Scenes to Personalized VLA Manipulation
  - 楼宇尺度孪生 + 个性化 VLA
- **Re3Sim** · 2025 · 预印本 · [arXiv 2502.08645](https://arxiv.org/abs/2502.08645) · [项目](https://xshenhan.github.io/Re3Sim)
  - Re³Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation
  - 高斯背景 + 光追网格前景的孪生，特权规划专家生成示教；只用仿真数据，零样本真实超过 58%
- **CASHER** · 2024 · RSS 2025 · [arXiv 2412.01770](https://arxiv.org/abs/2412.01770) · [项目](https://casher-robot-learning.github.io/CASHER)
  - Robot Learning with Super-Linear Scaling
  - 人力投入相对环境数呈亚线性
- **DREAM** · 2026 · 预印本 · [arXiv 2608.29078](https://arxiv.org/abs/2608.29078)
  - DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation
  - 部署场景内无人类演示的 VLA 适配
- **AutoRSR** · 2026 · 预印本 · [arXiv 2610.20336](https://arxiv.org/abs/2610.20336)
  - AutoRSR: Automated Real-to-Sim-to-Real Data Generation for Scalable Robot Learning
  - 扫描、配准、生成的自动化流水线
- **GaussianFactory** · 2026 · 预印本 · [arXiv 2609.21112](https://arxiv.org/abs/2609.21112)
  - Demonstration Synthesis from a Single Scan via Gaussian Splatting for Visuomotor Policy Learning
  - 生成循环中不用物理引擎
- **PhyVisGen** · 2026 · 预印本 · [arXiv 2609.25653](https://arxiv.org/abs/2609.25653)
  - PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation
  - 同时提高物理和视觉保真度
- **ARSTAG** · 2026 · 预印本 · [arXiv 2609.24563](https://arxiv.org/abs/2609.24563) · [项目](https://boweili666.github.io/ARSTAG)
  - ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation
  - 智能体式的孪生构建与数据生成
- **FPSA** · 2026 · 预印本 · [arXiv 2609.18293](https://arxiv.org/abs/2609.18293) · [项目](https://fpsa-r2s2r.github.io)
  - Function-Preserving Data Generation for Zero-Shot Real-to-Sim-to-Real Manipulation
  - 形状变化时不破坏配合界面
- **GenSim2** · 2024 · CoRL 2024 · [arXiv 2410.03645](https://arxiv.org/abs/2410.03645) · [项目](https://gensim2.github.io)
  - GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs
  - LLM 生成任务和场景
- **ExpertGen** · 2026 · 预印本 · [arXiv 2603.15956](https://arxiv.org/abs/2603.15956)
  - ExpertGen: Scalable Sim-to-Real Expert Policy Learning from Imperfect Behavior Priors
  - 用 RL 精炼的专家替代脚本专家
- **DiscoDemo** · 2026 · 预印本 · [arXiv 2610.32093](https://arxiv.org/abs/2610.32093) · [项目](https://davian-robotics.github.io/DiscoDemo)
  - DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning
  - 解法多样性本身提升模仿学习
- **DATAFARM** · 2026 · 预印本 · [arXiv 2609.12316](https://arxiv.org/abs/2609.12316) · [项目](https://prpl-group.com/datafarm)
  - DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models
  - 规划器数据的"风格"决定 VLA 能否学会

### 2.3 孪生周边的变化

- **ACDC** · 2024 · CoRL 2024 · [arXiv 2410.07408](https://arxiv.org/abs/2410.07408) · [项目](https://digital-cousins.github.io)
  - Automated Creation of Digital Cousins for Robust Policy Learning
  - 只用精确孪生会过拟合；在所有资产上做朴素随机化也不够
- **SimFoundry** · 2026 · 预印本 · [arXiv 2606.28276](https://arxiv.org/abs/2606.28276) · [项目](https://research.nvidia.com/labs/gear/simfoundry)
  - SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation
  - 孪生加三类 cousin 的完整流程
- **RoboCousin** · 2026 · 预印本 · [arXiv 2609.08339](https://arxiv.org/abs/2609.08339)
  - RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation
  - 再次验证 cousin 优于只用孪生

### 2.4 世界模型生成数据

- **DreamGen** · 2025 · CoRL 2025 · [arXiv 2505.12705](https://arxiv.org/abs/2505.12705) · [代码](https://github.com/NVIDIA/GR00T-Dreams)
  - DreamGen: Unlocking Generalization in Robot Learning through Video World Models
  - 世界模型生成的 neural trajectories
- **AnchorDream** · 2025 · ICRA 2026† · [arXiv 2512.11797](https://arxiv.org/abs/2512.11797) · [项目](https://jay-ye.github.io/AnchorDream)
  - AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis
  - 以机器人运动为锚，避免本体幻觉
- **Grounded-Dreamer** · 2026 · 预印本 · [arXiv 2610.13164](https://arxiv.org/abs/2610.13164) · [项目](https://fffstrong.github.io/Grounded-Dreamer)
  - Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding
  - 世界模型数据接上物理校验
- **RoboCurate** · 2026 · 预印本 · [arXiv 2602.18742](https://arxiv.org/abs/2602.18742) · [项目](https://seungkukim.github.io/robocurate)
  - RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning
  - 对 IDM 标出的动作做仿真校验

### 2.5 决定生成或采集什么

- **MetaGenSim** · 2026 · CoRL 2026 · [arXiv 2610.19479](https://arxiv.org/abs/2610.19479) · [项目](https://meta-gensim.github.io)
  - Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training
  - 优化"仿真生成什么"，而不只是"生成多少"
- **EmbodiRSI** · 2026 · 预印本 · [arXiv 2609.38905](https://arxiv.org/abs/2609.38905)
  - EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation
  - 在部署场景孪生中做反馈驱动的递归改进
- **TANDEM** · 2026 · 预印本 · [arXiv 2609.28314](https://arxiv.org/abs/2609.28314) · [项目](https://prpl-group.com/tandem)
  - TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning
  - 人力只花在规划器做不到的阶段
- **F4R** · 2026 · 预印本 · [arXiv 2609.35575](https://arxiv.org/abs/2609.35575)
  - F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement
  - 以失败为中心的 real-to-sim 闭环

### 2.6 与现实同步的孪生

- **Real-is-Sim** · 2025 · 预印本 · [arXiv 2504.03597](https://arxiv.org/abs/2504.03597) · [项目](https://realissim.rai-inst.com)
  - Real-is-Sim: Bridging the Sim-to-Real Gap with a Dynamic Digital Twin
  - 把跨域责任从策略转到孪生同步机制

## 3. 模型侧的 gap 处理

### 3.1 域对齐与配对数据

- **Mechanistic Co-Train** · 2026 · ICML 2026 · [arXiv 2604.13645](https://arxiv.org/abs/2604.13645) · [项目](https://science-of-co-training.github.io)
  - A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies
  - 只做对齐会抹掉域信息导致负迁移，应"对齐 + 可分"
- **Invariance Co-training** · 2025 · 预印本 · [arXiv 2512.05230](https://arxiv.org/abs/2512.05230) · [项目](https://invariance-cotraining.github.io)
  - Invariance Co-training for Robot Visual Generalization
  - 用配对多视角渲染学到对视角 / 光照不变的状态表征
- **OT Co-Train** · 2025 · NeurIPS 2025 · [arXiv 2509.18631](https://arxiv.org/abs/2509.18631) · [项目](https://ot-sim2real.github.io)
  - Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training
  - 在共享潜空间里用 UOT 对齐 sim/real，同时保留与动作相关的信息
- **BIFROST** · 2026 · 预印本 · [arXiv 2607.01410](https://arxiv.org/abs/2607.01410) · [项目](https://未找到)
  - BIFROST: Bridging Invariant Feature Representation for Observation-space Sim2Real Transfer
  - 用"同起点同动作"的配对片段学 sim/real 共享的行为等价潜空间
- **EgoBridge** · 2025 · NeurIPS 2025 · [arXiv 2509.19626](https://arxiv.org/abs/2509.19626) · [项目](https://ego-bridge.github.io)
  - EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data
  - 与 Cheng et al. 同一 OT 思路，用于人–机器人联合训练
- **Weak Pairwise** · 2015 · 预印本 · [arXiv 1511.07111](https://arxiv.org/abs/1511.07111)
  - Adapting Deep Visuomotor Representations with Weak Pairwise Constraints
  - sim–real 配对对齐表征的最早工作之一
- **Best of Sim and Real** · 2025 · 预印本 · [arXiv 2509.25747](https://arxiv.org/abs/2509.25747) · [项目](https://未列出)
  - Best of Sim and Real: Decoupled Visuomotor Manipulation via Learning Control in Simulation and Perception in Real
  - 控制在仿真学，感知只在真实学
- **simDP** · 2026 · Sensors 2026† · [DOI](https://doi.org/10.3390/s26134079)
  - simDP: Sim-to-Real Transfer with Shared Action Spaces
  - 共享动作空间 + 只换编码器

### 3.2 观测空间

- **Point Bridge** · 2026 · 预印本 · [arXiv 2601.16212](https://arxiv.org/abs/2601.16212) · [项目](https://pointbridge3d.github.io)
  - Point Bridge: 3D Representations for Cross Domain Policy Learning
  - 用领域无关的点表征取代 RGB，联合训练收益远超图像联合训练
- **Any3D-VLA** · 2026 · ICML 2026 · [arXiv 2602.00807](https://arxiv.org/abs/2602.00807) · [项目](https://xianzhefan.github.io/Any3D-VLA.github.io)
  - Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds
  - 训练时混合多种深度来源，使 3D 特征对深度来源不敏感
- **CDM** · 2025 · 预印本 · [arXiv 2509.02530](https://arxiv.org/abs/2509.02530) · [项目](https://manipulation-as-in-simulation.github.io)
  - Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots
  - 把真实传感器"变成仿真"，策略用无噪声仿真深度训练即可上线
- **Sparse2Act** · 2026 · 预印本 · [arXiv 2606.12759](https://arxiv.org/abs/2606.12759) · [项目](https://未列出)
  - Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation
  - 用动作作监督预训练可跨域复用的 3D 编码器
- **S2GS** · 2025 · 预印本 · [arXiv 2512.04731](https://arxiv.org/abs/2512.04731) · [项目](https://未列出)
  - Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting
  - 用语义高斯特征场作为 sim/real 共享输入
- **Humanoid Dex Sim2Real** · 2025 · CoRL 2025 · [arXiv 2502.20396](https://arxiv.org/abs/2502.20396) · [项目](https://toruowo.github.io/recipe)
  - Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids
  - 稀疏物体位置 + 稠密分割深度，加执行器自动调参
- **VIRAL** · 2025 · 预印本 · [arXiv 2511.15200](https://arxiv.org/abs/2511.15200) · [项目](https://viral-humanoid.github.io)
  - VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
  - 用算力规模（最多 64 GPU）把 RGB 蒸馏学生做到零样本可用
- **Cloak** · 2026 · 预印本 · [arXiv 2606.22836](https://arxiv.org/abs/2606.22836) · [项目](https://未列出)
  - Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA
  - 把机器人本体从观测中"隐身"，不靠分割或生成模型

### 3.3 视觉翻译与写实渲染

- **RCAN** · 2018 · CVPR 2019 · [arXiv 1812.07252](https://arxiv.org/abs/1812.07252)
  - Sim-to-Real via Sim-to-Sim: Data-efficient Robotic Grasping via Randomized-to-Canonical Adaptation Networks
  - 反向思路：把真实翻译成仿真
- **RL-CycleGAN** · 2020 · CVPR 2020 · [arXiv 2006.09001](https://arxiv.org/abs/2006.09001)
  - RL-CycleGAN: Reinforcement Learning Aware Simulation-To-Real
  - 任务感知的图像翻译
- **RetinaGAN** · 2020 · ICRA 2021 · [arXiv 2011.03148](https://arxiv.org/abs/2011.03148) · [项目](https://retinagan.github.io)
  - RetinaGAN: An Object-aware Approach to Sim-to-Real Transfer
  - 物体结构保持的 sim→real 翻译
- **Cosmos-Transfer1** · 2025 · 预印本 · [arXiv 2503.14492](https://arxiv.org/abs/2503.14492) · [代码](https://github.com/nvidia-cosmos/cosmos-transfer1)
  - Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control
  - 通用 sim→real 视频翻译底座，策略收益尚无一手论文数字
- **RoboTransfer** · 2025 · 预印本 · [arXiv 2505.23171](https://arxiv.org/abs/2505.23171) · [项目](https://horizonrobotics.github.io/robot_lab/robotransfer)
  - RoboTransfer: Controllable Geometry-Consistent Video Diffusion for Manipulation Policy Transfer
  - 几何一致的多视角生成增强；不能当作 sim2real 策略证据
- **RoboRender** · 2026 · 预印本 · [arXiv 2610.09254](https://arxiv.org/abs/2610.09254) · [项目](https://robo-render.github.io)
  - RoboRender: Robot-Oriented Video Generation for Visual Sim-to-Real Transfer
  - 目前 sim→real 生成渲染最强的零样本策略数字
- **Seeing Realism** · 2026 · ICML 2026 · [arXiv 2605.02757](https://arxiv.org/abs/2605.02757) · [代码](https://github.com/nanfangxiansheng/Seeing-Realism-from-Simulation)
  - Seeing Realism from Simulation: Efficient Video Transfer for Vision-Language-Action Data Augmentation
  - 面向 VLA 的低成本 sim→real 视频增强
- **EmbodieDreamer** · 2025 · 预印本 · [arXiv 2507.05198](https://arxiv.org/abs/2507.05198) · [项目](https://embodiedreamer.github.io)
  - EmbodieDreamer: Advancing Real2Sim2Real Transfer for Policy Training via Embodied World Modeling
  - 视觉翻译与执行器参数对齐同时做
- **SplatSim** · 2024 · ICRA 2025 · [arXiv 2409.10161](https://arxiv.org/abs/2409.10161) · [代码](https://github.com/qureshinomaan/SplatSim)
  - SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting
  - 3DGS 渲染让纯 RGB 策略零样本可用
- **TwinAligner** · 2025 · 预印本 · [arXiv 2512.19390](https://arxiv.org/abs/2512.19390) · [项目](https://twin-aligner.github.io)
  - TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation
  - 视觉 + 动力学同时对齐的孪生，仿真训练接近真实训练
- **RenderBench** · 2026 · 预印本 · [arXiv 2610.08684](https://arxiv.org/abs/2610.08684) · [项目](https://未列出)
  - RenderBench: Benchmarking Render-to-Real Video Transfer with Reconstructed Digital Twins
  - 用配对孪生评测 render→real 翻译是否保持几何与动态

### 3.4 动作空间与动力学适配

- **Action-Space Study** · 2023 · 预印本 · [arXiv 2312.03673](https://arxiv.org/abs/2312.03673)
  - On the Role of the Action Space in Robot Manipulation Learning and Sim-to-Real Transfer
  - 高阶导数控制、能限制跟踪误差的动作空间迁移更好
- **RMA-Arms** · 2023 · CVPR 2024 · [arXiv 2312.04670](https://arxiv.org/abs/2312.04670)
  - Rapid Motor Adaptation for Robotic Manipulator Arms
  - RMA 在机械臂操作上的移植
- **TAM** · 2026 · CoRL 2026 · [arXiv 2606.06218](https://arxiv.org/abs/2606.06218) · [项目](https://dongwon-son.github.io/tam-project-page)
  - TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation
  - 与上层策略无关的动力学适配层
- **TDC** · 2026 · CoRL 2026 · [arXiv 2602.14174](https://arxiv.org/abs/2602.14174) · [项目](https://yifei-y.github.io/project-pages/TDC)
  - TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation
  - 只让策略输出仿真可迁移的那部分控制量
- **Torque-Obs Alignment** · 2026 · 预印本 · [arXiv 2609.29031](https://arxiv.org/abs/2609.29031)
  - Simple Torque-Observation Alignment for Zero-Shot Sim-to-Real Grasping with a Direct-Drive Gripper
  - 本体 / 力矩观测的尺度、偏置、噪声三步对齐
- **Chunk-VLA Pipeline** · 2026 · IROS 2026 Workshop · [arXiv 2609.21817](https://arxiv.org/abs/2609.21817) · [项目](https://gitlab.isir.upmc.fr/kappel/sim2real_public_chunk_control)
  - A Sim-to-Real Integration Pipeline for Training and Deployment of Chunk-Based VLA Manipulation Policies
  - 用重放得到配对数据，是孪生场景下最便宜的配对来源

## 4. 共训练之后的策略提升

### 4.1 孪生内 RL 与真实数据锚定

- **RialTo** · 2024 · RSS 2024 · [arXiv 2403.03949](https://arxiv.org/abs/2403.03949) · [项目](https://real-to-sim-to-real.github.io/RialTo)
  - Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation
  - 少量真实演示 + 扫描孪生内 RL 鲁棒化的原型
- **RL-Co** · 2026 · 预印本 · [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · [项目](https://rl-co-training.github.io)
  - Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models
  - 把“仿真 RL + 真实 SFT 锚”做成 VLA 通用两阶段配方
- **TacCoRL** · 2026 · 预印本 · [arXiv 2606.11743](https://arxiv.org/abs/2606.11743) · [项目](https://tac-corl.github.io)
  - TacCoRL: Integrating Tactile Feedback into VLA via Simulation
  - 真实数据锚的强度存在最佳区间的直接证据
- **SCORE** · 2026 · 预印本 · [arXiv 2606.27475](https://arxiv.org/abs/2606.27475) · [项目](https://weirdlabuw.github.io/score)
  - Support-Constrained RL Enables Real-World Policy Improvement without Real-World Experience
  - 把“锚”从分布距离（KL / W1）换成支撑约束
- **VT-Refine** · 2025 · CoRL 2025 · [arXiv 2510.14930](https://arxiv.org/abs/2510.14930) · [项目](https://binghao-huang.github.io/vt_refine)
  - VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation Fine-Tuning
  - 少量真实演示 → 孪生 RL 精修双臂插装
- **ConCent** · 2026 · 预印本 · [arXiv 2606.30268](https://arxiv.org/abs/2606.30268)
  - ConCent: Contact-Centric Real-to-Sim-to-Real Learning from One Demonstration
  - 用真实演示的接触事件约束 RL，防止利用仿真接触

### 4.2 孪生 RL 衔接真实 RL；仿真残差

- **TwinRL** · 2026 · 预印本 · [arXiv 2602.09023](https://arxiv.org/abs/2602.09023) · [项目](https://twinrl.github.io)
  - TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation
  - 孪生既扩展 SFT 支撑，又为真实 RL 预热
- **SimLauncher** · 2025 · IROS 2025† · [arXiv 2507.04452](https://arxiv.org/abs/2507.04452)
  - SimLauncher: Launching Sample-Efficient Real-world Robotic Reinforcement Learning via Simulation Pre-training
  - 孪生预训练给真实 RL 当“发射器”
- **OC-ResRL** · 2026 · 预印本 · [arXiv 2606.18953](https://arxiv.org/abs/2606.18953) · [项目](https://microsoft.com/en-us/research/articles/object-centric-residual-rl)
  - Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement
  - 物体中心观测让仿真残差可零样本迁移
- **VLaRL** · 2026 · 预印本 · [arXiv 2609.30868](https://arxiv.org/abs/2609.30868)
  - VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL
  - 以 VLA 潜变量作为 sim-to-real 接口
- **ResiP** · 2024 · 预印本 · [arXiv 2407.16677](https://arxiv.org/abs/2407.16677) · [项目](https://residual-assembly.github.io)
  - From Imitation to Refinement -- Residual RL for Precise Assembly
  - 残差 RL 精修 BC，但蒸馏成为瓶颈
- **Warp RL** · 2026 · 预印本 · [arXiv 2606.31043](https://arxiv.org/abs/2606.31043)
  - Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation
  - 加性残差改不了方差和形状，换成分布变换

### 4.3 真机少量修正

- **TRANSIC** · 2024 · CoRL 2024 · [arXiv 2405.10315](https://arxiv.org/abs/2405.10315) · [项目](https://transic-robot.github.io)
  - TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction
  - 人工纠正只训练残差，避免遗忘仿真策略
- **SPARR** · 2026 · 预印本 · [arXiv 2602.23253](https://arxiv.org/abs/2602.23253)
  - SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly
  - 仿真状态 base + 真实视觉残差
- **HandelBot** · 2026 · 预印本 · [arXiv 2603.12243](https://arxiv.org/abs/2603.12243) · [项目](https://amberxie88.github.io/handelbot)
  - HandelBot: Real-World Piano Playing via Fast Adaptation of Dexterous Robot Policies
  - 毫米级任务：仿真给结构，真实补细节
- **ReDex** · 2026 · 预印本 · [arXiv 2610.07525](https://arxiv.org/abs/2610.07525)
  - ReDex: Repairing Sim-to-Real Dexterous Policies by Finger-Level Compliant Interaction
  - 局部、逐指的人工纠正修补仿真灵巧策略
- **Sim2Online** · 2026 · 预印本 · [arXiv 2602.20220](https://arxiv.org/abs/2602.20220) · [代码](https://github.com/yardenas/panda-rl-kit)
  - What Matters for Simulation to Online Reinforcement Learning on Real Robots
  - 仿真→真实在线 RL 的工程配方
- **SimPT** · 2026 · 预印本 · [arXiv 2610.29161](https://arxiv.org/abs/2610.29161)
  - SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training
  - 用仿真替人做“纠正”来迭代后训练算法
- **PA-RL** · 2024 · 预印本 · [arXiv 2412.06685](https://arxiv.org/abs/2412.06685) · [项目](https://policyagnosticrl.github.io)
  - Policy Agnostic RL: Offline RL and Online RL Fine-Tuning of Any Class and Backbone
  - 对大策略做 actor-critic 微调的通用接口
- **ConRFT** · 2025 · RSS 2025† · [arXiv 2502.05450](https://arxiv.org/abs/2502.05450) · [项目](https://cccedric.github.io/conrft)
  - ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy
  - VLA 的真实 HIL RL 微调基线
- **HIL-SERL** · 2024 · Science Robotics 2025† · [arXiv 2410.21845](https://arxiv.org/abs/2410.21845) · [项目](https://hil-serl.github.io)
  - Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning
  - 真实 RL 修正的工程标杆
- **EXPO** · 2025 · 预印本 · [arXiv 2507.07986](https://arxiv.org/abs/2507.07986)
  - EXPO: Stable Reinforcement Learning with Expressive Policies
  - 不直接对表达性策略求 Q 梯度的稳定在线微调

### 4.4 专家蒸馏回通才

- **RLDG** · 2024 · 预印本 · [arXiv 2412.09858](https://arxiv.org/abs/2412.09858) · [项目](https://generalist-distillation.github.io)
  - RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning
  - RL 数据比人类演示更适合蒸馏进通才
- **PLD** · 2025 · 预印本 · [arXiv 2511.00091](https://arxiv.org/abs/2511.00091) · [项目](https://wenlixiao.com/self-improve-VLA-PLD)
  - Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
  - Probe-Learn-Distill 自我改进闭环
- **AutoMate** · 2024 · 预印本 · [arXiv 2407.08028](https://arxiv.org/abs/2407.08028) · [项目](https://bingjietang718.github.io/automate)
  - AutoMate: Specialist and Generalist Assembly Policies over Diverse Geometries
  - 仿真专家→通才蒸馏，真实精度基本保留
- **SGS** · 2026 · CoRL 2026 · [arXiv 2610.12465](https://arxiv.org/abs/2610.12465) · [项目](https://sgs-rl.github.io)
  - A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control
  - 蒸馏本身不丢精度，掉点主要在 sim-to-real
- **OmniReset** · 2026 · 预印本 · [arXiv 2603.15789](https://arxiv.org/abs/2603.15789) · [项目](https://weirdlabuw.github.io/omnireset)
  - Emergent Dexterity via Diverse Resets and Large-Scale Reinforcement Learning
  - 单一奖励、无课程，靠重置覆盖状态空间

### 4.5 接触密集装配的纯仿真 RL

- **PACE** · 2026 · 预印本 · [arXiv 2609.07534](https://arxiv.org/abs/2609.07534)
  - Proprioception-Anchored Cross-Modal Pretraining for Zero-Shot Sim-to-Real Contact-Rich Assembly
  - 以跨域最一致的本体信号锚定表征
- **IndustReal** · 2023 · RSS 2023 · [arXiv 2305.17110](https://arxiv.org/abs/2305.17110) · [项目](https://sites.google.com/nvidia.com/industreal)
  - IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality
  - 接触密集装配纯仿真 RL 迁移的起点
- **FORGE** · 2024 · 预印本 · [arXiv 2408.04587](https://arxiv.org/abs/2408.04587) · [项目](https://noseworm.github.io/forge)
  - FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty
  - 力阈值让仿真策略对控制增益和位姿误差更稳
- **SRSA** · 2025 · 预印本 · [arXiv 2503.04538](https://arxiv.org/abs/2503.04538) · [项目](https://srsa2024.github.io)
  - SRSA: Skill Retrieval and Adaptation for Robotic Assembly Tasks
  - 从专家库检索最易微调的技能
- **InsertAnything** · 2026 · 预印本 · [arXiv 2609.24511](https://arxiv.org/abs/2609.24511) · [项目](https://mzhsoul.github.io/InsertAnything)
  - InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality
  - 位姿 + 紧凑力反馈即可跨几何迁移
- **Play2Perfect** · 2026 · 预印本 · [arXiv 2606.26428](https://arxiv.org/abs/2606.26428) · [项目](https://play2perfect.github.io)
  - Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?
  - 先玩后精：灵巧装配的仿真先验
- **Blind Assembly** · 2026 · 预印本 · [arXiv 2610.23849](https://arxiv.org/abs/2610.23849) · [项目](https://younghyopark.me/blind-proprioceptive-assembly)
  - Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts
  - 本体感知本身就是可迁移的接触传感器

### 4.6 在线适应真实动力学

- **CoRMA** · 2026 · 预印本 · [arXiv 2605.22082](https://arxiv.org/abs/2605.22082)
  - CoRMA: Contrastive RMA for Contact-Rich Meta-Adaptation
  - 把 RMA 的物理参数换成接触语义上下文
- **TeAR** · 2026 · 预印本 · [arXiv 2609.36182](https://arxiv.org/abs/2609.36182)
  - Test-Time Adaptation of Manipulation Policies Under Actuator Degradation
  - 用遥测在测试时矫正动作

## 5. 补充

以下论文与本方向相关，本轮只核实了元数据，没有提取完整数字。

- **DextrAH-RGB** · 2024 · 预印本 · [arXiv 2412.01791](https://arxiv.org/abs/2412.01791)
  - DextrAH-RGB: Visuomotor Policies to Grasp Anything with Dexterous Hands
  - 视觉 teacher–student：特权状态 RL 教师蒸馏为 RGB 灵巧抓取学生
- **ClutterDexGrasp** · 2025 · CoRL 2025 · [arXiv 2506.14317](https://arxiv.org/abs/2506.14317)
  - ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes
  - 杂乱场景灵巧抓取的 sim-to-real，学生为 DP3 点云策略
- **DexPoint** · 2022 · CoRL 2022 · [arXiv 2211.09423](https://arxiv.org/abs/2211.09423)
  - DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation
  - 点云 RL 加想象手部点云，用于灵巧操作 sim-to-real
- **ReDOA** · 2026 · 预印本 · [arXiv 2610.25691](https://arxiv.org/abs/2610.25691)
  - ReDOA: Real-World Distillation via Observation Alignment for Image-Based Manipulation Policy Learning
  - 仿真状态教师在真机上执行，蒸馏为真实图像学生
- **Mirage** · 2024 · RSS 2024 · [arXiv 2402.19249](https://arxiv.org/abs/2402.19249)
  - Mirage: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting
  - cross-painting：遮去目标机器人并补画源机器人，实现跨本体零样本迁移
- **RoboEngine** · 2025 · 预印本 · [arXiv 2503.18738](https://arxiv.org/abs/2503.18738)
  - RoboEngine: Plug-and-Play Robot Data Augmentation with Semantic Robot Segmentation and Background Generation
  - 机器人语义分割 + 背景生成的即插即用数据增强
- **GenAug** · 2023 · 预印本 · [arXiv 2302.06671](https://arxiv.org/abs/2302.06671)
  - GenAug: Retargeting behaviors to unseen situations via Generative Augmentation
  - 生成式图像增强，把行为迁移到未见场景（real→real）
- **ROSIE** · 2023 · 预印本 · [arXiv 2302.11550](https://arxiv.org/abs/2302.11550)
  - Scaling Robot Learning with Semantically Imagined Experience
  - 文生图模型对真实示教做语义增强（real→real）
- **ReShoot** · 2026 · 预印本 · [arXiv 2609.19661](https://arxiv.org/abs/2609.19661)
  - ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning
  - 对已录示教做生成式视觉域随机化
- **RoboVIP** · 2026 · 预印本 · [arXiv 2601.05241](https://arxiv.org/abs/2601.05241)
  - RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
  - 带视觉身份提示的多视角视频生成，用于操作数据增强
- **VideoWeaver** · 2026 · 预印本 · [arXiv 2603.25420](https://arxiv.org/abs/2603.25420)
  - VideoWeaver: Multimodal Multi-View Video-to-Video Transfer for Embodied Agents
  - 多模态多视角 video-to-video 迁移
- **TC-Light** · 2025 · 预印本 · [arXiv 2506.18904](https://arxiv.org/abs/2506.18904)
  - TC-Light: Temporally Coherent Generative Rendering for Realistic World Transfer
  - 时间一致的生成式重渲染，用于真实感世界迁移
- **Cosmos-Transfer2.5** · 2025 · 预印本 · [arXiv 2511.00062](https://arxiv.org/abs/2511.00062)
  - World Simulation with Video Foundation Models for Physical AI
  - Cosmos 世界模型 2.5 版技术报告，含条件视频迁移
- **ViserDex** · 2026 · 预印本 · [arXiv 2604.11138](https://arxiv.org/abs/2604.11138)
  - ViserDex: Visual Sim-to-Real for Robust Dexterous In-hand Reorientation
  - 在高斯表征空间做域随机化，用于灵巧手内重定向的视觉 sim-to-real
- **Robot-Aligned 3DGS** · 2026 · 预印本 · [arXiv 2610.35626](https://arxiv.org/abs/2610.35626)
  - Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies
  - 与机器人对齐的 3DGS 渲染腕部相机数据；1500 条生成轨迹 80.0% vs 150 条遥操作 58.7%
- **GS-Playground** · 2026 · RSS 2026 · [arXiv 2604.25459](https://arxiv.org/abs/2604.25459)
  - GS-Playground: A High-Throughput Photorealistic Simulator for Vision-Informed Robot Learning
  - 高吞吐量的写实高斯仿真器
- **SimWeaver** · 2026 · 预印本 · [arXiv 2606.15338](https://arxiv.org/abs/2606.15338)
  - SimWeaver: Zero-Shot RGB Sim-to-Real for Deformable Manipulation
  - ISP 感知的光度增强，用于可变形物体操作的零样本 RGB sim-to-real
- **Viewpoint Study** · 2026 · 预印本 · [arXiv 2609.32762](https://arxiv.org/abs/2609.32762)
  - An Empirical Study on What Matters for Viewpoint-Generalizable Policies in Visual Imitation Learning
  - 视觉模仿学习中视角泛化因素的实证研究
- **ECG** · 2026 · 预印本 · [arXiv 2610.22576](https://arxiv.org/abs/2610.22576)
  - Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations
  - Embodiment-Classifier Guidance：冻结 π0，用分类器引导跨动力学迁移，只在 LIBERO 上测试
- **World Translation** · 2026 · 预印本 · [arXiv 2607.18154](https://arxiv.org/abs/2607.18154)
  - World Translation: Minimizing Sim-to-Real Gap with Backward Dynamics Extraction and Unpaired Domain Translation
  - 反向动力学提取 + 非配对域翻译，在动力学层缩小 sim-to-real gap
- **DADP** · 2026 · 预印本 · [arXiv 2602.04037](https://arxiv.org/abs/2602.04037)
  - DADP: Domain Adaptive Diffusion Policy
  - 域自适应扩散策略
- **Cosmos Policy Sim2Real** · 2026 · CVPR 2026 Workshop · [arXiv 2606.31101](https://arxiv.org/abs/2606.31101)
  - Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors
  - 基于 Cosmos Policy，每任务约 800 条规划示教，零样本真机平均 35%
- **HumanoidMimicGen** · 2026 · 预印本 · [arXiv 2605.27724](https://arxiv.org/abs/2605.27724)
  - HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning
  - 全身规划生成人形移动操作数据；真实 30–50 条 + 仿真 500–1000 条共训练，平均分 0.51 → 0.71
- **PhysWorld** · 2025 · 预印本 · [arXiv 2511.07416](https://arxiv.org/abs/2511.07416)
  - Robot Learning from a Physical World Model
  - 生成视频 → 重建物理世界 → 残差 RL 落地；10 个真实任务 82% vs 次优 67%
- **Fail2Progress** · 2025 · CoRL 2025 · [arXiv 2509.01746](https://arxiv.org/abs/2509.01746)
  - Fail2Progress: Learning from Real-World Robot Failures with Stein Variational Inference
  - 用 Stein 变分推断批量生成与真实失败相似的仿真环境
- **Mulligan** · 2026 · 预印本 · [arXiv 2610.05882](https://arxiv.org/abs/2610.05882)
  - Mulligan: Performance-Guided Data Collection for Efficient On-Robot Learning
  - 只在真机上做：把初始状态集中到失败处，成功率提升 10–34 个百分点
- **RoboPocket** · 2026 · CoRL 2026 · [arXiv 2603.05504](https://arxiv.org/abs/2603.05504)
  - RoboPocket: Improve Robot Policies Instantly with Your Phone
  - 手机 AR 显示策略预测，引导无机器人的纠偏采集，样本效率最高 2×
- **CoDA** · 2026 · 预印本 · [arXiv 2610.22362](https://arxiv.org/abs/2610.22362)
  - CoDA: Co-Evolution of Data Engines and Action Policies
  - 数据引擎与策略共同进化，OOD 5.3% → 27.6%
- **GenSim** · 2023 · ICLR 2024 · [arXiv 2310.01361](https://arxiv.org/abs/2310.01361)
  - GenSim: Generating Robotic Simulation Tasks via Large Language Models
  - LLM 生成仿真任务与专家代码；真实长程任务 +25%
- **RoboGen** · 2023 · ICML 2024 · [arXiv 2311.01455](https://arxiv.org/abs/2311.01455)
  - RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation
  - 生成式仿真自动产生任务、场景与技能，只在仿真中评测
- **ATHENA** · 2026 · 预印本 · [arXiv 2606.16208](https://arxiv.org/abs/2606.16208)
  - ATHENA: Accelerated Multi-Task Heterogeneous Influence Functions for Robot Data Curation
  - VLA 规模的多任务影响函数数据筛选，未测 sim+real 混合
- **IWR** · 2025 · CoRL 2025 · [arXiv 2509.01657](https://arxiv.org/abs/2509.01657)
  - Data Retrieval with Importance Weights for Few-Shot Imitation Learning
  - 带重要性权重的数据检索，用于少样本模仿学习，单域测试
- **Temperature Sampling** · 2025 · 预印本 · [arXiv 2510.19373](https://arxiv.org/abs/2510.19373)
  - Using Temperature Sampling to Effectively Train Robot Learning Policies on Imbalanced Datasets
  - 温度采样处理不平衡数据集，单域测试
- **Data Analogies** · 2026 · 预印本 · [arXiv 2603.06450](https://arxiv.org/abs/2603.06450)
  - Data Analogies Enable Efficient Cross-Embodiment Transfer
  - 跨本体迁移中，配对的数据类比比无结构的多样性更有效
