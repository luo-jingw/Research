# ISSUE-001

Status: open

Area: real2sim

## Observation

第一轮 real2sim 综述（`topics/real2sim/papers.md`）中，部分论文的发表处或数值只来自二手来源，或在一手来源中自相矛盾。

## Impact

在引用这些论文的发表处或数值前，需要回到一手来源确认。`papers.md` 中这些条目的发表处标有 †。

## Evidence

| 条目 | 问题 |
|---|---|
| RigPI (2606.25212) | arXiv Comments 字段写 "Accepted to … IROS 2027" |
| Scalable Real2Sim (2503.00370) | IROS 2025 只出现在作者 GitHub 仓库，arXiv 页面未列发表处 |
| SPARK (2512.01629)、PhysX-Anything (2511.13648) | CVPR 2026 来自 cvpr.thecvf.com 虚拟会场页面，未在论文页面确认 |
| URDF-Anything+ (2603.14010) | NeurIPS 2026 来自 neurips.cc 海报页面，未在论文页面确认 |
| SIMPLER (2405.05941) | 物理后端（SAPIEN/ManiSkill2）未从论文正文确认 |
| Mem-World (2606.18960) | 摘要只给出 "Pearson 比 Ctrl-World 高 14.5%"；r=0.97 vs 0.85 只见于搜索摘要 |
| Cosmos-Surg-dVRK (2510.16240) | r > 0.92 只见于二手总结 |
| MolmoSpaces (2602.11337) | 发表处未确认 |
| GaussGym (2510.15352) | 论文一处写 IsaacGym，另一处写 IsaacSim |
| BayesSim (1906.01728) | RSS 2019 版的"真实"数据由仿真器生成，没有真机实验 |
| "Contact-UAN"、"MatPhys" (2605.19386) | 只见于索引列表或参考文献，未找到论文页面 |
| Awesome-Real2Sim2Real GitHub 列表 | 至少两处发表处错误：EmbodiedSplat 应为 ICCV 2025，CRISP 应为 ICLR 2026 |

## Hypotheses

- RigPI 的 "IROS 2027" 可能是 "IROS 2026" 的笔误。

## Next Experiment

引用任一条目前，打开该论文的 arXiv 最新版本、会议论文集或项目页核对；Awesome 类列表只用于发现论文，不作为发表处来源。

## Resolution

# ISSUE-002

Status: open

Area: humanoid-motion-tracking

## Observation

第一轮 humanoid-motion-tracking 综述（`topics/humanoid-motion-tracking/papers.md`）中，部分发表处只来自其他论文的引用或二手页面，部分方法细节未从一手来源确认；检索预算在 2025–2026 世界模型分支上提前耗尽。

## Impact

引用标 † 的发表处或下列细节前需回到一手来源确认。可微世界模型分支（papers.md §7–§10）的 2025–2026 覆盖可能不完整。

## Evidence

| 条目 | 问题 |
|---|---|
| H2O、OmniH2O、HumanPlus、ExBody、TWIST、UniTracker、LATENT、PHUMA | 发表处只来自其他论文的引用 |
| BeyondMimic、SONIC | Science Robotics 11(117) 来自 SuperMimic 参考文献，未打开期刊页面 |
| GMR | ICRA 2026 只见于一处引用 |
| QWM、FADA | CoRL 2026 来自作者或实验室页面，arXiv 页面未列发表处 |
| FADA | 一个检索来源未找到 arXiv；另一个检索来源给出 arXiv 2606.28476 |
| SuperDyno | 只读了摘要，策略梯度估计器的具体形式未确认 |
| BONES-SEED | 数据集页面未打开，规模数字来自 SONIC 与 SuperMimic 的引用 |
| GMT、ExBody2 | 发表处未确认 |
| GigaBrain-WBC-0.5 (2608.18234) | arXiv 元数据中名称为 "InterTrack" |
| 可微世界模型分支 | 2025–2026 只覆盖了检索时打开过页面的课题组：ETH RSL、UCSD Hansen、NVIDIA、Georgiev、Y. Song、PKU Libin Liu、CMU LeCAR |

## Hypotheses

## Next Experiment

- 引用前打开对应论文的 arXiv 最新版本或会议论文集核对。
- 补检 2025–2026 年"经学习动力学反传梯度训练腿足/人形策略"的工作，核对 survey.md §3 的覆盖。

## Resolution
