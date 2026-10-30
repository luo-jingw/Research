# humanoid-motion-tracking 论文目录

- 快照日期：2026-10-30
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：已确认的发表处；"预印本" 表示检索时未找到发表处。标 † 的条目发表处只来自引用或二手页面，见根目录 `issues.md` → ISSUE-002。
- 每条的标题、年份、arXiv 编号均经 arXiv 页面、arXiv API 或论文集核实。
- 机器人字段：✓ 表示有真机部署。
- 分节对应 [survey.md](survey.md) 的分类。

## 1. 图形学根源

- **DeepMimic** · 2018 · ACM TOG 37(4), SIGGRAPH 2018 · [arXiv 1804.02717](https://arxiv.org/abs/1804.02717)
  - DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills
  - 模仿奖励 + 任务目标，每段动作一个 PPO 专家
- **NPMP** · 2018 · ICLR 2019 · [arXiv 1811.11711](https://arxiv.org/abs/1811.11711)
  - Neural Probabilistic Motor Primitives for Humanoid Control
  - 把多个专家蒸馏进一个可复用的潜空间运动策略
- **AMP** · 2021 · ACM TOG 40(4), SIGGRAPH 2021 · [arXiv 2104.02180](https://arxiv.org/abs/2104.02180)
  - AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control
  - 对抗式运动先验替代跟踪奖励
- **PHC** · 2023 · ICCV 2023 · [arXiv 2305.06456](https://arxiv.org/abs/2305.06456) · [项目](https://zhengyiluo.github.io/PHC)
  - Perpetual Humanoid Control for Real-time Simulated Avatars
  - 一个跟踪器模仿 98.9% 的 AMASS，带摔倒恢复
- **PULSE** · 2023 · ICLR 2024 Spotlight · [arXiv 2310.04582](https://arxiv.org/abs/2310.04582) · [代码](https://github.com/ZhengyiLuo/PULSE)
  - Universal Humanoid Motion Representations for Physics-Based Control
  - PHC → DAgger 蒸馏进 VAE 潜空间 → 下游 PPO
- **MaskedMimic** · 2024 · ACM TOG 43(6), SIGGRAPH Asia 2024 · [arXiv 2409.14393](https://arxiv.org/abs/2409.14393) · [项目](https://research.nvidia.com/labs/par/maskedmimic)
  - MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting
  - 把控制看作从部分目标做动作补全

## 2. 真机动作跟踪：2024

- **H2O** · 2024 · IROS 2024† · H1 ✓ · [arXiv 2403.04436](https://arxiv.org/abs/2403.04436) · [项目](https://human2humanoid.com)
  - Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  - SMPL 形状拟合重定向 + 特权模仿器做 "sim-to-data" 过滤，RGB 全身遥操作
- **OmniH2O** · 2024 · CoRL 2024† · H1 ✓ · [arXiv 2406.08858](https://arxiv.org/abs/2406.08858) · [项目](https://omni.human2humanoid.com)
  - OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
  - 特权教师 → 稀疏输入学生；运动学位姿作为 VR、RGB、自主控制的统一接口
- **HumanPlus** · 2024 · CoRL 2024† · H1 ✓ · [arXiv 2406.10454](https://arxiv.org/abs/2406.10454) · [项目](https://humanoid-ai.github.io)
  - HumanPlus: Humanoid Shadowing and Imitation from Humans
  - RGB 影随采集数据，再学习自主技能
- **ExBody** · 2024 · RSS 2024† · H1 ✓ · [arXiv 2402.16796](https://arxiv.org/abs/2402.16796) · [项目](https://expressive-humanoid.github.io)
  - Expressive Whole-Body Control for Humanoid Robots
  - 上身模仿动作，腿部只跟踪根速度
- **ExBody2** · 2024 · 预印本 · G1 ✓ · [arXiv 2412.13196](https://arxiv.org/abs/2412.13196) · [项目](https://exbody2.github.io)
  - ExBody2: Advanced Expressive Humanoid Whole-Body Control
  - 速度跟踪与关键点跟踪分离；教师过滤不可行数据
- **HOVER** · 2024 · ICRA 2025 · H1 ✓ · [arXiv 2410.21229](https://arxiv.org/abs/2410.21229) · [项目](https://hover-versatile-humanoid.github.io)
  - HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots
  - 一个掩码多模式学生覆盖运动学、关节、根指令模式

## 3. 真机动作跟踪：2025 的分化

- **ASAP** · 2025 · RSS 2025 · G1 ✓ · [arXiv 2502.01143](https://arxiv.org/abs/2502.01143) · [项目](https://agile.human2humanoid.com)
  - ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills
  - 每动作 PPO 专家 → 用真机数据学残差动作模型 → 在修正仿真中微调
- **KungfuBot** · 2025 · NeurIPS 2025 · G1 ✓ · [arXiv 2506.12851](https://arxiv.org/abs/2506.12851) · [项目](https://kungfubot.github.io)
  - KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills
  - 双层自适应跟踪容差课程，学功夫与舞蹈
- **VideoMimic** · 2025 · CoRL 2025 · G1 ✓ · [arXiv 2505.03729](https://arxiv.org/abs/2505.03729) · [项目](https://videomimic.net)
  - Visual Imitation Enables Contextual Humanoid Control
  - 单目 4D 人 + 场景重建 → 跟踪 → 蒸馏为本体 + 高度图策略，上楼梯、坐下
- **TWIST** · 2025 · CoRL 2025† · G1 ✓ · [arXiv 2505.02833](https://arxiv.org/abs/2505.02833) · [项目](https://humanoid-teleop.github.io)
  - TWIST: Teleoperated Whole-Body Imitation System
  - 特权教师（看未来帧）→ RL + BC 学生，动捕全身遥操作
- **GMT** · 2025 · 预印本 · G1 ✓ · [arXiv 2506.14770](https://arxiv.org/abs/2506.14770) · [项目](https://gmt-humanoid.github.io)
  - GMT: General Motion Tracking for Humanoid Whole-Body Control
  - 自适应采样 + 动作混合专家，教师 → 学生
- **BumbleBee** · 2025 · 预印本 · G1 ✓ · [arXiv 2506.12779](https://arxiv.org/abs/2506.12779) · [项目](https://beingbeyond.github.io/BumbleBee)
  - From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots
  - 聚类专家用真机残差动作精化后蒸馏为通用策略
- **UniTracker** · 2025 · IEEE RA-L 2026† · G1 ✓ · [arXiv 2507.07356](https://arxiv.org/abs/2507.07356) · [项目](https://yinkangning0124.github.io/Humanoid-UniTracker)
  - UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots
  - 部分观测先验对齐全观测编码器的 CVAE 学生
- **BeyondMimic** · 2025 · Science Robotics 2026† · G1 ✓ · [arXiv 2508.08241](https://arxiv.org/abs/2508.08241) · [项目](https://beyondmimic.github.io)
  - BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion
  - 统一 MDP 与超参数的每动作 PPO 配方 → 潜状态–动作扩散 → classifier guidance 做新任务
- **Any2Track** · 2025 · 预印本 · G1 ✓ · [arXiv 2509.13833](https://arxiv.org/abs/2509.13833) · [项目](https://zzk273.github.io/Any2Track)
  - Track Any Motions under Any Disturbances
  - 通用跟踪器上加基于历史的在线动力学适应

## 4. 规模化与基础模型：2025–2026

- **SONIC** · 2025 · Science Robotics 2026† · G1 ✓ · [arXiv 2511.07820](https://arxiv.org/abs/2511.07820) · [项目](https://nvlabs.github.io/GEAR-SONIC)
  - SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control
  - 单个通用 PPO，611 h 数据、1.2M→42M 参数、128 GPU × 7 天；FSQ token 接口连接规划器、VR、VLA
- **BFM-Zero** · 2025 · ICLR 2026 · G1 ✓ · [arXiv 2511.04131](https://arxiv.org/abs/2511.04131)
  - BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised RL
  - 对照路线：Forward-Backward 无监督 RL，一个潜空间统一动作、目标与奖励
- **OmniXtreme** · 2026 · 预印本 · G1 ✓ · [arXiv 2602.23843](https://arxiv.org/abs/2602.23843) · [项目](https://extreme-humanoid.github.io)
  - OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control
  - 专家教师 → flow matching 学生 → 执行器感知的 RL 精化
- **HoloMotion-1** · 2026 · 技术报告 · G1 ✓ · [arXiv 2605.15336](https://arxiv.org/abs/2605.15336) · [代码](https://github.com/HorizonRobotics/HoloMotion)
  - HoloMotion-1 Technical Report
  - >2000 h 以视频为主的数据，稀疏 MoE Transformer 直接用 PPO 训练
- **Humanoid-GPT** · 2026 · CVPR 2026 · G1 ✓ · [arXiv 2606.03985](https://arxiv.org/abs/2606.03985) · [代码](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT)
  - Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking
  - 约 300 个聚类专家 → 并行 DAgger 蒸馏进因果 GPT，20 亿帧
- **SuperMimic** · 2026 · CoRL 2026 Oral · G1 ✓ · [arXiv 2610.28480](https://arxiv.org/abs/2610.28480) · [项目](https://supermimic.github.io)
  - SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model
  - 拟合仿真转移的可微世界模型 + BPTT，1 H100 × 3 h 超过 SONIC；精读见 [notes/2026-supermimic.md](notes/2026-supermimic.md)
- **SONIC-K1** · 2026 · 预印本 · Booster K1（部分） · [arXiv 2610.39327](https://arxiv.org/abs/2610.39327) · [项目](https://kyry.me/sonic-k1)
  - SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU
  - 在单张共享 GPU 上把 SONIC 配方移植到小型人形

## 5. 接口、交互与非平地：2025–2026

- **HDMI** · 2025 · 预印本 · G1 ✓ · [arXiv 2509.16757](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io)
  - HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos
  - 从视频同时跟踪机器人与物体，交互奖励；部署需动捕物体位姿
- **ResMimic** · 2025 · 预印本 · G1 ✓ · [arXiv 2510.05070](https://arxiv.org/abs/2510.05070) · [项目](https://resmimic.github.io)
  - ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning
  - 冻结通用跟踪器 + 残差 PPO，加入物体感知
- **TWIST2** · 2025 · 预印本 · G1 ✓ · [arXiv 2511.02832](https://arxiv.org/abs/2511.02832) · [项目](https://yanjieze.com/TWIST2)
  - TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System
  - 免动捕 VR 全身遥操作，15 min 采 100 条示教
- **LATENT** · 2026 · IROS 2026† · G1 ✓ · [arXiv 2603.12686](https://arxiv.org/abs/2603.12686) · [项目](https://zzk273.github.io/LATENT)
  - Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data
  - PPO 跟踪器 → DAgger 潜空间 → 带潜动作屏障的高层 PPO，打网球对拉
- **SceneBot** · 2026 · 预印本 · G1 ✓ · [arXiv 2606.27581](https://arxiv.org/abs/2606.27581) · [项目](https://ericcsr.github.io/scenebot)
  - SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction
  - 以逐连杆接触标签为条件消解场景交互歧义，搬箱上楼
- **GigaBrain-WBC-0.5** · 2026 · 技术报告 · G1 ✓ · [arXiv 2608.18234](https://arxiv.org/abs/2608.18234) · [项目](https://shepherd1226.github.io/gigabrain-wbc-0.5)
  - GigaBrain-WBC-0.5: A Behavior World Model for Robust Humanoid Whole-Body Tracking with Environment Interaction
  - 约 2,200 h 数据自动标注支撑几何；地形交互成功率 81.3%，摔倒恢复 99.3%
- **PGMT** · 2026 · 预印本 · G1 ✓ · [arXiv 2609.08511](https://arxiv.org/abs/2609.08511) · [项目](https://luyili.github.io/pgmt)
  - PGMT: Perceptive General Motion Tracking for Humanoid Robots
  - 跟踪与恢复先验 + 地形感知，越过最高 37 cm 障碍
- **HumanoidNDM** · 2026 · CoRL 2026 · G1 ✓ · [arXiv 2610.34126](https://arxiv.org/abs/2610.34126)
  - HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model
  - 真机数据训练神经动力学模型，策略经模型反传梯度在线微调，免动捕
- **METATRON** · 2026 · 预印本 · G1 ✓ · [arXiv 2610.38027](https://arxiv.org/abs/2610.38027) · [项目](https://research.nvidia.com/labs/par/projects/metatron)
  - METATRON: A Promptable Whole-Body Execution Layer for Humanoids
  - 4 个专家跟踪器蒸馏为冻结的提示条件基础策略，技能由编码智能体写成代码

## 6. 数据集与重定向

- **AMASS** · 2019 · ICCV 2019 · [arXiv 1904.03278](https://arxiv.org/abs/1904.03278)
  - AMASS: Archive of Motion Capture as Surface Shapes
  - 统一 SMPL 格式的动捕语料，PHC、H2O、GMT、TWIST 的默认数据
- **LAFAN1** · 2020 · SIGGRAPH 2020 · [arXiv 2102.04942](https://arxiv.org/abs/2102.04942)
  - Robust Motion In-betweening
  - BeyondMimic、GMR、SuperMimic 使用其 G1 重定向版本（40 段，2.45 h）
- **BONES-SEED** · 2026 · 数据集 · [Hugging Face](https://huggingface.co/datasets/bones-studio/seed)
  - BONES-SEED: Skeletal everyday embodiment dataset
  - SONIC 训练数据的公开部分，142,220 条序列、288 h；SuperMimic 过滤为 129,514 条、264.56 h
- **PHUMA** · 2025 · CoRL 2026† · [arXiv 2510.26236](https://arxiv.org/abs/2510.26236) · [项目](https://davian-robotics.github.io/PHUMA)
  - PHUMA: Physically Reliable Humanoid Locomotion Dataset
  - 73 h 动捕 + 视频，经物理筛选
- **GMR** · 2025 · ICRA 2026† · [arXiv 2510.02252](https://arxiv.org/abs/2510.02252) · [代码](https://github.com/YanjieZe/GMR)
  - Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking
  - 重定向伪影比奖励调参更限制跟踪鲁棒性；SONIC 数据使用的重定向器之一
- **OmniRetarget** · 2025 · 预印本 · [arXiv 2509.26633](https://arxiv.org/abs/2509.26633) · [项目](https://omniretarget.github.io)
  - OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
  - 交互网格 Laplacian 重定向保持接触，支持数据增广

## 7. 可微学习代理模型：角色与人形

- **SuperTrack** · 2021 · ACM TOG 40(6), SIGGRAPH Asia 2021 · 无 arXiv · [项目](https://theorangeduck.com/page/supertrack-motion-tracking-physically-simulated-characters-using-supervised-learning)
  - SuperTrack: Motion Tracking for Physically Simulated Characters using Supervised Learning
  - 8 帧窗口拟合世界模型，32 帧窗口反传跟踪损失，无 critic
- **ControlVAE** · 2022 · ACM TOG 41(6), SIGGRAPH Asia 2022 · [arXiv 2210.06063](https://arxiv.org/abs/2210.06063)
  - ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters
  - 世界模型、技能潜空间与生成式控制器联合学习
- **DiffMimic** · 2023 · ICLR 2023 · [arXiv 2304.03274](https://arxiv.org/abs/2304.03274) · [项目](https://diffmimic.github.io)
  - DiffMimic: Efficient Motion Mimicking with Differentiable Physics
  - 真可微仿真器上做模仿，Demonstration Replay 稳定长视界反传
- **MoConVQ** · 2023 · ACM TOG 43(4), SIGGRAPH 2024 · [arXiv 2310.10198](https://arxiv.org/abs/2310.10198) · [项目](https://moconvq.github.io)
  - MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations
  - MBRL 学习 VQ-VAE 运动 token，数十小时动作数据
- **SuperDyno** · 2025 · ICLR 2025 Workshop on World Models · [OpenReview](https://openreview.net/forum?id=FPgKt7bA8w)
  - Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics
  - 中等规模神经动力学模型作为可微仿真器，扩展到数万段动作

## 8. 可微仿真策略学习

- **Suh et al.** · 2022 · ICML 2022 · [arXiv 2202.00817](https://arxiv.org/abs/2202.00817)
  - Do Differentiable Simulators Give Better Policy Gradients?
  - 刚性与不连续使一阶梯度可能比零阶更差（偏差–方差分析）
- **SHAC** · 2022 · ICLR 2022 · [arXiv 2204.07137](https://arxiv.org/abs/2204.07137) · [代码](https://github.com/NVlabs/DiffRL)
  - Accelerated Policy Learning with Parallel Differentiable Simulation
  - 短视界截断 BPTT + 平滑 critic 自举
- **AHAC** · 2024 · ICML 2024 · [arXiv 2405.17784](https://arxiv.org/abs/2405.17784) · [代码](https://github.com/imgeorgiev/DiffRL)
  - Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation
  - 自适应截断视界，在刚性接触前停止
- **Song et al.** · 2024 · CoRL 2024 Oral · [arXiv 2403.14864](https://arxiv.org/abs/2403.14864)
  - Learning Quadruped Locomotion Using Differentiable Simulation
  - IsaacGym 前向 + 可微单刚体代理反向，Mini Cheetah 零样本上真机
- **Schwarke et al.** · 2024 · CoRL 2025 · [arXiv 2404.02887](https://arxiv.org/abs/2404.02887)
  - Learning Deployable Locomotion Control via Differentiable Simulation
  - 用穿透深度的 sigmoid 平滑硬接触，ANYmal D 零样本上真机
- **SAPO** · 2024 · ICLR 2025 Spotlight · [arXiv 2412.12089](https://arxiv.org/abs/2412.12089) · [项目](https://rewarped.github.io)
  - Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation
  - 熵正则随机策略用解析梯度训练，含可变形物体
- **Back to Newton's Laws** · 2024 · Nature Machine Intelligence 2025 · [arXiv 2407.10648](https://arxiv.org/abs/2407.10648)
  - Back to Newton's Laws: Learning Vision-based Agile Flight via Differentiable Physics
  - 极简可微质点模型 + 深度渲染训练视觉飞行，零样本上真机

## 9. 世界模型用于机器人策略优化

- **MAAC** · 2020 · ICLR 2020 · [arXiv 2005.08068](https://arxiv.org/abs/2005.08068)
  - Model-Augmented Actor-Critic: Backpropagating through Paths
  - 学习模型上 H 步路径梯度 + 终端 Q
- **Dreamer** · 2019 · ICLR 2020 · [arXiv 1912.01603](https://arxiv.org/abs/1912.01603)
  - Dream to Control: Learning Behaviors by Latent Imagination
  - 通过潜空间想象反传价值梯度训练 actor
- **DreamerV3** · 2023 · Nature 2025 · [arXiv 2301.04104](https://arxiv.org/abs/2301.04104) · [项目](https://danijar.com/dreamerv3)
  - Mastering Diverse Domains through World Models
  - 连续动作也改用 REINFORCE，一套固定配置
- **DayDreamer** · 2022 · CoRL 2022 · [arXiv 2206.14176](https://arxiv.org/abs/2206.14176) · [项目](https://danijar.com/daydreamer)
  - DayDreamer: World Models for Physical Robot Learning
  - 直接在实体机器人上训练 Dreamer，无仿真器
- **TD-MPC2** · 2023 · ICLR 2024 Spotlight · [arXiv 2310.16828](https://arxiv.org/abs/2310.16828) · [项目](https://tdmpc2.com)
  - TD-MPC2: Scalable, Robust World Models for Continuous Control
  - 潜空间世界模型做短视界规划 + 终端价值
- **Puppeteer** · 2024 · ICLR 2025 · [arXiv 2405.18418](https://arxiv.org/abs/2405.18418) · [项目](https://nicklashansen.com/rlpuppeteer)
  - Hierarchical World Models as Visual Whole-Body Humanoid Controllers
  - 高层视觉世界模型指挥低层跟踪世界模型，56 自由度仿真人形
- **PWM** · 2024 · ICLR 2025 · [arXiv 2407.02466](https://arxiv.org/abs/2407.02466) · [项目](https://imgeorgiev.com/pwm)
  - PWM: Policy Learning with Multi-Task World Models
  - 正则化世界模型比真实接触动力学更平滑，有利于一阶梯度
- **RWM** · 2025 · NeurIPS 2025 EWM Workshop · [arXiv 2501.10100](https://arxiv.org/abs/2501.10100) · [代码](https://github.com/leggedrobotics/robotic_world_model)
  - Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics
  - 长视界神经仿真器 + 模型内 PPO；报告 SHAC 经同一世界模型不收敛
- **QWM** · 2026 · CoRL 2026† · [arXiv 2604.08780](https://arxiv.org/abs/2604.08780) · [代码](https://github.com/modanesh/QWM)
  - Morphology-Conditioned World Model for Cross-Embodiment Quadrupedal Locomotion
  - 形态条件潜动力学，零样本迁移到未见四足

## 10. 在真实数据上拟合动力学

- **FOWM** · 2023 · CoRL 2023 Oral · [arXiv 2310.16029](https://arxiv.org/abs/2310.16029) · [项目](https://yunhaifeng.com/FOWM)
  - Finetuning Offline World Models in the Real World
  - 离线真实数据世界模型在线微调，规划时权衡回报与认知不确定性
- **RWM-U** · 2025 · ICLR 2026 World Models Workshop · [arXiv 2504.16680](https://arxiv.org/abs/2504.16680) · [代码](https://github.com/leggedrobotics/robotic_world_model_lite)
  - Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots
  - 仿真 + 约 1 h 真实转移，集成不确定性惩罚的模型内 PPO；真实数据过多反而变差
- **NeRD** · 2025 · CoRL 2025 · [arXiv 2508.15755](https://arxiv.org/abs/2508.15755) · [代码](https://github.com/NVlabs/neural-robot-dynamics)
  - Neural Robot Dynamics
  - 神经求解器可用真实数据微调，抛方块位置误差 0.036 → 0.018 m
- **PIN-WM** · 2025 · RSS 2025 · [arXiv 2504.16693](https://arxiv.org/abs/2504.16693)
  - PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation
  - 少量真实视频 + 高斯渲染损失端到端辨识可微物理参数
- **Ishihara et al.** · 2024 · 预印本 · [arXiv 2409.08488](https://arxiv.org/abs/2409.08488)
  - Hierarchical Learning Framework for Whole-Body Model Predictive Control of a Real Humanoid Robot
  - 解析模型 + 真机上学习的残差动力学，用于全身 MPC
- **PIA** · 2026 · 预印本 · [arXiv 2610.26757](https://arxiv.org/abs/2610.26757) · [项目](https://toyotaresearchinstitute.github.io/pia-mbrl)
  - Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing
  - 仿真预训练世界模型作为有偏先验，<1 h 实车数据适应
- **FADA** · 2026 · CoRL 2026† · [arXiv 2606.28476](https://arxiv.org/abs/2606.28476) · [项目](https://lecar-lab.github.io/FADA-humanoid)
  - FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control
  - 只用约 2 min 目标数据微调逆动力学模块；适应的是控制器而非仿真器

HumanoidNDM（§5）也属于本节：真机数据训练的神经动力学模型 + 经模型反传梯度微调策略。

## 11. SuperMimic 非官方复现

以下均为 GitHub / Hugging Face 仓库，不是论文；数字为仓库作者自报。截至 2026-10-30，arXiv 上尚无引用 SuperMimic 的论文。

- [github.com/zita-ch/supermimic_vibed](https://github.com/zita-ch/supermimic_vibed)
  - 复现范围：仅 LAFAN1 40 段实验（论文 Fig. 4a），Isaac Lab 3 + Newton/MuJoCo-Warp；README 自述用 AI 编码助手 1 小时写成，未经审查
  - 自报结果：1 × RTX PRO 6000 上 1.47 GPU-h，回报 0.829，0/40 失败；关闭自碰撞、bf16、奖励与终止头用解析式
- [huggingface.co/kevinhenryz/realmimic](https://huggingface.co/kevinhenryz/realmimic)
  - 复现范围：129,491 条 BONES-SEED，1 × RTX 4090 从头训练 10.5 h；仅仿真
  - 自报结果：自有评测器 10 个失败、得分 0.9545，SONIC 发布版 218 个失败、0.875；页面自述 20 个以内的失败差异属于噪声
- [github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real)
  - 复现范围：基于 CuboiLeo/SuperMimic-Reproduced
  - 自报结果：LAFAN1 严格设置 0.56（论文 0.82）；BONES-SEED 0.93、约 13 万条中 46 个失败（论文 25）；真机 G1 舞蹈两次成功（系松安全绳），此前 9 个模型失败
- [github.com/YHFone/supermimic-mjlab](https://github.com/YHFone/supermimic-mjlab)
  - 复现范围：LAFAN1 40 段，无域随机化评测
  - 自报结果：40/40 成功，回报 0.895

## 补充（已核实，只列编号）

MuscleVAE (2312.07340, SIGGRAPH Asia 2023)，SVG (1510.09142, NIPS 2015)，MBPO (NeurIPS 2019)，Newt (2511.19584)，TD-M(PC)² (2502.03550, L4DC 2026)，SPI-Active (2505.14266, CoRL 2025)，APG (2209.13052, ICRA 2023)，Learning More With Less (2501.10499)，MimicAll (2610.33508，跨 16 个人形家族共享的跟踪器)
