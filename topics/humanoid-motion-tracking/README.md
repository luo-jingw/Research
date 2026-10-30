# humanoid-motion-tracking

人形机器人全身控制的动作跟踪路线：在仿真中训练策略跟踪重定向后的人体动作，再迁移到真机；以及用可微学习动力学 / 世界模型训练这类控制器的分支。锚点论文是 SuperMimic。

- 状态：第一轮综述完成（快照 2026-10-30）
- 最后更新：2026-10-30

## 范围

包含：
- 基于物理的动作跟踪：图形学根源、真机人形跟踪器、专家 / 蒸馏 / 通用训练范式、规模化；
- 跟踪器作为底层控制器的上层接口：遥操作、速度、扩散引导、token、潜动作、残差物体策略、提示；
- 动作数据集与重定向；
- 可微学习代理模型、可微仿真策略学习、世界模型策略优化，以及在真实数据上拟合动力学。

不包含：
- 场景、物体与物理参数的 real2sim 重建，见 [real2sim](../real2sim/README.md)；
- 不以跟踪为核心的人形运动控制（纯速度行走、基于模型的 MPC），只在对比时提及。

## 关键词

motion tracking, motion imitation, whole-body control, humanoid, retargeting, teacher-student distillation, generalist tracker, differentiable world model, BPTT, analytic policy gradient, model-based RL, SuperMimic, BeyondMimic, SONIC

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 两条谱系的脉络、SuperMimic 的位置、社区复现、文献自述的开放问题、入门阅读顺序 |
| [papers.md](papers.md) | 论文目录，按分支分节，含 SuperMimic 非官方复现列表 |
| [notes/2026-supermimic.md](notes/2026-supermimic.md) | SuperMimic 精读笔记 |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据：根目录 `issues.md` → ISSUE-002
- 候选研究方向：根目录 `opportunities.md`，`Area: humanoid-motion-tracking`
