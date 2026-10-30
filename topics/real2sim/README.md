# real2sim

把真实世界的场景、物体与动力学重建进仿真器，用于机器人策略训练、数据生成、策略评测与规划。

- 状态：第一轮综述完成（快照 2026-10-30）
- 最后更新：2026-10-30

## 范围

包含：
- 操作场景的几何、布局与资产重建，数字孪生与数字表亲；
- 铰接物体重建与 URDF/MJCF 生成；
- 高斯/NeRF 渲染耦合的仿真，及不做动力学的逼真数据生成；
- 物体物理参数辨识：刚体、可变形、颗粒、流体；残差物理与混合仿真；
- 机器人侧动力学对齐：执行器建模、残差动作、参数辨识；
- real2sim 策略评测，以及学习型世界模型作为对照范式；
- 足式运动与导航、自动驾驶闭环仿真、人类视频 → 仿真。

不包含：
- 纯仿真内的域随机化与 sim-to-real 策略结构设计，只在与 real2sim 对比时提及；
- 人形动作跟踪谱系本身，见 [humanoid-motion-tracking](../humanoid-motion-tracking/README.md)。

## 关键词

real2sim, real-to-sim-to-real, digital twin, digital cousin, Gaussian splatting simulation, articulated object reconstruction, system identification, differentiable simulation, physical digital twin, MPM, residual physics, real-to-sim evaluation, MMRV, world model evaluator

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 三轴分类框架、各分支脉络、2025–2026 趋势、文献自述的开放问题、入门阅读顺序 |
| [papers.md](papers.md) | 论文目录，按分支分节 |
| `notes/` | 精读笔记（尚无） |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据：根目录 `issues.md` → ISSUE-001
- 候选研究方向：根目录 `opportunities.md`，`Area: real2sim`
