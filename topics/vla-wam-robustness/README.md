# vla-wam-robustness

VLA（vision-language-action model）与 WAM（world action model）对部署时 setup 漂移的鲁棒性。setup 漂移指相机位姿、光照、纹理、背景、模糊与传感器噪声等条件与训练时不同。核心问题有三个：这类漂移让策略退化多少、为什么退化；在冻结或基本冻结主干的前提下，现有方法在哪个位置、用什么监督校正；条件注入结构怎样限定了可以校正的位置。

- 状态：第一轮综述完成（快照 2026-11-20）
- 最后更新：2026-11-20

## 范围

包含：
- 鲁棒性基准与"为什么不鲁棒"的分析，包括 WAM 与 VLA 的鲁棒性比较、腕部相机等评测口径问题；
- FTM 谱系，即冻结或少参数的视觉域适应：改视觉 token 或编码器、在图像一侧复原视角或画面、训练时让策略对相机鲁棒（作为上界参照）、少样本与一次演示适应；
- 无标签测试时适应：视觉控制策略上的经典 TTA、VLA 上的测试时训练、冻结策略的推理期引导、WAM 与世界模型、扩散与流匹配特有的信号、通用 TTA 代表作；
- 条件注入结构与干预位置：VLA 与 WAM 的注入形式、读哪一层、在前缀 KV / 残差流 / 动作专家上的干预，单独分析了 ImageWAM 的注入方式。

不包含：
- 策略层面的漂移（新物体、新任务、新指令、目标位置变化），只在说明基准口径时提到；
- sim2real 的训练配方，见 [sim-real-cotraining](../sim-real-cotraining/README.md)；
- 训练数据的分布形状与泛化，见 [data-distribution-generalization](../data-distribution-generalization/README.md)。

## 关键词

VLA robustness, world action model, camera viewpoint shift, wrist camera, lighting, texture, sensor corruption, LIBERO-Plus, RoboTwin 2.0-Plus, visual domain adaptation, feature transformation, LoRA, novel view synthesis, viewpoint canonicalization, one-shot adaptation, test-time adaptation, test-time training, action chunk consistency, flow matching, prefix KV cache, mixture-of-transformers, cross-attention, adaLN, activation steering, ImageWAM

## 文件

| 文件 | 内容 |
|---|---|
| [survey.md](survey.md) | 定义与范围、五轴分类框架、四个分支（基准与分析、FTM 谱系、无标签 TTA、条件注入与干预）、ImageWAM 注入方式、横向趋势、文献自述的开放问题、现有综述的分类对照、阅读顺序 |
| [papers.md](papers.md) | 论文目录，共 144 项：17 项基准、WAM 与 VLA 比较和分析；32 项 FTM 谱系；45 项无标签 TTA；48 项条件注入结构与干预；2 篇 WAM 综述 |
| [notes/2025-ftm.md](notes/2025-ftm.md) | 锚点论文 FTM / FLA 的精读笔记 |
| `reports/` | 对外汇报材料（尚无） |

## 相关记录

- 待核实的元数据、原文内部不一致、只来自模型摘录的数字与召回缺口：根目录 `issues.md` → ISSUE-007
- 候选研究方向：本轮未记录
