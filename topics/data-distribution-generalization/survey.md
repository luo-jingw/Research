# data-distribution-generalization 综述

- 快照日期：2026-11-06
- 引用：论文用简称，元数据见 [papers.md](papers.md)；"P§x" 指 papers.md 的节号。
- 锚点论文精读：[notes/2025-infant-lumpy.md](notes/2025-infant-lumpy.md)
- 百分数默认是成功率或准确率；"个百分点"表示绝对差。

## 0. 这个方向讨论什么

核心问题：在训练数据总量相同的前提下，什么样的分布形状泛化最好，均匀分布是否最优。锚点论文 Infant Lumpy 给出一个反例：婴儿每个类别的视觉经验由少数实例主导，按这种结构构造的训练集，对新实例的泛化优于均匀采样。

"分布形状"在文献中至少有五层含义，本综述分开讨论：

1. **类别、概念或任务之间的频率**：长尾识别、Zipf 类别分布、LLM 的域配比、机器人多任务的示教数不均衡。
2. **类内实例之间的频率**：同一类别里少数实例占大部分样本（Infant Lumpy、Physics LM 3.1 的 celebrity）。
3. **重复的方式**：逐字重复同一个样本，与同一实例在不同视角、改写、增强下的"有变化的重复"。
4. **属性或因素组合的覆盖**：每个属性值是否出现、哪些组合出现、组合之间是否连通。
5. **同一状态下的动作分布**：示教的风格、速度是否一致。这一层是具身数据特有的。

另有两个时间维度：样本是否在时间上成簇（burstiness），以及训练过程中分布是否按顺序变化（课程）。

泛化目标也分四种，同一种分布对不同目标的效果可能相反：

- 分布内的尾部类别或实例；
- 同一类别的新实例；
- 每个属性值都见过、但组合没见过（组合 OOD）；
- 训练范围之外的取值（外推）。

## 1. 分类框架

三个正交的轴：

- **轴 1：改变的是哪一层分布**（§0 的 1–5 层）
  - 类别频率：§3.1–§3.3、§5.5、§6.3
  - 类内实例频率与重复方式：§2、§3.4、§5.2
  - 组合覆盖：§4、§6.1、§6.4
  - 动作分布：§6.2
  - 随机化或生成分布：§6.5
- **轴 2：评测的泛化目标**：尾部、新实例、组合 OOD、外推（§0）。
- **轴 3：分布作用在模型的哪一部分**
  - 表征与决策头分开看：长尾识别中两者对分布的偏好相反（§3.1）。
  - 学习目标自带的先验：联合嵌入 SSL 隐含均匀聚类先验（§3.1）。
  - 训练预算：预算越短，最优分布越偏斜（§5.2）。
  - 模型结构：模块化、加性结构需要的组合覆盖远少于单体网络（§4.3）。

## 2. 认知发展：婴儿输入与人类学习（P§1）

### 2.1 婴儿的视觉输入偏斜且成簇

- **类别层面**：Clerkin 2017 记录 8.5–10.5 月龄婴儿 147 次居家用餐的头戴相机图像，场景杂乱，但物体类别的频次分布 "extremely right skewed"，极少数物体几乎一直在场。
- **实例层面**（Infant Lumpy）：
  - 14 个婴儿、87 次进餐、8 个类别。单次进餐内，出现最多的实例平均占该类别的 0.61，前三个实例占 0.92。
  - 同一婴儿的多次进餐合计，排名第一的实例占 0.48，前三个占 0.78，其余实例构成长尾。
  - 同一实例的图像本身差异很大，正放、倒放、遮挡、反光下的差异可以超过不同实例之间。
  - 用相似度图描述：多个稠密簇，簇之间由稀疏的高相似边连接，作者称为 "lumpy"。婴儿图的孤立节点比例为 0.20，三种零模型为 0.26–0.50。
- **时间层面**：Clerkin & Smith 2022 发现，跨片段看类别普遍在场、命名稀少；片段内名称与指称物共现，但每对只出现在少数片段中。Smith 2018 认为婴儿的感知运动发展产生一系列随时间变化、高度选择性的数据集，构成课程。

### 2.2 相似与多样的混合

同一团队的三篇工作逐步收窄变量：

- **Bambach 2018**：26 对亲子玩 24 个玩具。按 GIST 相似度从 10,000 帧中选出"相似 25%"和"多样 25%"子集，与按原始分布随机抽样的同样大小子集比较。多样优于相似，但保留原始"大量相似 + 多样长尾"的子集最好。
- **Tsutsui 2021**：同一数据上扫描多样与相似的配比，每类 25–200 张。
  - 每类 25 张时，纯多样约 52%，纯相似约 32%。
  - 任何样本量下，两者混合都优于单独任一种。
  - 每类 100–200 张时，75% 相似 + 25% 多样与原始儿童数据持平。
  - COCO 训练、ShapeNet 测试时，最佳混合也优于随机抽样。
- **Infant Lumpy**：在 ShapeNet 和 PetFace 上构造 Lumpy 与 Uniform 两组条件，图像总数相同，类别频率都均匀，只改变类内实例分布。
  - ShapeNet 的 Lumpy 组让一个实例占该类训练图的 35%，Uniform 组 6 个实例各占约 1/6。
  - ResNet-18、ResNet-50、TinyViT 从零训练，共 62 次。所有模型、所有数据集上 Lumpy 对新实例的泛化都更好，混合效应模型的主效应 D = 3.83（95% CI 2.8–4.8），作者称 "small but we believe meaningful"。
  - 参照量级：ResNet-50 在 ShapeNet Uniform 上的泛化准确率约 0.57，随机水平 1/6。
- **作者自述的未决问题**（Infant Lumpy）：实例频率偏斜与同一实例的外观变化两者的贡献尚未拆开；与数据增广的关系未厘清。

### 2.3 用儿童数据训练视觉模型

- **能学到什么**：
  - Orhan 2020：时间分类目标在 SAYCam 上学到的表征 "sometimes even outperforming" ImageNet 基线；对比学习目标在所有条件下都不如时间分类，作者归因于纵向视频的长程时间相关。
  - Orhan & Lake 2024：单个儿童约 200 小时视频，最好的嵌入模型达到 ImageNet 训练模型的约 70%，但 "less object-centric"。
  - CVCL：一名儿童 61 小时视听数据学到许多词–指称映射。
- **单一来源的极端情形**：
  - Pandey 2023：在游戏引擎中重建小鸡的饲养环境，只有单个物体、有限视角，训练的 ViT 解决了与小鸡相同的视角不变识别任务，作者结论 "ViTs were not more data hungry than newborn visual systems"。
  - DoRA：单段长视频预训练在 ADE20k 上比 ImageNet 上的 DINO 高 1.5 mIoU。
  - 这两项都依赖利用时间连续性的目标（时间对比、跨帧跟踪）。
- **规模上的反面证据**：BabyView 在帧数相当时不优于 SAYCam，按对数线性外推，达到人类或 ImageNet 预训练水平需要 10^7 小时以上。
- **顺序**：Sheybani 2023 中按发展顺序（2–4 月 → 6–8 月 → 10–12 月）预训练优于反序和随机混合，作者归因于最小婴儿视觉输入的 "slowness and simplicity"。效应在 VideoMAE 上大、在 JEPA-TT 和 SimCLR-TT 上小，训练变长后减弱。

### 2.4 人类实验：Zipf 分布不比均匀差

- **词与构式**：
  - Goldberg 2004：单一原型动词的高频次促进构式意义的学习。
  - Kurumada 2013：Zipf 分布促进语境中的词切分；单词识别成绩主要由该词频次预测。
  - Lavi-Rotbain & Arnon 2022：15 种语言的儿童导向语音一元熵相近，自然的可预测性水平促进切分。
- **映射与统计学习**：
  - Hendrickson & Perfors 2019：理论预测 Zipf 下跨情境词学习更难，实验中没有受损且往往更好。
  - Lavi-Rotbain & Arnon 2021：儿童与成人在 Zipf 条件下的视觉统计学习都好于均匀条件，低频三元组也受益。
  - Wolters 2024：两种偏斜分布下儿童的词–指称学习都好于均匀，低频项也是。
- **类内变化**：Perry 2010 中 18 月龄儿童学类别时，类内范例多变比高度相似更能推广到新成员。
- **作者给出的机制**：高频项作为锚，帮助切分或消解其他项的歧义（Kurumada 2013、Hendrickson & Perfors 2019）；分布熵低、更可预测（Lavi-Rotbain & Arnon 2022、Wolters 2024）；高频原型促成抽象（Goldberg 2004）。
- 这些实验偏斜的是项目之间的频次，Infant Lumpy 偏斜的是类内单一实例的占比。

## 3. 视觉：长尾、数据整理与同一实例的多视角（P§2）

### 3.1 表征不怕偏斜，分类器怕

- **监督长尾识别**：
  - Decoupling：按原始分布（instance-balanced）学到的表征最可泛化，作者认为数据不均衡 "might not be an issue" 对表征学习而言，只重平衡分类器即可。
  - BBN：固定分类器时，用原始分布学到的表征误差更低，重加权和重采样损害表征。
- **自监督**：
  - SSP Imbalance：自监督预训练在所有长尾方法上都带来提升，不均衡越严重收益越大。
  - SSL Imbalance：相同样本量下，SSL 的均衡与不均衡差距小于监督学习，OOD 评估上更明显。
- **目标函数的隐含先验**（Uniform Cluster Prior）：SimCLR、MSN、VICReg 等联合嵌入方法隐含"均匀聚类"先验，类不均衡 mini-batch 下 IN1K top-1 最多降 17.7；MAE、data2vec "relatively unaffected"。在 iNat18 上把均匀先验换成真实的长尾先验，下游全部提升（iNat18 +3.0%）。

### 3.2 稀有样本需要被记住

- Long Tail Memorization：子群体频次长尾时，要接近最优泛化误差，就必须记忆稀有样本的标签。
- Memorization Influence：ImageNet 上移除高记忆样本损失约 3.4% 测试准确率，移除同样数量的随机样本约 2.6%。

### 3.3 网络规模的数据整理：压平概念长尾

- **概念频次决定零样本表现**：Concept Frequency 中，zero-shot 表现与预训练概念频次呈对数线性关系；Neglected Tails 中 CLIP 在十多个 ImageNet 概念上低于 10%。
- **人为制造不均衡**：SSL Curation 把 ImageNet 按幂律重采样，SSL 线性准确率随 α = 0 / 0.5 / 1 / 2 为 82.7 / 79.0 / 74.2 / 57.0。原文没有说明各 α 下的总样本量是否相同。
- **截头留尾**：MetaCLIP 给每个元数据条目设上限 t=20k，头部子采样、尾部全保留，ImageNet zero-shot 从 60.8% 升到 65.5%；t=15k 或 35k 略差。
- **平衡不等于越多越好**：
  - DataComp 在固定训练所见样本数时，更小、过滤更严的子集（更多重复）可以泛化更好，CLIP-score 过滤保留约 30% 时最优。
  - DINOv2 的检索式整理在多数基准上更好，ADE-20k 上未整理数据略高（48.5 vs 47.7）。
- 这些工作调整的是概念之间的分布，没有研究每个概念内部用几个实例、每个实例多少视角。

### 3.4 同一实例的多视角

- Contrastive Invariances：实例判别型对比学习缺乏视角不变性和类内实例不变性；用视频中同一实例的自然时间变换作正对，可以提高视角不变性。
- CRIB：增量学习中物体重复出现显著减轻灾难性遗忘。
- One Video Stream：非 IID 的单一视频流学习可以接近 batch size 1 的 IID 学习。

### 3.5 小结

- 偏斜发生在类内实例或视角之间，并伴随外观变化时，小规模实验支持它有益（Bambach 2018、Tsutsui 2021、Infant Lumpy）。
- 偏斜发生在类别或概念之间时，表征层面基本不受伤（Decoupling、SSL Imbalance），但大规模开放类别设定下尾部系统性失败，压平头部有益（Concept Frequency、MetaCLIP、SSL Curation）。
- 检索范围内没有论文在大规模自监督中系统扫描"实例数 × 每实例视角数"并在新实例上评测。

## 4. 组合泛化与覆盖条件（P§3）

### 4.1 每个属性值都见过还不够

- CLEVR-CoGenT：条件 A 中立方体只取 4 种颜色、圆柱取另外 4 种，测试时互换；立方体和圆柱的颜色问答准确率 85% → 51%，球体不受影响。
- Schott 2022：dSprites、Shapes3D、MPI3D 等数据上，17 种方法、2000 多个模型在 composition、插值、外推划分上都大幅下降，原文 "regardless of supervision signal and architectural bias"。
- compositional zero-shot learning 的评测陷阱：
  - TMN 提出 generalized CZSL 评估，只评未见组合时朴素基线与复杂方法相当。
  - OW-CZSL 把测试搜索空间扩到全部 state × object，所有方法严重退化。
  - C-GQA 的组合空间超过 9.3k，test AUC 3.6%。
- CLIP：单物体属性组合泛化 92%，双物体属性绑定接近失败（CLIP Binding）；组合性能与表征解耦程度相关，数据量本身不能直接预测（CLIP Disentanglement）；单个物体的预训练频率能预测其未共现组合上的表现（CLIP Pair Frequency）。

### 4.2 覆盖比数据量重要

- Visual CG Scaling：
  - 数据量增加 4 倍、不增加新组合时，未见组合上仍有 60–80% 的准确率下降。
  - 组合覆盖在 0–10% 时模型学到伪特征；覆盖到 75–100% 时表征强烈线性化，多数数据集上零样本准确率 90% 以上。
  - 若表征线性分解，每个概念值只需 k=2 个组合就能完美泛化；作者说明这一命题在概念值增多时依赖的线性独立假设可能失效。
- CLEVR-HOPE：增加数据量不缩小系统性差距，增加属性多样性可以；多样性 6 时差距 7–14%，≥16 时接近 0。
- Category-Viewpoint OOD：数据量固定时，增加见过的类别–视角组合数显著提升未见组合的泛化。
- AO-CLEVr：8 色 × 3 形状，见过的组合越多，未见组合越好。
- CLIP DG-CG：域多样性是关键；只部分见过某个域时，组合泛化可能低于完全没见过该域。

### 4.3 理论给出的条件

各篇的形式不同，可归为三类条件：

- **边际覆盖**：每个分量或 slot 的取值范围都要被训练覆盖。
  - CG First Principles 称之为 compositional support；Provable OC CG 要求每个 slot 的边际覆盖全范围。
- **连通或秩条件**：
  - CG First Principles 的 sufficient support（雅可比满秩）；
  - Additive Decoders 要求支撑路径连通；
  - Modular Hyperteacher 要求 connected support，每个任务只含 1 个模块（K=1）时失败；
  - CRM 要求测试组合落在训练组合的仿射包内。
- **模型结构匹配**：组合式、加性、模块化结构，或线性正交分解的表征。
  - CG First Principles：正交支撑下组合式模型 R² 0.951，单体模型 −0.500。
  - Modular Hyperteacher：模块化结构下线性数量的稀疏组合就足够；ANIL、MAML 无论支撑如何都失败。
  - Linear Orthogonal CG：视觉嵌入模型的组合泛化要求表征线性分解且跨概念正交。
- **单体网络的规模路线**：Scaling CG 中，只要训练分布 "sufficiently covers the task space"，扩大数据和模型规模的 MLP 也能组合泛化，任务组成可以从隐层线性解码。
- **失败机制**：CG Kernel Theory 证明固定表征的核模型是 conjunction-wise additive，训练数据的统计会造成 memorization leak 与 shortcut bias。

### 4.4 哪些覆盖形状可行

- **可行**：
  - 对角带：Visual CG Scaling 按 (i, i+j mod n) 取组合；
  - 星形：Multiplicative Emergence 训练 000/100/010/001；
  - L 形或正交支撑：只对加性或组合式模型有效（Additive Decoders、CG First Principles）。
- **失败**：
  - 每个元素只有一个固定伙伴：SQOOP 中每个物体只有 1 个搭配伙伴时，MAC 错误率 13.67%、FiLM 34.73%，增加到 2 个起出现质变；
  - 训练节点在概念图上不相邻：Multiplicative Emergence；
  - 只有单因子样本：Factorize and Compose 中只有 1D 条纹时失败，加少量组合样本即可，样本复杂度从二次降到线性；
  - 支撑过窄或有缺口：CG First Principles 中 "fails exactly where the support is incomplete"。
- **数据总量固定时**，把样本分散到更多组合上一致更好（Category-Viewpoint OOD、SQOOP、CLEVR-HOPE、Visual CG Scaling、AO-CLEVr）。

### 4.5 频率：热门无害，冷门有害

- Scaling CG（M=16 个模块，K=3）："having a small set of popular modules who appear more frequently poses no issue"，而少数冷门模块 "does lead to a noticeable drop"。作者归因于冷门模块代表性不足，而不是频率不对称本身。
- Multiplicative Emergence：低频概念的组合需要多得多的训练步数。
- Hidden Capabilities：concept signal 决定概念的学习速度，信号不平衡时出现概念记忆。
- CLIP Pair Frequency：单个物体的预训练频率能预测组合表现；作者建议平衡物体频率，未做实验。
- **偏斜 × 组合留出没有直接实验**：MOSAIC 的组合留出实验刻意使用均匀分布（"a uniform distribution over seen pairs to avoid confounding effects from frequency imbalance"）；偏斜只出现在不留出组合的实验中，结论是场景复杂度的作用大于概念不均衡。

### 4.6 生成模型

- MOSAIC：在 10×10 等组合矩阵上留出 0、1、3、5、8 条对角线，留出越多，组合泛化越会 "collapses"，空间关系最受影响。
- Factorize and Compose：扩散模型能组合但不能插值。
- Forced Rendering：解耦的输入不足以组合泛化，模型在后层重新纠缠，靠数据叠加记忆。

## 5. LLM 与序列模型（P§4）

### 5.1 分布性质决定 ICL 与 in-weights 学习

- Bursty ICL（Omniglot 序列）：
  - burstiness、大量稀有类和偏斜的类别频率共同促成 in-context learning。
  - 类别频率均匀（Zipf 指数 α=0）时只有 ICL；α 增大后 in-weights 学习增强、ICL 减弱；α=1 时两者在同一模型中共存，原文限定 "for this particular training regime"。
  - 稀有类在任何 α 下都没有被记住。
- ICL Mechanistic：极简 attention-only 网络复现了这些数据依赖，ICL 由 induction head 的突然形成驱动。
- 时间维度：Transient ICL 中 ICL 先出现后消失，让位于 in-weights 学习，L2 正则使其更持久；Strategy Coopetition 给出 ICL 消失后的渐近策略。
- 覆盖维度：ICL Task Diversity 中预训练任务数超过阈值（D=8 时约 2^14–2^15）后才能解新任务，低于阈值时模型像以已见任务为先验的 Bayesian 估计器。

### 5.2 头部帮助尾部

- **Physics LM 3.1**（合成传记）：
  - 知识要能被提取，预训练阶段就必须有多样改写。
  - 只给 10 万名 celebrity 做多样改写，minority 组本身的数据不变、也不用于问答微调，minority 的问答准确率 bioS 从 4.4% 升到 86.8%，bioR 从 10.0% 升到 76.3%。
  - 只有形式相近的 celebrity 数据才有这一效果。
- **Fact Learning Dynamics**（合成传记的事实回忆）：
  - 学习分三阶段，中间有平台期。不均衡分布缩短平台期、拖慢知识获取；知识获取速度主要取决于最稀有个体的频率。
  - 训练预算固定为 16k 步时，使平台期最短的 α 在 0.6–0.8 之间，与个体数无关。
  - 先只训练一部分个体、再训练全体的调度显著增加最终知识量，个体数大时更明显。
  - 作者把这种调度类比为婴儿经历的隐式课程。
- **自然长尾下尾部学得差**：Long-Tail Knowledge 中 QA 准确率与相关预训练文档数相关且有因果，稀有题外推需要超过 10^18 参数；PopQA 中扩大规模对低流行度事实改善有限；Knowledge Overshadowing 中主导知识遮蔽冷门知识。
- **重复的方式**：Fact Acquisition 中重复注入的知识遗忘更快；Physics LM 3.3 中随机 junk 数据使知识容量最多降 20 倍，高度重复的 junk 无害。

### 5.3 组合：比例与覆盖

- Grokked Reasoners：隐式推理只能通过 grokking 获得；推断事实与原子事实之比 φ 决定泛化速度，固定 φ 时数据量几乎没有影响，作者称决定因素是 "critical data distribution"。composition 任务的 OOD 准确率训练到 2M 步仍为 0。
- MCD：保持原子分布相近、最大化复合分布散度来划测试集，复合散度与准确率 "surprisingly strong negative correlation"。
- Skill Composition：只用 k=2、3 的技能组合微调，就提升 k=4、5 和 held-out 技能的组合。
- Data Factors CG：更多样、单样例重复频率更低的数据集组合泛化更好；合成数据上简单样例诱导的组合性更强，真实语言数据上简单与困难样例均衡混合最好。
- Coverage Principle：单个实例的泛化成败可以由覆盖它的上下文数预测；二跳泛化所需数据至少随 token 集大小二次增长，参数扩大 20 倍也不提高数据效率。
- Implicit Multi-hop：隐式 k 跳推理所需数据随 k 指数增长，课程能缓解但不能消除。

### 5.4 幂律优于均匀：组合推理

- Power Law CR：
  - 在多步算术、k-hop state tracking、合成多跳 QA 等任务上，"training under power-law distributions consistently outperforms training under uniform distributions"。测试集都按技能均匀采样。
  - 默认幂律指数 α=1，state tracking 用 α=1.5。均匀分布下模型不借助 CoT 或课程学不会 state tracking，幂律下可以直接学会。
  - 理论上，极简技能组合任务在均匀分布下需要 d^Ω(k) 的样本或运行时间，幂律下梯度下降只需 d^O(1)。
  - 机制：幂律采样带来的不对称改善了病态的损失地形，模型先学会高频的技能组合，再学低频的。
- 作者自述实验多在算法或合成预训练设定中，能否迁移到真实技能组合尚待验证。

### 5.5 配比、重复与去重

- **最优配比既不是自然分布也不是均匀**：DoReMi 用 Group DRO 求域权重，达到基线所需步数少 2.6 倍；Data Mixing Laws 中优化配比相当于默认配比多训 48% 步数；RegMix 发现域间交互常常违反直觉。
- **多语言**：mT5、XLM-R 用 α=0.3 的温度采样压平自然分布；UniMax 指出这会把最低资源语言重复 100 多次，改为先均匀分配预算、再给每种语言设重复上限，效果更好。
- **重复的利弊取决于量与对象**：
  - Repeated Data：把 0.1% 的数据重复 100 次，800M 模型降到 400M 模型的水平。
  - Data-Constrained：整体重复 4 个 epoch 与唯一数据几乎相同，约 16 个 epoch 后价值急剧下降。
  - Dedup：去重后逐字输出记忆文本的频率降为十分之一。
  - D4：重复使用多样化挑选的数据优于基线，重复随机数据差于基线。
  - Repeated Examples：固定训练步数时，小数据多次重复优于大数据单次，模乘法 92% 对学不会。
  - Long-CoT Repetition：400 个样本训练 128 个 epoch，比 51,200 个样本训练 1 个 epoch 高 12–26 个百分点。
- **临界比例**：Mixing Phase Transition 中，知识密集数据的混合比低于临界值时几乎学不到，临界比与模型规模成幂律关系。

## 6. 具身与机器人策略（P§5）

### 6.1 因素组合与采集策略

- **不需要全组合**（Robot-Data-Comp）：
  - 因素包括物体位置、物体类型、桌面纹理、桌高、相机位置、干扰物。
  - 仿真中 Stair、L、Diagonal 策略只用 20 次因素改动就接近全组合（需 100 次）；Stair 在因素多时最好，也是唯一随数据量继续变好的策略。
  - 真机迁移到新厨房：Stair 31/40，L 24/40，不变化 1/40。
  - 视觉因素容易组合，"物体位置 × 桌高"组合最弱。
- **因素难度**（Factor World）：新相机位置最难、新背景最易，仿真与真机排序一致；多数因素对不叠加难度；连续因素的训练范围半径线性增大时 gap 约翻倍。
- **分布形状**（F-ACIL）：
  - 原文 "the distribution required for effective generalization is neither Gaussian-like nor Quasi-uniform"。
  - 按因素比例迭代扩展的分布，物体空间比准均匀省约 2–3 倍数据，物体–动作空间约 3–4 倍；高斯基线要超过 32k 条才达到它用 2–4k 条的水平。
  - 颜色对成功率影响有限，被排除出因素空间。
- **多样性优于数量**：
  - Data Scaling Laws：泛化随环境数、物体数近似幂律增长；8 / 16 / 32 对环境–物体分别在 400 / 800 / 1,600 条时饱和，推荐每对约 50 条。
  - GO-1-Pro：任务多样性比每任务示教数重要。
  - Env Drivers：训练物体与词的数量、第一人称视角、视觉输入多样性决定系统性泛化。
- **因素之间的相关比边际分布更危险**（Shortcut-OXE）：
  - 捷径来自子集内多样性低与子集间差异大。
  - 真机实验中两个视角各对应一个物体，视角能预测任务；加入一个在两个视角下都采集的第三个物体后，捷径程度 0.6 → 0，OOD 成功率 0.2 → 0.75；视角增广为 0.15 与 0.55。
  - 作者建议固定不重要或难以变化的因素，系统变化关心的因素，并刻意制造"只变一个因素"的桥接数据。
- **空间覆盖**：MOVE 让物体在采集中运动，在同等数据量下扩大空间覆盖；Sim2Real-VLA Study 中空间随机化比外观随机化更有效；Sim&Real Co-Train 中真实示教不覆盖工作区中部、仿真覆盖全区域时，中部位置成功率 Panda 11% → 28%，GR-1 43% → 100%。

### 6.2 动作的一致性与速度

- **同一状态下动作要一致**：
  - IL Data Quality：action divergence 越大策略越差；状态多样性不总是有益，适量噪声能扩大覆盖，过多则数据过稀。
  - robomimic：多操作员混合数据不如同等数量的熟练操作员数据，经验少的操作员轨迹更长。
  - DemInf：按状态–动作互信息过滤示教，RoboMimic +5–10%。
- **速度多模态**：
  - GO-1-Pro 区分两种专家多样性：轨迹的空间变化有益，执行速度的变化有害；统一动作速率后平均分 0.46 → 0.53（+15%），相当于 2.5 倍预训练数据。作者自述该去偏不适用于速度本身有意义的动态任务。
  - ISR：按信息等距重采样轨迹，跨操作员成功率约 +25%。
- **速度作为条件**：MoMo 把运动模式作为连续条件，只示教过一种模式的任务也能执行新模式；TempoVLA 用变速轨迹增广加速度条件。
- **任务无关的时序要打散**：CTR 中窄时序示教让双臂之间产生虚假耦合，在约束内重组时序后，最差状态成功率 56% → 76%。
- **轨迹内不是匀速最好**：
  - PIP：策略空转来自训练数据中精细段的小动作。
  - Perfect-Demo：对齐段放慢的示教 67.8%，流畅示教 52.2%，作者归因于更宽的恢复状态覆盖。
  - DemoSpeedup、ESPADA 只加速非精确段。
- **风格要贴近预训练分布**：DATAFARM 中原始 TAMP 数据微调 π0.5 只有 8.3%，与预训练分布对齐后 56.7%；DREAM 把生成数据难学归因于频繁的腕部旋转和冗余运动。

### 6.3 不均衡与重加权

- **偏斜伤稀有部分**：Zipfian Env 中按 Zipf 训练的 IMPALA 均匀评测 0.69、稀有评测 0.24；Balanced BC 证明逐样本等权会偏向多数行为。
- **重采样只能部分修复**：
  - Balanced BC：上采样到等比例后与平衡数据基本无差异，但等权忽略难度，按可达精度定权更好。
  - APA：任务级长尾下重采样几乎无效（基线 26.5%，三种设置 25.1–27.1%）；尾部任务的失败集中在接近目标阶段，从头部任务迁移接近段后 36.1%。
  - Temperature Sampling 只在单域测试。
- **时间上的不均衡**：FrameSkip 中低变化段主导按帧等权的训练，只保留 20% 唯一帧，66.50% → 76.15%。

### 6.4 组合泛化基准与方法

- **早期基准**：gSCAN 含留出颜色–形状组合的 8 个划分，基线只通过 1 个；CompoSuite 中某个组成只出现在一个训练任务时，零样本组合难得多。
- **VLA 基准**：
  - LIBERO-PRO：标准评测 90% 以上的策略在泛化评测上降到 0.0%。
  - LIBERO-Plus：相机与初始状态扰动下 95% → 30% 以下；成对扰动有一致的负组合性 gap。
  - COLOSSEUM：单因素扰动下降 30–50%，叠加 ≥75%；干扰物数、目标颜色、光照最伤。
  - Colosseum V2：初始位姿随机化是最主要的动作扰动，π0.5 单臂 −12.9%、双臂 −51.4%。
  - MESA：单臂最强基线域内 62.8%、组合 46.7%；加入 736 个辅助任务没有一致收益；MimicGen 生成的数据初始位置偏向易成功区域。
- **补组合的方法**：CRAFT 用反事实技能对缓解视觉捷径，真机未示教组合 9/60 → 43/60；ACT-VLA 合成组合示教，LIBERO Spatial-OOD 35.5% → 88.2%，只在仿真。

### 6.5 随机化分布

- 固定的均匀随机化被多篇超过：
  - Active DR 把次优、高方差策略归因于环境参数的均匀采样；
  - BayesSim 用真实轨迹推断的参数后验做随机化，优于均匀先验；
  - ADR 自动扩张随机化边界，比固定档位更快；
  - DORAEMON 在成功率约束下逐步增大随机化熵，优于直接用全范围均匀；
  - UED-Quadruped 中均匀关卡随机化进入 0/20 个最优组，成本相同、只改采样分布的偏易或混合难度分布进入多个最优组。
- 证据多来自 RL 的动力学随机化。模仿学习数据生成的对应证据：MetaGenSim 中均匀生成的仿真数据共训练后 23/80，低于纯真实 26/80，学到的生成分布 58/80；TUCO 中全部仿真池与随机半数子集都是 25.8%，影响函数选出的子集 85.8%。

### 6.6 四个具体分布的文献结论

- **行程长度**：
  - 回合时长与示教质量相关：robomimic 中经验少的操作员轨迹更长。
  - 按帧等权时，长度决定各阶段的曝光量（FrameSkip、ISR）。
  - 空间行程的支撑集比形状更先决定泛化：Factor World 中训练范围线性增大时 gap 约翻倍。
  - 缺口：检索范围内没有论文在固定其他因素时单独改变行程长度分布，也没有论文研究 sim 与 real 的长度错配对共训练的影响。
- **速度**：
  - 不加条件时，一致优于多样（GO-1-Pro、ISR、IL Data Quality）。
  - 需要多种速度时，做成显式条件（MoMo、TempoVLA、SpeedAug）。
  - 轨迹内的精确段不宜加速（Perfect-Demo、PIP、DemoSpeedup、ESPADA）。
  - 缺口：没有论文研究 sim + real 共训练中的速度分布；Speed prior 把示教重定时到手持采集的节奏，没有在共训练中测试。
- **抓取位置与姿态**：
  - 支撑集要覆盖测试范围（Colosseum V2、LIBERO-PRO、LIBERO-Plus、Sim&Real Co-Train）。
  - 支撑集内的明显不均衡伤少数区域，补到等比例能修复（Balanced BC）。
  - 均匀不是最优：按难度定权更好（Balanced BC）；F-ACIL 的动作因素是平面位置与 yaw，按比例扩展比准均匀省 2–4 倍数据；Mulligan 把初始状态集中到失败处，提升 10–34 个百分点。
  - 重采样不能代替新位姿（APA）；仿真生成器会改变位姿分布（MESA）。
  - 缺口：没有论文在等数据量下比较均匀、中心加密、难点加密的连续位姿分布。
- **颜色与形状组合**：
  - 不需要铺满所有组合，关键是每个属性值出现在多个不同上下文中（Robot-Data-Comp、F-ACIL、Env Drivers）。
  - 颜色较易组合，改变抓取运动的形状或尺寸较难（Robot-Data-Comp）；但目标颜色从未变化时仍是最伤的扰动之一（COLOSSEUM）。
  - 打破属性之间、属性与数据子集之间的相关（Shortcut-OXE、CRAFT）。
  - 缺口：没有论文在 sim + real 中控制"颜色 × 形状"的覆盖方式并做真机评测。

## 7. 横向结论

1. **均匀通常不是最优，但"偏斜有益"只在特定层级成立**。
   - 偏斜发生在类内实例或技能之间、且头部有变化地重复时，多个领域报告优于均匀：Infant Lumpy、Bambach 2018、Tsutsui 2021、Physics LM 3.1、Power Law CR、Fact Learning Dynamics。
   - 类别或概念层面的长尾在大规模设定中损害尾部：Concept Frequency、SSL Curation、Long-Tail Knowledge、Zipfian Env。
2. **头部可以多，尾部不能少**。
   - 热门模块无害、冷门模块有害（Scaling CG）。
   - 截头留尾（MetaCLIP），给重复设上限（UniMax）。
   - 知识获取速度由最稀有个体决定（Fact Learning Dynamics）。
3. **有变化的重复不同于逐字重复**：Infant Lumpy 的头部实例有大量视角；Physics LM 3.1 的 celebrity 有多种改写。逐字重复会加快遗忘或浪费容量：Fact Acquisition、Repeated Data、Dedup、Data Factors CG。
4. **偏斜主要改善优化，覆盖决定上限**。
   - 偏斜缩短平台期、提供垫脚石：Fact Learning Dynamics、Power Law CR、Bursty ICL。
   - 新任务与 OOD 组合仍受覆盖约束：ICL Task Diversity、Grokked Reasoners、Coverage Principle、Implicit Multi-hop。
5. **组合覆盖有可操作的条件**：每个属性值都出现，每个值至少有 2 个不同的搭配伙伴，组合图连通，模型结构与组合方式匹配。来源：CG First Principles、Modular Hyperteacher、SQOOP、Visual CG Scaling、Additive Decoders、Robot-Data-Comp。
6. **因素之间、因素与数据来源之间的相关，比边际分布的形状更危险**：Shortcut-OXE、CG Kernel Theory、CLIP DG-CG、Co-occurrence Bias。
7. **"均匀最优"常常来自学习目标或评测的假设**：联合嵌入 SSL 内置均匀先验（Uniform Cluster Prior）；表征与分类器偏好不同（Decoupling、BBN）。
8. **具身数据多一层动作分布**：同一状态下动作要一致，速度多样性要显式条件化：IL Data Quality、GO-1-Pro、MoMo、TempoVLA。
9. **随机化或生成分布：均匀可以作为终点，不宜作为起点**：ADR、DORAEMON、UED-Quadruped、MetaGenSim。

## 8. 文献自述的开放问题

- 实例频率偏斜与同一实例的外观变化，两者对泛化的贡献尚未拆开（Infant Lumpy）。
- lumpy 结构只对类别形成的最早阶段有利，还是在任何阶段都有利（Infant Lumpy）。
- 如何构造能从偏斜输入中学习的模型，是未来工作的关键挑战（BabyView）。
- "相似 + 多样"组合的具体机制与最优配比（Bambach 2018、Tsutsui 2021）。
- 发展课程何时、对哪类学习目标重要（Sheybani 2023）。
- 自监督预训练中真实的类先验通常未知，如何设定特征先验（Uniform Cluster Prior）。
- 平衡作为 SSL 数据准则尚未系统研究（SSL Curation）。
- "sufficiently covers" 没有量化定义（Scaling CG）。
- 理论只覆盖核模型，对深度网络的证据是定性的（CG Kernel Theory）。
- 预训练模型的表征只部分线性分解（Visual CG Scaling、Linear Orthogonal CG）。
- 组合留出下 counting 在训练损失下降时仍退化，没有机制解释（MOSAIC）。
- ICL 与 in-weights 学习共存的最佳点随训练设定变化（Bursty ICL）。
- 数据调度如何根据平台期结束时机自适应，后期仍需逐步多样化（Fact Learning Dynamics）。
- 幂律优势能否迁移到真实技能组合（Power Law CR）。
- 完全记住训练集为何与更好的泛化同时出现（Long-CoT Repetition）。
- 适合大模型的配比不一定适合小模型（Mixing Phase Transition）。
- OOD 组合失败需要架构层面的改进（Grokked Reasoners、Coverage Principle）。
- 速度去偏不适用于速度本身重要的动态任务（GO-1-Pro）。
- 结构化采集会让未纳入考虑的因素变差，需要先验数据才能恢复（Robot-Data-Comp）。
- 因素化表示 "neither unique nor necessarily optimal"（F-ACIL）。
- 如何在大规模数据中识别具体捷径、度量任务相关因素的多样性（Shortcut-OXE）。
- 模仿精度不等于任务成功，离线方法无法平衡各行为的测试表现（Balanced BC）。
- 随机化分布可能塌缩到容易区域，有先验时如何围绕先验增长（DORAEMON）。

## 9. 入门阅读顺序

1. **Infant Lumpy**：问题的出发点；先读精读笔记中的实验口径。
2. **Bambach 2018、Tsutsui 2021**：同一团队的前作，"相似 + 多样"混合的配比扫描。
3. **Lavi-Rotbain & Arnon 2021**：人类视觉学习中 Zipf 与均匀的直接对照。
4. **Decoupling、Uniform Cluster Prior**：分清表征与决策头，以及学习目标自带的分布先验。
5. **Physics LM 3.1、Fact Learning Dynamics**：头部帮助尾部的受控实验，以及偏斜与覆盖的权衡。
6. **Power Law CR**：组合推理上幂律优于均匀的实验与理论。
7. **CG First Principles、Visual CG Scaling**：组合泛化的覆盖条件，后者的 (n, k) 网格可直接作为实验模板。
8. **Scaling CG**：热门与冷门模块的不对称结论。
9. **Robot-Data-Comp、F-ACIL**：机器人数据的因素组合与分布形状。
10. **Shortcut-OXE**：因素相关与桥接数据。
11. **IL Data Quality、GO-1-Pro**：动作一致性与速度多模态。
