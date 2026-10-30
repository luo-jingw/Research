# SuperMimic

- 标题：SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model
- 作者：Qiayuan Liao, Yiyang Shao, Junfeng Long, Kevin Zakka, Roberto Horowitz, Pieter Abbeel, Koushil Sreenath（UC Berkeley）
- 发表：CoRL 2026 Oral；arXiv:2610.28480（v1，2026-10-20）
- 链接：[arXiv](https://arxiv.org/abs/2610.28480) · [项目页](https://supermimic.github.io)
- 代码：arXiv 页面未列出官方代码仓库（2026-10-30 查询）
- 阅读来源：arXiv v1 PDF 全文

## 问题

通过跟踪大规模人体动作数据集（motion tracking）训练人形机器人全身控制器，是获得通用、高表现力全身行为的主流路线。现有流水线都用 model-free RL（PPO），扩展到大量动作时有两种做法：

- 每段动作训练一个专家再蒸馏成一个策略（BeyondMimic 路线），蒸馏有损；
- 直接在大动作库上暴力训练单个通用策略（SONIC 路线），需要集群级算力：SONIC 用 128 张 L40 训练约 168 h，约 21,000 GPU-h。

论文的论点：不同参考动作共享同一套人形机器人刚体动力学，model-free RL 没有显式利用这一共享结构，而是从带噪声的仿真 rollout 中反复估计动作后果，所以扩展动作数量等于扩展算力。

## 方法

一个 Dyna 式训练循环，三步交替：

1. **采数据**：当前策略 πθ 在仿真器（MuJoCo Warp）中执行带噪声的动作，转移写入固定大小的 replay buffer。动作噪声只用于拓宽世界模型的拟合范围。
2. **拟合世界模型**：确定性、可微的世界模型 fω，以每个 episode 的仿真上下文 ξ（域随机化参数：摩擦、标定偏置、躯干质心）为条件，预测下一状态、奖励、无噪声观测、终止概率。在 replay buffer 中采样 k=8 步窗口，从记录的初始状态出发，沿记录的动作自回归展开，损失为状态 L2 + 奖励平方误差 + 观测 L2 + 终止 BCE。
3. **更新策略**：冻结世界模型，从 buffer 中的状态出发做 H=32 步想象 rollout，对回报做 BPTT 得到解析策略梯度；critic Vψ 在想象转移上用 GAE 目标拟合，自举 H 之后的回报（SHAC 式短视界 actor–critic）。用可微的软生存权重 ĉt 替代硬终止，critic 不用 EMA 目标网络。

关键设计点：

- 梯度来自学到的模型而非仿真器本身，所以仿真器不需要可微，兼容非光滑接触。
- 观测噪声在世界模型之外采样后再加回，世界模型只预测无噪声观测。
- 策略是确定性的；动作是低 PD 增益下的关节设定点，相当于力矩代理。
- 跟踪奖励沿用 BeyondMimic，去掉了自碰撞惩罚（该项防的是随机策略的 reward hacking，确定性策略下无收益）；去掉了 BeyondMimic 的根速度扰动（状态不连续，确定性世界模型无法刻画），只对物理参数做域随机化。
- 策略输入最近 10 帧本体观测（关节位置、关节速度、IMU 角速度、投影重力、上一动作，G1 为 29 自由度）；目标为未来 K=10 帧参考动作。

## 关键结果

- **超过 SONIC 已发布 checkpoint 的归一化回报**
  - SuperMimic：1 × H100，3 h
  - 基线：SONIC：128 × L40，约 168 h
- **129,514 条动作基准上的失败数**
  - SuperMimic：25（1 GPU，3 h）；0（2 GPU，9.8 h）
  - 基线：SONIC checkpoint：179
- **LAFAN1 受控对比，达到回报 0.82**
  - SuperMimic：1 GPU，1.2 h
  - 基线：PPO-Sim 18 h 内未达到；最终 0.60（1 GPU）/ 0.70（4 GPU）/ 0.72（8 GPU）
- **训练数据**
  - SuperMimic：BONES-SEED 264.56 h
  - 基线：SONIC 611 h

论文自述的算力比：墙钟约 56×，GPU-h 约 7200×（标题用 >1000×）。论文同时说明 H100 与 L40 峰值算力不同（fp32 为 0.74×，tensor core 为 5.5×），SONIC 不是在相同条件下重训的。

失败数基准的口径（Appendix F）：

- 129,514 条动作是两种方法共同的训练动作，论文明确说明失败数衡量的是对训练动作的覆盖程度，不是对新动作的泛化。
- 评测在无域随机化、无观测噪声、确定性物理、足底摩擦 1.0 的同一仿真中进行，每条动作从首帧播放一次。
- 失败判定统一用 SuperMimic 自己的训练终止条件（根高度偏差 > 0.25 m 或倾斜误差 > 0.8）；SONIC 原本的判定只看根与末端执行器高度偏差 > 0.25 m，不含姿态项。
- SONIC 已发布 checkpoint 整组失败的动作包括全部 44 个翻转、全部 22 个侧滚、一套舞蹈的全部 8 个动作，以及 24 个立定跳远中的 15 个；SONIC v1.1 checkpoint 失败 239 条。SuperMimic 在 1 GPU × 3 h 时的 25 个失败中有 14 个集中在 5 个难动作组（共 195 条），任何一组的失败数都不多于 SONIC。

## 消融

- **世界模型 rollout 速度**：H100 上，2k–16k 并行环境时比 MuJoCo Warp 快 10× 以上，64k 时 62×。
- **一阶梯度的作用**：在同一世界模型上跑 PPO（PPO-WM）做对照，BPTT 达到 PPO-WM 最佳回报所需想象步数少约 64×，说明收益不只来自 rollout 速度。
- **critic 与视界**：无 critic 时 H≤16 训练失败；有 critic 时 H=16 等于无 critic 的 H=32；H=32 最快达到 0.82；H 从 64 增到 128，达到该回报的时间近 3 倍且最终回报下降。仿真中 T-pose 站立受 0.5–4 m/s 推扰时，有 critic 的策略在 0.5–2.4 s 内恢复，无 critic 的策略在 0.5 m/s 下也无法稳定，4 m/s 时摔倒。
- **数据规模**：动作数据从 1 h 增到 264 h，世界模型预测误差保持稳定，达到固定回报所需算力增长缓慢。

## 真机

同一个通用跟踪器不做逐动作调参，部署到 Unitree G1：跳步、侧滚（躯干和四肢着地的接触密集动作）、90° 翻转、原地 360° 翻转。

## 下游接口

初步实验：通过同一个世界模型，用速度跟踪奖励直接 RL 训练速度编码器，与用动作跟踪奖励训练的蒸馏编码器对比。在 672 个阶跃指令上，RL 编码器在 650 个上稳态误差更低，蒸馏编码器在 15 个上更低；只有蒸馏编码器在 7 个动作库数据极少的快速转向上摔倒。

## 论文陈述的局限

- 多接口联合训练研究不足：速度奖励只更新速度编码器，不更新共享解码器。
- 世界模型只从仿真转移学习；论文指出真机数据可用于细化它，且其可微性可用于系统辨识。
- 只在平地训练，没有地形和物体交互。

## 在谱系中的位置

论文 Table 1 按训练阶段对比相关方法（Mimic / Latent / Downstream 三阶段，合并单元格表示联合训练）：

| 方法 | Mimic | Latent | Downstream | 下游训练信号 | 真机 |
|---|---|---|---|---|---|
| NPMP | SVG(0) | BC | SVG(0) | RL | ✗ |
| ControlVAE | MBRL（联合） | MBRL（联合） | MBRL | RL | ✗ |
| PhysicsVAE | PPO | BC | PPO | RL | ✗ |
| PULSE | PPO | DAgger | PPO | RL | ✗ |
| MaskedMimic | A2C | DAgger（联合） | DAgger（联合） | Distill | ✗ |
| BeyondMimic | PPO | DAgger | CGD（classifier guidance diffusion） | Distill | ✓ |
| SONIC | PPO（三阶段联合） | PPO（联合） | PPO（联合） | Distill | ✓ |
| LATENT | PPO | DAgger | PPO | RL | ✓ |
| SuperMimic | MBRL（三阶段联合） | MBRL（联合） | MBRL（联合） | Distill / RL | ✓ |

两条交汇的线：

- **大规模物理动作跟踪**：DeepMimic → PHC → SONIC；SuperMimic 沿用 BeyondMimic 的跟踪形式化与奖励，以 SONIC 为主要对比对象。
- **可微学习动力学用于运动控制**：SuperTrack → ControlVAE → MoConVQ → SuperDyno；SuperMimic 把这条线推到单 GPU 训练大规模人形跟踪器并做到真机部署。模型式策略优化方面引用 Dreamer、DreamerV3、TD-MPC、DayDreamer、SHAC、Song et al. 可微仿真四足，以及 ETH 的 RWM / RWM-U。与 RWM / RWM-U 的区别：后者在想象 rollout 上用 PPO，且世界模型用其他策略的轨迹预训练；SuperMimic 对回报求导，且世界模型在训练中用自身策略采集的数据拟合。

## 与 real2sim 的关系

SuperMimic 的世界模型拟合的是仿真器而不是真实世界，属于 sim 内的学习型代理模型。论文把"用真机数据细化世界模型、利用其可微性做系统辨识"列为未来工作，这正是 [real2sim](../../real2sim/README.md) 中动力学对齐分支要解决的问题。
