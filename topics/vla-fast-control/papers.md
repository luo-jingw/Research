# vla-fast-control 论文目录

- 快照日期：2026-10-30
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment 字段或论文集确认的发表处；"预印本" 表示未找到发表处。标 † 的发表处未在一手来源确认，见根目录 `issues.md` → ISSUE-003。
- 每条的标题、年份、arXiv 编号均经 arxiv.org 页面核实；数字取自摘要或正文。
- 延迟数字都注明硬件；不同论文的测量口径（是否含图像编码、网络、几步去噪）不同，不能直接横比。
- 分节对应 [survey.md](survey.md) 的分类。

## A. 推理加速与实时执行

### A1. 动作表示与解码

- **π0** · 2024 · RSS 2025 · [arXiv 2410.24164](https://arxiv.org/abs/2410.24164) · [项目](https://physicalintelligence.company/blog/pi0)
  - π0: A Vision-Language-Action Flow Model for General Robot Control
  - VLM + flow matching 动作专家，10 步去噪、动作块 H=50；RTX 4090 上 73 ms（图像编码 14 + 前缀 32 + 去噪 27），配合分块 50 Hz
- **FAST** · 2025 · 预印本 · [arXiv 2501.09747](https://arxiv.org/abs/2501.09747) · [项目](https://pi.website/research/fast)
  - FAST: Efficient Action Tokenization for Vision-Language-Action Models
  - DCT + BPE 动作 token 让自回归 VLA 能学高频动作；但每块约 750 ms，比扩散版 π0（约 100 ms）慢
- **OpenVLA-OFT** · 2025 · RSS 2025 · [arXiv 2502.19645](https://arxiv.org/abs/2502.19645) · [项目](https://openvla-oft.github.io)
  - Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success
  - 并行解码 + 分块 + 连续 L1 回归；吞吐 26–43×，A100 单图 240 → 73 ms；LIBERO 76.5 → 97.1%
- **PD-VLA** · 2025 · IROS 2025 · [arXiv 2503.02310](https://arxiv.org/abs/2503.02310)
  - PD-VLA: Accelerating VLA Model Integrated with Action Chunking via Parallel Decoding
  - 免训练 Jacobi 不动点并行解码，执行频率 2.52×
- **DD-VLA** · 2025 · ICML 2026 · [arXiv 2508.20072](https://arxiv.org/abs/2508.20072)
  - Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in VLA Policies
  - VLM 内掩码离散扩散并行细化动作，真机 9.69 Hz
- **DriftingVLA** · 2026 · 预印本 · [arXiv 2608.29749](https://arxiv.org/abs/2608.29749)
  - DriftingVLA: Native One-Step VLA Generation via Per-Dimension Temporal Drifting
  - 原生一步生成动作块，3.36× 更快，成功率优于多步
- **One-step Euler** · 2026 · CoRL 2026 · [arXiv 2610.30735](https://arxiv.org/abs/2610.30735)
  - When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies
  - 不重训、只用 1 步 Euler，延迟降 1.6–4.8×；大模型无明显损失，小模型在长视界上退化

### A2. 模型级加速

- **DeeR-VLA** · 2024 · NeurIPS 2024 · [arXiv 2411.02359](https://arxiv.org/abs/2411.02359) · [代码](https://github.com/yueyang130/DeeR-VLA)
  - DeeR-VLA: Dynamic Inference of Multimodal LLMs for Efficient Robot Execution
  - 多出口 LLM 按难度提前退出，LLM 计算降 5.2–6.5×
- **VLA-Cache** · 2025 · NeurIPS 2025 · [arXiv 2502.02175](https://arxiv.org/abs/2502.02175) · [项目](https://vla-cache.github.io)
  - VLA-Cache: Efficient VLA Manipulation via Adaptive Token Caching
  - 跨帧复用静态视觉 token 的 KV，CUDA 延迟最多 1.7×
- **EfficientVLA** · 2025 · 预印本 · [arXiv 2506.10100](https://arxiv.org/abs/2506.10100)
  - EfficientVLA: Training-Free Acceleration and Compression for VLA Models
  - 层剪枝 + 视觉 token 选择 + 扩散头缓存，1.93×，FLOPs 降到 28.9%
- **SpecPrune-VLA** · 2025 · ICML 2026 · [arXiv 2509.05614](https://arxiv.org/abs/2509.05614)
  - SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning
  - 用全局历史做静态 + 动态 token 剪枝，LIBERO 1.57×、真机 1.70×
- **Spec-VLA** · 2025 · EMNLP 2025 · [arXiv 2507.22424](https://arxiv.org/abs/2507.22424)
  - Spec-VLA: Speculative Decoding for VLA Models with Relaxed Acceptance
  - 对有序动作 token 做投机解码，按动作 bin 距离放宽接受，1.42×
- **BitVLA** · 2025 · 预印本 · [arXiv 2506.07530](https://arxiv.org/abs/2506.07530) · [代码](https://github.com/ustcwhy/BitVLA)
  - BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation
  - 三值权重原生 1-bit VLA；A100 三图 73 ms vs OFT 321 ms，显存降 11×
- **QuantVLA** · 2026 · CVPR 2026 · [arXiv 2602.20309](https://arxiv.org/abs/2602.20309)
  - QuantVLA: Scale-Calibrated Post-Training Quantization for VLA Models
  - 含 DiT 动作头的 W4A8 后训练量化，π0.5 显存 4.27 → 1.28 GB；摘要未报延迟
- **TinyVLA** · 2024 · 预印本 · [arXiv 2409.12514](https://arxiv.org/abs/2409.12514) · [项目](https://tiny-vla.github.io)
  - TinyVLA: Towards Fast, Data-Efficient VLA Models for Robotic Manipulation
  - 小 VLM + 扩散头，延迟比 OpenVLA 低约 20×
- **SmolVLA** · 2025 · 预印本 · [arXiv 2506.01844](https://arxiv.org/abs/2506.01844) · [代码](https://github.com/huggingface/lerobot)
  - SmolVLA: A VLA Model for Affordable and Efficient Robotics
  - 0.45B，开源异步推理栈；异步使任务时间 13.75 → 9.7 s
- **VLA-Adapter** · 2025 · 预印本 · [arXiv 2509.09372](https://arxiv.org/abs/2509.09372) · [项目](https://vla-adapter.github.io)
  - VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model
  - 0.5B 骨干 + Bridge Attention，36.5 ms / 219.2 Hz
- **TurboVLA** · 2026 · 预印本 · [arXiv 2607.27205](https://arxiv.org/abs/2607.27205) · [代码](https://github.com/H-EmbodVis/TurboVLA)
  - TurboVLA: Real-Time VLA Model at 32 Hz on an RTX 4090 with <1 GB VRAM
  - 去掉 LLM 通路，RTX 4090 上 31.2 ms、0.9 GiB
- **Realtime-VLA** · 2025 · 预印本 · [arXiv 2510.26742](https://arxiv.org/abs/2510.26742) · [代码](https://github.com/Dexmal/realtime-vla)
  - Running VLAs at Real-time Speed
  - CUDA graph、kernel 融合、去 CPU 开销；π0 双视角 RTX 4090 上 106.5 → 27.3 ms

### A3. 执行级：分块、异步与实时分块

- **ACT** · 2023 · RSS 2023† · [arXiv 2304.13705](https://arxiv.org/abs/2304.13705) · [项目](https://tonyzhaozh.github.io/aloha)
  - Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
  - 动作分块（k=100）+ 时间集成；2080 Ti 上约 10 ms，50 Hz
- **BID** · 2024 · 预印本 · [arXiv 2408.17355](https://arxiv.org/abs/2408.17355) · [项目](https://bid-robot.github.io)
  - Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling
  - 采样多个动作块，按前后一致性选择
- **RTC** · 2025 · NeurIPS 2025 · [arXiv 2506.07339](https://arxiv.org/abs/2506.07339) · [项目](https://pi.website/research/real_time_chunking)
  - Real-Time Execution of Action Chunking Flow Policies
  - 异步执行时冻结已承诺动作、用引导 flow 补全其余；π0.5 76 → 97 ms，注入 +200 ms 延迟仍不退化
- **A2C2** · 2025 · 预印本 · [arXiv 2509.23224](https://arxiv.org/abs/2509.23224)
  - Leave No Observation Behind: Real-time Correction for VLA Action Chunks
  - 每步运行 0.31M 参数的修正头，比 RTC 高 7–23 个点（仿真）
- **VLASH** · 2025 · 预印本 · [arXiv 2512.01031](https://arxiv.org/abs/2512.01031) · [代码](https://github.com/mit-han-lab/vlash)
  - VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference
  - 用上一块动作把状态前推到执行时刻再推理；最大反应延迟 546 → 46 ms，任务完成快 1.5–2×
- **Training-time RTC** · 2025 · 预印本 · [arXiv 2512.05964](https://arxiv.org/abs/2512.05964)
  - Training-Time Action Conditioning for Efficient Real-Time Chunking
  - 训练时模拟延迟并做前缀条件，π0.6 远程 H100 端到端 135 → 108 ms
- **Legato** · 2026 · RSS 2026 · [arXiv 2602.12978](https://arxiv.org/abs/2602.12978) · [项目](https://lyfeng001.github.io/Legato)
  - Learning Native Continuation for Action Chunking Flow Policies
  - 从已知动作与噪声的混合开始去噪，平滑度与完成时间比 RTC 好约 10%
- **FASTER** · 2026 · 预印本 · [arXiv 2603.19199](https://arxiv.org/abs/2603.19199) · [项目](https://innovator-zero.github.io/FASTER)
  - FASTER: Rethinking Real-Time Flow VLAs
  - 近端动作先 1 步出，反应时间由首动作时间与执行视界决定；反应快 2.3–3.1×
- **EagleVLA** · 2026 · CoRL 2026 Spotlight · [arXiv 2607.12659](https://arxiv.org/abs/2607.12659) · [代码](https://github.com/PKU-SEC-Lab/EagleVLA)
  - EagleVLA: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference
  - Jetson Orin 上 π0.5 原本约 1.4 s；控制频率比 PyTorch 高 14.71×
- **REACT** · 2026 · CoRL 2026 Spotlight · [arXiv 2610.12007](https://arxiv.org/abs/2610.12007) · [项目](https://react-vla.github.io)
  - REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models
  - 交错时间步的滚动去噪缓冲；反应 734 ms，H50E50 为 1505 ms，人类 705 ms

### A4. 双系统

- **RoboDual** · 2024 · 预印本 · [arXiv 2410.08001](https://arxiv.org/abs/2410.08001) · [项目](https://opendrivelab.com/RoboDual)
  - Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation
  - OpenVLA 通才 + 20M DiT 专才，15 Hz vs 3.9 Hz，真机 +26.7%
- **Hi Robot** · 2025 · ICML 2025 · [arXiv 2502.19417](https://arxiv.org/abs/2502.19417) · [项目](https://pi.website/research/hirobot)
  - Hi Robot: Open-Ended Instruction Following with Hierarchical VLA Models
  - 高层 VLM 输出语言子步骤给 π0；低层 73 ms
- **Helix** · 2025 · 博客 · [项目](https://figure.ai/news/helix)
  - Helix（Figure AI 技术博客，无论文）
  - S2 7B 7–9 Hz + S1 80M 200 Hz，潜向量耦合，机载嵌入式 GPU
- **GR00T N1** · 2025 · 预印本 · [arXiv 2503.14734](https://arxiv.org/abs/2503.14734) · [项目](https://developer.nvidia.com/isaac/gr00t)
  - GR00T N1: An Open Foundation Model for Generalist Humanoid Robots
  - 联合训练的 S2 10 Hz / S1 120 Hz；L40 上 16 步动作块 63.9 ms；也是仿真 + 视频生成数据共训练的代表（见 C1）
- **Gemini Robotics** · 2025 · 预印本 · [arXiv 2503.20020](https://arxiv.org/abs/2503.20020)
  - Gemini Robotics: Bringing AI into the Physical World
  - 云端骨干 <160 ms + 机载解码器，端到端约 250 ms，有效 50 Hz
- **FiS-VLA** · 2025 · 预印本 · [arXiv 2506.01953](https://arxiv.org/abs/2506.01953) · [项目](https://fast-in-slow.github.io)
  - Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning
  - S1 共享 S2 的末端层；块长 8 时 117.7 Hz

## B. 超过示教速度的执行

### B1. 示教重定时后重训

- **DemoSpeedup** · 2025 · CoRL 2025† · [arXiv 2506.05064](https://arxiv.org/abs/2506.05064) · [项目](https://demospeedup.github.io)
  - DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration
  - 代理策略动作熵高的片段多下采样、精确片段少下采样，最高 3×
- **ESPADA** · 2025 · 预印本 · [arXiv 2512.07371](https://arxiv.org/abs/2512.07371) · [项目](https://project-espada.github.io/espada)
  - ESPADA: Execution Speedup via Semantics Aware Demonstration Data Downsampling for Imitation Learning
  - VLM-LLM 按夹爪–物体 3D 关系分段，只加速非关键段，约 2×
- **AdaTempo** · 2026 · 预印本 · [arXiv 2610.02706](https://arxiv.org/abs/2610.02706)
  - AdaTempo: Learning Shared Relative Tempo from Demonstrations for Faster Robot Manipulation
  - 多条示教的相对节奏共识给出连续加速曲线，最高 3.57×
- **VOLT** · 2026 · 预印本 · [arXiv 2606.06323](https://arxiv.org/abs/2606.06323) · [项目](https://volt2026.github.io/VOLT2026)
  - VOLT: Vision and Language Trajectory Segmentation for Faster-than-Demonstration Policies
  - 视觉语言模型分出精确段，其余下采样
- **Speed prior** · 2026 · 预印本 · [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · [项目](https://mllab.snu.ac.kr/projects/learned_speed_prior)
  - Retiming Robot Demonstrations with a Learned Speed Prior
  - 从 DROID 遥操作与 FastUMI-100K 手持数据学速度先验，把示教重定时到手持节奏；真机 6.02 → 3.50 s，成功率不变
- **EgoSpeedUp** · 2026 · 预印本 · [arXiv 2609.29310](https://arxiv.org/abs/2609.29310)
  - EgoSpeedUp: Transferring Human Manipulation Tempo to Robot Policies
  - 用人类视频的分阶段节奏重定时机器人示教，执行时间 −36.5%

### B2. 推理时重定时与速度条件策略

- **SAIL** · 2025 · CoRL 2025 · [arXiv 2506.11948](https://arxiv.org/abs/2506.11948) · [项目](https://nadunranawaka1.github.io/sail-policy)
  - SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies
  - 全栈处理：误差自适应引导、预测到达位姿 + 高增益 OSC、按复杂度调速、延迟感知调度；仿真 4×、真机 3.2×
- **RACE** · 2026 · ICLR 2026 · 无 arXiv · [OpenReview](https://openreview.net/forum?id=INsLvSCJ4z) · [项目](https://clvrai.github.io/RACE)
  - Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed
  - 模仿期望状态 + TOPP-RA 在机器人限幅下重定时每块，最高 4×
- **FreeSpeed** · 2026 · 预印本 · [arXiv 2610.05734](https://arxiv.org/abs/2610.05734) · [项目](https://yuxuanhu9.github.io/FreeSpeed)
  - FreeSpeed: Training-Free Speed Control for Generative Robot Policies
  - 按相邻动作方向不一致性重采样动作块，真机 0.38–1.97× 可在线调
- **SuP** · 2026 · 预印本 · [arXiv 2603.20658](https://arxiv.org/abs/2603.20658)
  - Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation
  - 离线 RL 训练外挂调度器，世界模型状态偏差作安全代理，1.8×
- **TempoVLA** · 2026 · 预印本 · [arXiv 2606.06491](https://arxiv.org/abs/2606.06491)
  - TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
  - 变速轨迹增广 + 速度条件，多模态 LLM 按阶段选速度
- **PaceVLA** · 2026 · 预印本 · [arXiv 2610.25961](https://arxiv.org/abs/2610.25961) · [项目](https://pacevla.github.io)
  - PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models
  - 多时间粒度解码器 + 路由，最高 1.8×；传送带 3.6 → 6.3 件/分钟
- **AutoSpeed** · 2026 · ECCV 2026 · [arXiv 2607.01051](https://arxiv.org/abs/2607.01051)
  - AutoSpeed: Annotation-Free Stage-Adaptive Motion Speed Learning for Robot Manipulation
  - 无标注地按阶段学习速度
- **RoboPace** · 2026 · 预印本 · [arXiv 2610.09696](https://arxiv.org/abs/2610.09696) · [项目](https://robopace.airoa.io)
  - RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies
  - 在线 TOPP-RA，在预测接触附近设速度上限；5 个指令中 4 个用时约一半
- **EPCC** · 2026 · 预印本 · [arXiv 2609.22798](https://arxiv.org/abs/2609.22798) · [项目](https://expert-play-contouring.netlify.app)
  - Expert-Play Contouring Control: Faster-than-Demonstration Planning from Slow Expert and Fast Play
  - 慢专家轨迹给轮廓，快速 play 数据训练的世界模型给动力学，吞吐 2.0×

### B3. 提升节拍的 RL

- **HIL-SERL** · 2024 · Science Robotics 2025† · [arXiv 2410.21845](https://arxiv.org/abs/2410.21845) · [项目](https://hil-serl.github.io)
  - Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning
  - 真机 RL 1–2.5 h；节拍比模仿学习快 1.8×（5.4 s vs 9.6 s），成功率约 2×
- **ConRFT** · 2025 · RSS 2025† · [arXiv 2502.05450](https://arxiv.org/abs/2502.05450) · [项目](https://cccedric.github.io/conrft)
  - ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy
  - Octo + 一致性头，离线 BC+Q → 人在环在线 RL；45–90 min 达 96.3%，episode 缩短 1.9×
- **π*0.6** · 2025 · 预印本 · [arXiv 2511.14759](https://arxiv.org/abs/2511.14759) · [项目](https://pi.website/blog/pistar06)
  - π*0.6: a VLA That Learns From Experience
  - RECAP：价值函数 + 优势条件化，利用示教、rollout 与人工干预；最难任务每小时成功数 >2×、失败约减半
- **RL-100** · 2025 · 预印本 · [arXiv 2510.14830](https://arxiv.org/abs/2510.14830) · [项目](https://lei-kun.github.io/RL-100)
  - RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning
  - 模仿 → 离线 RL → 在线 RL，1000/1000 成功，完成时间达到或超过遥操作专家
- **SpeedTuning** · 2026 · ICRA 2025（arXiv comment） · [arXiv 2608.09138](https://arxiv.org/abs/2608.09138) · [项目](https://daivdyuan.github.io/speed-tuning)
  - SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning
  - 单独的 RL 策略逐块预测速度因子，>2.4×
- **SpeedAug** · 2025 · 预印本 · [arXiv 2512.00062](https://arxiv.org/abs/2512.00062)
  - SpeedAug: Policy Acceleration via Tempo-Enriched Policy and RL Fine-Tuning
  - 节奏增广先验 + RL 调节奏，真机 16 min 在线后吞吐 1.8×
- **PAKT** · 2026 · CoRL 2026（arXiv comment） · [arXiv 2609.25630](https://arxiv.org/abs/2609.25630) · [项目](https://pakt-website.github.io/pakt-website)
  - PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning
  - 执行限幅下的示教 + 参考生成器 + 力矩级阻抗控制，节拍比 HIL-SERL 再降 23–48%
- **SPARR** · 2026 · 预印本 · [arXiv 2602.23253](https://arxiv.org/abs/2602.23253)
  - SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly
  - 仿真基策略 + 真实视觉残差，节拍 −29.7%，成功率 +38.4%

### B4. 遥操作与数据采集

- **UMI** · 2024 · RSS 2024† · [arXiv 2402.10329](https://arxiv.org/abs/2402.10329) · [项目](https://umi-gripper.github.io)
  - Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots
  - 手持夹爪以人的速度采动态示教，推理时做延迟匹配
- **I2RLC** · 2026 · 预印本 · [arXiv 2604.16850](https://arxiv.org/abs/2604.16850)
  - Refinement of Accelerated Demonstrations via Incremental Iterative Reference Learning Control for Fast Contact-Rich Imitation Learning
  - 迭代学习控制逐步提速并精化示教，示教最高 10× 加速
- **VarSpeed-BIL** · 2021 · IEEE 期刊 2022（arXiv note） · [arXiv 2102.10283](https://arxiv.org/abs/2102.10283)
  - Imitation Learning for Variable Speed Contact Motion for Operation up to Control Bandwidth
  - 双边控制力感知示教，速度作为指令输入，接近控制带宽

### B5. 动力学、控制与延迟

- **STDArm** · 2025 · RSS 2025 · [arXiv 2504.18792](https://arxiv.org/abs/2504.18792)
  - STDArm: Transferring Visuomotor Policies From Static Data Training to Dynamic Robot Manipulation
  - 动作管理器 + 运动稳定器 + 在线延迟估计，静态数据训练的策略用于移动底盘
- **FODMP** · 2026 · 预印本 · [arXiv 2603.24806](https://arxiv.org/abs/2603.24806)
  - FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent Robot Actions
  - 一步扩散生成带加速度曲线的运动基元，推理快 7–10×，可接快球
- **TossingBot** · 2019 · RSS 2019 · [arXiv 1903.11239](https://arxiv.org/abs/1903.11239) · [项目](https://tossingbot.cs.princeton.edu)
  - TossingBot: Learning to Throw Arbitrary Objects with Residual Physics
  - 物理预测释放速度 + 学习残差，每小时 500+ 次拾取

### B6. 速度基准与指标

- **ParcelStow** · 2026 · 预印本 · [arXiv 2609.01453](https://arxiv.org/abs/2609.01453) · [代码](https://github.com/coenwerem/parcelstow)
  - Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds
  - 示教最高速度下专家 84%、ACT 53%；47 个失败中 35 个是插入错位
- **LIBERO-Dynamic** · 2026 · 预印本 · [arXiv 2610.24579](https://arxiv.org/abs/2610.24579)
  - LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments
  - 物体速度分档，世界时间按标定的模型延迟推进；所有策略都退化

## C. 少量遥操作数据 + 仿真

### C1. 仿真–真实共训练

- **Sim&Real Co-Train** · 2025 · 预印本 · [arXiv 2503.24361](https://arxiv.org/abs/2503.24361) · [项目](https://co-training.github.io)
  - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation
  - 每任务 20 条真实 + 约 1k 条 MimicGen 类仿真，仿真采样比 0.9–0.99；6 任务平均 45.3 → 83.2%
- **Sim&Real Pushing** · 2025 · IROS 2025 · [arXiv 2503.22634](https://arxiv.org/abs/2503.22634) · [项目](https://sim-and-real-cotraining.github.io)
  - Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies for Planar Pushing from Pixels
  - 仿真收益会饱和，只有更多真实数据能抬高上限；接触任务中物理 gap 比视觉 gap 更重要
- **DreamGen** · 2025 · CoRL 2025 · [arXiv 2505.12705](https://arxiv.org/abs/2505.12705) · [代码](https://github.com/NVIDIA/GR00T-Dreams)
  - DreamGen: Unlocking Generalization in Robot Learning through Video World Models
  - 只遥操作 1 个任务，视频世界模型生成"神经轨迹"，学会 22 个新行为；另见 [real2sim](../real2sim/papers.md) §9
- **RoboTwin 2.0** · 2025 · 预印本 · [arXiv 2506.18088](https://arxiv.org/abs/2506.18088) · [项目](https://robotwin-platform.github.io)
  - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation
  - 10 条真实 + 1,000 条五轴域随机化合成数据，相对提升 +367%
- **R2S2R Grounding** · 2026 · 预印本 · [arXiv 2610.00821](https://arxiv.org/abs/2610.00821) · [项目](https://industrialnext.github.io/r2s2r-grounding)
  - Getting Out and Getting Back: World and Behavior Grounding in Real2Sim2Real Co-Training
  - 100 条真实 + 1,500 条仿真，52 → 86%；物理对齐 +18 点、行为对齐 +10 点
- **MetaGenSim** · 2026 · CoRL 2026 · [arXiv 2610.19479](https://arxiv.org/abs/2610.19479) · [项目](https://meta-gensim.github.io)
  - Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training
  - 元学习"仿真什么"；每任务 10 条真实，VLA 19/80 → 52/80
- **SARI** · 2026 · 预印本 · [arXiv 2610.02804](https://arxiv.org/abs/2610.02804) · [项目](https://icra27-sari.vercel.app)
  - SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation
  - GS 孪生生成自由空间接近段，真实数据只采接触段；采集时间 −34.3%

### C2. 纯合成数据预训练

- **GraspVLA** · 2025 · 预印本 · [arXiv 2505.03233](https://arxiv.org/abs/2505.03233) · [项目](https://pku-epic.github.io/GraspVLA-web)
  - GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data
  - 十亿帧合成抓取数据，零样本抓取约 90%
- **InternData-A1** · 2025 · 预印本 · [arXiv 2511.16651](https://arxiv.org/abs/2511.16651)
  - InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy
  - 630k 条 / 7,433 h 纯仿真预训练达到官方 π0 水平；仿真:真实"汇率"1:1 到 8:1
- **MolmoBot** · 2026 · 预印本 · [arXiv 2603.16861](https://arxiv.org/abs/2603.16861)
  - MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation
  - 1.8M 条 MuJoCo 仿真轨迹，零真实数据，真机抓放 79.2%（π0.5 为 39.2%）
- **Sim2Real-VLA Study** · 2026 · 预印本 · [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
  - Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models
  - >10k 次真机试验；空间随机化最关键，逐帧随机化优于逐 episode；另见 [real2sim](../real2sim/papers.md) §10

### C3. 仿真 RL 微调

- **RL4VLA** · 2025 · NeurIPS 2025 · [arXiv 2505.19789](https://arxiv.org/abs/2505.19789) · [项目](https://rlvla.github.io)
  - What Can RL Bring to VLA Generalization? An Empirical Study
  - ManiSkill 中 PPO 优于 DPO、GRPO，提升语义与执行层面 OOD 泛化
- **VLA-RL** · 2025 · 预印本 · [arXiv 2505.18719](https://arxiv.org/abs/2505.18719)
  - VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning
  - OpenVLA-7B 轨迹级 RL + VLM 过程奖励，LIBERO 40 任务 +4.5%
- **RIPT-VLA** · 2025 · 预印本 · [arXiv 2505.17016](https://arxiv.org/abs/2505.17016) · [项目](https://ariostgx.github.io/ript_vla)
  - Interactive Post-Training for Vision-Language-Action Models
  - 无 critic 的留一法优势；1 条示教 4% → 97%
- **SimpleVLA-RL** · 2025 · 预印本 · [arXiv 2509.09674](https://arxiv.org/abs/2509.09674) · [代码](https://github.com/PRIME-RL/SimpleVLA-RL)
  - SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning
  - 结果奖励 RL；LIBERO-Long 17.3 → 91.7%；零真实数据下真机 17.5 → 38.5%
- **RLinf-VLA** · 2025 · RSS 2026 · [arXiv 2509.15965](https://arxiv.org/abs/2509.15965) / [arXiv 2510.06710](https://arxiv.org/abs/2510.06710) · [代码](https://github.com/RLinf/RLinf)
  - RLinf / RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models
  - 统一 VLA RL 基础设施；LIBERO-130 98.11%；真机初步测试 RL 后动作更直接
- **RL-Co** · 2026 · 预印本 · [arXiv 2602.12628](https://arxiv.org/abs/2602.12628) · [项目](https://rl-co-training.github.io)
  - Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models
  - SFT 共训练 → 仿真 RL + 真实 SFT 锚定损失；真机 +24%（OpenVLA）/ +20%（π0.5）；Open Drawer 上 200 条纯真实基线不优于 20 条的 RL-Co
- **GenWorld-RL** · 2026 · CoRL 2026 · [arXiv 2603.18532](https://arxiv.org/abs/2603.18532) · [项目](https://horizonrobotics.github.io/gail/scale-vla-rl)
  - Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds
  - 100 个生成场景中 RL，零任务示教；真机 21.7 → 75%，执行快 1.13×
- **TwinRL** · 2026 · 预印本 · [arXiv 2602.09023](https://arxiv.org/abs/2602.09023) · [项目](https://twinrl.github.io)
  - TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation
  - 手机扫描 3DGS 孪生 + 30 条示教 → 孪生 RL → 人在环真机 RL，约 20 min 达近 100%
- **iRe-VLA** · 2025 · ICRA 2025 · [arXiv 2501.16664](https://arxiv.org/abs/2501.16664)
  - Improving Vision-Language-Action Model with Online Reinforcement Learning
  - RL 与监督学习交替，稳定大 VLA 的 RL

### C4. 真机 RL 微调

- **RLDG** · 2024 · 预印本 · [arXiv 2412.09858](https://arxiv.org/abs/2412.09858) · [项目](https://generalist-distillation.github.io)
  - RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning
  - RL 专家生成的数据蒸馏进通才策略，比人类示教高最多 40%
- **PA-RL** · 2024 · 预印本 · [arXiv 2412.06685](https://arxiv.org/abs/2412.06685) · [项目](https://policyagnosticrl.github.io)
  - Policy Agnostic RL: Offline RL and Online RL Fine-Tuning of Any Class and Backbone
  - 与策略类别无关的 RL，OpenVLA 40 min 内 40 → 70%
- **DSRL** · 2025 · 预印本 · [arXiv 2506.15799](https://arxiv.org/abs/2506.15799) · [项目](https://diffusion-steering.github.io)
  - Steering Your Diffusion Policy with Latent Space Reinforcement Learning
  - 冻结权重，对输入噪声做 SAC；首次真机 RL 微调 π0
- **RLT** · 2026 · 预印本 · [arXiv 2604.23073](https://arxiv.org/abs/2604.23073) · [项目](https://pi.website/research/rlt)
  - RL Token: Bootstrapping Online RL with Vision-Language-Action Models
  - π0.6 上用"RL token"训练小 actor-critic；关键阶段快最多 3×，部分任务快于遥操作
- **EXPO-FT** · 2026 · 预印本 · [arXiv 2605.25477](https://arxiv.org/abs/2605.25477) · [项目](https://pd-perry.github.io/expo-ft)
  - EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models
  - 冻结 π0.5 + 编辑策略的离策略 RL；每任务 10–40 条示教，平均 19.1 min 在线达 30/30

ConRFT、π*0.6、HIL-SERL、RL-100 也属于本节，列在 B3。

### C5. 残差 RL

- **ResiP** · 2024 · 预印本 · [arXiv 2407.16677](https://arxiv.org/abs/2407.16677) · [项目](https://residual-assembly.github.io)
  - From Imitation to Refinement -- Residual RL for Precise Assembly
  - 分块扩散策略上的闭环残差 PPO → 蒸馏到 RGB；真机 50–60% vs 纯真实 20–30%
- **Policy Decorator** · 2024 · 预印本 · [arXiv 2412.13630](https://arxiv.org/abs/2412.13630) · [项目](https://policydecorator.github.io)
  - Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model
  - 与模型无关的残差 RL，受控探索，保持动作平滑
- **ResFiT** · 2025 · 预印本 · [arXiv 2509.19301](https://arxiv.org/abs/2509.19301) · [项目](https://residual-offpolicy-rl.github.io)
  - Residual Off-Policy RL for Finetuning Behavior Cloning Policies
  - 真机 29 自由度人形上的离策略逐步残差，134 次 rollout 14 → 64%
- **PLD** · 2025 · 预印本 · [arXiv 2511.00091](https://arxiv.org/abs/2511.00091) · [项目](https://wenlixiao.com/self-improve-VLA-PLD)
  - Self-Improving Vision-Language-Action Models with Data Generation via Residual RL
  - 残差 RL 作为数据引擎再 SFT 回 VLA；真机 ≤2 h 达 100%
- **OC-ResRL** · 2026 · 预印本 · [arXiv 2606.18953](https://arxiv.org/abs/2606.18953) · [项目](https://microsoft.com/en-us/research/articles/object-centric-residual-rl)
  - Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement
  - GR00T N1.5 + 仅在仿真训练的物体位姿空间残差，零样本真机 42 → 76%
- **VLaRL** · 2026 · 预印本 · [arXiv 2609.30868](https://arxiv.org/abs/2609.30868)
  - VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL
  - 在 VLA 潜空间上训练仿真残差 + 仿真→真实潜映射；按钮 67.5 → 100%

## 补充（已核实，只列编号）

- 推理与执行：CEED-VLA (2506.13725)，MoLe-VLA (2503.20384)，SP-VLA (2506.12723)，LightVLA (2509.12594)，两步去噪 (2609.39822)，Coda (2609.21216)，HybridFlow (2602.13718)，Xiaomi-Robotics-0 (2602.12684)，Realtime-VLA V2 (2603.26360)，Reflex (2607.14695, ICML 2026)，FlashVLA (2608.27384)，DiscreteRTC (2604.25050)，AR 策略实时执行 (2606.13355)，VLA-Perf (2602.18397)，Consistency Policy (2405.07503)，One-Step Diffusion Policy (2410.21257)，S2 调用调度 (2610.05025, NeurIPS 2026; 2610.21160)，综述 2510.24795 (TPAMI)、2510.17111
- 速度：Proleptic Temporal Ensemble (2410.16981)，ISR (2606.22907)，TempoBridge (2610.09451)，VFILC (2606.20056, IROS 2026)，变速示教回放 (2412.03252)，无传感器四通道双边遥操作 (2507.06174)，VR vs SpaceMouse (2601.13042)，DQAF (2605.26349)，MPC 支架真机 RL (2609.14878)，SiLRI (2512.24288)，时间最优手内 RL (2411.13148)，全身抛掷 (2506.16986)，乒乓球 (2408.03906)，ForeTime-VLA (2608.20735)
- 少量数据 + 仿真：Sim-Real 域适应共训练 (2509.18631, NeurIPS 2025)，TUCO (2610.05407)，TacCoRL (2606.11743)，LWD (2605.00416)，BORA (2605.30226)，BEE (2609.27450)，VLA-Precision (2609.04355)，HiL-ResRL (2606.22860)，ACCRUE (2610.18596)，VLA-RFT (2510.00406)，WMPO (2511.09515)，WoVR (2602.13977)，World-Gymnast (2602.02454)
- 未找到 arXiv：MiniVLA
