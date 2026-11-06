# data-distribution-generalization 论文目录

- 快照日期：2026-11-06
- 年份：首次公开的年份（arXiv 或正式发表，取较早者）。
- 会议/期刊：arXiv comment / journal-ref 字段、论文集、期刊页或 DOI 记录确认的发表处；"预印本" 表示未找到发表处。标 † 的发表处只见于索引或二手来源，见根目录 `issues.md` → ISSUE-005。
- 有 arXiv 的条目，标题、年份、编号经 arxiv.org 页面核实；期刊论文没有 arXiv 的，元数据取自 DOI（Crossref）或 PubMed 记录。
- 与其他方向重复的论文沿用其他方向 `papers.md` 中的简称与发表处。
- 分节对应 [survey.md](survey.md) 的分类；一篇论文只列在主归属的一节。

## 1. 认知发展：婴儿输入与人类学习

### 1.1 婴儿视觉输入的统计

- **Infant Lumpy** · 2025 · PNAS 2026 · [arXiv 2510.15060](https://arxiv.org/abs/2510.15060)
  - A solution to generalized learning from small training sets found in infants' repeated visual experiences of individual objects
  - 婴儿每个类别的视觉经验由少数实例主导、外观多变；"lumpy"训练集对新实例的泛化优于均匀采样。精读笔记：[notes/2025-infant-lumpy.md](notes/2025-infant-lumpy.md)
- **Clerkin 2017** · 2017 · Phil. Trans. R. Soc. B · [DOI 10.1098/rstb.2016.0055](https://doi.org/10.1098/rstb.2016.0055)
  - Real-world visual statistics and infants' first-learned object names
  - 居家用餐场景杂乱，但物体类别频次极度右偏，极少数物体几乎一直在场
- **Clerkin & Smith 2022** · 2022 · PNAS · [DOI 10.1073/pnas.2123239119](https://doi.org/10.1073/pnas.2123239119)
  - Real-world statistics at two timescales and a mechanism for infant learning of object names
  - 跨片段看类别普遍在场、命名稀少；片段内名称与指称物共现，但每对只出现在少数片段
- **Smith 2018** · 2018 · Trends in Cognitive Sciences · [DOI 10.1016/j.tics.2018.02.004](https://doi.org/10.1016/j.tics.2018.02.004)
  - The Developing Infant Creates a Curriculum for Statistical Learning
  - 感知运动发展产生随时间变化、每个时间点都高度选择性的输入序列

### 1.2 用婴儿与儿童数据训练模型

- **SAYCam** · 2021 · Open Mind · [DOI 10.1162/opmi_a_00039](https://doi.org/10.1162/opmi_a_00039)
  - SAYCam: A Large, Longitudinal Audiovisual Dataset Recorded From the Infant's Perspective
  - 6–32 个月婴儿约每周 2 小时的头戴相机纵向音视频语料
- **Orhan 2020** · 2020 · NeurIPS 2020 · [arXiv 2007.16189](https://arxiv.org/abs/2007.16189)
  - Self-supervised learning through the eyes of a child
  - 时间分类目标在儿童视频上学到可用表征；对比学习目标在所有条件下都不如时间分类
- **Orhan & Lake 2024** · 2023 · Nature Machine Intelligence 2024 · [arXiv 2305.15372](https://arxiv.org/abs/2305.15372) · [代码](https://github.com/eminorhan/silicon-menagerie)
  - Learning high-level visual representations from a child's perspective without strong inductive biases
  - 单个儿童约 200 小时视频训练的最佳嵌入模型，达到 ImageNet 训练模型的约 70%
- **CVCL** · 2024 · Science · [DOI 10.1126/science.adi1374](https://doi.org/10.1126/science.adi1374)
  - Grounded language acquisition through the eyes and ears of a single child
  - 一名儿童 61 小时的视听数据足以学到许多词–指称映射，并能泛化到新的视觉指称物
- **BabyView** · 2024 · CCN 2025（arXiv comment） · [arXiv 2406.10447](https://arxiv.org/abs/2406.10447)
  - The BabyView dataset: High-resolution egocentric videos of infants' and young children's everyday experiences
  - 868 小时高分辨率居家视频；帧数相当时不优于 SAYCam，外推需 10^7 小时以上才能追上精选数据
- **Sheybani 2023** · 2023 · NeurIPS 2023 · [DOI 10.52202/075280-2360](https://doi.org/10.52202/075280-2360)
  - Curriculum Learning With Infant Egocentric Videos
  - 按发展顺序预训练优于反序和随机混合；效应随模型和训练长度变化
- **Bambach 2018** · 2018 · NeurIPS 2018 · [论文集](https://proceedings.neurips.cc/paper/2018/hash/48ab2f9b45957ab574cf005eb8a76760-Abstract.html)
  - Toddler-Inspired Visual Object Learning
  - 样本量相同时，保留"相似为主 + 多样长尾"的原始幼儿分布，优于纯相似子集和纯多样子集
- **Tsutsui 2021** · 2021 · CVPR 2021 Workshop (EPIC) · [arXiv 2106.06694](https://arxiv.org/abs/2106.06694)
  - Reverse-engineer the Distributional Structure of Infant Egocentric Views for Training Generalizable Image Classifiers
  - 相似与多样的混合在各样本量下都优于任一单独；每类 100–200 张时，75% 相似 + 25% 多样与原始儿童数据持平
- **Pandey 2023** · 2023 · NeurIPS 2023 · [arXiv 2312.02843](https://arxiv.org/abs/2312.02843)
  - Are Vision Transformers More Data Hungry Than Newborn Visual Systems?
  - 用小鸡饲养环境中的单物体、有限视角数据训练的 ViT，解决了与小鸡相同的视角不变识别任务
- **DoRA** · 2023 · ICLR 2024 · [arXiv 2310.08584](https://arxiv.org/abs/2310.08584) · [项目](https://shashankvkt.github.io/dora)
  - Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video
  - 单段长视频预训练在 ADE20k 上比 ImageNet 上的 DINO 高 1.5 mIoU

### 1.3 人类学习中的偏斜输入

- **Goldberg 2004** · 2004 · Cognitive Linguistics · [DOI 10.1515/cogl.2004.011](https://doi.org/10.1515/cogl.2004.011)
  - Learning argument structure generalizations
  - 单一原型动词的高频次促进构式意义的学习
- **Kurumada 2013** · 2013 · Cognition · [DOI 10.1016/j.cognition.2013.02.002](https://doi.org/10.1016/j.cognition.2013.02.002)
  - Zipfian frequency distributions facilitate word segmentation in context
  - Zipf 分布促进语境中的词切分；单词识别成绩主要由该词频次预测
- **Hendrickson & Perfors 2019** · 2019 · Cognition · [DOI 10.1016/j.cognition.2019.03.005](https://doi.org/10.1016/j.cognition.2019.03.005)
  - Cross-situational learning in a Zipfian environment
  - 理论预测 Zipf 更难，实验中跨情境词学习没有受损且往往更好
- **Lavi-Rotbain & Arnon 2021** · 2020 · Cognition 2021 · [DOI 10.1016/j.cognition.2020.104492](https://doi.org/10.1016/j.cognition.2020.104492)
  - Visual statistical learning is facilitated in Zipfian distributions
  - 儿童与成人在 Zipf 条件下的视觉统计学习都好于均匀条件，低频三元组也受益
- **Lavi-Rotbain & Arnon 2022** · 2022 · Cognition · [DOI 10.1016/j.cognition.2022.105038](https://doi.org/10.1016/j.cognition.2022.105038)
  - The learnability consequences of Zipfian distributions in language
  - 15 种语言儿童导向语音的一元熵相近；自然的可预测性水平促进词切分
- **Wolters 2024** · 2024 · Cognition · [DOI 10.1016/j.cognition.2024.105932](https://doi.org/10.1016/j.cognition.2024.105932)
  - Zipfian distributions facilitate children's learning of novel word-referent mappings
  - 两种偏斜分布下儿童的词–指称学习都好于均匀分布，低频项也是
- **Perry 2010** · 2010 · Psychological Science · [DOI 10.1177/0956797610389189](https://doi.org/10.1177/0956797610389189)
  - Learn locally, think globally: Exemplar variability supports higher-order generalization and word learning
  - 18 月龄儿童学类别时，类内范例多变比高度相似更能推广到新成员

### 1.4 补充

- **Tsutsui 2019** · 2019 · CVPR 2019 Workshop (EPIC) · [arXiv 1906.01415](https://arxiv.org/abs/1906.01415)
  - Active Object Manipulation Facilitates Visual Object Learning: An Egocentric Vision Study
  - 有手部操作的视图作训练数据时优于无手视图
- **Tsutsui 2020** · 2020 · CogSci 2020 · [arXiv 2006.02802](https://arxiv.org/abs/2006.02802)
  - A Computational Model of Early Word Learning from the Infant's Point of View
  - 从婴儿眼动与第一视角视频端到端学习名称–物体映射
- **Orhan 2024 Video** · 2024 · CogSci 2024（arXiv comment） · [arXiv 2402.00300](https://arxiv.org/abs/2402.00300)
  - Self-supervised learning of video representations from a child's perspective
  - 同一儿童数据上，视频模型学到的物体表征比图像模型更准确、更稳健
- **Vong & Lake 2025** · 2025 · 预印本 · [arXiv 2507.14749](https://arxiv.org/abs/2507.14749)
  - On the robustness of modeling grounded word learning through a child's egocentric input
  - 用自动转写把 SAYCam 扩展到 3 名儿童、500 多小时，复现词–指称学习并报告个体差异
- **BabyCL** · 2026 · 预印本 · [arXiv 2606.05115](https://arxiv.org/abs/2606.05115)
  - Continual Visual and Verbal Learning Through a Child's Egocentric Input
  - 按时间顺序单遍训练 SAYCam，缩小与离线打乱多轮训练的差距
- **Toddler Gaze SSL** · 2024 · 预印本 · [arXiv 2411.01969](https://arxiv.org/abs/2411.01969)
  - Toddlers' Active Gaze Behavior Supports Self-Supervised Object Learning
  - 按注视点裁剪的中央视野有助于学到不变的物体表征
- **Gaze Object SSL** · 2025 · 预印本 · [arXiv 2501.02966](https://arxiv.org/abs/2501.02966)
  - Human Gaze Boosts Object-Centered Representation Learning
  - 人类注视引导的裁剪提升物体中心的表征学习
- **Wonnacott 2012** · 2012 · Journal of Memory and Language · [DOI 10.1016/j.jml.2011.11.004](https://doi.org/10.1016/j.jml.2011.11.004)
  - Input effects on the acquisition of a novel phrasal construction in 5 year olds
  - 偏斜与均衡输入对构式习得的影响；结论未核实，见 ISSUE-005

## 2. 视觉：长尾、数据整理与同一实例的多视角

### 2.1 长尾识别：表征与分类器

- **Decoupling** · 2019 · ICLR 2020 · [arXiv 1910.09217](https://arxiv.org/abs/1910.09217)
  - Decoupling Representation and Classifier for Long-Tailed Recognition
  - 按原始（实例均衡）分布学到的表征最可泛化，只需重平衡分类器
- **BBN** · 2019 · CVPR 2020 · [arXiv 1912.02413](https://arxiv.org/abs/1912.02413)
  - BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition
  - 重加权、重采样有利于分类器但损害表征
- **SSP Imbalance** · 2020 · NeurIPS 2020 · [arXiv 2006.07529](https://arxiv.org/abs/2006.07529)
  - Rethinking the Value of Labels for Improving Class-Imbalanced Learning
  - 自监督预训练在所有长尾方法上都带来提升，不均衡越严重收益越大
- **SSL Imbalance** · 2021 · ICLR 2022 · [arXiv 2110.05025](https://arxiv.org/abs/2110.05025)
  - Self-supervised Learning is More Robust to Dataset Imbalance
  - 相同样本量下，SSL 的均衡与不均衡差距小于监督学习，OOD 评估上更明显
- **Uniform Cluster Prior** · 2022 · ICLR 2023† · [arXiv 2210.07277](https://arxiv.org/abs/2210.07277)
  - The Hidden Uniform Cluster Prior in Self-Supervised Learning
  - 联合嵌入 SSL 隐含均匀聚类先验，类不均衡 mini-batch 下 IN1K 最多降 17.7；换成长尾先验后 iNat18 等下游提升
- **Long Tail Memorization** · 2019 · STOC 2020 · [arXiv 1906.05271](https://arxiv.org/abs/1906.05271)
  - Does Learning Require Memorization? A Short Tale about a Long Tail
  - 子群体频次长尾时，接近最优泛化误差必须记忆稀有样本的标签
- **Memorization Influence** · 2020 · NeurIPS 2020 · [arXiv 2008.03703](https://arxiv.org/abs/2008.03703)
  - What Neural Networks Memorize and Why: Discovering the Long Tail via Influence Estimation
  - 移除 ImageNet 高记忆样本损失约 3.4% 测试准确率，移除同样数量随机样本约 2.6%

### 2.2 大规模数据整理

- **MetaCLIP** · 2023 · ICLR 2024 · [arXiv 2309.16671](https://arxiv.org/abs/2309.16671)
  - Demystifying CLIP Data
  - 每个元数据条目设上限 t=20k（头部子采样、尾部全保留），ImageNet zero-shot 从 60.8% 升到 65.5%
- **DINOv2** · 2023 · TMLR · [arXiv 2304.07193](https://arxiv.org/abs/2304.07193)
  - DINOv2: Learning Robust Visual Features without Supervision
  - 检索式整理的 LVD-142M 在多数基准上优于同来源的未整理数据，ADE-20k 上未整理数据略高
- **SSL Curation** · 2024 · TMLR · [arXiv 2405.15613](https://arxiv.org/abs/2405.15613)
  - Automatic Data Curation for Self-Supervised Learning: A Clustering-Based Approach
  - ImageNet 按幂律重采样后，SSL 线性准确率 82.7 → 57.0（α 0 → 2）；层次 k-means 均衡采样
- **DataComp** · 2023 · NeurIPS 2023 Datasets & Benchmarks · [arXiv 2304.14108](https://arxiv.org/abs/2304.14108)
  - DataComp: In search of the next generation of multimodal datasets
  - 固定训练所见样本数时，更小、过滤更严的子集可以泛化更好；CLIP-score 过滤保留约 30% 最优
- **Concept Frequency** · 2024 · NeurIPS 2024 · [arXiv 2404.04125](https://arxiv.org/abs/2404.04125)
  - No "Zero-Shot" Without Exponential Data: Pretraining Concept Frequency Determines Multimodal Model Performance
  - zero-shot 表现与预训练概念频次呈对数线性关系
- **Neglected Tails** · 2024 · CVPR 2024 · [arXiv 2401.12425](https://arxiv.org/abs/2401.12425) · [项目](https://shubhamprshr27.github.io/neglected-tails-of-vlms)
  - The Neglected Tails in Vision-Language Models
  - LAION 概念分布长尾；CLIP 在十多个 ImageNet 概念上低于 10%

### 2.3 同一实例的多视角

- **Contrastive Invariances** · 2020 · NeurIPS 2020 · [arXiv 2007.13916](https://arxiv.org/abs/2007.13916)
  - Demystifying Contrastive Self-Supervised Learning: Invariances, Augmentations and Dataset Biases
  - 实例判别型对比学习缺乏视角不变性；用视频中同一实例的自然时间变换作正对可以提高
- **CRIB** · 2019 · CVPR 2019 · [DOI 10.1109/cvpr.2019.00898](https://doi.org/10.1109/cvpr.2019.00898)
  - Incremental Object Learning From Contiguous Views
  - 增量学习中物体重复出现显著减轻灾难性遗忘
- **One Video Stream** · 2023 · CVPR 2024（arXiv comment） · [arXiv 2312.00598](https://arxiv.org/abs/2312.00598)
  - Learning from One Continuous Video Stream
  - 非 IID 的单一视频流学习可以接近 batch size 1 的 IID 学习

## 3. 组合泛化与覆盖条件

### 3.1 视觉组合留出的实证

- **CLEVR-CoGenT** · 2016 · CVPR 2017† · [arXiv 1612.06890](https://arxiv.org/abs/1612.06890)
  - CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning
  - 训练时立方体与圆柱各只取 4 种颜色，测试互换；颜色问答准确率 85% → 51%
- **Schott 2022** · 2021 · ICLR 2022 · [arXiv 2107.08221](https://arxiv.org/abs/2107.08221)
  - Visual Representation Learning Does Not Generalize Strongly Within the Same Domain
  - 17 种方法、2000 多个模型在 composition、插值、外推划分上都明显退化
- **TMN** · 2019 · ICCV 2019† · [arXiv 1905.05908](https://arxiv.org/abs/1905.05908)
  - Task-Driven Modular Networks for Zero-Shot Compositional Learning
  - 提出 generalized CZSL 评估；只评未见组合时朴素基线与复杂方法相当
- **OW-CZSL** · 2021 · CVPR 2021 · [arXiv 2101.12609](https://arxiv.org/abs/2101.12609)
  - Open World Compositional Zero-Shot Learning
  - 测试搜索空间扩到全部 state × object 时，所有方法严重退化
- **C-GQA** · 2021 · CVPR 2021 · [arXiv 2102.01987](https://arxiv.org/abs/2102.01987) · [代码](https://github.com/ExplainableML/czsl)
  - Learning Graph Embeddings for Compositional Zero-shot Learning
  - C-GQA 组合空间超过 9.3k，test AUC 3.6%
- **AO-CLEVr** · 2020 · NeurIPS 2020 · [arXiv 2006.14610](https://arxiv.org/abs/2006.14610) · [代码](https://github.com/nv-research-israel/causal_comp)
  - A causal view of compositional zero-shot recognition
  - 8 色 × 3 形状，见过的组合越多，未见组合越好
- **Category-Viewpoint OOD** · 2020 · Nature Machine Intelligence 2022† · [arXiv 2007.08032](https://arxiv.org/abs/2007.08032)
  - When and how CNNs generalize to out-of-distribution category-viewpoint combinations
  - 数据量固定时，增加见过的类别–视角组合数显著提升未见组合的泛化
- **SQOOP** · 2018 · ICLR 2019 · [arXiv 1811.12889](https://arxiv.org/abs/1811.12889)
  - Systematic Generalization: What Is Required and Can It Be Learned?
  - 每个物体只有 1 个搭配伙伴时通用模型失败，增加到 2 个起出现质变；树状模块网络完美泛化
- **CLEVR-HOPE** · 2023 · EMNLP 2024 · [arXiv 2311.08695](https://arxiv.org/abs/2311.08695)
  - Attribute Diversity Determines the Systematicity Gap in VQA
  - 增加数据量不缩小系统性差距，增加属性多样性可以；多样性 ≥16 时差距接近 0
- **Visual CG Scaling** · 2025 · ICML 2025 · [arXiv 2507.07102](https://arxiv.org/abs/2507.07102) · [代码](https://github.com/oshapio/visual-compositional-generalization)
  - Does Data Scaling Lead to Visual Compositional Generalization?
  - 组合泛化由多样性而非数据量驱动；组合覆盖高时表征趋向线性分解
- **CLIP DG-CG** · 2025 · ICML 2025 · [arXiv 2502.09507](https://arxiv.org/abs/2502.09507)
  - When and How Does CLIP Enable Domain and Compositional Generalization?
  - 域多样性是关键；部分见过的域上，组合泛化可能低于完全未见的域
- **CLIP Disentanglement** · 2024 · ECCV 2024 · [arXiv 2407.05897](https://arxiv.org/abs/2407.05897)
  - Deciphering the Role of Representation Disentanglement: Investigating Compositional Generalization in CLIP Models
  - 属性–物体组合泛化与表征解耦程度相关，预训练数据量本身不能直接预测
- **CLIP Binding** · 2022 · Findings of EACL 2024 · [arXiv 2212.10537](https://arxiv.org/abs/2212.10537) · [代码](https://github.com/marthaflinderslewis/clip-binding)
  - Does CLIP Bind Concepts? Probing Compositionality in Large Image Models
  - 单物体组合泛化 92%，双物体属性绑定接近失败
- **CLIP Pair Frequency** · 2025 · NeurIPS 2024 Workshop · [arXiv 2502.18326](https://arxiv.org/abs/2502.18326)
  - Pretraining Frequency Predicts Compositional Generalization of CLIP on Real-World Tasks
  - 单个物体在预训练中的频率能预测其未共现组合上的表现
- **OC vs Dense CG** · 2026 · 预印本 · [arXiv 2602.16689](https://arxiv.org/abs/2602.16689)
  - Are Object-Centric Representations Better At Compositional Generalization?
  - 下游模型小、数据少时，物体中心表征在留出组合上更好
- **Lost in Latent Space** · 2022 · NeurIPS 2022 · [arXiv 2204.02283](https://arxiv.org/abs/2204.02283)
  - Lost in Latent Space: Disentangled Models and the Challenge of Combinatorial Generalisation
  - 解耦模型在留出因子组合上失败时，编码器本身就映射错误

### 3.2 生成模型中的组合

- **Multiplicative Emergence** · 2023 · NeurIPS 2023 · [arXiv 2310.09336](https://arxiv.org/abs/2310.09336)
  - Compositional Abilities Emerge Multiplicatively: Exploring Diffusion Models on a Synthetic Task
  - 组合能力按概念图距离依次、乘性涌现；低频概念需要多得多的训练步数
- **Hidden Capabilities** · 2024 · NeurIPS 2024 · [arXiv 2406.19370](https://arxiv.org/abs/2406.19370)
  - Emergence of Hidden Capabilities: Exploring Learning Dynamics in Concept Space
  - concept signal 决定概念学习速度；信号不平衡时出现概念记忆
- **MOSAIC** · 2026 · ICML 2026 · [arXiv 2605.00273](https://arxiv.org/abs/2605.00273)
  - When Do Diffusion Models learn to Generate Multiple Objects?
  - 场景复杂度的作用大于概念不均衡；留出的组合越多，组合泛化越会崩溃
- **Factorize and Compose** · 2024 · NeurIPS 2024 · [arXiv 2408.13256](https://arxiv.org/abs/2408.13256)
  - How Diffusion Models Learn to Factorize and Compose
  - 只有单因子样本时失败，加少量组合样本就够；能组合但不能插值
- **Forced Rendering** · 2025 · 预印本 · [arXiv 2501.18797](https://arxiv.org/abs/2501.18797)
  - Compositional Generalization via Forced Rendering of Disentangled Latents
  - 解耦的输入不足以组合泛化，模型会在后层重新纠缠
- **CoInD** · 2025 · 预印本 · [arXiv 2503.04687](https://arxiv.org/abs/2503.04687)
  - Compositional World Knowledge leads to High Utility Synthetic data
  - 普通条件扩散生成缺失组合不忠实，强制条件独立后改善

### 3.3 理论：什么样的覆盖保证组合泛化

- **CG First Principles** · 2023 · NeurIPS 2023 · [arXiv 2307.05596](https://arxiv.org/abs/2307.05596)
  - Compositional Generalization from First Principles
  - compositional support 与 sufficient support 两个条件；组合式模型在正交支撑下 R² 0.951，单体模型 −0.500
- **Provable OC CG** · 2023 · ICLR 2024 · [arXiv 2310.05327](https://arxiv.org/abs/2310.05327)
  - Provable Compositional Generalization for Object-Centric Learning
  - 每个 slot 的边际覆盖全范围时，加性解码器加一致性损失可证明组合泛化
- **Provable OC** · 2023 · ICML 2023 · [arXiv 2305.14229](https://arxiv.org/abs/2305.14229)
  - Provably Learning Object-Centric Representations
  - 生成过程满足组合性与不可约性时物体表征可辨识
- **Additive Decoders** · 2023 · NeurIPS 2023 · [arXiv 2307.02598](https://arxiv.org/abs/2307.02598)
  - Additive Decoders for Latent Variables Identification and Cartesian-Product Extrapolation
  - L 形支撑上只有加性解码器能外推，支撑须路径连通
- **Modular Hyperteacher** · 2023 · ICLR 2024 · [arXiv 2312.15001](https://arxiv.org/abs/2312.15001) · [代码](https://github.com/smonsays/modular-hyperteacher)
  - Discovering modular solutions that generalize compositionally
  - 模块化结构下线性数量的稀疏组合就足够；需要 compositional 与 connected support
- **Scaling CG** · 2025 · NeurIPS 2025 · [arXiv 2507.07207](https://arxiv.org/abs/2507.07207) · [代码](https://github.com/smonsays/scale-compositionality)
  - Scaling can lead to compositional generalization
  - 覆盖足够时扩规模的 MLP 能组合泛化；少数热门模块无害，少数冷门模块明显有害
- **CG Kernel Theory** · 2024 · ICLR 2025 · [arXiv 2405.16391](https://arxiv.org/abs/2405.16391)
  - When does compositional structure yield compositional generalization? A kernel theory
  - 固定表征的核模型是 conjunction-wise additive；训练统计导致 memorization leak 与 shortcut bias
- **CRM** · 2024 · ICML 2025 · [arXiv 2410.06303](https://arxiv.org/abs/2410.06303) · [代码](https://github.com/facebookresearch/compositional-risk-minimization)
  - Compositional Risk Minimization
  - 测试组合落在训练组合的仿射包内即可外推；Waterbirds worst-group 43.0 → 78.7
- **Nonlinear Extrapolation** · 2022 · 预印本 · [arXiv 2211.11719](https://arxiv.org/abs/2211.11719)
  - First Steps Toward Understanding the Extrapolation of Nonlinear Models to Unseen Domains
  - 边际分布近似不变时，加性模型能外推到未见的联合分布
- **Linear Orthogonal CG** · 2026 · ICML 2026 · [arXiv 2602.24264](https://arxiv.org/abs/2602.24264) · [代码](https://github.com/oshapio/necessary-compositionality)
  - Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models
  - 组合泛化要求表征线性分解且跨概念正交

## 4. LLM 与序列模型

### 4.1 分布性质与 in-context learning 的出现

- **Bursty ICL** · 2022 · NeurIPS 2022 · [arXiv 2205.05055](https://arxiv.org/abs/2205.05055) · [代码](https://github.com/deepmind/emergent_in_context_learning)
  - Data Distributional Properties Drive Emergent In-Context Learning in Transformers
  - burstiness 与大量稀有类促成 ICL；均匀分布只有 ICL，Zipf 指数约 1 时 ICL 与 in-weights 学习共存
- **Transient ICL** · 2023 · NeurIPS 2023 · [arXiv 2311.08360](https://arxiv.org/abs/2311.08360)
  - The Transient Nature of Emergent In-Context Learning in Transformers
  - ICL 先出现后消失，让位于 in-weights 学习；L2 正则使其更持久
- **ICL Task Diversity** · 2023 · NeurIPS 2023 · [arXiv 2306.15063](https://arxiv.org/abs/2306.15063) · [代码](https://github.com/mansheej/icl-task-diversity)
  - Pretraining task diversity and the emergence of non-Bayesian in-context learning for regression
  - 预训练任务数超过阈值（D=8 时约 2^14–2^15）后才能解新任务
- **ICL Mechanistic** · 2023 · ICLR 2024 · [arXiv 2312.03002](https://arxiv.org/abs/2312.03002)
  - The mechanistic basis of data dependence and abrupt learning in an in-context classification task
  - 极简网络复现 burstiness 与偏斜 rank-frequency 对 ICL / IWL 权衡的作用
- **Strategy Coopetition** · 2025 · ICML 2025 · [arXiv 2503.05631](https://arxiv.org/abs/2503.05631)
  - Strategy Coopetition Explains the Emergence and Transience of In-Context Learning
  - ICL 消失后的渐近策略是 context-constrained in-weights learning，与 ICL 既竞争又合作
- **ICL Plateau** · 2024 · TMLR 2025 · [arXiv 2410.05448](https://arxiv.org/abs/2410.05448)
  - Task Diversity Shortens the ICL Plateau
  - 同时训练多种 ICL 任务会缩短损失平台期
- **ICL Competition** · 2024 · ICLR 2025 · [arXiv 2412.01003](https://arxiv.org/abs/2412.01003)
  - Competition Dynamics Shape Algorithmic Phases of In-Context Learning
  - 多种算法竞争产生 ICL 的瞬态；低任务多样性缩短平台期但 OOD 更差
- **Rational ICL** · 2025 · NeurIPS 2025 · [arXiv 2506.17859](https://arxiv.org/abs/2506.17859)
  - In-Context Learning Strategies Emerge Rationally
  - 分层 Bayesian 框架描述记忆型与泛化型预测器之间的转换
- **In-context Pretraining** · 2023 · ICLR 2024 · [arXiv 2310.10638](https://arxiv.org/abs/2310.10638)
  - In-context Pretraining: Language Modeling Beyond Document Boundaries
  - 相关文档拼进同一上下文（人为 burstiness），ICL +8%，阅读理解 +15%

### 4.2 头部、尾部与知识获取

- **Physics LM 3.1** · 2023 · ICML 2024 · [arXiv 2309.14316](https://arxiv.org/abs/2309.14316)
  - Physics of Language Models: Part 3.1, Knowledge Storage and Extraction
  - 预训练加入多样改写的 celebrity，minority 组 QA 准确率 4.4% → 86.8%（bioS）
- **Physics LM 3.3** · 2024 · ICLR 2025 · [arXiv 2404.05405](https://arxiv.org/abs/2404.05405)
  - Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws
  - 随机 junk 数据使知识容量最多降 20 倍，高度重复的 junk 无害；域名前缀缓解损失
- **Long-Tail Knowledge** · 2022 · ICML 2023 · [arXiv 2211.08411](https://arxiv.org/abs/2211.08411)
  - Large Language Models Struggle to Learn Long-Tail Knowledge
  - QA 准确率与相关预训练文档数相关且有因果；稀有题外推需要超过 10^18 参数
- **PopQA** · 2022 · ACL 2023 · [arXiv 2212.10511](https://arxiv.org/abs/2212.10511) · [代码](https://github.com/AlexTMallen/adaptive-retrieval)
  - When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories
  - 低流行度事实难学，扩大规模改善有限
- **Fact Acquisition** · 2024 · NeurIPS 2024 · [arXiv 2406.11813](https://arxiv.org/abs/2406.11813)
  - How Do Large Language Models Acquire Factual Knowledge During Pretraining?
  - 重复注入的知识遗忘更快，改写注入更稳；遗忘与步数呈幂律
- **Knowledge Overshadowing** · 2025 · Findings of ACL 2025 · [arXiv 2502.16143](https://arxiv.org/abs/2502.16143)
  - The Law of Knowledge Overshadowing: Towards Understanding, Predicting, and Preventing LLM Hallucination
  - 主导知识遮蔽冷门知识，幻觉率随相对流行度的对数近似线性增长
- **Term Frequency** · 2022 · Findings of EMNLP 2022 · [arXiv 2202.07206](https://arxiv.org/abs/2202.07206)
  - Impact of Pretraining Term Frequencies on Few-Shot Numerical Reasoning
  - 最常见 10% 的项比最罕见 10% 的项准确率高出最多 70 个百分点以上
- **Co-occurrence Bias** · 2023 · Findings of EMNLP 2023 · [arXiv 2310.08256](https://arxiv.org/abs/2310.08256)
  - Impact of Co-occurrence on Factual Knowledge of Large Language Models
  - 共现偏差使模型偏向高共现的错误答案

### 4.3 组合与系统性泛化

- **Grokked Reasoners** · 2024 · NeurIPS 2024 · [arXiv 2405.15071](https://arxiv.org/abs/2405.15071) · [代码](https://github.com/OSU-NLP-Group/GrokkedTransformer)
  - Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization
  - 推断 / 原子事实之比 φ 决定泛化速度，数据量影响很小；composition 的 OOD 准确率始终为 0
- **Skill Composition** · 2024 · NeurIPS 2024 · [arXiv 2409.19808](https://arxiv.org/abs/2409.19808)
  - Can Models Learn Skill Composition from Examples?
  - 只用 k=2、3 的技能组合微调，提升 k=4、5 和 held-out 技能的组合
- **MCD** · 2019 · ICLR 2020 · [arXiv 1912.09713](https://arxiv.org/abs/1912.09713)
  - Measuring Compositional Generalization: A Comprehensive Method on Realistic Data
  - 原子分布相近、复合分布散度最大的划分；复合散度与准确率强负相关
- **MLC** · 2023 · Nature · [PMC10620072](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/)
  - Human-like systematic generalization through a meta-learning neural network
  - 在动态组合任务流上元学习，系统性输出率 82.4%，人类 80.7%
- **Data Factors CG** · 2023 · EMNLP 2023 · [arXiv 2311.04420](https://arxiv.org/abs/2311.04420) · [代码](https://github.com/owenzx/data4comp)
  - Data Factors for Better Compositional Generalization
  - 更多样、单样例重复更少的数据集组合泛化更好
- **Compositionality Decomposed** · 2019 · JAIR 2020 · [arXiv 1908.08351](https://arxiv.org/abs/1908.08351)
  - Compositionality decomposed: how do neural networks generalise?
  - 系统性、生产性、替换性、局部性、过度泛化五项测试
- **Skill Emergence Theory** · 2023 · 预印本 · [arXiv 2307.15936](https://arxiv.org/abs/2307.15936)
  - A Theory for Emergence of Complex Skills in Language Models
  - k 元技能组合的能力与基本技能以基本相同的 scaling 出现
- **Skill-Mix** · 2023 · ICLR 2024 · [arXiv 2310.17567](https://arxiv.org/abs/2310.17567)
  - Skill-Mix: a Flexible and Expandable Family of Evaluations for AI models
  - 随机抽 k 个技能要求组合的评测，组合数超出训练覆盖
- **Coverage Principle** · 2025 · ICLR 2026 · [arXiv 2505.20278](https://arxiv.org/abs/2505.20278)
  - Characterizing Pattern Matching and Its Limits on Compositional Task Structures
  - 单个实例的泛化成败可由覆盖它的上下文数预测；二跳所需数据至少随 token 集大小二次增长
- **Grokking in the Wild** · 2025 · ICML 2025 · [arXiv 2504.20752](https://arxiv.org/abs/2504.20752)
  - Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers
  - 用合成数据把推断 / 原子比提高到阈值以上，2WikiMultiHopQA 95–100%
- **Implicit Multi-hop** · 2025 · EMNLP 2025 · [arXiv 2505.17923](https://arxiv.org/abs/2505.17923)
  - Language models can learn implicit multi-hop reasoning, but only if they have lots of training data
  - 隐式 k 跳推理所需数据随 k 指数增长，课程只能缓解
- **Synthetic Compositional** · 2023 · ICML 2024 · [arXiv 2311.12997](https://arxiv.org/abs/2311.12997)
  - Compositional Capabilities of Autoregressive Transformers: A Study on Synthetic, Interpretable Tasks
  - 训练数据中组合顺序的偏差导致部分组合学不会
- **SCAN** · 2017 · ICML 2018 · [arXiv 1711.00350](https://arxiv.org/abs/1711.00350)
  - Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks
  - 指令到动作序列的组合泛化基准
- **COGS** · 2020 · EMNLP 2020 · [arXiv 2010.05465](https://arxiv.org/abs/2010.05465)
  - COGS: A Compositional Generalization Challenge Based on Semantic Interpretation
  - 分布内 96–99%，组合泛化集 16–35%

### 4.4 数据配比、重复与去重

- **DoReMi** · 2023 · NeurIPS 2023 · [arXiv 2305.10429](https://arxiv.org/abs/2305.10429)
  - DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining
  - Group DRO 求域权重，所有域困惑度都改善，达到基线所需步数少 2.6 倍
- **Data Mixing Laws** · 2024 · ICLR 2025 · [arXiv 2403.16952](https://arxiv.org/abs/2403.16952)
  - Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
  - 性能可表示为配比的函数；优化配比相当于默认配比多训 48% 步数
- **RegMix** · 2024 · ICLR 2025 · [arXiv 2407.01492](https://arxiv.org/abs/2407.01492) · [代码](https://github.com/sail-sg/regmix)
  - RegMix: Data Mixture as Regression for Language Model Pre-training
  - 小模型回归选配比；域间交互常常违反直觉
- **UniMax** · 2023 · ICLR 2023 · [arXiv 2304.09151](https://arxiv.org/abs/2304.09151)
  - UniMax: Fairer and more Effective Language Sampling for Large-Scale Multilingual Pretraining
  - 先均匀分配预算、再给每种语言设重复上限，优于温度采样
- **mT5** · 2020 · NAACL 2021 · [arXiv 2010.11934](https://arxiv.org/abs/2010.11934)
  - mT5: A massively multilingual pre-trained text-to-text transformer
  - 多语言温度采样 p(L) ∝ |L|^α，α=0.3
- **XLM-R** · 2019 · ACL 2020 · [arXiv 1911.02116](https://arxiv.org/abs/1911.02116)
  - Unsupervised Cross-lingual Representation Learning at Scale
  - 多语言采样 α=0.3
- **Repeated Data** · 2022 · 预印本 · [arXiv 2205.10487](https://arxiv.org/abs/2205.10487)
  - Scaling Laws and Interpretability of Learning from Repeated Data
  - 0.1% 的数据重复 100 次，800M 模型降到 400M 模型的水平
- **Data-Constrained** · 2023 · NeurIPS 2023 · [arXiv 2305.16264](https://arxiv.org/abs/2305.16264) · [代码](https://github.com/huggingface/datablations)
  - Scaling Data-Constrained Language Models
  - 重复 4 个 epoch 与唯一数据几乎相同，约 16 个 epoch 后价值急剧下降
- **Dedup** · 2021 · ACL 2022 · [arXiv 2107.06499](https://arxiv.org/abs/2107.06499) · [代码](https://github.com/google-research/deduplicate-text-datasets)
  - Deduplicating Training Data Makes Language Models Better
  - 去重后逐字输出记忆文本的频率降为十分之一
- **D4** · 2023 · NeurIPS 2023 Datasets & Benchmarks · [arXiv 2308.12284](https://arxiv.org/abs/2308.12284)
  - D4: Improving LLM Pretraining via Document De-Duplication and Diversification
  - 重复使用多样化挑选的数据优于基线，重复随机数据差于基线
- **Mixing Phase Transition** · 2025 · NeurIPS 2025 · [arXiv 2505.18091](https://arxiv.org/abs/2505.18091)
  - Data Mixing Can Induce Phase Transitions in Knowledge Acquisition
  - 知识数据的混合比低于临界值时几乎学不到，临界比与模型规模成幂律
- **Repeated Examples** · 2024 · NeurIPS 2024 Workshop · [arXiv 2410.07041](https://arxiv.org/abs/2410.07041)
  - Emergent properties with repeated examples
  - 固定训练步数时，小数据多次重复优于大数据单次；模乘法 92% vs 学不会
- **Long-CoT Repetition** · 2026 · COLM 2026 · [arXiv 2602.11149](https://arxiv.org/abs/2602.11149)
  - Data Repetition Beats Data Scaling in Long-CoT Supervised Fine-Tuning
  - 400 个样本训练 128 个 epoch，比 51,200 个样本训练 1 个 epoch 高 12–26 个百分点
- **Quantization Model** · 2023 · NeurIPS 2023 · [arXiv 2303.13506](https://arxiv.org/abs/2303.13506)
  - The Quantization Model of Neural Scaling
  - quanta 使用频率服从幂律、按频率依次学会时，推出损失的幂律 scaling

### 4.5 受控合成：频率形状与泛化

- **Power Law CR** · 2026 · ICML 2026† · [arXiv 2604.22951](https://arxiv.org/abs/2604.22951)
  - The Power of Power Law: Asymmetry Enables Compositional Reasoning
  - 测试集均匀采样时，幂律训练仍一致优于均匀训练；理论上均匀需 d^Ω(k) 样本，幂律 d^O(1)
- **Fact Learning Dynamics** · 2025 · COLM 2025 · [arXiv 2503.21676](https://arxiv.org/abs/2503.21676)
  - How do language models learn facts? Dynamics, curricula and hallucinations
  - 不均衡分布缩短平台期、拖慢知识获取；先子集后全体的调度增加最终知识量
- **Zipf Tokenizer** · 2025 · EMNLP 2025 · [arXiv 2507.22543](https://arxiv.org/abs/2507.22543) · [代码](https://github.com/yanjinhe/Tokenizer)
  - Pre-trained Models Perform the Best When Token Distributions Follow Zipf's Law
  - token 分布最贴近 Zipf 的词表大小下游性能最好

## 5. 具身与机器人策略

### 5.1 因素组合与采集策略

- **Robot-Data-Comp** · 2024 · RSS 2024 · [arXiv 2403.05110](https://arxiv.org/abs/2403.05110) · [项目](http://iliad.stanford.edu/robot-data-comp/)
  - Efficient Data Collection for Robotic Manipulation via Compositional Generalization
  - 策略能组合大多数因素对；Stair 采集策略在多因素时最好，真机新厨房 31/40
- **Factor World** · 2023 · 预印本 · [arXiv 2307.03659](https://arxiv.org/abs/2307.03659) · [项目](https://sites.google.com/view/generalization-gap)
  - Decomposing the Generalization Gap in Imitation Learning for Visual Robotic Manipulation
  - 新相机位置最难、新背景最易；连续因素的训练范围线性增大时 gap 约翻倍
- **F-ACIL** · 2026 · 预印本 · [arXiv 2603.25583](https://arxiv.org/abs/2603.25583) · [项目](https://f-acil.github.io)
  - Towards Generalizable Robotic Data Flywheel: High-Dimensional Factorization and Composition
  - 按因素比例迭代扩展的分布，比准均匀省 2–4 倍数据、比窄高斯省 5–10 倍
- **Data Scaling Laws** · 2024 · ICLR 2025 · [arXiv 2410.18647](https://arxiv.org/abs/2410.18647)
  - Data Scaling Laws in Imitation Learning for Robotic Manipulation
  - 泛化随环境数、物体数近似幂律增长；每对环境–物体约 50 条示教后饱和
- **GO-1-Pro** · 2025 · 预印本 · [arXiv 2507.06219](https://arxiv.org/abs/2507.06219) · [代码](https://github.com/OpenDriveLab/AgiBot-World)
  - Is Diversity All You Need for Scalable Robotic Manipulation?
  - 任务多样性比每任务示教数重要；专家间的速度多模态有害，去偏后平均分 +15%
- **Env Drivers** · 2019 · ICLR 2020† · [arXiv 1910.00571](https://arxiv.org/abs/1910.00571)
  - Environmental drivers of systematicity and generalization in a situated agent
  - 训练物体与词的数量、第一人称视角、视觉输入多样性决定具身智能体的系统性泛化
- **PVR-Robust** · 2023 · 预印本 · [arXiv 2312.12444](https://arxiv.org/abs/2312.12444)
  - What Makes Pre-Trained Visual Representations Successful for Robust Manipulation?
  - ViT 的涌现分割能力最能预测光照、纹理、干扰物偏移下的 OOD 表现
- **Shortcut-OXE** · 2025 · CoRL 2025 · [arXiv 2508.06426](https://arxiv.org/abs/2508.06426) · [项目](https://lucky-light-sun.github.io/proj/shortcut-learning-in-grps/)
  - Shortcut Learning in Generalist Robot Policies: The Role of Dataset Diversity and Fragmentation
  - 捷径来自子集内多样性低与子集间差异大；在两个视角下都采集的桥接物体消除视角捷径
- **MOVE** · 2025 · 预印本 · [arXiv 2512.04813](https://arxiv.org/abs/2512.04813) · [代码](https://github.com/lucywang720/MOVE)
  - MOVE: A Simple Motion-Based Data Collection Paradigm for Spatial Generalization in Robotic Manipulation
  - 采集时让物体运动，在同等数据量下扩大空间覆盖

### 5.2 动作数据的一致性与风格

- **IL Data Quality** · 2023 · NeurIPS 2023 · [arXiv 2306.02437](https://arxiv.org/abs/2306.02437)
  - Data Quality in Imitation Learning
  - 同一状态下动作越不一致（action divergence）策略越差；状态多样性不总是有益
- **robomimic** · 2021 · CoRL 2021 · [arXiv 2108.03298](https://arxiv.org/abs/2108.03298) · [项目](https://arise-initiative.github.io/robomimic-web/)
  - What Matters in Learning from Offline Human Demonstrations for Robot Manipulation
  - 多操作员混合数据不如同等数量的熟练操作员数据；经验少的操作员轨迹更长
- **DemInf** · 2025 · RSS 2025 · [arXiv 2502.08623](https://arxiv.org/abs/2502.08623) · [项目](https://jhejna.github.io/demonstration-info)
  - Robot Data Curation with Mutual Information Estimators
  - 按状态–动作互信息给示教打分并过滤，RoboMimic +5–10%
- **ISR** · 2026 · 预印本 · [arXiv 2606.22907](https://arxiv.org/abs/2606.22907) · [项目](https://d-robotics-ai-lab.github.io/isr.page)
  - Improving Robotic Imitation Learning via Trajectory Standardization
  - 按信息等距重采样轨迹，跨操作员成功率约 +25%
- **MoMo** · 2026 · 预印本 · [arXiv 2607.26315](https://arxiv.org/abs/2607.26315)
  - MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization
  - 运动模式作为连续条件，只示教过一种模式的任务也能执行新模式
- **CTR** · 2026 · 预印本 · [arXiv 2610.26507](https://arxiv.org/abs/2610.26507) · [代码](https://github.com/MINT-SJTU/CTR)
  - Learn the Task, Not the Schedule: Reducing Spurious Cross-Arm Coupling in Bimanual Imitation Learning
  - 在约束内重组双臂时序，打破任务无关的时序相关；最差状态成功率 56% → 76%
- **PIP** · 2025 · IROS 2025（arXiv comment） · [arXiv 2508.15669](https://arxiv.org/abs/2508.15669)
  - Exploiting Policy Idling for Dexterous Manipulation
  - 策略空转来自训练数据中精细段的小动作；在空转处施加扰动，真机插入 +15–35%
- **Perfect-Demo** · 2026 · 预印本 · [arXiv 2606.15587](https://arxiv.org/abs/2606.15587)
  - Perfect Demo Makes Poor Teacher: Learning Robust Alignment from Critical Motion Segments
  - 对齐段放慢的示教优于流畅示教（67.8% vs 52.2%），收益来自更宽的恢复状态覆盖

### 5.3 不均衡与重加权

- **APA** · 2026 · ICRA 2026 · [arXiv 2602.06512](https://arxiv.org/abs/2602.06512) · [项目](https://mldxy.github.io/Project-VLA-long-tail/)
  - Beyond the Majority: Long-tail Imitation Learning for Robotic Manipulation
  - 任务级长尾下重采样几乎无效（26.5% vs 25.1–27.1%）；从头部任务迁移接近段才有效
- **Balanced BC** · 2025 · 预印本 · [arXiv 2508.06319](https://arxiv.org/abs/2508.06319) · [项目](https://collab.me.vt.edu/data_curation/)
  - Towards Balanced Behavior Cloning from Imbalanced Datasets
  - 逐样本等权偏向多数行为；上采样到等比例基本修复，按可达精度定权更好
- **Zipfian Env** · 2022 · CoLLAs 2022† · [arXiv 2203.08222](https://arxiv.org/abs/2203.08222)
  - Zipfian environments for Reinforcement Learning
  - 按 Zipf 训练的 RL 智能体在稀有情形上表现差：均匀评测 0.69，稀有评测 0.24
- **FrameSkip** · 2026 · 预印本 · [arXiv 2605.13757](https://arxiv.org/abs/2605.13757) · [代码](https://github.com/ZGC-EmbodyAI/FrameSkip)
  - FrameSkip: Learning from Fewer but More Informative Frames in VLA Training
  - 低变化段主导按帧等权的训练；保留 20% 唯一帧，66.50% → 76.15%

### 5.4 组合泛化基准与方法

- **CompoSuite** · 2022 · CoLLAs 2022 · [arXiv 2207.04136](https://arxiv.org/abs/2207.04136) · [代码](https://github.com/Lifelong-ML/CompoSuite)
  - CompoSuite: A Compositional Reinforcement Learning Benchmark
  - 256 个组合任务；某个组成只出现在一个训练任务中时，零样本组合难得多
- **gSCAN** · 2020 · NeurIPS 2020 · [arXiv 2003.05161](https://arxiv.org/abs/2003.05161)
  - A Benchmark for Systematic Generalization in Grounded Language Understanding
  - 含留出颜色–形状组合的 8 个系统性划分，基线只通过 1 个
- **COLOSSEUM** · 2024 · RSS 2024 · [arXiv 2402.08191](https://arxiv.org/abs/2402.08191) · [项目](https://robot-colosseum.github.io/)
  - THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation
  - 单因素扰动下降 30–50%，叠加 ≥75%；干扰物数、目标颜色、光照最伤
- **Colosseum V2** · 2026 · RA-L（arXiv comment） · [arXiv 2605.27759](https://arxiv.org/abs/2605.27759)
  - Colosseum V2: Benchmarking Generalization for Vision-Language-Action Models
  - 初始位姿随机化是最主要的动作扰动，π0.5 双臂 −51.4%
- **CRAFT** · 2026 · 预印本 · [arXiv 2610.00524](https://arxiv.org/abs/2610.00524) · [项目](https://taegeunyang.github.io/craft/)
  - Same Scene, Different Task: Skill Alignment for Compositional Generalization in VLAs
  - 反事实技能对缓解视觉捷径，真机未示教组合 9/60 → 43/60
- **ACT-VLA** · 2026 · 预印本 · [arXiv 2607.00351](https://arxiv.org/abs/2607.00351)
  - Unleashing More Actions via Action Compositional Training for VLA Models
  - 合成组合示教，LIBERO Spatial-OOD 35.5% → 88.2%，只在仿真
- **MESA** · 2026 · CoRL 2026 · [arXiv 2611.05567](https://arxiv.org/abs/2611.05567) · [项目](https://pairlab.github.io/MESA)
  - MESA: An Evaluation Framework for Compositional, Semantic, and Spatial Generalization in Robotics
  - 组合评测 46.7%，域内 62.8%；MimicGen 生成的数据初始位置偏向易成功区域
- **LIBERO-PRO** · 2025 · 预印本 · [arXiv 2510.03827](https://arxiv.org/abs/2510.03827) · [代码](https://github.com/Zxy-MLlab/LIBERO-PRO)
  - LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization
  - 标准评测 90% 以上的策略在泛化评测上降到 0.0%
- **LIBERO-Plus** · 2025 · 预印本 · [arXiv 2510.13626](https://arxiv.org/abs/2510.13626)
  - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models
  - 相机与初始状态扰动下 95% → 30% 以下；成对扰动有一致的负组合性 gap

### 5.5 随机化分布的选择

- **ADR** · 2019 · 预印本 · [arXiv 1910.07113](https://arxiv.org/abs/1910.07113) · [项目](https://openai.com/blog/solving-rubiks-cube/)
  - Solving Rubik's Cube with a Robot Hand
  - 边界自动扩张的随机化分布比固定档位更快达到高 sim2sim 表现
- **Active DR** · 2019 · CoRL 2019 · [arXiv 1904.04762](https://arxiv.org/abs/1904.04762) · [代码](https://github.com/montrealrobotics/active-domainrand)
  - Active Domain Randomization
  - 把次优、高方差策略归因于环境参数的均匀采样，改为学习采样策略
- **BayesSim** · 2019 · RSS 2019 · [arXiv 1906.01728](https://arxiv.org/abs/1906.01728) · [代码](https://github.com/rafaelpossas/bayes_sim)
  - BayesSim: adaptive domain randomization via probabilistic inference for robotics simulators
  - 由真实轨迹推断的参数后验做随机化，优于均匀先验
- **DORAEMON** · 2023 · ICLR 2024 · [arXiv 2311.01885](https://arxiv.org/abs/2311.01885) · [项目](https://gabrieletiboni.github.io/doraemon/)
  - Domain Randomization via Entropy Maximization
  - 在成功率约束下逐步增大随机化熵，优于直接用全范围均匀
- **UED-Quadruped** · 2026 · 预印本 · [arXiv 2610.40364](https://arxiv.org/abs/2610.40364) · [代码](https://github.com/Solvro/ml-wojtek-ued)
  - Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds
  - 均匀关卡随机化进入 0/20 个最优组；成本相同的偏易或混合难度分布进入多个最优组

### 5.6 其他方向已收录、本方向引用的论文

- **Sim&Real Co-Train** · 2025 · 预印本 · [arXiv 2503.24361](https://arxiv.org/abs/2503.24361) · [项目](https://co-training.github.io)
  - Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation
  - 真实示教不覆盖工作区中部、仿真覆盖全区域时，中部位置成功率 Panda 11% → 28%，GR-1 43% → 100%
- **Sim&Real Pushing** · 2025 · IROS 2025 · [arXiv 2503.22634](https://arxiv.org/abs/2503.22634) · [项目](https://sim-and-real-cotraining.github.io)
  - Empirical Analysis of Sim-and-Real Cotraining of Diffusion Policies for Planar Pushing from Pixels
  - 存在物理差距时，策略需要能分辨样本来自哪个域
- **Mechanistic Co-Train** · 2026 · ICML 2026 · [arXiv 2604.13645](https://arxiv.org/abs/2604.13645) · [项目](https://science-of-co-training.github.io)
  - A Mechanistic Analysis of Sim-and-Real Co-Training in Generative Robot Policies
  - 共训练的主效应是"对齐 + 可分"的结构化表征对齐
- **TUCO** · 2026 · 预印本 · [arXiv 2610.05407](https://arxiv.org/abs/2610.05407)
  - TUCO: Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training
  - 全部仿真池与随机半数子集相同（25.8%），影响函数选出的子集 85.8%
- **MetaGenSim** · 2026 · CoRL 2026 · [arXiv 2610.19479](https://arxiv.org/abs/2610.19479) · [项目](https://meta-gensim.github.io)
  - Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training
  - 均匀生成的仿真数据 23/80，低于纯真实 26/80；学到的生成分布 58/80
- **Mulligan** · 2026 · 预印本 · [arXiv 2610.05882](https://arxiv.org/abs/2610.05882)
  - Mulligan: Performance-Guided Data Collection for Efficient On-Robot Learning
  - 把初始状态集中到失败处，成功率提升 10–34 个百分点
- **Temperature Sampling** · 2025 · 预印本 · [arXiv 2510.19373](https://arxiv.org/abs/2510.19373)
  - Using Temperature Sampling to Effectively Train Robot Learning Policies on Imbalanced Datasets
  - 温度采样处理不平衡数据集，单域测试
- **DemoGen** · 2025 · 预印本 · [arXiv 2502.16932](https://arxiv.org/abs/2502.16932) · [项目](https://demo-generation.github.io)
  - DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning
  - 视觉运动策略的空间泛化局限在示教配置附近
- **Sim2Real-VLA Study** · 2026 · 预印本 · [arXiv 2603.22876](https://arxiv.org/abs/2603.22876)
  - Grounding Sim-to-Real Generalization in Robotic Manipulation: An Empirical Study with Vision-Language-Action Models
  - 空间随机化比外观随机化更有效
- **DATAFARM** · 2026 · 预印本 · [arXiv 2609.12316](https://arxiv.org/abs/2609.12316) · [项目](https://prpl-group.com/datafarm)
  - DATAFARM: Distribution-Aligned Task and Motion Planning for Fine-Tuning Vision-Language-Action Models
  - 规划器数据的风格与 VLA 预训练分布对齐后才能学会
- **DREAM** · 2026 · 预印本 · [arXiv 2608.29078](https://arxiv.org/abs/2608.29078)
  - DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation
  - 生成轨迹中频繁的腕部旋转和冗余运动让 VLA 难以学习
- **DemoSpeedup** · 2025 · CoRL 2025† · [arXiv 2506.05064](https://arxiv.org/abs/2506.05064) · [项目](https://demospeedup.github.io)
  - DemoSpeedup: Accelerating Visuomotor Policies via Entropy-Guided Demonstration Acceleration
  - 只加速代理策略动作熵高的片段，精确片段少加速
- **ESPADA** · 2025 · 预印本 · [arXiv 2512.07371](https://arxiv.org/abs/2512.07371) · [项目](https://project-espada.github.io/espada)
  - ESPADA: Execution Speedup via Semantics Aware Demonstration Data Downsampling for Imitation Learning
  - 只加速非关键段
- **Speed prior** · 2026 · 预印本 · [arXiv 2610.32676](https://arxiv.org/abs/2610.32676) · [项目](https://mllab.snu.ac.kr/projects/learned_speed_prior)
  - Retiming Robot Demonstrations with a Learned Speed Prior
  - 用学到的速度先验把示教重定时到手持采集的节奏
- **TempoVLA** · 2026 · 预印本 · [arXiv 2606.06491](https://arxiv.org/abs/2606.06491)
  - TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
  - 变速轨迹增广 + 速度条件
- **SpeedAug** · 2025 · 预印本 · [arXiv 2512.00062](https://arxiv.org/abs/2512.00062)
  - SpeedAug: Policy Acceleration via Tempo-Enriched Policy and RL Fine-Tuning
  - 节奏增广先验 + RL 调节奏
