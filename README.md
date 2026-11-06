# Research

多方向的科研调研工作区。每个研究方向（topic）一个目录，包含综述、论文目录、精读笔记与汇报材料。

## Topics

| Topic | 状态 | 范围 |
|---|---|---|
| [real2sim](topics/real2sim/README.md) | 第一轮综述 · 2026-10-30 | 把真实世界的场景、物体、动力学重建进仿真器，用于机器人策略训练、数据生成与评测 |
| [humanoid-motion-tracking](topics/humanoid-motion-tracking/README.md) | 第一轮综述 · 2026-10-30 | 人形机器人全身控制的动作跟踪路线（DeepMimic → BeyondMimic → SONIC → SuperMimic），含可微学习动力学 / 世界模型训练分支 |
| [vla-fast-control](topics/vla-fast-control/README.md) | 第一轮综述 · 2026-10-30 | VLA 实机快速控制：推理加速与实时执行、超过示教速度的执行、少量遥操作数据 + 仿真的训练配方 |
| [sim-real-cotraining](topics/sim-real-cotraining/README.md) | 第一轮综述 · 2026-10-31 | 大量仿真数据 + 少量真实遥操作的训练配方：混合与分阶段、gap 对齐、孪生内数据生成、共训练后的策略提升 |
| [data-distribution-generalization](topics/data-distribution-generalization/README.md) | 第一轮综述 · 2026-11-06 | 训练数据的分布形状与泛化：频率偏斜与长尾、同一实例的多变重复、属性组合的覆盖、动作风格的一致性；覆盖认知发展、视觉、LLM 与具身 |

每个 topic 目录下：

| 文件 | 内容 |
|---|---|
| `README.md` | 范围、关键词、状态、文件索引 |
| `survey.md` | 综述：分类框架、各分支脉络、趋势、文献自述的开放问题、入门阅读顺序 |
| `papers.md` | 论文目录，元数据经检索核实 |
| `notes/` | 精读笔记 |
| `reports/` | 汇报材料 |

## 跨 topic 的记录

| 文件 | 内容 |
|---|---|
| [opportunities.md](opportunities.md) | 基于调研提出的候选研究方向，`Area:` 标明所属 topic |
| [issues.md](issues.md) | 待核实的论文元数据与未解决问题 |
| [PROJECT.md](PROJECT.md) | 目录结构、命名、状态归属与写作约定 |
