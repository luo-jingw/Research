# vla-fast-control

用少量人工遥操作数据 + 仿真建模，训练能在真机上快速执行的 VLA 策略。"快"包含三层：反应快（推理延迟与实时执行）、执行快（超过示教速度）、数据少（少量示教 + 仿真）。

- 状态：第一轮综述完成（快照 2026-10-30）
- 最后更新：2026-10-30

## 范围

包含：
- VLA 推理加速：动作表示与解码、量化/剪枝/缓存/提前退出、小 VLA、系统工程；
- 实时执行：动作分块、异步推理、实时分块（RTC）及其后续、延迟补偿、双系统；
- 超过示教速度的执行：示教重定时、推理时重定时、速度条件策略、提升节拍的 RL、遥操作侧、底层控制与动力学；
- 少量遥操作 + 仿真：仿真–真实共训练、纯合成预训练、仿真 RL、真机 RL、残差 RL。

不包含：
- 场景/资产重建与物理参数辨识本身，见 [real2sim](../real2sim/README.md)；
- 人形全身动作跟踪，见 [humanoid-motion-tracking](../humanoid-motion-tracking/README.md)。

## 关键词

VLA, inference acceleration, action chunking, real-time chunking, asynchronous inference, dual-system, faster-than-demonstration, speed adaptation, cycle time, throughput, sim-and-real co-training, VLA reinforcement learning, residual RL, few-shot teleoperation

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 三层"快"的框架、全流程六环节、延迟预算、加速失败原因、真实示教预算、三层交汇处的已有工作、开放问题、入门阅读顺序 |
| [papers.md](papers.md) | 论文目录，按 A 推理与执行 / B 超过示教速度 / C 少量数据 + 仿真 分节 |
| `notes/` | 精读笔记（尚无） |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据：根目录 `issues.md` → ISSUE-003
- 候选研究方向：根目录 `opportunities.md`，`Area: vla-fast-control`
