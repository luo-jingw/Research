# vla-fast-control 论文目录

- 快照日期：2026-10-30
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment 字段或论文集确认的发表处；"arXiv" 表示未找到发表处。标 † 的发表处未在一手来源确认，见根目录 `issues.md` → ISSUE-003。
- 每条的标题、年份、arXiv 编号均经 arxiv.org 页面核实；数字取自摘要或正文。
- 延迟数字都注明硬件；不同论文的测量口径（是否含图像编码、网络、几步去噪）不同，不能直接横比。
- 分节对应 [survey.md](survey.md) 的分类。

## A. 推理加速与实时执行

### A1. 动作表示与解码

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| π0 | π0: A Vision-Language-Action Flow Model for General Robot Control | 2024 | RSS 2025 | 2410.24164 | physicalintelligence.company/blog/pi0 | VLM + flow matching 动作专家，10 步去噪、动作块 H=50；RTX 4090 上 73 ms（图像编码 14 + 前缀 32 + 去噪 27），配合分块 50 Hz |
| FAST | FAST: Efficient Action Tokenization for Vision-Language-Action Models | 2025 | arXiv | 2501.09747 | pi.website/research/fast | DCT + BPE 动作 token 让自回归 VLA 能学高频动作；但每块约 750 ms，比扩散版 π0（约 100 ms）慢 |
| OpenVLA-OFT | Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | 2025 | RSS 2025 | 2502.19645 | openvla-oft.github.io | 并行解码 + 分块 + 连续 L1 回归；吞吐 26–43×，A100 单图 240 → 73 ms；LIBERO 76.5 → 97.1% |
| PD-VLA | PD-VLA: Accelerating VLA Model Integrated with Action Chunking via Parallel Decoding | 2025 | IROS 2025 | 2503.02310 | — | 免训练 Jacobi 不动点并行解码，执行频率 2.52× |
| DD-VLA | Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in VLA Policies | 2025 | ICML 2026 | 2508.20072 | — | VLM 内掩码离散扩散并行细化动作，真机 9.69 Hz |
| DriftingVLA | DriftingVLA: Native One-Step VLA Generation via Per-Dimension Temporal Drifting | 2026 | arXiv | 2608.29749 | — | 原生一步生成动作块，3.36× 更快，成功率优于多步 |
| One-step Euler | When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies | 2026 | CoRL 2026 | 2610.30735 | — | 不重训、只用 1 步 Euler，延迟降 1.6–4.8×；大模型无明显损失，小模型在长视界上退化 |

### A2. 模型级加速

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| DeeR-VLA | DeeR-VLA: Dynamic Inference of Multimodal LLMs for Efficient Robot Execution | 2024 | NeurIPS 2024 | 2411.02359 | github.com/yueyang130/DeeR-VLA | 多出口 LLM 按难度提前退出，LLM 计算降 5.2–6.5× |
| VLA-Cache | VLA-Cache: Efficient VLA Manipulation via Adaptive Token Caching | 2025 | NeurIPS 2025 | 2502.02175 | vla-cache.github.io | 跨帧复用静态视觉 token 的 KV，CUDA 延迟最多 1.7× |
| EfficientVLA | EfficientVLA: Training-Free Acceleration and Compression for VLA Models | 2025 | arXiv | 2506.10100 | — | 层剪枝 + 视觉 token 选择 + 扩散头缓存，1.93×，FLOPs 降到 28.9% |
| SpecPrune-VLA | SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning | 2025 | ICML 2026 | 2509.05614 | — | 用全局历史做静态 + 动态 token 剪枝，LIBERO 1.57×、真机 1.70× |
| Spec-VLA | Spec-VLA: Speculative Decoding for VLA Models with Relaxed Acceptance | 2025 | EMNLP 2025 | 2507.22424 | — | 对有序动作 token 做投机解码，按动作 bin 距离放宽接受，1.42× |
| BitVLA | BitVLA: 1-bit Vision-Language-Action Models for Robotics Manipulation | 2025 | arXiv | 2506.07530 | github.com/ustcwhy/BitVLA | 三值权重原生 1-bit VLA；A100 三图 73 ms vs OFT 321 ms，显存降 11× |
| QuantVLA | QuantVLA: Scale-Calibrated Post-Training Quantization for VLA Models | 2026 | CVPR 2026 | 2602.20309 | — | 含 DiT 动作头的 W4A8 后训练量化，π0.5 显存 4.27 → 1.28 GB；摘要未报延迟 |
| TinyVLA | TinyVLA: Towards Fast, Data-Efficient VLA Models for Robotic Manipulation | 2024 | arXiv | 2409.12514 | tiny-vla.github.io | 小 VLM + 扩散头，延迟比 OpenVLA 低约 20× |
| SmolVLA | SmolVLA: A VLA Model for Affordable and Efficient Robotics | 2025 | arXiv | 2506.01844 | github.com/huggingface/lerobot | 0.45B，开源异步推理栈；异步使任务时间 13.75 → 9.7 s |
| VLA-Adapter | VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model | 2025 | arXiv | 2509.09372 | vla-adapter.github.io | 0.5B 骨干 + Bridge Attention，36.5 ms / 219.2 Hz |
| TurboVLA | TurboVLA: Real-Time VLA Model at 32 Hz on an RTX 4090 with <1 GB VRAM | 2026 | arXiv | 2607.27205 | github.com/H-EmbodVis/TurboVLA | 去掉 LLM 通路，RTX 4090 上 31.2 ms、0.9 GiB |
| Realtime-VLA | Running VLAs at Real-time Speed | 2025 | arXiv | 2510.26742 | github.com/Dexmal/realtime-vla | CUDA graph、kernel 融合、去 CPU 开销；π0 双视角 RTX 4090 上 106.5 → 27.3 ms |

### A3. 执行级：分块、异步与实时分块

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| ACT | Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | 2023 | RSS 2023† | 2304.13705 | tonyzhaozh.github.io/aloha | 动作分块（k=100）+ 时间集成；2080 Ti 上约 10 ms，50 Hz |
| BID | Bidirectional Decoding: Improving Action Chunking via Guided Test-Time Sampling | 2024 | arXiv | 2408.17355 | bid-robot.github.io | 采样多个动作块，按前后一致性选择 |
| RTC | Real-Time Execution of Action Chunking Flow Policies | 2025 | NeurIPS 2025 | 2506.07339 | pi.website/research/real_time_chunking | 异步执行时冻结已承诺动作、用引导 flow 补全其余；π0.5 76 → 97 ms，注入 +200 ms 延迟仍不退化 |
| A2C2 | Leave No Observation Behind: Real-time Correction for VLA Action Chunks | 2025 | arXiv | 2509.23224 | — | 每步运行 0.31M 参数的修正头，比 RTC 高 7–23 个点（仿真） |
| VLASH | VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference | 2025 | arXiv | 2512.01031 | github.com/mit-han-lab/vlash | 用上一块动作把状态前推到执行时刻再推理；最大反应延迟 546 → 46 ms，任务完成快 1.5–2× |
| Training-time RTC | Training-Time Action Conditioning for Efficient Real-Time Chunking | 2025 | arXiv | 2512.05964 | — | 训练时模拟延迟并做前缀条件，π0.6 远程 H100 端到端 135 → 108 ms |
| Legato | Learning Native Continuation for Action Chunking Flow Policies | 2026 | RSS 2026 | 2602.12978 | lyfeng001.github.io/Legato | 从已知动作与噪声的混合开始去噪，平滑度与完成时间比 RTC 好约 10% |
| FASTER | FASTER: Rethinking Real-Time Flow VLAs | 2026 | arXiv | 2603.19199 | innovator-zero.github.io/FASTER | 近端动作先 1 步出，反应时间由首动作时间与执行视界决定；反应快 2.3–3.1× |
| EagleVLA | EagleVLA: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference | 2026 | CoRL 2026 Spotlight | 2607.12659 | github.com/PKU-SEC-Lab/EagleVLA | Jetson Orin 上 π0.5 原本约 1.4 s；控制频率比 PyTorch 高 14.71× |
| REACT | REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models | 2026 | CoRL 2026 Spotlight | 2610.12007 | react-vla.github.io | 交错时间步的滚动去噪缓冲；反应 734 ms，H50E50 为 1505 ms，人类 705 ms |

### A4. 双系统

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RoboDual | Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation | 2024 | arXiv | 2410.08001 | opendrivelab.com/RoboDual | OpenVLA 通才 + 20M DiT 专才，15 Hz vs 3.9 Hz，真机 +26.7% |
| Hi Robot | Hi Robot: Open-Ended Instruction Following with Hierarchical VLA Models | 2025 | ICML 2025 | 2502.19417 | pi.website/research/hirobot | 高层 VLM 输出语言子步骤给 π0；低层 73 ms |
| Helix | Helix（Figure AI 技术博客，无论文） | 2025 | 博客 | — | figure.ai/news/helix | S2 7B 7–9 Hz + S1 80M 200 Hz，潜向量耦合，机载嵌入式 GPU |
| GR00T N1 | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025 | arXiv | 2503.14734 | developer.nvidia.com/isaac/gr00t | 联合训练的 S2 10 Hz / S1 120 Hz；L40 上 16 步动作块 63.9 ms；也是仿真 + 视频生成数据共训练的代表（见 C1） |
| Gemini Robotics | Gemini Robotics: Bringing AI into the Physical World | 2025 | arXiv | 2503.20020 | — | 云端骨干 <160 ms + 机载解码器，端到端约 250 ms，有效 50 Hz |
| FiS-VLA | Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning | 2025 | arXiv | 2506.01953 | fast-in-slow.github.io | S1 共享 S2 的末端层；块长 8 时 117.7 Hz |

## B. 超过示教速度的执行

### B1. 示教重定时后重训

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| DemoSpeedup | DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration | 2025 | CoRL 2025† | 2506.05064 | demospeedup.github.io | 代理策略动作熵高的片段多下采样、精确片段少下采样，最高 3× |
| ESPADA | ESPADA: Execution Speedup via Semantics Aware Demonstration Data Downsampling for Imitation Learning | 2025 | arXiv | 2512.07371 | project-espada.github.io/espada | VLM-LLM 按夹爪–物体 3D 关系分段，只加速非关键段，约 2× |
| AdaTempo | AdaTempo: Learning Shared Relative Tempo from Demonstrations for Faster Robot Manipulation | 2026 | arXiv | 2610.02706 | — | 多条示教的相对节奏共识给出连续加速曲线，最高 3.57× |
| VOLT | VOLT: Vision and Language Trajectory Segmentation for Faster-than-Demonstration Policies | 2026 | arXiv | 2606.06323 | volt2026.github.io/VOLT2026 | 视觉语言模型分出精确段，其余下采样 |
| Speed prior | Retiming Robot Demonstrations with a Learned Speed Prior | 2026 | arXiv | 2610.32676 | mllab.snu.ac.kr/projects/learned_speed_prior | 从 DROID 遥操作与 FastUMI-100K 手持数据学速度先验，把示教重定时到手持节奏；真机 6.02 → 3.50 s，成功率不变 |
| EgoSpeedUp | EgoSpeedUp: Transferring Human Manipulation Tempo to Robot Policies | 2026 | arXiv | 2609.29310 | — | 用人类视频的分阶段节奏重定时机器人示教，执行时间 −36.5% |

### B2. 推理时重定时与速度条件策略

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| SAIL | SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies | 2025 | CoRL 2025 | 2506.11948 | nadunranawaka1.github.io/sail-policy | 全栈处理：误差自适应引导、预测到达位姿 + 高增益 OSC、按复杂度调速、延迟感知调度；仿真 4×、真机 3.2× |
| RACE | Time Optimal Execution of Action Chunk Policies Beyond Demonstration Speed | 2026 | ICLR 2026 | 无 arXiv（OpenReview INsLvSCJ4z） | clvrai.github.io/RACE | 模仿期望状态 + TOPP-RA 在机器人限幅下重定时每块，最高 4× |
| FreeSpeed | FreeSpeed: Training-Free Speed Control for Generative Robot Policies | 2026 | arXiv | 2610.05734 | yuxuanhu9.github.io/FreeSpeed | 按相邻动作方向不一致性重采样动作块，真机 0.38–1.97× 可在线调 |
| SuP | Speedup Patch: Learning a Plug-and-Play Policy to Accelerate Embodied Manipulation | 2026 | arXiv | 2603.20658 | — | 离线 RL 训练外挂调度器，世界模型状态偏差作安全代理，1.8× |
| TempoVLA | TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies | 2026 | arXiv | 2606.06491 | — | 变速轨迹增广 + 速度条件，多模态 LLM 按阶段选速度 |
| PaceVLA | PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models | 2026 | arXiv | 2610.25961 | pacevla.github.io | 多时间粒度解码器 + 路由，最高 1.8×；传送带 3.6 → 6.3 件/分钟 |
| AutoSpeed | AutoSpeed: Annotation-Free Stage-Adaptive Motion Speed Learning for Robot Manipulation | 2026 | ECCV 2026 | 2607.01051 | — | 无标注地按阶段学习速度 |
| RoboPace | RoboPace: Contact-Aware Time-Optimal Retiming for Action-Chunk Policies | 2026 | arXiv | 2610.09696 | robopace.airoa.io | 在线 TOPP-RA，在预测接触附近设速度上限；5 个指令中 4 个用时约一半 |
| EPCC | Expert-Play Contouring Control: Faster-than-Demonstration Planning from Slow Expert and Fast Play | 2026 | arXiv | 2609.22798 | expert-play-contouring.netlify.app | 慢专家轨迹给轮廓，快速 play 数据训练的世界模型给动力学，吞吐 2.0× |

### B3. 提升节拍的 RL

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| HIL-SERL | Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning | 2024 | Science Robotics 2025† | 2410.21845 | hil-serl.github.io | 真机 RL 1–2.5 h；节拍比模仿学习快 1.8×（5.4 s vs 9.6 s），成功率约 2× |
| ConRFT | ConRFT: A Reinforced Fine-tuning Method for VLA Models via Consistency Policy | 2025 | RSS 2025† | 2502.05450 | cccedric.github.io/conrft | Octo + 一致性头，离线 BC+Q → 人在环在线 RL；45–90 min 达 96.3%，episode 缩短 1.9× |
| π*0.6 | π*0.6: a VLA That Learns From Experience | 2025 | arXiv | 2511.14759 | pi.website/blog/pistar06 | RECAP：价值函数 + 优势条件化，利用示教、rollout 与人工干预；最难任务每小时成功数 >2×、失败约减半 |
| RL-100 | RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning | 2025 | arXiv | 2510.14830 | lei-kun.github.io/RL-100 | 模仿 → 离线 RL → 在线 RL，1000/1000 成功，完成时间达到或超过遥操作专家 |
| SpeedTuning | SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning | 2026 | ICRA 2025（arXiv comment） | 2608.09138 | daivdyuan.github.io/speed-tuning | 单独的 RL 策略逐块预测速度因子，>2.4× |
| SpeedAug | SpeedAug: Policy Acceleration via Tempo-Enriched Policy and RL Fine-Tuning | 2025 | arXiv | 2512.00062 | — | 节奏增广先验 + RL 调节奏，真机 16 min 在线后吞吐 1.8× |
| PAKT | PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning | 2026 | CoRL 2026（arXiv comment） | 2609.25630 | pakt-website.github.io/pakt-website | 执行限幅下的示教 + 参考生成器 + 力矩级阻抗控制，节拍比 HIL-SERL 再降 23–48% |
| SPARR | SPARR: Simulation-based Policies with Asymmetric Real-world Residuals for Assembly | 2026 | arXiv | 2602.23253 | — | 仿真基策略 + 真实视觉残差，节拍 −29.7%，成功率 +38.4% |

### B4. 遥操作与数据采集

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| UMI | Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots | 2024 | RSS 2024† | 2402.10329 | umi-gripper.github.io | 手持夹爪以人的速度采动态示教，推理时做延迟匹配 |
| I2RLC | Refinement of Accelerated Demonstrations via Incremental Iterative Reference Learning Control for Fast Contact-Rich Imitation Learning | 2026 | arXiv | 2604.16850 | — | 迭代学习控制逐步提速并精化示教，示教最高 10× 加速 |
| VarSpeed-BIL | Imitation Learning for Variable Speed Contact Motion for Operation up to Control Bandwidth | 2021 | IEEE 期刊 2022（arXiv note） | 2102.10283 | — | 双边控制力感知示教，速度作为指令输入，接近控制带宽 |

### B5. 动力学、控制与延迟

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| STDArm | STDArm: Transferring Visuomotor Policies From Static Data Training to Dynamic Robot Manipulation | 2025 | RSS 2025 | 2504.18792 | — | 动作管理器 + 运动稳定器 + 在线延迟估计，静态数据训练的策略用于移动底盘 |
| FODMP | FODMP: Fast One-Step Diffusion of Movement Primitives Generation for Time-Dependent Robot Actions | 2026 | arXiv | 2603.24806 | — | 一步扩散生成带加速度曲线的运动基元，推理快 7–10×，可接快球 |
| TossingBot | TossingBot: Learning to Throw Arbitrary Objects with Residual Physics | 2019 | RSS 2019 | 1903.11239 | tossingbot.cs.princeton.edu | 物理预测释放速度 + 学习残差，每小时 500+ 次拾取 |

### B6. 速度基准与指标

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| ParcelStow | Does Imitation Learning Preserve Temporal Robustness in Dexterous Manipulation? An Expert-Learner Comparison Across Task Execution Speeds | 2026 | arXiv | 2609.01453 | github.com/coenwerem/parcelstow | 示教最高速度下专家 84%、ACT 53%；47 个失败中 35 个是插入错位 |
| LIBERO-Dynamic | LIBERO-Dynamic: Benchmarking Robotic Manipulation in Dynamic Environments | 2026 | arXiv | 2610.24579 | — | 物体速度分档，世界时间按标定的模型延迟推进；所有策略都退化 |

## C. 少量遥操作数据 + 仿真

### C1. 仿真–真实共训练

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| Sim&Real Co-Train | Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation | 2025 | arXiv | 2503.24361 | co-training.github.io | 每任务 20 条真实 + 约 1k 条 MimicGen 类仿真，仿真采样比 0.9–0.99；6 任务平均 45.3 → 83.2% |
| Sim&Real Pushing | Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies for Planar Pushing from Pixels | 2025 | IROS 2025 | 2503.22634 | sim-and-real-cotraining.github.io | 仿真收益会饱和，只有更多真实数据能抬高上限；接触任务中物理 gap 比视觉 gap 更重要 |
| DreamGen | DreamGen: Unlocking Generalization in Robot Learning through Video World Models | 2025 | CoRL 2025 | 2505.12705 | github.com/NVIDIA/GR00T-Dreams | 只遥操作 1 个任务，视频世界模型生成"神经轨迹"，学会 22 个新行为；另见 [real2sim](../real2sim/papers.md) §9 |
| RoboTwin 2.0 | RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | 2025 | arXiv | 2506.18088 | robotwin-platform.github.io | 10 条真实 + 1,000 条五轴域随机化合成数据，相对提升 +367% |
| R2S2R Grounding | Getting Out and Getting Back: World and Behavior Grounding in Real2Sim2Real Co-Training | 2026 | arXiv | 2610.00821 | industrialnext.github.io/r2s2r-grounding | 100 条真实 + 1,500 条仿真，52 → 86%；物理对齐 +18 点、行为对齐 +10 点 |
| MetaGenSim | Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training | 2026 | CoRL 2026 | 2610.19479 | meta-gensim.github.io | 元学习"仿真什么"；每任务 10 条真实，VLA 19/80 → 52/80 |
| SARI | SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation | 2026 | arXiv | 2610.02804 | icra27-sari.vercel.app | GS 孪生生成自由空间接近段，真实数据只采接触段；采集时间 −34.3% |

### C2. 纯合成数据预训练

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| GraspVLA | GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data | 2025 | arXiv | 2505.03233 | pku-epic.github.io/GraspVLA-web | 十亿帧合成抓取数据，零样本抓取约 90% |
| InternData-A1 | InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy | 2025 | arXiv | 2511.16651 | — | 630k 条 / 7,433 h 纯仿真预训练达到官方 π0 水平；仿真:真实"汇率"1:1 到 8:1 |
| MolmoBot | MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation | 2026 | arXiv | 2603.16861 | — | 1.8M 条 MuJoCo 仿真轨迹，零真实数据，真机抓放 79.2%（π0.5 为 39.2%） |
| Sim2Real-VLA Study | Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models | 2026 | arXiv | 2603.22876 | — | >10k 次真机试验；空间随机化最关键，逐帧随机化优于逐 episode；另见 [real2sim](../real2sim/papers.md) §10 |

### C3. 仿真 RL 微调

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RL4VLA | What Can RL Bring to VLA Generalization? An Empirical Study | 2025 | NeurIPS 2025 | 2505.19789 | rlvla.github.io | ManiSkill 中 PPO 优于 DPO、GRPO，提升语义与执行层面 OOD 泛化 |
| VLA-RL | VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning | 2025 | arXiv | 2505.18719 | — | OpenVLA-7B 轨迹级 RL + VLM 过程奖励，LIBERO 40 任务 +4.5% |
| RIPT-VLA | Interactive Post-Training for Vision-Language-Action Models | 2025 | arXiv | 2505.17016 | ariostgx.github.io/ript_vla | 无 critic 的留一法优势；1 条示教 4% → 97% |
| SimpleVLA-RL | SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | 2025 | arXiv | 2509.09674 | github.com/PRIME-RL/SimpleVLA-RL | 结果奖励 RL；LIBERO-Long 17.3 → 91.7%；零真实数据下真机 17.5 → 38.5% |
| RLinf-VLA | RLinf / RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models | 2025 | RSS 2026 | 2509.15965 / 2510.06710 | github.com/RLinf/RLinf | 统一 VLA RL 基础设施；LIBERO-130 98.11%；真机初步测试 RL 后动作更直接 |
| RL-Co | Beyond Imitation: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models | 2026 | arXiv | 2602.12628 | rl-co-training.github.io | SFT 共训练 → 仿真 RL + 真实 SFT 锚定损失；真机 +24%（OpenVLA）/ +20%（π0.5）；Open Drawer 上 200 条纯真实基线不优于 20 条的 RL-Co |
| GenWorld-RL | Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds | 2026 | CoRL 2026 | 2603.18532 | horizonrobotics.github.io/gail/scale-vla-rl | 100 个生成场景中 RL，零任务示教；真机 21.7 → 75%，执行快 1.13× |
| TwinRL | TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation | 2026 | arXiv | 2602.09023 | twinrl.github.io | 手机扫描 3DGS 孪生 + 30 条示教 → 孪生 RL → 人在环真机 RL，约 20 min 达近 100% |
| iRe-VLA | Improving Vision-Language-Action Model with Online Reinforcement Learning | 2025 | ICRA 2025 | 2501.16664 | — | RL 与监督学习交替，稳定大 VLA 的 RL |

### C4. 真机 RL 微调

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| RLDG | RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning | 2024 | arXiv | 2412.09858 | generalist-distillation.github.io | RL 专家生成的数据蒸馏进通才策略，比人类示教高最多 40% |
| PA-RL | Policy Agnostic RL: Offline RL and Online RL Fine-Tuning of Any Class and Backbone | 2024 | arXiv | 2412.06685 | policyagnosticrl.github.io | 与策略类别无关的 RL，OpenVLA 40 min 内 40 → 70% |
| DSRL | Steering Your Diffusion Policy with Latent Space Reinforcement Learning | 2025 | arXiv | 2506.15799 | diffusion-steering.github.io | 冻结权重，对输入噪声做 SAC；首次真机 RL 微调 π0 |
| RLT | RL Token: Bootstrapping Online RL with Vision-Language-Action Models | 2026 | arXiv | 2604.23073 | pi.website/research/rlt | π0.6 上用"RL token"训练小 actor-critic；关键阶段快最多 3×，部分任务快于遥操作 |
| EXPO-FT | EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models | 2026 | arXiv | 2605.25477 | pd-perry.github.io/expo-ft | 冻结 π0.5 + 编辑策略的离策略 RL；每任务 10–40 条示教，平均 19.1 min 在线达 30/30 |

ConRFT、π*0.6、HIL-SERL、RL-100 也属于本节，列在 B3。

### C5. 残差 RL

| 简称 | 标题 | 年份 | 会议/期刊 | arXiv | 项目/代码 | 一句话 |
|---|---|---|---|---|---|---|
| ResiP | From Imitation to Refinement -- Residual RL for Precise Assembly | 2024 | arXiv | 2407.16677 | residual-assembly.github.io | 分块扩散策略上的闭环残差 PPO → 蒸馏到 RGB；真机 50–60% vs 纯真实 20–30% |
| Policy Decorator | Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model | 2024 | arXiv | 2412.13630 | policydecorator.github.io | 与模型无关的残差 RL，受控探索，保持动作平滑 |
| ResFiT | Residual Off-Policy RL for Finetuning Behavior Cloning Policies | 2025 | arXiv | 2509.19301 | residual-offpolicy-rl.github.io | 真机 29 自由度人形上的离策略逐步残差，134 次 rollout 14 → 64% |
| PLD | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | 2025 | arXiv | 2511.00091 | wenlixiao.com/self-improve-VLA-PLD | 残差 RL 作为数据引擎再 SFT 回 VLA；真机 ≤2 h 达 100% |
| OC-ResRL | Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement | 2026 | arXiv | 2606.18953 | microsoft.com/en-us/research/articles/object-centric-residual-rl | GR00T N1.5 + 仅在仿真训练的物体位姿空间残差，零样本真机 42 → 76% |
| VLaRL | VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL | 2026 | arXiv | 2609.30868 | — | 在 VLA 潜空间上训练仿真残差 + 仿真→真实潜映射；按钮 67.5 → 100% |

## 补充（已核实，未列入主表）

- 推理与执行：CEED-VLA (2506.13725)，MoLe-VLA (2503.20384)，SP-VLA (2506.12723)，LightVLA (2509.12594)，两步去噪 (2609.39822)，Coda (2609.21216)，HybridFlow (2602.13718)，Xiaomi-Robotics-0 (2602.12684)，Realtime-VLA V2 (2603.26360)，Reflex (2607.14695, ICML 2026)，FlashVLA (2608.27384)，DiscreteRTC (2604.25050)，AR 策略实时执行 (2606.13355)，VLA-Perf (2602.18397)，Consistency Policy (2405.07503)，One-Step Diffusion Policy (2410.21257)，S2 调用调度 (2610.05025, NeurIPS 2026; 2610.21160)，综述 2510.24795 (TPAMI)、2510.17111
- 速度：Proleptic Temporal Ensemble (2410.16981)，ISR (2606.22907)，TempoBridge (2610.09451)，VFILC (2606.20056, IROS 2026)，变速示教回放 (2412.03252)，无传感器四通道双边遥操作 (2507.06174)，VR vs SpaceMouse (2601.13042)，DQAF (2605.26349)，MPC 支架真机 RL (2609.14878)，SiLRI (2512.24288)，时间最优手内 RL (2411.13148)，全身抛掷 (2506.16986)，乒乓球 (2408.03906)，ForeTime-VLA (2608.20735)
- 少量数据 + 仿真：Sim-Real 域适应共训练 (2509.18631, NeurIPS 2025)，TUCO (2610.05407)，TacCoRL (2606.11743)，LWD (2605.00416)，BORA (2605.30226)，BEE (2609.27450)，VLA-Precision (2609.04355)，HiL-ResRL (2606.22860)，ACCRUE (2610.18596)，VLA-RFT (2510.00406)，WMPO (2511.09515)，WoVR (2602.13977)，World-Gymnast (2602.02454)
- 未找到 arXiv：MiniVLA
