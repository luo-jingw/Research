# vla-drawing-writing 论文目录

- 快照日期：2026-11-18
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment 字段或论文集页面确认的发表处；"预印本" 表示未找到发表处。标 † 的发表处只见于 PDF 页眉或二手来源，见根目录 `issues.md` → ISSUE-006。
- 标题、年份、arXiv 编号经 arxiv.org 页面核实。
- 与其他方向重复的论文沿用其他方向 `papers.md` 中的简称与发表处。
- 分节对应 [survey.md](survey.md) 的分类；一篇论文只列在主归属的一节。

## 1. 仿真中的 VLA / WAM 写画

- **BURGER** · 2026 · 预印本 · [arXiv 2610.40532](https://arxiv.org/abs/2610.40532) · [项目](https://siyingzhao.github.io/BURGER/)
  - BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing
  - 语言条件简笔画基准：282 个任务、28,200 条仿真示教，评测 π0、π0.5、π0-FAST、OpenVLA、OpenVLA-OFT，并在 Franka 上部署 π0.5
- **DAP** · 2025 · CoRL 2026 · [arXiv 2510.27114](https://arxiv.org/abs/2510.27114) · [项目](https://dynamics-aligned-policy.github.io)
  - Learning Robust Visuomotor Policies via Dynamics Alignment
  - 策略与动作条件动力学模型联合采样动作和未来观测；在 ManiSkill3 DrawTriangle-v1 上与 π0、UVA 对比

## 2. 真机中的 VLA / WAM 写画

- **DreamZero** · 2026 · 预印本 · [arXiv 2602.15922](https://arxiv.org/abs/2602.15922) · [项目](https://dreamzero0.github.io/)
  - World Action Models are Zero-shot Policies
  - 14B 视频扩散 WAM，联合去噪未来视频与动作；零样本任务含用马克笔画圆、用刷子涂画，与 GR00T N1.6、π0.5 对比
- **VLAW** · 2026 · 预印本 · [arXiv 2602.12063](https://arxiv.org/abs/2602.12063) · [项目](https://sites.google.com/view/vlaw-arxiv)
  - VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
  - 用真机 rollout 微调动作条件视频世界模型，再用它生成的合成轨迹微调 π0.5；白板画圆是五个任务中最难的一个
- **FG-CLTP** · 2026 · 预印本 · [arXiv 2603.10871](https://arxiv.org/abs/2603.10871)
  - FG-CLTP: Fine-Grained Contrastive Language Tactile Pretraining for Robotic Manipulation
  - 触觉点云预训练编码器，接入 π0.5 架构得到触觉 VLA 3D-TLA；真机任务含白板书写

## 3. 世界模型预测写画画面

- **VT-WM** · 2026 · 预印本 · [arXiv 2602.06001](https://arxiv.org/abs/2602.06001)
  - Visuo-Tactile World Models
  - 视觉 + 触觉的动作条件世界模型；"scribble with marker" 只用于想象保真度评测
- **DreamFAR** · 2026 · 预印本 · [arXiv 2611.22001](https://arxiv.org/abs/2611.22001)
  - DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects
  - 双臂遥操作数据上训练的动作条件世界模型；对"在白板上写一句话"做 60 秒 rollout 的定性对比

## 4. 写字只出现在训练数据中

- **RDT-1B** · 2024 · ICLR 2025† · [arXiv 2410.07864](https://arxiv.org/abs/2410.07864)
  - RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation
  - 微调数据集覆盖 300+ 任务，"even including writing math equations"；评测任务不含写字

## 5. 含写画任务的环境与基准

- **ManiSkill3** · 2024 · 预印本 · [arXiv 2410.00425](https://arxiv.org/abs/2410.00425) · [项目](http://maniskill.ai/)
  - ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI
  - GPU 并行仿真；官方任务库含 DrawTriangle-v1、DrawSVG-v1、TableTopFreeDraw-v1，用预置"墨点"模拟笔迹
- **ManiSkill2** · 2023 · ICLR 2023 · [arXiv 2302.04659](https://arxiv.org/abs/2302.04659)
  - ManiSkill2: A Unified Benchmark for Generalizable Manipulation Skills
  - 软体任务 Write：在 MPM 黏土上写出目标字符，IoU > 0.8 判成功
- **PlasticineLab** · 2021 · ICLR 2021 · [arXiv 2104.03311](https://arxiv.org/abs/2104.03311)
  - PlasticineLab: A Soft-Body Manipulation Benchmark with Differentiable Physics
  - 可微软体基准；Writer 任务用胶囊形笔在橡皮泥上刻出目标涂鸦
- **BPP** · 2026 · 预印本 · [arXiv 2606.30457](https://arxiv.org/abs/2606.30457)
  - What Enables In-Context Behavior Prompting for Manipulation?
  - 提出 DrawAnything-Sim/Real：2000 个程序生成的绘画训练任务、人类手绘的未见评测任务，Chamfer 距离评测；策略是以示教为提示的扩散策略
- **Grip, Trace, Write** · 2026 · CoRL 2026 Workshop PhysWM · [arXiv 2611.10451](https://arxiv.org/abs/2611.10451) · [项目](https://dexwriting.github.io/)
  - Grip, Trace, Write: Force-Aware Imitation and Reinforcement Learning for High-DoF Robotic Handwriting
  - MuJoCo 力感知手写环境：高自由度手自由握笔，墨迹由接触力和笔尖速度决定；策略为 BC + RL

## 6. 被评测的 VLA / WAM 基座

- **π0** · 2024 · RSS 2025 · [arXiv 2410.24164](https://arxiv.org/abs/2410.24164) · [项目](https://physicalintelligence.company/blog/pi0)
  - π0: A Vision-Language-Action Flow Model for General Robot Control
  - flow matching 动作头的 VLA；BURGER、DAP 的被测模型
- **π0.5** · 2025 · CoRL 2025 · [arXiv 2504.16054](https://arxiv.org/abs/2504.16054)
  - π0.5: a Vision-Language-Action Model with Open-World Generalization
  - BURGER、DreamZero、VLAW 的被测或基座模型；3D-TLA 沿用其架构
- **FAST** · 2025 · 预印本 · [arXiv 2501.09747](https://arxiv.org/abs/2501.09747) · [项目](https://pi.website/research/fast)
  - FAST: Efficient Action Tokenization for Vision-Language-Action Models
  - 自回归动作 token 化，对应 BURGER 中的 π0-FAST
- **OpenVLA** · 2024 · CoRL 2024 · [arXiv 2406.09246](https://arxiv.org/abs/2406.09246)
  - OpenVLA: An Open-Source Vision-Language-Action Model
  - 自回归离散动作 token 的开源 VLA；BURGER 的被测模型
- **OpenVLA-OFT** · 2025 · RSS 2025 · [arXiv 2502.19645](https://arxiv.org/abs/2502.19645) · [项目](https://openvla-oft.github.io)
  - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
  - 并行解码 + 动作块；BURGER 比较了动作块长度 1 与 8
- **UVA** · 2025 · RSS 2025 · [arXiv 2503.00200](https://arxiv.org/abs/2503.00200)
  - Unified Video Action Model
  - 联合建模视频与动作；DAP 在 DrawTriangle-v1 上的基线
- **Ctrl-World** · 2025 · ICLR 2026 · [arXiv 2510.10125](https://arxiv.org/abs/2510.10125)
  - Ctrl-World: A Controllable Generative World Model for Robot Manipulation
  - 动作条件视频世界模型；VLAW 中被真机 rollout 微调后用作学习的模拟器

## 7. 相邻工作：控制器不是 VLA / WAM

### 7.1 毛笔、颜料与绘画仿真

- **Robot Calligraphy POC** · 2019 · IROS 2020 · [arXiv 1911.08002](https://arxiv.org/abs/1911.08002)
  - Robot Calligraphy using Pseudospectral Optimal Control in Conjunction with a Novel Dynamic Brush Model
  - 动态虚拟毛笔模型 + 轨迹优化写汉字
- **FRIDA** · 2022 · 预印本 · [arXiv 2210.00664](https://arxiv.org/abs/2210.00664)
  - FRIDA: A Collaborative Robot Painter with a Differentiable, Real2Sim2Real Planning Environment
  - 可微绘画仿真（real2sim2real）+ 规划，按语言或图像作画
- **Spline-FRIDA** · 2024 · 预印本 · [arXiv 2412.00597](https://arxiv.org/abs/2412.00597)
  - Spline-FRIDA: Towards Diverse, Humanlike Robot Painting Styles with a Sample-Efficient, Differentiable Brush Stroke Model
  - 用动作捕捉的艺术家笔触训练可微笔触动力学模型
- **From Scratch to Sketch** · 2022 · ICRA 2022 · [arXiv 2208.04833](https://arxiv.org/abs/2208.04833)
  - From Scratch to Sketch: Deep Decoupled Hierarchical Reinforcement Learning for Robotic Sketching Agent
  - 分层 RL 分别学笔触渲染与运动控制
- **Sim-to-Real Brush** · 2023 · 预印本 · [arXiv 2309.08457](https://arxiv.org/abs/2309.08457)
  - Sim-to-Real Brush Manipulation using Behavior Cloning and Reinforcement Learning
  - 在 MyPaint 虚拟环境中用 BC + RL 训练画笔策略，迁移到真机
- **CalliRewrite** · 2024 · ICRA 2024 · [arXiv 2405.15776](https://arxiv.org/abs/2405.15776)
  - CalliRewrite: Recovering Handwriting Behaviors from Calligraphy Images without Supervision
  - 无监督地从书法图像恢复笔顺，再用 RL 微调工具控制
- **IMPASTO** · 2026 · 预印本 · [arXiv 2603.29315](https://arxiv.org/abs/2603.29315)
  - IMPASTO: Integrating Model-Based Planning with Learned Dynamics Models for Robotic Oil Painting Reproduction
  - 油画缺少可信仿真器，改为学习像素动力学模型 + MPC

### 7.2 力 / 触觉书写

- **Membranes** · 2022 · CoRL 2022 · [arXiv 2209.13432](https://arxiv.org/abs/2209.13432)
  - Manipulation via Membranes: High-Resolution and Highly Deformable Tactile Sensing and Control
  - 学习软触觉膜动力学，控制抓着的马克笔作画
- **Flying Calligrapher** · 2024 · RA-L（ICRA 2025 报告） · [arXiv 2407.05587](https://arxiv.org/abs/2407.05587)
  - Flying Calligrapher: Contact-Aware Motion and Force Planning and Control for Aerial Manipulation
  - 空中机械臂同时跟踪法向力与切向轨迹，做空中书法
- **Force Generative IL** · 2026 · IEEE Access · [arXiv 2602.06620](https://arxiv.org/abs/2602.06620)
  - Force Generative Imitation Learning: Bridging Position Trajectory and Force Commands through Control Technique
  - 从位置轨迹生成力指令，用于白板书写类任务
- **Semantic-Contact Fields** · 2026 · RSS 2026 · [arXiv 2602.13833](https://arxiv.org/abs/2602.13833)
  - Semantic-Contact Fields for Category-Level Generalizable Tactile Tool Manipulation
  - 触觉扩散策略，仿真生成触觉数据；真机任务含蜡笔绘画
- **VISTA** · 2026 · 预印本 · [arXiv 2608.25872](https://arxiv.org/abs/2608.25872)
  - VISTA: Visually Inferred Spatial ConTact Attention for Contact-Rich Manipulation
  - 用视觉推断的柔顺夹爪形变场作接触反馈；任务含毛笔书法
- **In-Hand Pen Writing** · 2026 · 预印本 · [arXiv 2609.11775](https://arxiv.org/abs/2609.11775)
  - Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation
  - 仿人手手内持笔书写，在真机上实时估计手–物体雅可比
- **TacGB** · 2026 · 预印本 · [arXiv 2609.34006](https://arxiv.org/abs/2609.34006)
  - TacGooseBumps (TacGB): Retrofitting Normal-Only Tactile Sensors with Shear Encoding for Learning Contact-Rich Manipulation
  - 给只测法向力的触觉传感器加剪切编码；任务含白板画线

### 7.3 VLM 规划 + 执行、数据与渲染

- **CoBrush** · 2026 · IROS 2026 · [arXiv 2609.35476](https://arxiv.org/abs/2609.35476)
  - CoBrush: A Hierarchical Planning Framework for Human-Robot Co-Painting
  - 意图推断、空间定位与笔触控制分层的人机共绘；VLM 只做规划
- **Handwritten Alphabet LfD** · 2026 · ICDL 2026 · [arXiv 2608.06221](https://arxiv.org/abs/2608.06221)
  - Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation
  - 22 人、52 种大小写字母的 3,142 条手写示教数据集与类人度评测
- **Online-Offline Handwriting** · 2026 · ECCV 2026 · [arXiv 2608.03198](https://arxiv.org/abs/2608.03198)
  - Bridging Online and Offline Handwriting via Differentiable Physical Rendering
  - 用可微物理渲染连接笔迹轨迹与笔迹图像

## 8. 易混淆：任务涉及笔、字母或草图，但不是写画

- **RT-Sketch** · 2024 · 预印本 · [arXiv 2403.02709](https://arxiv.org/abs/2403.02709)
  - RT-Sketch: Goal-Conditioned Imitation Learning from Hand-Drawn Sketches
  - 手绘草图作为目标条件，任务本身是摆放物体
- **ChatVLA-2** · 2025 · 预印本 · [arXiv 2505.21906](https://arxiv.org/abs/2505.21906)
  - ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge
  - 机器人读白板上的算式，再选出对应数字卡片，本身不书写
- **GR-Dexter** · 2025 · 预印本 · [arXiv 2512.24210](https://arxiv.org/abs/2512.24210)
  - GR-Dexter Technical Report
  - 书法只出现在遥操作能力展示（Fig. 5）中，VLA 评测不含书写
