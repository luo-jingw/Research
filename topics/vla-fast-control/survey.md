# VLA 实机快速控制综述

- 快照日期：2026-10-30
- 研究问题：用少量人工遥操作数据 + 仿真建模，训练出能在真机上快速执行的 VLA 策略。
- 引用格式：方法简称，元数据见 [papers.md](papers.md)，节号写作 `P§xn`（如 `P§A3`）。
- 本文只写可溯源到文献的内容。基于这些文献提出的研究设想记录在根目录 `opportunities.md`（`Area: vla-fast-control`）。

## 0. "快"的三层含义

- **反应快**（§2）
  - 问题：从观测到执行动作的延迟；动作块之间是否停顿或抖动
  - 衡量：推理延迟（ms）、控制频率（Hz）、反应时间
- **执行快**（§3）
  - 问题：动作本身比人工示教更快完成任务
  - 衡量：任务完成时间、节拍、吞吐量、相对示教的加速比
- **数据少**（§4）
  - 问题：少量遥操作示教 + 仿真或生成数据就能训出可部署策略
  - 衡量：真实示教条数、真机成功率

三层互相约束，文献中有直接证据：

- **推理延迟限制可达到的加速比**：SAIL 指出动作队列排空会让机器人停顿，延迟也给平均加速设了上限；RACE 为异步推理做测试时动作块搜索；LIBERO-Dynamic 按标定的模型延迟推进世界时间，所有策略都退化。
- **加速会改变动力学，需要仿真或动力学模型**：SAIL 自述没有处理机器人–物体动力学的变化，并呼吁引入动力学模型或仿真数据；EPCC 用快速 play 数据训练世界模型来弥补慢示教中缺失的快速动力学；Sim&Real Pushing 发现接触任务中物理 gap 比视觉 gap 更重要。
- **RL 同时提升成功率与速度**：折扣奖励天然奖励更早完成。HIL-SERL 1.8×、ConRFT 1.9×、π*0.6 每小时成功数 >2×、RLT 关键阶段最多 3×、GenWorld-RL 仿真 RL 后真机快 1.13×。

## 1. 全流程框架

把研究问题拆成六个环节，每个环节对应一组文献：

```
少量遥操作示教
  │  ① 采集：示教速度与质量受接口限制（UMI、PAKT、Speed prior）
  ▼
数据扩充
  │  ② 仿真 / 生成数据：共训练（Sim&Real Co-Train、RL-Co）、纯合成预训练（MolmoBot）、
  │     real2sim 孪生与数据生成（TwinRL、SARI；另见 real2sim 综述）
  ▼
策略
  │  ③ 选型：大 VLA + 双系统（GR00T N1、Helix），或小 VLA（SmolVLA、VLA-Adapter、TurboVLA）
  ▼
策略改进
  │  ④ RL：仿真 RL（SimpleVLA-RL、GenWorld-RL）、真机 RL（π*0.6、RLT、EXPO-FT）、残差 RL（OC-ResRL）
  ▼
提速
  │  ⑤ 速度：示教重定时（DemoSpeedup）、推理时重定时（SAIL、RACE）、速度条件 VLA（TempoVLA、PaceVLA）、RL 提节拍
  ▼
执行
     ⑥ 实时：推理加速（OFT、Realtime-VLA）、异步与实时分块（RTC、VLASH）、底层控制器（高增益 OSC、阻抗）
```

## 2. 反应快：推理加速与实时执行（P§A）

### 2.1 延迟预算

| 模型族 | 延迟 | 硬件 |
|---|---|---|
| OpenVLA 7B | 每动作 0.33 s（4–6 Hz） | A100 / RTX 4090 |
| OpenVLA-OFT | 单图 73 ms/块，三图 321 ms | A100 |
| π0 | 73 ms；工程优化后 27.3 ms | RTX 4090 |
| π0-FAST | 约 750 ms/块 | RTX 4090 |
| π0.5 | 5 步 76 ms；CUDA graph 23–32 ms | RTX 4090 / H100 |
| π0.5（机载） | 约 1.4 s | Jetson Orin |
| π0.6 | 端到端 108–135 ms | 远程 H100 |
| GR00T N1 | 63.9 ms/块；S2 10 Hz，S1 120 Hz | L40 |
| Helix | S2 7–9 Hz，S1 200 Hz | 机载嵌入式 GPU |
| Gemini Robotics | 端到端约 250 ms | 云 + 机载 |
| TurboVLA / VLA-Adapter | 31.2 / 36.5 ms | RTX 4090 |
| ACT | 约 10 ms | RTX 2080 Ti |

- 来源：OpenVLA-OFT、RoboDual（OpenVLA）；π0、Realtime-VLA（π0，双视角）；FAST；RTC、VLASH、EagleVLA（π0.5）；Training-time RTC（π0.6）；GR00T N1；Figure 博客（Helix）；Gemini Robotics；TurboVLA；VLA-Adapter；ACT。
- π0 的 73 ms 分解为图像编码 14 ms + VLM 前缀 32 ms + 10 步去噪 27 ms。

文献中的共同模式：桌面 GPU 上 2–3B 的 flow VLA 每块 25–80 ms，Jetson 级设备上 0.3–1.4 s；50 Hz 的控制频率都来自"动作分块 + 异步执行"，不来自逐步推理。VLA-Perf 的解析模型估计：通过 Wi-Fi 调用服务器上的 RTX 4090，除网络极差外都快于机载推理。

### 2.2 动作表示与解码

- 自回归逐维 token 的延迟随块长 × 自由度增长。FAST 改进了可学性但没改进速度（约 750 ms/块 vs 扩散版约 100 ms）。
- 并行解码去掉串行：OpenVLA-OFT 一次双向前向输出整块连续动作，吞吐 26–43×；PD-VLA、CEED-VLA 做 Jacobi 不动点解码；DD-VLA 做固定步掩码离散扩散。
- flow 头（π0、GR00T）的代价是一次前缀 + N 次专家前向，2026 年工作压缩 N：DriftingVLA 训练原生一步映射（3.36×）；两步去噪把 π0.5 从 61.6 ms 降到 22.0 ms；One-step Euler 发现大 flow VLA 不重训直接用 1 步即可（1.6–4.8×），但 SmolVLA、FLOWER 等小模型在长视界上退化。
- 权衡：L1 回归最快但只能表达单峰分布（OFT 自述）；VLA-Perf 的解析模型认为动作专家的延迟主要由去噪步数而非块长决定。

### 2.3 模型级加速

- VLM 前缀占大头：π0 的 73 ms 中前缀占 32–46 ms。
- 免训练方法通常 1.4–2×、成功率略降，多在仿真中测，且常以 FLOPs 或 CUDA 延迟报告：缓存与剪枝（VLA-Cache、EfficientVLA、SpecPrune-VLA）、提前退出（DeeR-VLA、MoLe-VLA）、投机解码（Spec-VLA，只适用于自回归 VLA）。
- 量化：从 OpenVLA 的 int4 部署，到原生三值权重（BitVLA，4.4×），再到含 DiT 头的 W4A8 PTQ（QuantVLA，报告显存节省而非墙钟加速）。
- 小 VLA 原始加速最大，可能牺牲广泛预训练：TinyVLA 比 OpenVLA 快约 20×，VLA-Adapter 36.5 ms，TurboVLA 31 ms 且不含 LLM。
- 系统工程：Realtime-VLA 的 kernel 工作把 π0 在 RTX 4090 上从 106 ms 降到 27 ms；EagleVLA 在 Jetson Orin 上控制频率提高 14.7×，两者都无精度损失。

### 2.4 执行级：分块、异步与实时分块

- **问题**：同步执行动作块，推理期间机器人停顿；朴素异步执行在块边界产生跳变，且反应滞后。
- **演进**：ACT（分块 + 时间集成）→ BID（采样多块再选择）→ SmolVLA（异步队列）→ RTC（冻结已承诺动作、引导 flow 补全其余）。RTC 每次调用多约 21 ms（76 → 97 ms），但注入 +200 ms 延迟后不退化；时间集成则振荡到触发机器人保护停止。
- **去掉 RTC 的推理开销**：训练时前缀条件（Training-time RTC、Legato、Xiaomi-Robotics-0）。
- **延迟补偿**：以执行时刻的未来状态或特征为条件（VLASH 最大反应延迟 546 → 46 ms；EagleVLA），或每步修正头（A2C2）。
- **以反应时间为中心（最新）**：FASTER 指出反应时间由首动作时间和执行视界决定，先用 1 步去噪出近端动作；REACT、FlashVLA、Reflex 用滚动或流式缓冲。REACT 测得 H50E50 反应 1.5 s，滚动去噪约 0.73 s（人类 0.705 s）。
- **设计轴**：一致性在哪里保证（推理时引导 / 训练时前缀）；补偿什么（动作 / 状态 / 观测）；执行视界与反应性的权衡。

### 2.5 双系统

- VLM 骨干 1–10 Hz，控制需要 50–200 Hz。
- 接口形式：潜向量（Helix、RoboDual 3.8×）、语言（Hi Robot）、联合训练同址（GR00T N1，10 / 120 Hz）、云端骨干 + 机载解码器（Gemini Robotics）、参数共享（FiS-VLA，117.7 Hz）。
- 权衡：独立的 S1 用不上 VLM 的知识（FiS-VLA 的批评）；Hi Robot 两层分开训练、互不了解对方能力。VLA-Perf 认为 S1/S2 异步的收益取决于硬件与网络；2026 年开始研究何时调用 S2。

## 3. 执行快：超过示教速度（P§B）

### 3.1 直接加速为什么会失败

- 控制器动力学变化：跟踪误差把状态推出分布、相邻动作块不一致、误差累积；高增益下指令位姿超调；测试时改速度产生不可恢复的 OOD 观测（SAIL, FreeSpeed）
- 推理延迟：动作队列排空导致停顿，延迟限制平均加速比；异步推理使块错位；观测过时（SAIL, DemoSpeedup, RACE, LIBERO-Dynamic）
- 机器人–物体动力学变化：惯性把物体甩出工作区；推得更快会过冲；慢示教不包含快速结果（SAIL, EPCC, I2RLC, VarSpeed-BIL）
- 精确阶段不耐加速：抓取、对齐、插入最先失败；ParcelStow 中高速下 47 个 ACT 失败有 35 个是插入错位（DemoSpeedup, ESPADA, VOLT, AdaTempo, AutoSpeed, ParcelStow）
- 接触处的本体差异：人的节奏让更硬的机器人过冲或碰撞；只考虑物理限幅的重定时"largely fail"（RoboPace）
- 抖动：均匀加速的 jerk 约为学习重定时的 2 倍（Speed prior）

### 3.2 示教重定时后重训

- 模仿学习复制示教的慢节奏；均匀下采样会破坏精确阶段。各方法的区别在于由什么决定哪里压缩：策略熵（DemoSpeedup）、视觉语言模型给出的语义（ESPADA、VOLT）、多条示教共享的节奏（AdaTempo）、外部节奏来源（EgoSpeedUp 用人类视频，Speed prior 用跨任务学到的先验）。
- 加速 1.7–3.6×，成功率不变或略升。代价是每个速度设定都要重训；这些方法都不对快速动力学建模；Speed prior 不能超过已有示教者达到过的节奏。

### 3.3 推理时重定时与速度条件策略

- 从启发式或学习的调度器（FreeSpeed、SuP）走向机器人限幅下的时间最优路径参数化（RACE、RoboPace、Speed prior 的跟踪器）。速度条件策略把速度作为输入，也能减速（TempoVLA、PaceVLA、AutoSpeed）。
- 关键设计：路径不变、只改时间；让策略输出到达状态或期望状态而非指令，使输出在任意速度下都有效（SAIL、RACE）；是否对快速动力学建模（只有 EPCC 通过 play 数据世界模型做了）。
- 只重定时在路径本身转弯、抓取的地方会饱和（FreeSpeed）。

### 3.4 提升节拍的 RL

- 只学速度的 RL：SpeedTuning（>2.4×）、SpeedAug（16 min 在线后吞吐 1.8×），代价低、适用面窄。
- 通用真机 RL，折扣使策略更快：HIL-SERL、ConRFT、RL-100、π*0.6。这是 VLA 级策略在真机上快于其遥操作数据的仅有结果。
- 系统层改进：PAKT 改进控制器与示教接口而非 RL 算法，节拍比 HIL-SERL 再降 23–48%；SPARR 用仿真基策略 + 真实残差，节拍 −29.7%。
- 代价是人工监督：奖励标注、干预、复位（π*0.6 自述）。

### 3.5 遥操作侧

- 接口限制示教速度：DemoSpeedup 指出缺少完整无遮挡的 3D 视野与触觉本体感；Speed prior 指出遥操作比手持采集慢、新手会犹豫；动态任务上 VR 控制器优于 SpaceMouse（2601.13042）。
- 三类补救：更快或更具物理性的采集（UMI、双边或力反馈遥操作）；事后修正（I2RLC、Speed prior、EgoSpeedUp）；让示教保持在机器人可跟踪的范围内（PAKT）。
- 反方向的风险：RoboPace 指出人手持采集的节奏在接触附近对更硬的机器人太快。

### 3.6 动力学、控制与延迟

- 控制器：低增益遥操作控制器在高速下跟踪失真，提高增益又会让指令位姿超调；SAIL 改为预测到达位姿并用高增益 OSC 跟踪。接触密集的 RL 系统用带参考限幅的阻抗控制（HIL-SERL、ConRFT）或参考生成器 + 力矩级阻抗控制（PAKT）。
- 学习–控制混合：迭代学习控制精化参考（I2RLC、VFILC）；双边位置–力控制工作到控制带宽（VarSpeed-BIL）。
- 延迟：调度（SAIL、RACE）、延迟匹配（UMI）、在线估计（STDArm）。
- 动态任务给学习策略加结构先验：残差物理（TossingBot）、高频残差策略（全身抛掷）、运动基元（FODMP）。

### 3.7 指标

- 在用的指标：节拍、每小时成功数（π*0.6）、每小时拾取数（TossingBot）、带后悔的吞吐（SAIL）、相对示教加速比（RACE、AdaTempo）。
- ParcelStow 扫描执行速度、LIBERO-Dynamic 扫描物体速度与延迟，都显示退化不均匀且在名义速度下看不出来。
- 没有共享的真机速度基准。

## 4. 数据少：少量遥操作 + 仿真（P§C）

### 4.1 真实示教预算

- **真实示教：0**
  - 结果：SimpleVLA-RL 真机 38.5%；GenWorld-RL 75%；GraspVLA 抓取约 90%；MolmoBot 79.2%
  - 补充数据 / 方法：大规模随机化合成数据，或强通用 checkpoint + 仿真 RL
- **真实示教：0（真机在线 RL）**
  - 结果：DSRL 用 65–80 个在线 episode 微调 π0
  - 补充数据 / 方法：冻结权重，对噪声做 RL
- **真实示教：1 个任务的遥操作**
  - 结果：DreamGen 学会 22 个新行为
  - 补充数据 / 方法：视频世界模型生成轨迹
- **真实示教：10 / 任务**
  - 结果：RoboTwin 2.0 相对 +367%；MetaGenSim 19/80 → 52/80
  - 补充数据 / 方法：1k 条域随机化合成数据；元学习的生成分布
- **真实示教：10–40 / 任务**
  - 结果：EXPO-FT 30/30
  - 补充数据 / 方法：约 19 min 真机离策略 RL
- **真实示教：约 20 / 任务**
  - 结果：Sim&Real Co-Train 45 → 83%；ConRFT 96.3%；RL-Co 的 Open Drawer 上 200 条纯真实基线不优于它
  - 补充数据 / 方法：约 1k 条仿真 / 任务；45–90 min 人在环 RL；仿真 RL + 真实锚定
- **真实示教：约 30 / 任务**
  - 结果：TwinRL 近 100%；OC-ResRL 76%；VLaRL
  - 补充数据 / 方法：3DGS 孪生 RL + 约 20 min 真机 RL；仿真训练的残差

### 4.2 仿真–真实共训练

- 基线配方（Sim&Real Co-Train）：每任务约 20 条真实 + 约 1k 条 MimicGen 类仿真，仿真采样比 0.9–0.99。
- Sim&Real Pushing：仿真带来的收益会饱和，只有更多真实数据能抬高上限；接触任务中物理保真比视觉保真更重要。
- 2026 年的问题从"仿真多少"变为"仿真什么"：MetaGenSim 元学习生成分布；SARI 仿真只负责自由空间接近、真实数据负责接触；R2S2R Grounding 区分物理对齐与行为对齐（分别 +18 点、+10 点）。
- 基础模型规模：GR00T N1、DreamGen 加入仿真与视频生成两层数据。
- 设计轴：混合比、仿真与任务的对齐程度、仿真数据是否由真实示教播种。

### 4.3 纯合成预训练

- 规模足够时，纯仿真 VLA 可零样本迁移：GraspVLA、MolmoBot、InternData-A1。InternData-A1 测得 1–8 条仿真 episode 抵 1 条真实，取决于任务难度。
- Sim2Real-VLA Study：空间随机化最关键，RL 增加鲁棒性；逼真度提升真实成功率，但在中等光追后饱和。
- 代价是大量资产与程序化生成工程；结果主要集中在抓放和铰接物体。

### 4.4 仿真 RL

- 演进：PPO 可行性（VLA-RL、RL4VLA）→ 无 critic 的结果奖励 RL（RIPT-VLA、SimpleVLA-RL）→ 共享基础设施（RLinf）。从 1 条示教出发，RL 几乎让 LIBERO 饱和。
- 纯仿真 RL 也能提高真机成功率：SimpleVLA-RL 17.5 → 38.5%，GenWorld-RL 21.7 → 75%。
- 最可部署的模式是"SFT 共训练 → 仿真 RL + 真实数据锚定损失"（RL-Co、TacCoRL）。
- 仿真中以在策略的 PPO / GRPO 为主；flow matching VLA 需要代理似然（ReinFlow、PPOFlow）。
- 仿真 RL 也让执行更快更直接：GenWorld-RL 1.13–1.25×；RLinf-VLA 报告 RL 后动作更直接。

### 4.5 真机 RL

- 以离策略、人在环为主：PA-RL、ConRFT、TwinRL、EXPO-FT，以及 DSRL 的噪声引导。
- 趋势是冻结 VLA 的大部分，只训练轻量头、编辑策略或残差，并锚定到基策略。
- π*0.6 与 RLT 给出 RL 提速的最清楚证据：吞吐 >2×，关键阶段最多快 3×，有时快于遥操作。
- 快的方法都是任务特定的；LWD、ACCRUE 尝试保持通用性。

### 4.6 残差 RL

- 残差在分块模仿策略之上补充闭环精度：ResiP、Policy Decorator；ResFiT 在真机上做；PLD 把残差蒸馏回 VLA。
- 最新方向：残差只在仿真训练，通过可迁移的观测空间零样本上真机——物体位姿（OC-ResRL，42 → 76%）或 VLA 自身潜空间（VLaRL）。
- 权衡：特权状态残差需要蒸馏，图像残差碰到视觉 gap；位姿或潜空间残差依赖位姿跟踪或潜空间映射。

## 5. 三层交汇处的已有工作

| 工作 | 少量真实数据 | 仿真 / 模型 | 速度 |
|---|---|---|---|
| SAIL | 遥操作示教 | 无（自述需要动力学模型或仿真数据） | 3.2× 真机，含延迟感知调度 |
| EPCC | 慢专家示教 | 快速 play 数据训练的世界模型 | 吞吐 2.0× |
| RACE | 示教 | 机器人运动学限幅（TOPP-RA） | 最高 4× |
| GenWorld-RL | 0 条任务示教 | 100 个生成场景中 RL | 真机执行快 1.13× |
| SPARR | 真实残差数据 | 仿真基策略 | 节拍 −29.7% |
| TwinRL | 30 条 | 3DGS 孪生 RL | 未报告速度 |
| π*0.6 / RLT | 示教 + 干预 | 无仿真，真机 RL | 吞吐 >2× / 关键阶段最多 3× |
| PAKT | 运动学示教 | 无仿真；参考生成 + 力矩阻抗控制 | 节拍比 HIL-SERL 再降 23–48% |

检索范围内没有同时满足三点的工作：少量遥操作示教 + 动力学经辨识的仿真 + 以节拍或吞吐为优化目标。

## 6. 文献自述的开放问题

- RTC 推理开销大（每步去噪 2.5×），只适用于扩散 / flow 策略，未在高动态场景（如足式）真机测试（RTC）
- 训练时 RTC 只支持硬前缀，训练用的延迟分布必须匹配实际（Training-time RTC）
- 当前 VLA 利用机器人状态不足，测试时前推状态不微调就不够（VLASH）
- 动态场景中缓存收益缩小（VLA-Cache）
- 一步积分只对足够训练、足够大的模型成立（One-step Euler）
- 机载算力与带宽随模型增大仍落后于 GPU 服务器（EagleVLA）
- 长开环动作块在场景变化后过时（REACT）
- 未处理机器人–物体动力学变化；有限离线数据限制算法修复；需要动力学模型或仿真数据，并与底层控制器联合优化（SAIL）
- 动力学失配带来小幅下降；加速率手设且依赖操作者；忽略推理延迟（DemoSpeedup）
- 节奏只是线索，不是最大可行速度；可能吸收操作者共同的习惯（AdaTempo）
- 不能超过已观测到的节奏（Speed prior）
- 请求速度不总能达到；转弯、抓取、释放附近加速受限；没有力或触觉反馈（FreeSpeed）
- 依赖世界模型的覆盖范围；增加规划开销（EPCC）
- 依赖人工奖励标注、干预、复位；探索是贪心的；干预不能提高总体速度（π*0.6）
- 共训练结果"still not perfect"，混合比需要细调（Sim&Real Co-Train）
- 仿真收益饱和；物理 gap 比视觉 gap 更重要（Sim&Real Pushing）
- 需手工搭建仿真环境，只支持刚体（RL-Co）
- SFT 成功率为 0 时 RL 无法起步（SimpleVLA-RL）
- 真机 RL 探索不超出 SFT 数据的支撑集（TwinRL）
- 基 VLA 需要约 40% 成功率才能开始 RL（EXPO-FT）
- 依赖 6 自由度位姿跟踪，遮挡与杂乱下失效（OC-ResRL）
- 困难任务需要约 8 倍于真实数据的仿真数据（InternData-A1）

## 7. 入门阅读顺序

1. **π0**：分块 flow VLA 的参照，给出逐组件延迟分解（RTX 4090 上 73 ms）
2. **OpenVLA-OFT**：说明解码方式主导速度：并行解码 + 分块，吞吐 26×，成功率反而更高
3. **RTC → VLASH**：异步执行的标准形式（冻结 + 补全）与开源的延迟补偿，含实测延迟
4. **SAIL**：把超过示教速度的执行作为全栈问题，列出失败原因，给出带后悔的吞吐指标
5. **DemoSpeedup → RACE**：示教重定时基线，与基于期望状态 + TOPP-RA 的物理约束加速
6. **Sim&Real Co-Train → Sim&Real Pushing**：少量真实 + 大量仿真的基准配方，以及物理 gap 比视觉 gap 更重要的证据
7. **RL-Co**：SFT 共训练 → 仿真 RL + 真实锚定的端到端配方
8. **SimpleVLA-RL**：从 1 条示教出发的仿真 RL，零真实数据迁移到真机
9. **HIL-SERL → π*0.6 → RLT**：真机 RL 同时提升成功率与节拍的证据链
10. **OC-ResRL**：冻结 VLA + 只在仿真训练的残差零样本上真机的模板
11. **GR00T N1、SmolVLA**：开放可微调的双系统参照；小数据、低成本硬件下的实用选择
