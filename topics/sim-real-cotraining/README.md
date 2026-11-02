# sim-real-cotraining

大量仿真数据 + 少量真实遥操作数据训练机器人策略：仿真数据提供行为的覆盖面，真实数据校准视觉、动力学与行为细节。重点是部署场景已有数字孪生时的训练配方。

- 状态：第一轮综述完成（快照 2026-10-31）
- 最后更新：2026-11-02

## 范围

包含：
- 仿真与真实数据的混合与分阶段配方：共训练混合比、仿真预训练 → 真实后训练、数据金字塔、仿真数据的折算价值；
- 模型侧的 gap 处理：域对齐、观测与动作空间选择、视觉翻译；
- 在孪生内或孪生周围生成仿真数据：真实示教播种的扩增、孪生内遥操作与规划器、表亲变化、世界模型生成数据、真实数据该采哪些；
- 共训练之后的策略提升：孪生内 RL、真实数据锚定、残差、真机少量修正、仿真专家蒸馏。

不包含：
- 孪生本身的重建、系统辨识与 real2sim 评测，见 [real2sim](../real2sim/README.md)；
- 推理延迟与执行提速，见 [vla-fast-control](../vla-fast-control/README.md)；
- 人形动作跟踪，见 [humanoid-motion-tracking](../humanoid-motion-tracking/README.md)。

## 关键词

sim-and-real co-training, sim-to-real, real-to-sim-to-real, digital twin, digital cousin, data pyramid, synthetic data, MimicGen, co-training ratio, domain adaptation, residual RL, sim pretraining

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 方向名称与分类框架；数据组合、孪生内数据生成、模型侧 gap 处理、部署场景孪生的用法与仿真成功率低于真机的原因、共训练后的策略提升；趋势、开放问题、入门阅读顺序 |
| [papers.md](papers.md) | 论文目录，142 篇按综述分节，另 34 篇补充 |
| [notes/2025-sim-real-cotrain.md](notes/2025-sim-real-cotrain.md) | 锚点论文精读：Sim-and-Real Co-Training |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据：根目录 `issues.md` → ISSUE-004
- 候选研究方向：根目录 `opportunities.md` → OPT-006（孪生配对数据的共训练对齐）、OPT-007（用孪生决定采集哪些真实遥操作）
