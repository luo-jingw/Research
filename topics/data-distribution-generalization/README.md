# data-distribution-generalization

训练数据的分布形状如何影响泛化：频率偏斜与长尾、同一实例的多变重复、属性组合的覆盖、动作风格的一致性。核心问题是数据总量相同时均匀分布是否最优，证据横跨认知发展、视觉、LLM 与具身四个领域。

- 状态：第一轮综述完成（快照 2026-11-06）
- 最后更新：2026-11-06

## 范围

包含：
- 婴儿与儿童的视觉输入统计、用儿童数据训练模型、人类学习中的偏斜输入；
- 长尾识别中表征与分类器的分工、大规模视觉数据整理中的分布调整、同一实例的多视角；
- 组合泛化：属性组合留出的实证、覆盖条件的理论、生成模型中的组合、频率与组合的交互；
- LLM 与序列模型：分布性质与 in-context learning、头部与尾部知识、组合推理、数据配比与重复；
- 机器人策略数据：因素组合与采集策略、动作一致性与速度、不均衡与重加权、组合泛化基准、随机化分布的选择。

不包含：
- 仿真与真实数据的混合比、孪生内数据生成、域对齐，见 [sim-real-cotraining](../sim-real-cotraining/README.md)；本方向只引用其中与分布形状直接相关的结论；
- 执行提速与示教重定时的方法本身，见 [vla-fast-control](../vla-fast-control/README.md)；
- 孪生重建与物理辨识，见 [real2sim](../real2sim/README.md)。

## 关键词

long-tailed distribution, Zipf's law, skewed input, infant egocentric vision, lumpy similarity structure, data repetition, compositional generalization, compositional support, systematicity, data mixture, temperature sampling, burstiness, in-context learning, action divergence, demonstration diversity, domain randomization distribution

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 分布形状的五层拆分与分类框架；认知发展、视觉、组合泛化、LLM、具身五个分支；横向结论、开放问题、入门阅读顺序 |
| [papers.md](papers.md) | 论文目录，160 篇按综述分节，另 16 篇沿用其他方向的条目 |
| [notes/2025-infant-lumpy.md](notes/2025-infant-lumpy.md) | 锚点论文精读：婴儿重复的单实例视觉经验与 lumpy 训练集 |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据与相互矛盾的结论：根目录 `issues.md` → ISSUE-005
- 候选研究方向：根目录 `opportunities.md` → OPT-008（机器人数据上的锚点 + 变化）、OPT-009（偏斜 × 组合留出的交叉实验）、OPT-010（sim + real 共训练中的运动分布）
