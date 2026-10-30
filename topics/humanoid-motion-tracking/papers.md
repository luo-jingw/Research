# humanoid-motion-tracking 论文目录

- 快照日期：2026-10-30
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：已确认的发表处；"arXiv" 表示检索时未找到发表处。标 † 的条目发表处只来自引用或二手页面，见根目录 `issues.md` → ISSUE-002。
- 每条的标题、年份、arXiv 编号均经 arXiv 页面、arXiv API 或论文集核实。
- "机器人"列：✓ 表示有真机部署。
- 分节对应 [survey.md](survey.md) 的分类。

## 1. 图形学根源

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| DeepMimic | DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills | 2018 | ACM TOG 37(4), SIGGRAPH 2018 | 1804.02717 | — | 模仿奖励 + 任务目标，每段动作一个 PPO 专家 |
| NPMP | Neural Probabilistic Motor Primitives for Humanoid Control | 2018 | ICLR 2019 | 1811.11711 | — | 把多个专家蒸馏进一个可复用的潜空间运动策略 |
| AMP | AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control | 2021 | ACM TOG 40(4), SIGGRAPH 2021 | 2104.02180 | — | 对抗式运动先验替代跟踪奖励 |
| PHC | Perpetual Humanoid Control for Real-time Simulated Avatars | 2023 | ICCV 2023 | 2305.06456 | zhengyiluo.github.io/PHC | 一个跟踪器模仿 98.9% 的 AMASS，带摔倒恢复 |
| PULSE | Universal Humanoid Motion Representations for Physics-Based Control | 2023 | ICLR 2024 Spotlight | 2310.04582 | github.com/ZhengyiLuo/PULSE | PHC → DAgger 蒸馏进 VAE 潜空间 → 下游 PPO |
| MaskedMimic | MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | 2024 | ACM TOG 43(6), SIGGRAPH Asia 2024 | 2409.14393 | research.nvidia.com/labs/par/maskedmimic | 把控制看作从部分目标做动作补全 |

## 2. 真机动作跟踪：2024

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 机器人 | 一句话 |
|---|---|---|---|---|---|---|---|
| H2O | Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation | 2024 | IROS 2024† | 2403.04436 | human2humanoid.com | H1 ✓ | SMPL 形状拟合重定向 + 特权模仿器做 "sim-to-data" 过滤，RGB 全身遥操作 |
| OmniH2O | OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning | 2024 | CoRL 2024† | 2406.08858 | omni.human2humanoid.com | H1 ✓ | 特权教师 → 稀疏输入学生；运动学位姿作为 VR、RGB、自主控制的统一接口 |
| HumanPlus | HumanPlus: Humanoid Shadowing and Imitation from Humans | 2024 | CoRL 2024† | 2406.10454 | humanoid-ai.github.io | H1 ✓ | RGB 影随采集数据，再学习自主技能 |
| ExBody | Expressive Whole-Body Control for Humanoid Robots | 2024 | RSS 2024† | 2402.16796 | expressive-humanoid.github.io | H1 ✓ | 上身模仿动作，腿部只跟踪根速度 |
| ExBody2 | ExBody2: Advanced Expressive Humanoid Whole-Body Control | 2024 | arXiv | 2412.13196 | exbody2.github.io | G1 ✓ | 速度跟踪与关键点跟踪分离；教师过滤不可行数据 |
| HOVER | HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots | 2024 | ICRA 2025 | 2410.21229 | hover-versatile-humanoid.github.io | H1 ✓ | 一个掩码多模式学生覆盖运动学、关节、根指令模式 |

## 3. 真机动作跟踪：2025 的分化

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 机器人 | 一句话 |
|---|---|---|---|---|---|---|---|
| ASAP | ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | 2025 | RSS 2025 | 2502.01143 | agile.human2humanoid.com | G1 ✓ | 每动作 PPO 专家 → 用真机数据学残差动作模型 → 在修正仿真中微调 |
| KungfuBot | KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills | 2025 | NeurIPS 2025 | 2506.12851 | kungfubot.github.io | G1 ✓ | 双层自适应跟踪容差课程，学功夫与舞蹈 |
| VideoMimic | Visual Imitation Enables Contextual Humanoid Control | 2025 | CoRL 2025 | 2505.03729 | videomimic.net | G1 ✓ | 单目 4D 人 + 场景重建 → 跟踪 → 蒸馏为本体 + 高度图策略，上楼梯、坐下 |
| TWIST | TWIST: Teleoperated Whole-Body Imitation System | 2025 | CoRL 2025† | 2505.02833 | humanoid-teleop.github.io | G1 ✓ | 特权教师（看未来帧）→ RL + BC 学生，动捕全身遥操作 |
| GMT | GMT: General Motion Tracking for Humanoid Whole-Body Control | 2025 | arXiv | 2506.14770 | gmt-humanoid.github.io | G1 ✓ | 自适应采样 + 动作混合专家，教师 → 学生 |
| BumbleBee | From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots | 2025 | arXiv | 2506.12779 | beingbeyond.github.io/BumbleBee | G1 ✓ | 聚类专家用真机残差动作精化后蒸馏为通用策略 |
| UniTracker | UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots | 2025 | IEEE RA-L 2026† | 2507.07356 | yinkangning0124.github.io/Humanoid-UniTracker | G1 ✓ | 部分观测先验对齐全观测编码器的 CVAE 学生 |
| BeyondMimic | BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion | 2025 | Science Robotics 2026† | 2508.08241 | beyondmimic.github.io | G1 ✓ | 统一 MDP 与超参数的每动作 PPO 配方 → 潜状态–动作扩散 → classifier guidance 做新任务 |
| Any2Track | Track Any Motions under Any Disturbances | 2025 | arXiv | 2509.13833 | zzk273.github.io/Any2Track | G1 ✓ | 通用跟踪器上加基于历史的在线动力学适应 |

## 4. 规模化与基础模型：2025–2026

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 机器人 | 一句话 |
|---|---|---|---|---|---|---|---|
| SONIC | SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control | 2025 | Science Robotics 2026† | 2511.07820 | nvlabs.github.io/GEAR-SONIC | G1 ✓ | 单个通用 PPO，611 h 数据、1.2M→42M 参数、128 GPU × 7 天；FSQ token 接口连接规划器、VR、VLA |
| BFM-Zero | BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised RL | 2025 | ICLR 2026 | 2511.04131 | — | G1 ✓ | 对照路线：Forward-Backward 无监督 RL，一个潜空间统一动作、目标与奖励 |
| OmniXtreme | OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control | 2026 | arXiv | 2602.23843 | extreme-humanoid.github.io | G1 ✓ | 专家教师 → flow matching 学生 → 执行器感知的 RL 精化 |
| HoloMotion-1 | HoloMotion-1 Technical Report | 2026 | arXiv 技术报告 | 2605.15336 | github.com/HorizonRobotics/HoloMotion | G1 ✓ | >2000 h 以视频为主的数据，稀疏 MoE Transformer 直接用 PPO 训练 |
| Humanoid-GPT | Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking | 2026 | CVPR 2026 | 2606.03985 | github.com/GalaxyGeneralRobotics/Humanoid-GPT | G1 ✓ | 约 300 个聚类专家 → 并行 DAgger 蒸馏进因果 GPT，20 亿帧 |
| SuperMimic | SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model | 2026 | CoRL 2026 Oral | 2610.28480 | supermimic.github.io | G1 ✓ | 拟合仿真转移的可微世界模型 + BPTT，1 H100 × 3 h 超过 SONIC；精读见 [notes/2026-supermimic.md](notes/2026-supermimic.md) |
| SONIC-K1 | SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU | 2026 | arXiv | 2610.39327 | kyry.me/sonic-k1 | Booster K1（部分） | 在单张共享 GPU 上把 SONIC 配方移植到小型人形 |

## 5. 接口、交互与非平地：2025–2026

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 机器人 | 一句话 |
|---|---|---|---|---|---|---|---|
| HDMI | HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos | 2025 | arXiv | 2509.16757 | hdmi-humanoid.github.io | G1 ✓ | 从视频同时跟踪机器人与物体，交互奖励；部署需动捕物体位姿 |
| ResMimic | ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning | 2025 | arXiv | 2510.05070 | resmimic.github.io | G1 ✓ | 冻结通用跟踪器 + 残差 PPO，加入物体感知 |
| TWIST2 | TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System | 2025 | arXiv | 2511.02832 | yanjieze.com/TWIST2 | G1 ✓ | 免动捕 VR 全身遥操作，15 min 采 100 条示教 |
| LATENT | Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data | 2026 | IROS 2026† | 2603.12686 | zzk273.github.io/LATENT | G1 ✓ | PPO 跟踪器 → DAgger 潜空间 → 带潜动作屏障的高层 PPO，打网球对拉 |
| SceneBot | SceneBot: Contact-Prompted General Humanoid Whole Body Tracking with Scene-Interaction | 2026 | arXiv | 2606.27581 | ericcsr.github.io/scenebot | G1 ✓ | 以逐连杆接触标签为条件消解场景交互歧义，搬箱上楼 |
| GigaBrain-WBC-0.5 | GigaBrain-WBC-0.5: A Behavior World Model for Robust Humanoid Whole-Body Tracking with Environment Interaction | 2026 | arXiv 技术报告 | 2608.18234 | shepherd1226.github.io/gigabrain-wbc-0.5 | G1 ✓ | 约 2,200 h 数据自动标注支撑几何；地形交互成功率 81.3%，摔倒恢复 99.3% |
| PGMT | PGMT: Perceptive General Motion Tracking for Humanoid Robots | 2026 | arXiv | 2609.08511 | luyili.github.io/pgmt | G1 ✓ | 跟踪与恢复先验 + 地形感知，越过最高 37 cm 障碍 |
| HumanoidNDM | HumanoidNDM: Closing the Training-Deployment Gap of Motion Tracking via Humanoid Neural Dynamics Model | 2026 | CoRL 2026 | 2610.34126 | — | G1 ✓ | 真机数据训练神经动力学模型，策略经模型反传梯度在线微调，免动捕 |
| METATRON | METATRON: A Promptable Whole-Body Execution Layer for Humanoids | 2026 | arXiv | 2610.38027 | research.nvidia.com/labs/par/projects/metatron | G1 ✓ | 4 个专家跟踪器蒸馏为冻结的提示条件基础策略，技能由编码智能体写成代码 |

## 6. 数据集与重定向

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| AMASS | AMASS: Archive of Motion Capture as Surface Shapes | 2019 | ICCV 2019 | 1904.03278 | — | 统一 SMPL 格式的动捕语料，PHC、H2O、GMT、TWIST 的默认数据 |
| LAFAN1 | Robust Motion In-betweening | 2020 | SIGGRAPH 2020 | 2102.04942 | — | BeyondMimic、GMR、SuperMimic 使用其 G1 重定向版本（40 段，2.45 h） |
| BONES-SEED | BONES-SEED: Skeletal everyday embodiment dataset | 2026 | 数据集 | huggingface.co/datasets/bones-studio/seed | 同左 | SONIC 训练数据的公开部分，142,220 条序列、288 h；SuperMimic 过滤为 129,514 条、264.56 h |
| PHUMA | PHUMA: Physically Reliable Humanoid Locomotion Dataset | 2025 | CoRL 2026† | 2510.26236 | davian-robotics.github.io/PHUMA | 73 h 动捕 + 视频，经物理筛选 |
| GMR | Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking | 2025 | ICRA 2026† | 2510.02252 | github.com/YanjieZe/GMR | 重定向伪影比奖励调参更限制跟踪鲁棒性；SONIC 数据使用的重定向器之一 |
| OmniRetarget | OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction | 2025 | arXiv | 2509.26633 | omniretarget.github.io | 交互网格 Laplacian 重定向保持接触，支持数据增广 |

## 7. 可微学习代理模型：角色与人形

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| SuperTrack | SuperTrack: Motion Tracking for Physically Simulated Characters using Supervised Learning | 2021 | ACM TOG 40(6), SIGGRAPH Asia 2021 | 无 arXiv | theorangeduck.com/page/supertrack-motion-tracking-physically-simulated-characters-using-supervised-learning | 8 帧窗口拟合世界模型，32 帧窗口反传跟踪损失，无 critic |
| ControlVAE | ControlVAE: Model-Based Learning of Generative Controllers for Physics-Based Characters | 2022 | ACM TOG 41(6), SIGGRAPH Asia 2022 | 2210.06063 | — | 世界模型、技能潜空间与生成式控制器联合学习 |
| DiffMimic | DiffMimic: Efficient Motion Mimicking with Differentiable Physics | 2023 | ICLR 2023 | 2304.03274 | diffmimic.github.io | 真可微仿真器上做模仿，Demonstration Replay 稳定长视界反传 |
| MoConVQ | MoConVQ: Unified Physics-Based Motion Control via Scalable Discrete Representations | 2023 | ACM TOG 43(4), SIGGRAPH 2024 | 2310.10198 | moconvq.github.io | MBRL 学习 VQ-VAE 运动 token，数十小时动作数据 |
| SuperDyno | Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics | 2025 | ICLR 2025 Workshop on World Models | openreview.net/forum?id=FPgKt7bA8w | — | 中等规模神经动力学模型作为可微仿真器，扩展到数万段动作 |

## 8. 可微仿真策略学习

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| Suh et al. | Do Differentiable Simulators Give Better Policy Gradients? | 2022 | ICML 2022 | 2202.00817 | — | 刚性与不连续使一阶梯度可能比零阶更差（偏差–方差分析） |
| SHAC | Accelerated Policy Learning with Parallel Differentiable Simulation | 2022 | ICLR 2022 | 2204.07137 | github.com/NVlabs/DiffRL | 短视界截断 BPTT + 平滑 critic 自举 |
| AHAC | Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation | 2024 | ICML 2024 | 2405.17784 | github.com/imgeorgiev/DiffRL | 自适应截断视界，在刚性接触前停止 |
| Song et al. | Learning Quadruped Locomotion Using Differentiable Simulation | 2024 | CoRL 2024 Oral | 2403.14864 | — | IsaacGym 前向 + 可微单刚体代理反向，Mini Cheetah 零样本上真机 |
| Schwarke et al. | Learning Deployable Locomotion Control via Differentiable Simulation | 2024 | CoRL 2025 | 2404.02887 | — | 用穿透深度的 sigmoid 平滑硬接触，ANYmal D 零样本上真机 |
| SAPO | Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation | 2024 | ICLR 2025 Spotlight | 2412.12089 | rewarped.github.io | 熵正则随机策略用解析梯度训练，含可变形物体 |
| Back to Newton's Laws | Back to Newton's Laws: Learning Vision-based Agile Flight via Differentiable Physics | 2024 | Nature Machine Intelligence 2025 | 2407.10648 | — | 极简可微质点模型 + 深度渲染训练视觉飞行，零样本上真机 |

## 9. 世界模型用于机器人策略优化

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| MAAC | Model-Augmented Actor-Critic: Backpropagating through Paths | 2020 | ICLR 2020 | 2005.08068 | — | 学习模型上 H 步路径梯度 + 终端 Q |
| Dreamer | Dream to Control: Learning Behaviors by Latent Imagination | 2019 | ICLR 2020 | 1912.01603 | — | 通过潜空间想象反传价值梯度训练 actor |
| DreamerV3 | Mastering Diverse Domains through World Models | 2023 | Nature 2025 | 2301.04104 | danijar.com/dreamerv3 | 连续动作也改用 REINFORCE，一套固定配置 |
| DayDreamer | DayDreamer: World Models for Physical Robot Learning | 2022 | CoRL 2022 | 2206.14176 | danijar.com/daydreamer | 直接在实体机器人上训练 Dreamer，无仿真器 |
| TD-MPC2 | TD-MPC2: Scalable, Robust World Models for Continuous Control | 2023 | ICLR 2024 Spotlight | 2310.16828 | tdmpc2.com | 潜空间世界模型做短视界规划 + 终端价值 |
| Puppeteer | Hierarchical World Models as Visual Whole-Body Humanoid Controllers | 2024 | ICLR 2025 | 2405.18418 | nicklashansen.com/rlpuppeteer | 高层视觉世界模型指挥低层跟踪世界模型，56 自由度仿真人形 |
| PWM | PWM: Policy Learning with Multi-Task World Models | 2024 | ICLR 2025 | 2407.02466 | imgeorgiev.com/pwm | 正则化世界模型比真实接触动力学更平滑，有利于一阶梯度 |
| RWM | Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics | 2025 | NeurIPS 2025 EWM Workshop | 2501.10100 | github.com/leggedrobotics/robotic_world_model | 长视界神经仿真器 + 模型内 PPO；报告 SHAC 经同一世界模型不收敛 |
| QWM | Morphology-Conditioned World Model for Cross-Embodiment Quadrupedal Locomotion | 2026 | CoRL 2026† | 2604.08780 | github.com/modanesh/QWM | 形态条件潜动力学，零样本迁移到未见四足 |

## 10. 在真实数据上拟合动力学

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| FOWM | Finetuning Offline World Models in the Real World | 2023 | CoRL 2023 Oral | 2310.16029 | yunhaifeng.com/FOWM | 离线真实数据世界模型在线微调，规划时权衡回报与认知不确定性 |
| RWM-U | Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots | 2025 | ICLR 2026 World Models Workshop | 2504.16680 | github.com/leggedrobotics/robotic_world_model_lite | 仿真 + 约 1 h 真实转移，集成不确定性惩罚的模型内 PPO；真实数据过多反而变差 |
| NeRD | Neural Robot Dynamics | 2025 | CoRL 2025 | 2508.15755 | github.com/NVlabs/neural-robot-dynamics | 神经求解器可用真实数据微调，抛方块位置误差 0.036 → 0.018 m |
| PIN-WM | PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation | 2025 | RSS 2025 | 2504.16693 | — | 少量真实视频 + 高斯渲染损失端到端辨识可微物理参数 |
| Ishihara et al. | Hierarchical Learning Framework for Whole-Body Model Predictive Control of a Real Humanoid Robot | 2024 | arXiv | 2409.08488 | — | 解析模型 + 真机上学习的残差动力学，用于全身 MPC |
| PIA | Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing | 2026 | arXiv | 2610.26757 | toyotaresearchinstitute.github.io/pia-mbrl | 仿真预训练世界模型作为有偏先验，<1 h 实车数据适应 |
| FADA | FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control | 2026 | CoRL 2026† | 2606.28476 | lecar-lab.github.io/FADA-humanoid | 只用约 2 min 目标数据微调逆动力学模块；适应的是控制器而非仿真器 |

HumanoidNDM（§5）也属于本节：真机数据训练的神经动力学模型 + 经模型反传梯度微调策略。

## 11. SuperMimic 非官方复现

以下均为 GitHub / Hugging Face 仓库，不是论文；数字为仓库作者自报。截至 2026-10-30，arXiv 上尚无引用 SuperMimic 的论文。

| 仓库 | 复现范围 | 自报结果 |
|---|---|---|
| github.com/zita-ch/supermimic_vibed | 仅 LAFAN1 40 段实验（论文 Fig. 4a），Isaac Lab 3 + Newton/MuJoCo-Warp；README 自述用 AI 编码助手 1 小时写成，未经审查 | 1 × RTX PRO 6000 上 1.47 GPU-h，回报 0.829，0/40 失败；关闭自碰撞、bf16、奖励与终止头用解析式 |
| huggingface.co/kevinhenryz/realmimic | 129,491 条 BONES-SEED，1 × RTX 4090 从头训练 10.5 h；仅仿真 | 自有评测器 10 个失败、得分 0.9545，SONIC 发布版 218 个失败、0.875；页面自述 20 个以内的失败差异属于噪声 |
| github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real | 基于 CuboiLeo/SuperMimic-Reproduced | LAFAN1 严格设置 0.56（论文 0.82）；BONES-SEED 0.93、约 13 万条中 46 个失败（论文 25）；真机 G1 舞蹈两次成功（系松安全绳），此前 9 个模型失败 |
| github.com/YHFone/supermimic-mjlab | LAFAN1 40 段，无域随机化评测 | 40/40 成功，回报 0.895 |

## 补充（已核实，未列入主表）

MuscleVAE (2312.07340, SIGGRAPH Asia 2023)，SVG (1510.09142, NIPS 2015)，MBPO (NeurIPS 2019)，Newt (2511.19584)，TD-M(PC)² (2502.03550, L4DC 2026)，SPI-Active (2505.14266, CoRL 2025)，APG (2209.13052, ICRA 2023)，Learning More With Less (2501.10499)，MimicAll (2610.33508，跨 16 个人形家族共享的跟踪器)
