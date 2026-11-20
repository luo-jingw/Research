# vla-wam-robustness 论文目录

- 快照日期：2026-11-20
- 年份：arXiv v1 的年份。没有 arXiv 版本的条目，取页面或会议的年份。
- 会议/期刊：只取 arXiv comment 字段，或会议论文集、会议官网的论文页。
  - "预印本"表示这些来源里没有发表处，包括 comment 只写 "Under review"、只有页数或只有项目页的情况。
  - 标 † 的发表处没能在一手页面完整确认，例如只见于会议虚拟会场页，或 comment 没写年份。见根目录 `issues.md` → ISSUE-007。
  - 没有论文的模型写"官方页面"。
- 标题、年份、arXiv 编号来自 arxiv.org 的 abs、HTML 或 listing 页面。标"仅核实摘要"的条目没有读正文。
- 有几条的发表处与其他方向 `papers.md` 不一致：π0、π0.5、OpenVLA、OpenVLA-OFT、UVA、RDT-1B、LIBERO-Plus。本目录按上面的口径填写，差异记在 ISSUE-007。
- 分节对应 [survey.md](survey.md)，一篇论文只列在主归属的那一节。只在别人表格中出现、arXiv 编号没有核实的方法不列入，记在 ISSUE-007。

## 1. 扰动基准

- **LIBERO-Plus** · 2025 · CVPR 2026† · [arXiv 2510.13626](https://arxiv.org/abs/2510.13626) · [项目](https://sylvestf.github.io/LIBERO-plus) · [代码](https://github.com/sylvestf/LIBERO-plus)
  - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
  - 由 40 个 LIBERO 任务生成 10,030 个任务，覆盖 7 个扰动维度；相机和机器人初始状态伤害最大，语言扰动降幅小，是因为模型很少用语言。会议版标题为 "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models"
- **LIBERO-PRO** · 2025 · 预印本 · [arXiv 2510.03827](https://arxiv.org/abs/2510.03827) · [代码](https://github.com/Zxy-MLlab/LIBERO-PRO)
  - LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization
  - 替换物体、初始位置、指令和环境，说明 LIBERO 上 90% 以上的分数主要来自记住的轨迹和布局；没有相机维度，也没有传感器噪声维度
- **VLA-Arena** · 2025 · 预印本 · [arXiv 2512.22539](https://arxiv.org/abs/2512.22539) · [项目](https://vla-arena.github.io)
  - VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models
  - 视觉扰动按光照、物体颜色、相机、噪声逐级叠加，平均降幅从 13.5% 升到 50.5%；真机上先加光照、再加相机，成功率 60.0 → 37.0 → 20.0
- **Colosseum V2** · 2026 · RA-L · [arXiv 2605.27759](https://arxiv.org/abs/2605.27759)
  - Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models
  - 11 种视觉扰动、4 种语言扰动、3 种动作扰动；π0.5 在视觉扰动下平均降 7.7–9.9%，ACT 降约 29%，但 π0.5 对语言改写更敏感
- **COLOSSEUM** · 2024 · RSS 2024 · [arXiv 2402.08191](https://arxiv.org/abs/2402.08191) · [项目](https://robot-colosseum.github.io)
  - THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation
  - 14 个扰动轴；单一因素下成功率降 30–50%，组合扰动下至少降 75%；3D 模型（RVT、PerAct）对相机位姿鲁棒
- **Factor World** · 2023 · 预印本 · [arXiv 2307.03659](https://arxiv.org/abs/2307.03659) · [项目](https://sites.google.com/view/generalization-gap)
  - Decomposing the Generalization Gap in Imitation Learning for Visual Robotic Manipulation
  - 按难度给 11 个变化因素排序；真机 RT-1 上相机位置最难，只有 45.8
- **VLATest** · 2024 · FSE 2025 · [arXiv 2409.12894](https://arxiv.org/abs/2409.12894)
  - VLATest: Testing and Evaluating Vision-Language-Action Models for Robotic Manipulation
  - 相机每轴旋转 ±5°、平移不超过 5 cm 后，原来成功的案例只剩 34.0%；光照增强比减弱更伤
- **Eva-VLA** · 2025 · 预印本 · [arXiv 2509.18953](https://arxiv.org/abs/2509.18953)
  - Eva-VLA: Evaluating Vision-Language-Action Models' Robustness Under Real-World Physical Variations
  - 测物体 3D 旋转、点光源、对抗贴片三类扰动，分随机采样和 CMA-ES 最坏情况搜索两种；最坏情况下的 3D 物体变换伤害最大
- **RoboTwin 2.0** · 2025 · 预印本 · [arXiv 2506.18088](https://arxiv.org/abs/2506.18088)
  - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation
  - 强域随机化的双臂基准；只用 50 条干净示教训练时，在 Hard 设置下非预训练模型接近 0，π0 从 46.4 降到 16.3
- **INT-ACT** · 2025 · 预印本 · [arXiv 2506.09930](https://arxiv.org/abs/2506.09930) · [项目](https://ai4ce.github.io/INT-ACT/)
  - From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models
  - 用 50 个任务探测 OOD 物体、语言和干扰物下的表现：意图往往正确，但执行失败；SimplerEnv 的绿幕合成做不了光照和相机扰动，所以没有测这两类

## 2. WAM 与 VLA 的鲁棒性比较

- **WAM-vs-VLA** · 2026 · 预印本 · [arXiv 2603.22078](https://arxiv.org/abs/2603.22078) · [项目](https://robot-robustness.github.io/RoboTwin2.0-Plus/)
  - Do World Action Models Generalize Better than VLAs? A Robustness Study
  - 在 LIBERO-Plus 和自建的 RoboTwin 2.0-Plus 上比较 4 个 WAM 与十余个 VLA；结论是视频先验 "necessary but not sufficient"，相机和机器人初始状态对 WAM 仍然难
- **JAM** · 2026 · 预印本 · [arXiv 2610.37219](https://arxiv.org/abs/2610.37219)
  - Vision-Language-Action or World-Action? Just Action Models
  - 在 LIBERO-Plus 的 1,506 任务子集上对照骨干与训练目标；以视频生成器 Wan 为骨干的策略，无论训练目标是什么，Camera 都只有约 25
- **ZimaBlue** · 2026 · 预印本 · [arXiv 2609.00188](https://arxiv.org/abs/2609.00188)
  - ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training
  - 视频预训练的 WAM；LIBERO-Plus 零样本平均 86.7，其中 Camera 只有 58.1，作者称相机视角变化是关键瓶颈
- **Phoenix** · 2026 · 预印本 · [arXiv 2611.24938](https://arxiv.org/abs/2611.24938)
  - Phoenix: Learning Scene Structure Representations for Generalizable World-Action Models
  - 学习场景结构表征的 WAM；Table 1 汇总了 13 个 VLA 与 WAM 在 LIBERO-Plus 和 RoboTwin 2.0 Clean2Random 上的数字

## 3. "为什么不鲁棒"的分析

- **Shortcut-OXE** · 2025 · CoRL 2025 · [arXiv 2508.06426](https://arxiv.org/abs/2508.06426) · [项目](https://lucky-light-sun.github.io/proj/shortcut-learning-in-grps/)
  - Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation
  - 子数据集内部多样性低、子数据集之间差异大，都会诱发捷径；策略会把视角和动作绑在一起
- **Blackout-Freeze** · 2026 · 预印本 · [arXiv 2609.39145](https://arxiv.org/abs/2609.39145)
  - Blackout vs. Freeze: Analyzing Physical Failure Modes of VLAs under Camera Faults
  - 在场景相机或腕部相机上施加置黑和冻结两种故障；冻结比置黑更伤，把注意力重加权到本体感知也救不回来
- **VLA-Trace** · 2026 · 预印本 · [arXiv 2605.30117](https://arxiv.org/abs/2605.30117)
  - VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing
  - 用 CKA、注意力 knockout 和 patch 遮挡做诊断，发现 π0.5 主要依赖一条集中的视觉到动作通路；没有研究相机和光照

## 4. FTM 谱系：冻结或少参数的视觉域适应

### 4.1 改视觉 token 或编码器的少参数适应

- **FTM** · 2025 · CVPR 2026 · [arXiv 2512.02902](https://arxiv.org/abs/2512.02902)
  - VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling
  - 锚点论文：冻结 π0.5，只对视觉 token 做逐通道仿射（FTM，约 4K 参数），或给 SigLIP 加 LoRA（FLA，4.7M 参数），每个任务用一条新视角演示；精读见 [notes/2025-ftm.md](notes/2025-ftm.md)
- **WARP-VLA** · 2026 · 预印本 · [arXiv 2610.11508](https://arxiv.org/abs/2610.11508)
  - WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models
  - 编码器和策略都冻结，在两者之间加一个 MoE 特征变换，处理腕部相机的安装偏移
- **StableVLA** · 2026 · ICML 2026 · [arXiv 2605.18287](https://arxiv.org/abs/2605.18287) · [项目](https://dagroup-pku.github.io/StableVLA)
  - StableVLA: Towards Robust Vision-Language-Action Models without Extra Data
  - 在视觉到 LLM 的投影处加信息瓶颈适配器（小于 10M 参数），训练期使用，过滤 ImageNet-C 类腐蚀带来的视觉噪声
- **Not All Layers** · 2026 · 预印本 · [arXiv 2609.18084](https://arxiv.org/abs/2609.18084)
  - Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models
  - 先用 10 张无标注的目标观测诊断哪一层该调，再按区域分配 LoRA rank；外观漂移的适应代价在五个架构上都集中在视觉编码器
- **VLA-Retain** · 2026 · 预印本 · [arXiv 2610.27698](https://arxiv.org/abs/2610.27698)
  - VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs
  - 在相机或噪声子集上调视觉骨干与 connector 后，10 个配置中有 8 个在非目标扰动维度上平均变差
- **T3R** · 2026 · 预印本 · [arXiv 2611.08413](https://arxiv.org/abs/2611.08413)
  - T3R: Training-Free Two-Stage Token Refinement
  - 免训练的视觉 token 剪枝加注意力偏置（仅核实摘要）
- **CAPO** · 2026 · 预印本 · [arXiv 2602.01040](https://arxiv.org/abs/2602.01040)
  - Learning Adaptive Cross-Embodiment Visuomotor Policy with Contrastive Prompt Orchestration
  - 不是 VLA：在 CLIP 加 RL 策略上，用可学习的提示池表示光照、视场、旋转等域因素，编码器不微调（仅核实摘要）

### 4.2 在图像一侧变回训练视角，或复原画面

- **AnyCamVLA** · 2026 · IROS 2026 · [arXiv 2603.05868](https://arxiv.org/abs/2603.05868) · [项目](https://heo0224.github.io/AnyCamVLA)
  - AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models
  - 用前馈新视角合成模型 LVSM 把测试画面重渲染成训练相机的视角，策略冻结；需要已知测试相机和训练相机的内外参
- **GS-VLA** · 2026 · 预印本 · [arXiv 2608.19066](https://arxiv.org/abs/2608.19066)
  - GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting
  - 在冻结策略前挂一个 4.05M 参数的 U-Net，预测逐像素 3D 高斯并渲染到规范视角；需要度量深度
- **Homeward** · 2026 · 预印本 · [arXiv 2611.24455](https://arxiv.org/abs/2611.24455)
  - Homeward: No Place Like the Training View
  - 不需要训练：场景部分用 VGGT 估计的几何恢复，机械臂按 URDF 和关节角渲染，再合成回训练视角
- **CoRe-VLA** · 2026 · 预印本 · [arXiv 2609.37150](https://arxiv.org/abs/2609.37150)
  - CoRe-VLA: Preserving Cross-View Coordination in VLAs under Camera Shifts
  - 把 RGB-D 点云渲染到训练位姿，用 NAFNet 修补，并在推理端对齐动作块，让恢复后的外部视图与腕部视图重新协调
- **WACO** · 2026 · 预印本 · [arXiv 2611.24360](https://arxiv.org/abs/2611.24360) · [项目](https://peacelwh.github.io/WACO)
  - Towards Pose-Robust Few-Shot Vision-Language-Action Models
  - 以机械臂为标定靶估计相机和基座的位移，变形第三人称图像，并规范化状态与动作的坐标系；π0.5 需要全参微调
- **VistaBot** · 2026 · ICRA 2026 · [arXiv 2604.21914](https://arxiv.org/abs/2604.21914)
  - VistaBot: View-Robust Robot Manipulation via Spatiotemporal-Aware View Synthesis
  - 结合 4D 几何和视频扩散做视角合成，把得到的潜变量喂给策略；摘要称测试时不需要标定（仅核实摘要）
- **CRT** · 2026 · 预印本 · [arXiv 2602.01158](https://arxiv.org/abs/2602.01158)
  - Improving Robustness of Vision-Language-Action Models by Restoring Corrupted Visual Inputs
  - 在策略前放一个 Transformer 图像复原网络，用干净 / 腐蚀成对帧训练；对 π0.5 有效，但会伤害 SmolVLA 在干净画面上的性能

### 4.3 训练时让策略对相机鲁棒

- **Adapt3R** · 2025 · 预印本 · [arXiv 2503.04877](https://arxiv.org/abs/2503.04877) · [项目](https://pairlab.github.io/Adapt3R)
  - Adapt3R: Adaptive 3D Scene Representation for Domain Transfer in Imitation Learning
  - 用标定 RGB-D 点云加 2D 语义特征作为观测表示，需要重训整个策略；FTM 所用视角协议的来源
- **GeoAware-VLA** · 2025 · 预印本 · [arXiv 2509.14117](https://arxiv.org/abs/2509.14117) · [项目](https://alisharey.github.io/GeoAware-VLA)
  - GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model
  - 用冻结的 VGGT 加可训练投影替换 2D 编码器，在 BAKU、VQ-BeT 等轻量策略上重训
- **Cross-View AC** · 2026 · 预印本 · [arXiv 2608.06965](https://arxiv.org/abs/2608.06965)
  - Cross-View Action Consistency for Camera-Robust Vision-Language-Action Policies
  - 用同一仿真状态重渲染的视角对，约束两个视角下的动作流速度场一致；训练时全程遮蔽腕部相机
- **SCVC** · 2026 · 预印本 · [arXiv 2608.21402](https://arxiv.org/abs/2608.21402)
  - Selective Cross-View Consistency for World Action Models: Held-Out Viewpoint Robustness Without Test-Time Camera Information
  - 在 Cosmos Policy 上只对动作、未来本体状态、价值这些视角不变的块加一致性；§VI-B 另有一节 LIBERO-Plus 腕部相机审计
- **KYC** · 2025 · 预印本 · [arXiv 2510.02268](https://arxiv.org/abs/2510.02268) · [项目](https://ripl.github.io/know_your_camera)
  - Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning
  - 把 Plücker 射线图作为输入条件，显式告诉策略相机外参，以去掉背景捷径
- **CamVLA** · 2026 · 预印本 · [arXiv 2607.05396](https://arxiv.org/abs/2607.05396)
  - From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model
  - 动作头输出相机坐标系下的动作和手眼矩阵，让策略自己估计相机位置
- **VISTA** · 2024 · CoRL 2024 · [arXiv 2409.03685](https://arxiv.org/abs/2409.03685) · [项目](https://s-tian.github.io/projects/vista)
  - View-Invariant Policy Learning via Zero-Shot Novel View Synthesis
  - 用单图新视角合成做数据增广，训练视角不变的策略
- **InfiNoVA** · 2026 · 预印本 · [arXiv 2609.27734](https://arxiv.org/abs/2609.27734)
  - InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies
  - 用 4D 高斯渲染稠密的新视角做增广；摘要称真机未见视角下的平均成功率是 VISTA 增广的 5.4×（仅核实摘要；标题写法见 ISSUE-007）
- **PAIR** · 2026 · 预印本 · [arXiv 2611.11798](https://arxiv.org/abs/2611.11798)
  - PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation
  - 训练时的视角鲁棒表示（仅核实摘要）
- **OVOA-VLA** · 2026 · 预印本 · [arXiv 2611.26161](https://arxiv.org/abs/2611.26161)
  - One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency
  - 在各视角自己的相机坐标系下监督动作（仅核实摘要）
- **VersaCamVLA** · 2026 · NeurIPS 2026 · [arXiv 2610.12451](https://arxiv.org/abs/2610.12451)
  - VersaCamVLA: Camera-Configurable VLA Policies for Robotic Manipulation
  - 把相机集合编码进场景 token（仅核实摘要；标题来自检索结果，见 ISSUE-007）
- **View Collapse** · 2026 · 预印本 · [arXiv 2609.33707](https://arxiv.org/abs/2609.33707)
  - Does Adversarial Training Improve Generalization in Multi-View VLAs? Revealing and Mitigating View Collapse
  - 研究多视角 VLA 的对抗训练与视角坍缩（仅核实摘要）
- **LIT** · 2026 · 预印本 · [arXiv 2609.12641](https://arxiv.org/abs/2609.12641)
  - Breaking the Vision-Action Shortcut: Latent Interface Training
  - 训练时打破视觉到动作的捷径（仅核实摘要）
- **RageVLA** · 2026 · 预印本 · [arXiv 2611.23517](https://arxiv.org/abs/2611.23517)
  - RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO
  - 用增广训练感知和动作，针对 LIBERO 上的鲁棒性（只核实了 listing 标题）

### 4.4 少样本或一次演示适应

- **DART** · 2026 · ECCV 2026 · [arXiv 2607.00666](https://arxiv.org/abs/2607.00666) · [项目](https://twkang43.github.io/projects/dart)
  - Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts
  - 用权重算术抽取域方向（目标域增量减源域增量，经 SVD 子空间过滤后加回）；在每场景一条演示的更严协议下独立复现了 FLA
- **VLA-ZO** · 2026 · 预印本 · [arXiv 2610.06271](https://arxiv.org/abs/2610.06271)
  - VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models
  - 只用前向传播的零阶优化更新动作专家的 q/v LoRA，内存开销控制在部署端可承受的范围内
- **Robotic Steering** · 2025 · 预印本 · [arXiv 2511.22697](https://arxiv.org/abs/2511.22697)
  - Mechanistic Finetuning of Vision-Language-Action Models via Few-Shot Demonstrations
  - 依据可解释性分析选出 20 个 LLM 注意力头做 LoRA，视觉编码器和动作专家冻结；只测了光照漂移
- **RAGu** · 2026 · 预印本 · [arXiv 2611.10894](https://arxiv.org/abs/2611.10894)
  - Zero-Shot VLA Adaptation with Retrieved Guidance
  - 检索 DROID 演示并做几何标定（仅核实摘要）

## 5. 无标签测试时适应

### 5.1 视觉控制策略上的经典 TTA

- **PAD** · 2020 · ICLR 2021 · [arXiv 2007.04309](https://arxiv.org/abs/2007.04309) · [项目](https://nicklashansen.github.io/PAD)
  - Self-Supervised Policy Adaptation during Deployment
  - 部署时只保留逆动力学等自监督目标，在线更新共享的卷积编码器
- **ILA** · 2021 · RSS 2022 · [arXiv 2112.08526](https://arxiv.org/abs/2112.08526) · [项目](https://invariance-through-latent-alignment.github.io)
  - Invariance Through Latent Alignment
  - 不用配对数据和奖励，用对抗式潜特征对齐加冻结的动力学一致性，把目标域潜特征拉回源分布；直接测了相机位姿
- **MoVie** · 2023 · NeurIPS 2023 · [arXiv 2307.00972](https://arxiv.org/abs/2307.00972) · [项目](https://yangsizhe.github.io/MoVie)
  - MoVie: Visual Model-Based Policy Adaptation for View Generalization
  - 在编码器里插入 STN，以冻结的潜动力学模型的预测损失为监督，适应相机视角变化
- **TEMPO** · 2026 · NeurIPS 2026 · [arXiv 2610.20318](https://arxiv.org/abs/2610.20318)
  - Efficient Test-Time Adaptation For Robot Policies
  - 以冻结的分布式 critic 作为无奖励的性能代理，在线更新运动控制的 actor；没有视觉漂移实验

### 5.2 VLA 上的无标签测试时训练

- **SALT** · 2026 · 预印本 · [arXiv 2610.07946](https://arxiv.org/abs/2610.07946)
  - Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution
  - 以上一动作块中还没执行的剩余段为目标，只更新动作专家交叉注意力 key 投影的奇异值尺度；针对模糊、雾等腐蚀，没有相机位姿漂移
- **T³VF** · 2026 · ICML 2026 Workshop（CATS） · [arXiv 2605.08215](https://arxiv.org/abs/2605.08215)
  - Test-Time Training for Visual Foresight Vision-Language-Action Models
  - 以"预测的未来图像"和"实际看到的未来观测"作为监督对，只更新 Mantis 的 query tokens；在 LIBERO-Plus 的 Camera 维度上给出了数字
- **VANE** · 2026 · 预印本 · [arXiv 2608.09448](https://arxiv.org/abs/2608.09448)
  - VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction
  - 预测冻结 V-JEPA 2 对未来观测的表征，只更新 latent-prompt bank；更新先在影子副本上做，有未来证据支持才提交，否则回滚
- **TTT-VLA** · 2026 · 预印本 · [arXiv 2606.03127](https://arxiv.org/abs/2606.03127)
  - TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models
  - 在 π0.5 上加状态定位代理专家，训练时同时优化动作目标和代理目标；测试时只更新 latent prompt，代理专家也要保留
- **Juno-TTT** · 2026 · 预印本 · [arXiv 2610.09940](https://arxiv.org/abs/2610.09940) · [项目](https://juno-policy.github.io)
  - Juno: Taming Predictive Latents for Vision-Language-Action Models
  - 先用全部部署转移做 JEPA 预测，无标签地适应世界模型；再用"已验证成功"的执行把策略对齐过去
- **TT-VLA** · 2026 · 预印本 · [arXiv 2601.06748](https://arxiv.org/abs/2601.06748)
  - On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning
  - 以预训练进度估计器给出的逐步进度差为稠密奖励，在单个 episode 内用 LoRA 做 RL
- **EVOLVE-VLA** · 2025 · 预印本 · [arXiv 2512.14666](https://arxiv.org/abs/2512.14666)
  - EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
  - 用学到的进度估计器代替真值奖励做测试时训练（仅核实摘要）
- **T²VLA** · 2026 · 预印本 · [arXiv 2606.29892](https://arxiv.org/abs/2606.29892)
  - Trust Your Instincts: Confidence-Driven Test-Time RL for Vision-Language-Action Models
  - 把高置信度轨迹当作伪专家，以轨迹级相似度为内在奖励做测试时 RL（仅核实摘要）
- **PDF** · 2026 · 预印本 · [arXiv 2604.18107](https://arxiv.org/abs/2604.18107) · [代码](https://github.com/zhoujiahuan1991/CVPR2026-PDF)
  - Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models
  - VLA 冻结，对输入增广后让动作 token 投票，另用回合级延迟反馈训练一个 9M 参数的扰动头
- **Dune** · 2026 · 预印本 · [arXiv 2611.25400](https://arxiv.org/abs/2611.25400)
  - Dune: A Zeroth-Order Optimizer with Time-Conditioned Historical Error Regression for VLA Test-Time Adaptation
  - 面向 VLA 测试时适应的零阶优化器；损失里用到目标动作，来源没写，所以无法确认是否无标签

### 5.3 冻结策略的推理期引导与选择

- **VLS** · 2026 · 预印本 · [arXiv 2602.03973](https://arxiv.org/abs/2602.03973) · [项目](https://vision-language-steering.github.io/webpage)
  - VLS: Steering Pretrained Robot Policies via Vision-Language Models
  - 用 VLM 写出的可微奖励，在每个去噪步对冻结的扩散或流策略做梯度引导
- **V-GPS** · 2024 · CoRL 2024 · [arXiv 2410.13816](https://arxiv.org/abs/2410.13816) · [项目](https://nakamotoo.github.io/V-GPS)
  - Steering Your Generalists: Improving Robotic Foundation Models via Value Guidance
  - 用离线 RL 训练的语言条件 Q 函数给多个通用策略的候选动作重新排序
- **RoboMonkey** · 2025 · 预印本 · [arXiv 2506.17811](https://arxiv.org/abs/2506.17811)
  - RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models
  - 测试时扩展采样，由 VLM 验证器挑选动作（仅核实摘要）
- **TACO** · 2025 · 预印本 · [arXiv 2512.02834](https://arxiv.org/abs/2512.02834)
  - Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach
  - 借离线 RL 的反探索思路，用伪计数估计器验证动作块（仅核实摘要）
- **Retrieve-then-Steer** · 2026 · 预印本 · [arXiv 2605.10094](https://arxiv.org/abs/2605.10094)
  - Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs
  - 把环境验证过的成功片段存入记忆，按状态检索后注入流采样的中间状态（仅核实摘要）
- **Infer-Diagnose-Refine** · 2026 · 预印本 · [arXiv 2607.25516](https://arxiv.org/abs/2607.25516)
  - A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models
  - 比较真实视觉输入与零填充视觉输入下的动作差，免训练地诊断视觉通道该占多大权重（仅核实摘要）
- **ShadowVLA** · 2026 · NeurIPS 2026 Workshop（8th Robot Learning Workshop） · 无 arXiv（neurips.cc 论文页，链接未记录）
  - ShadowVLA: Test-Time Re-Grounding of Frozen VLA Policies from Self-Generated References
  - 先在规范场景里跑出一条成功 rollout 作参考，再用 RGB-D 配准把它映射到当前场景；针对物体位移，不是视觉漂移

### 5.4 WAM 与世界模型

- **WAM-TTT** · 2026 · 预印本 · [arXiv 2607.06988](https://arxiv.org/abs/2607.06988)
  - WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time
  - WAM 本身冻结，在无标签的人类视频上用视频预测损失只更新视频侧的快权重
- **T2-z** · 2026 · 预印本 · [arXiv 2610.22364](https://arxiv.org/abs/2610.22364)
  - T2-z: Test-Time Optimization of Environment Latents for Robotic World Models
  - 冻结世界模型，只用预测误差优化一个环境潜变量，对应摩擦、质量等不可观测因素（仅核实摘要）
- **Self-Correcting Planning** · 2026 · 预印本 · [arXiv 2611.23620](https://arxiv.org/abs/2611.23620)
  - How Uncertain Is My Action? Self-Correcting Visual Planning with Frozen World Models
  - 用冻结的潜世界模型诊断执行器偏移，并在规划器中补偿（仅核实摘要）
- **WorldAgen** · 2026 · 预印本 · [arXiv 2609.08162](https://arxiv.org/abs/2609.08162)
  - WorldAgen: Unified State-Action Prediction with Test-Time World Model Training
  - 测试时用探索动作采集真实转移，轻量更新世界模型（只读了 listing 摘要）

### 5.5 扩散与流匹配策略特有的信号

- **BID** · 2024 · 预印本 · [arXiv 2408.17355](https://arxiv.org/abs/2408.17355) · [项目](https://bid-robot.github.io)
  - Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling
  - 用候选动作块与上一块在重叠段上的一致性，以及与强、弱 checkpoint 的对比，从多个样本中选一个
- **Self-GAD** · 2025 · 预印本 · [arXiv 2508.12189](https://arxiv.org/abs/2508.12189) · [项目](https://rhea-mal.github.io/selfgad.github.io)
  - Self-Guided Action Diffusion
  - 把 BID 的一致性改成每个去噪步上的引导（仅核实摘要）
- **RTC** · 2025 · NeurIPS 2025 · [arXiv 2506.07339](https://arxiv.org/abs/2506.07339) · [项目](https://pi.website/research/real_time_chunking)
  - Real-Time Execution of Action Chunking Flow Policies
  - 冻结一定会执行的前几步，其余部分用引导做 inpainting，把重叠段一致性写成采样约束
- **Sentinel** · 2024 · CoRL 2024 · [arXiv 2410.04640](https://arxiv.org/abs/2410.04640) · [项目](https://sites.google.com/stanford.edu/sentinel)
  - Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress
  - 以相邻两次推理在重叠段上动作分布的差异（STAC）作为无标签的 OOD 监测量
- **FAIL-Detect** · 2025 · RSS 2025 · [arXiv 2503.08558](https://arxiv.org/abs/2503.08558)
  - Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies
  - 只用成功示范学一个不确定度信号，配合保形预测检测失败（仅核实摘要）
- **DVAC** · 2026 · 预印本 · [arXiv 2606.03847](https://arxiv.org/abs/2606.03847)
  - Denoising Tells When to Replan: Denoising-Variance Adaptive Chunking for Flow-Based Robot Policies
  - 以最后几个去噪步的方差为不确定度，只执行低方差的前缀（仅核实摘要）
- **GeCO** · 2026 · 预印本 · [arXiv 2603.17834](https://arxiv.org/abs/2603.17834) · [项目](https://hrh6666.github.io/GeCO)
  - Generative Control as Optimization: Time Unconditional Flow Matching for Adaptive and Robust Robotic Control
  - 时间无条件的流匹配，用优化后动作处的场范数做免训练的 OOD 检测（仅核实摘要）
- **τ0-WM** · 2026 · 预印本 · [arXiv 2606.01027](https://arxiv.org/abs/2606.01027) · [项目](https://tau0-wm.github.io)
  - $τ_0$-WM: A Unified Video-Action World Model for Robotic Manipulation
  - 统一的视频-动作世界模型，按重去噪一致性给候选动作排序（仅核实摘要）
- **Diffusion-TTA** · 2023 · NeurIPS 2023 · [arXiv 2311.16102](https://arxiv.org/abs/2311.16102) · [项目](https://diffusion-tta.github.io)
  - Diffusion-TTA: Test-time Adaptation of Discriminative Models via Generative Feedback
  - 以判别模型的输出为条件计算扩散去噪误差，再反传给判别模型；对象是分类等视觉任务，不是策略

### 5.6 通用 TTA 代表作

- **BN-adapt** · 2020 · NeurIPS 2020 · [arXiv 2006.16971](https://arxiv.org/abs/2006.16971) · [项目](https://domainadaptation.org/batchnorm)
  - Improving robustness against common corruptions by covariate shift adaptation
  - 只用测试样本的批统计替换 BN 的均值和方差
- **TENT** · 2020 · ICLR 2021 · [arXiv 2006.10726](https://arxiv.org/abs/2006.10726)
  - Tent: Fully Test-time Adaptation by Entropy Minimization
  - 以预测熵为目标，只更新归一化层的统计和通道仿射参数
- **TTT** · 2019 · ICML 2020 · [arXiv 1909.13231](https://arxiv.org/abs/1909.13231)
  - Test-Time Training with Self-Supervision for Generalization under Distribution Shifts
  - 测试前先在测试样本上做旋转预测这类自监督任务，更新共享特征提取器
- **TTT-MAE** · 2022 · 预印本 · [arXiv 2209.07522](https://arxiv.org/abs/2209.07522)
  - Test-Time Training with Masked Autoencoders
  - 把 TTT 的辅助任务换成 MAE 重建
- **MEMO** · 2021 · NeurIPS 2022 · [arXiv 2110.09506](https://arxiv.org/abs/2110.09506) · [代码](https://github.com/zhangmarvin/memo)
  - MEMO: Test Time Robustness via Adaptation and Augmentation
  - 对单个测试点做多个增广，最小化平均预测的边际熵
- **TPT** · 2022 · NeurIPS 2022 · [arXiv 2209.07511](https://arxiv.org/abs/2209.07511)
  - Test-Time Prompt Tuning for Zero-Shot Generalization in Vision-Language Models
  - 在 CLIP 上对单个样本做带置信度筛选的熵最小化，只调文本 prompt
- **TDA** · 2024 · CVPR 2024 · [arXiv 2403.18293](https://arxiv.org/abs/2403.18293) · [项目](https://kdiaaa.github.io/tda)
  - Efficient Test-Time Adaptation of Vision-Language Models
  - 不反传，只维护一个带正负伪标签的 KV 缓存
- **SAR** · 2023 · ICLR 2023 · [arXiv 2302.12400](https://arxiv.org/abs/2302.12400)
  - Towards Stable Test-Time Adaptation in Dynamic Wild World
  - 指出 BN 是 TTA 不稳定的主因，LN / GN 模型更稳但熵最小化仍会塌缩；提出可靠且锐度感知的熵最小化
- **CFA** · 2022 · IJCAI-ECAI 2022 · [arXiv 2206.13951](https://arxiv.org/abs/2206.13951)
  - Robustifying Vision Transformer without Retraining from Scratch by Test-Time Class-Conditional Feature Alignment
  - 在没有 BN 的 ViT 上，按类条件和整体两个层面对齐隐藏表征的分布
- **FOA** · 2024 · ICML 2024† · [arXiv 2404.01650](https://arxiv.org/abs/2404.01650)
  - Test-Time Model Adaptation with Only Forward Passes
  - 只用前向传播，以激活统计差异加熵为适应度，用 CMA-ES 优化新增的输入 prompt，再做激活平移
- **ActMAD** · 2022 · CVPR 2023 · [arXiv 2211.12870](https://arxiv.org/abs/2211.12870) · [项目](https://jmiemirza.github.io/ActMAD)
  - ActMAD: Activation Matching to Align Distributions for Test-Time-Training
  - 把多层的逐特征激活统计与训练统计对齐；本轮唯一在 VLA 上实测过的特征统计对齐方法（作为 SALT 的基线）

## 6. 条件注入结构与干预

### 6.1 VLA 的结构

- **π0** · 2024 · RSS 2025 · [arXiv 2410.24164](https://arxiv.org/abs/2410.24164)
  - π0: A Vision-Language-Action Flow Model for General Robot Control
  - 动作专家第 l 层读 PaliGemma 前缀第 l 层的 KV，三段 blockwise causal mask；流匹配动作头
- **π0.5** · 2025 · CoRL 2025 · [arXiv 2504.16054](https://arxiv.org/abs/2504.16054)
  - π0.5: a Vision-Language-Action Model with Open-World Generalization
  - 沿用逐层前缀 KV，信息单向从 VLM 流向动作专家；时间步经 adaptive RMSNorm 注入，状态离散成文本 token
- **FAST** · 2025 · 预印本 · [arXiv 2501.09747](https://arxiv.org/abs/2501.09747)
  - FAST: Efficient Action Tokenization for Vision-Language-Action Models
  - 用 DCT 加 BPE 把动作变成 token，放进 VLM 序列做自回归预测，对应文中的 π0-FAST
- **π0.5+KI** · 2025 · 预印本 · [arXiv 2505.23705](https://arxiv.org/abs/2505.23705)
  - Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better
  - 正向的逐层 KV 通路不变，用 stop-gradient 切断动作专家流回预训练权重的梯度
- **GR00T N1** · 2025 · 预印本 · [arXiv 2503.14734](https://arxiv.org/abs/2503.14734)
  - GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
  - 交替做交叉注意力和自注意力的 DiT，读 Eagle-2 LLM 第 12 层（中间层）的特征
- **GR00T N1.5** · 2025 · 官方页面 · [页面](https://research.nvidia.com/labs/gear/gr00t-n1_5)
  - 无论文，只有 NVIDIA research 官方页面
  - VLM 冻结，DiT 对 VL embedding 做交叉注意力，另加对齐未来 embedding 的 FLARE 目标
- **GR00T N1.6** · 2025 · 官方页面 · [页面](https://research.nvidia.com/labs/gear/gr00t-n1_6) · [代码](https://github.com/NVIDIA/Isaac-GR00T)
  - 无论文，只有 NVIDIA 官方页面和 Isaac-GR00T `n1d6` 分支代码
  - 代码把 LLM 截到前 16 层、取第 16 层输出；32 层 DiT 的交叉注意力在图像 token 和非图像 token 之间轮换
- **SmolVLA** · 2025 · 预印本 · [arXiv 2506.01844](https://arxiv.org/abs/2506.01844)
  - SmolVLA: A vision-language-action model for affordable and efficient robotics
  - 只用 LLM 前一半层，动作专家交替做交叉注意力和因果自注意力；消融比较了注入方式和层数
- **OpenVLA** · 2024 · CoRL 2024 · [arXiv 2406.09246](https://arxiv.org/abs/2406.09246) · [项目](https://openvla.github.io)
  - OpenVLA: An Open-Source Vision-Language-Action Model
  - 每维动作分成 256 个 bin，用 Llama 词表中的 token 表示，做 next-token 预测
- **OpenVLA-OFT** · 2025 · RSS 2025 · [arXiv 2502.19645](https://arxiv.org/abs/2502.19645) · [项目](https://openvla-oft.github.io)
  - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
  - 输入空动作 embedding，用双向掩码并行解码，再接 MLP 做 L1 回归；OFT+ 用 FiLM 把语言注入视觉编码器
- **RDT-1B** · 2024 · ICLR 2025† · [arXiv 2410.07864](https://arxiv.org/abs/2410.07864)
  - RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation
  - 每个 DiT block 做交叉注意力，图像和文本逐层交替（ACI），避免图像 token 淹没文本
- **DexVLA** · 2025 · 预印本 · [arXiv 2502.05855](https://arxiv.org/abs/2502.05855) · [项目](https://dex-vla.github.io)
  - DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control
  - reasoning token 经 FiLM 注入扩散专家
- **ScaleDP** · 2024 · 预印本 · [arXiv 2409.14411](https://arxiv.org/abs/2409.14411)
  - Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation
  - 把观测 embedding 分解成多个仿射层注入，类似 adaLN（仅核实摘要）
- **CogACT** · 2024 · 预印本 · [arXiv 2411.19650](https://arxiv.org/abs/2411.19650)
  - CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
  - 把整个条件压成一个 cognition token，与噪声动作放在同一序列里输入 DiT
- **DP** · 2023 · 预印本 · [arXiv 2303.04137](https://arxiv.org/abs/2303.04137)
  - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
  - 两种经典注入方式：CNN 版逐卷积层用 FiLM，Transformer 版每个 decoder block 做交叉注意力
- **Dita** · 2024 · 预印本 · [arXiv 2410.15959](https://arxiv.org/abs/2410.15959) · [项目](https://robodita.github.io)
  - Diffusion Transformer Policy
  - 图像特征、语言 token、时间步 embedding 拼在因果 Transformer 序列前部（in-context），不用 adaLN，也不用交叉注意力
- **VLA-Adapter** · 2025 · 预印本 · [arXiv 2509.09372](https://arxiv.org/abs/2509.09372)
  - VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model
  - policy 第 l 层通过带门控的交叉注意力读 VLM 第 l 层，并系统比较了读哪些层、读什么特征
- **ABot-M0** · 2026 · 预印本 · [arXiv 2602.11236](https://arxiv.org/abs/2602.11236)
  - ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning
  - 默认读 Qwen3-VL 最后一层；在 LIBERO-Plus 上比较了最后层、中间层和后 16 层
- **NEO-VLA** · 2026 · 预印本 · [arXiv 2611.06918](https://arxiv.org/abs/2611.06918)
  - From Pixels to Actions – Towards Native Vision-Language-Action Policies
  - 逐层 KV 联合注意力，专家第 j 层读骨干哪一层可以配置，并在骨干冻结和微调两种设置下比较
- **Layer Mystery** · 2026 · 预印本 · [arXiv 2609.36118](https://arxiv.org/abs/2609.36118)
  - The Layer Mystery of VLA: An Information-Theoretical Analysis of VLA Latent Interface
  - 比较单层与多层融合的条件接口，发现融合多半不如最好的单层，最优层随骨干和基准变化（仅核实摘要）
- **Should-AE-Train** · 2026 · 预印本 · [arXiv 2611.05249](https://arxiv.org/abs/2611.05249)
  - Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs
  - 比较逐层 KV 接口上梯度耦合与梯度隔离的效果，结论是隔离是否有益要看条件
- **VLAFlow** · 2026 · 预印本 · [arXiv 2607.01586](https://arxiv.org/abs/2607.01586)
  - VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment
  - 沿用逐层 KV 共享的接口，做共训练和未来潜变量对齐

### 6.2 WAM 的结构

- **ImageWAM** · 2026 · 预印本 · [arXiv 2606.19531](https://arxiv.org/abs/2606.19531) · [项目](https://zhangwenyao1.github.io/ImageWAM/) · [代码](https://github.com/yuyangalin/ImageWAM)
  - ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?
  - 用图像编辑 DiT 代替视频 DiT，动作专家逐层读编辑 DiT 的 KV；推理时不解码目标帧
- **Fast-WAM** · 2026 · 预印本 · [arXiv 2603.16666](https://arxiv.org/abs/2603.16666) · [项目](https://yuantianyuan01.github.io/FastWAM/)
  - Fast-WAM: Do World Action Models Need Test-time Future Imagination?
  - 视频 DiT 与动作专家共享注意力（MoT），动作只看干净的当前帧；去掉测试时视频生成后性能基本不变
- **Faster-WAM** · 2026 · 预印本 · [arXiv 2608.02365](https://arxiv.org/abs/2608.02365)
  - Faster-WAM: Do World Action Models Need Deep Action Modules?
  - 每个动作层、每个 head 对所有视频层的 KV 学一组 softmax 权重（Lite KV-Fusion），动作专家只剩 1 层
- **DreamZero** · 2026 · 预印本 · [arXiv 2602.15922](https://arxiv.org/abs/2602.15922) · [项目](https://dreamzero0.github.io)
  - World Action Models are Zero-shot Policies
  - 14B 视频 DiT 中视频与动作联合去噪、共享时间步；只测了未见环境与物体，没有因子化的视觉扰动实验
- **UVA** · 2025 · RSS 2025 · [arXiv 2503.00200](https://arxiv.org/abs/2503.00200) · [项目](https://unified-video-action-model.github.io)
  - Unified Video Action Model
  - 视频与动作共享一个联合 latent，用两个轻量扩散头分别解码，推理时可跳过视频解码（仅核实摘要）
- **UWM** · 2025 · 预印本 · [arXiv 2504.02792](https://arxiv.org/abs/2504.02792)
  - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets
  - 视频扩散和动作扩散在同一个 transformer 中进行，各自有独立的时间步（仅核实摘要）
- **GE-Act** · 2025 · 预印本 · [arXiv 2508.05635](https://arxiv.org/abs/2508.05635) · [项目](https://genie-envisioner.github.io)
  - Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation
  - Genie Envisioner 中的动作模块 GE-Act：第 i 个动作 block 对第 i 个视觉 block 的输出做交叉注意力
- **Cosmos Policy** · 2026 · 预印本 · [arXiv 2601.16163](https://arxiv.org/abs/2601.16163) · [项目](https://research.nvidia.com/labs/dir/cosmos-policy)
  - Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning
  - 不改结构，把动作、本体感受和价值写成新的 latent 帧插入视频序列，与视频一起去噪
- **Video Policy** · 2025 · 预印本 · [arXiv 2508.00795](https://arxiv.org/abs/2508.00795) · [项目](https://videopolicy.cs.columbia.edu)
  - Video Generators are Robot Policies
  - 把 SVD 视频 U-Net 解码器若干层的特征汇成一个全局条件向量，送入 1D CNN 动作网络
- **VPP** · 2024 · 预印本 · [arXiv 2412.14803](https://arxiv.org/abs/2412.14803)
  - Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations
  - 聚合 SVD U-Net 各上采样层的单步特征，在 DiT 中做交叉注意力
- **mimic-video** · 2025 · 预印本 · [arXiv 2512.15692](https://arxiv.org/abs/2512.15692) · [项目](https://mimic-video.github.io)
  - mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs
  - 动作 DiT 对 Cosmos-Predict2 第 19 层、部分去噪状态下的特征做交叉注意力
- **DiT4DiT** · 2026 · 预印本 · [arXiv 2603.10448](https://arxiv.org/abs/2603.10448)
  - DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control
  - 改自 GR00T-N1 的动作 DiT，对 Cosmos-Predict2.5-2B 第 18 层的特征做交叉注意力
- **LingBot-VA** · 2026 · 预印本 · [arXiv 2601.21998](https://arxiv.org/abs/2601.21998) · [项目](https://technology.robbyant.com/lingbot-va)
  - Causal World Modeling for Robot Control
  - 视频与动作在同一深度上各用独立 QKV 做联合自注意力，两种 token 交错排列，时间上因果
- **Motus** · 2025 · 预印本 · [arXiv 2512.13030](https://arxiv.org/abs/2512.13030)
  - Motus: A Unified Latent Action World Model
  - 理解、视频、动作三个专家的自注意力拼接（Tri-model Joint Attention）

### 6.3 干预与可解释性

- **KV steering** · 2025 · 预印本 · [arXiv 2507.08799](https://arxiv.org/abs/2507.08799)
  - KV Cache Steering for Controlling Frozen LLMs
  - LLM 上的工作：prefill 之后，对最后一个 prompt token 位置的 K、V 各加一次差均值向量
- **TempoFit** · 2026 · 预印本 · [arXiv 2603.07647](https://arxiv.org/abs/2603.07647) · [代码](https://github.com/LucioSunj/TempoFit)
  - TempoFit: Plug-and-Play Layer-Wise Temporal KV Memory for Long-Horizon Vision-Language-Action Manipulation
  - 不训练，在冻结 π0.5 的部分中间层上把检索到的历史 KV 残差注入前缀 K/V，再做范数保持
- **MI-Steering** · 2025 · CoRL 2025 · [arXiv 2509.00328](https://arxiv.org/abs/2509.00328)
  - Mechanistic interpretability for steering vision-language-action models
  - 把 VLM 的 FFN value vector 投影到 token 空间并按语义聚类，上调选中簇的权重来引导动作
- **CTRL-STEER** · 2026 · 预印本 · [arXiv 2606.00269](https://arxiv.org/abs/2606.00269)
  - Closed-Loop Neural Activation Control in Vision-Language-Action Models
  - 选出少数 FFN 神经元，用 PID 或 RL 动态调整引导系数
- **COAST** · 2026 · 预印本 · [arXiv 2605.17144](https://arxiv.org/abs/2605.17144)
  - Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States
  - 在动作专家某一层的残差流上乘一个 conceptor 门
- **RL²-VLA** · 2026 · 预印本 · [arXiv 2607.26991](https://arxiv.org/abs/2607.26991) · [项目](https://rl2-vla.github.io)
  - RL²-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models
  - 在动作专家 latent 上训练离线 RL 策略，把它的速度场与冻结 VLA 的速度场合成（仅核实摘要）
- **Present-not-Remembered** · 2026 · 预印本 · [arXiv 2607.03372](https://arxiv.org/abs/2607.03372)
  - Present but Not Remembered: Auditing How Frozen VLAs Encode, Deploy, and Steer Visual History
  - 用 interchange、attention knockout 和逐层注入审计冻结 VLA 怎样使用历史帧
- **DeepVision-VLA** · 2026 · 预印本 · [arXiv 2603.15618](https://arxiv.org/abs/2603.15618)
  - Look Before Acting: Enhancing Vision Foundation Representations for Vision-Language-Action Models
  - 把 DINOv3 后 16 层的 QKV 并入 VLA 的后 16 层，并比较了注入深层与浅层的效果
- **Knowing When to Stop** · 2026 · 预印本 · [arXiv 2609.00908](https://arxiv.org/abs/2609.00908)
  - Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs
  - 读动作专家对观测的注意力熵，据此截断动作块（仅核实摘要）
- **WA-LQR** · 2026 · 预印本 · [arXiv 2607.14943](https://arxiv.org/abs/2607.14943)
  - Steering Robustness into World Action Models via Mechanistic Interpretability and Optimal Control
  - 在 WAM 的 DiT 残差流上做 ActAdd 或 LQR 引导，针对相机朝向和相机噪声；本轮唯一面向鲁棒性的 WAM 引导工作
- **SteerTrace** · 2026 · 预印本 · [arXiv 2611.25719](https://arxiv.org/abs/2611.25719)
  - SteerTrace: Tracing How Target Attacks Steer World Action Models
  - 分别恢复未来 token、当前帧 token、FFN 神经元，追踪对抗攻击通过哪条通路影响 WAM 的动作（仅核实摘要）
- **StairVLA** · 2026 · 预印本 · [arXiv 2610.07756](https://arxiv.org/abs/2610.07756) · [项目](https://dicomsky.github.io/projects/stairvla)
  - StairVLA: Stage-Aware Hierarchical Action Generation for Vision-Language-Action Models
  - 按去噪阶段分配条件：早期偏重语言和视觉，后期偏重当前视觉（仅核实摘要）

## 7. WAM 综述

- **WAM-Survey** · 2026 · 预印本 · [arXiv 2609.16074](https://arxiv.org/abs/2609.16074) · [项目](https://rcl-robotics.github.io/Awesome-World-Action-Models)
  - World-Action Models for Robot Learning and Control: A Survey
  - 按 end-to-end 与 dual systems、joint 与 IDM 给 WAM 分类；没有引用 WAM 与 VLA 的鲁棒性正面对比
- **WAM-Tutorial** · 2026 · 预印本 · [arXiv 2607.00836](https://arxiv.org/abs/2607.00836) · [代码](https://github.com/clearlab-sustech/WorldModelSurvey)
  - From World Models to World Action Models: A Concise Tutorial for Robotics
  - 把 WAM 分成 imagine-then-execute、video-feature-conditioned、joint、auxiliary 四类；没有鲁棒性评测
