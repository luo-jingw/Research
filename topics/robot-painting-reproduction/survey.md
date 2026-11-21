# robot-painting-reproduction 综述

- 快照日期：2026-11-20
- 引用：论文用简称，元数据见 [papers.md](papers.md)；"P§x" 指 papers.md 的节号。
- 数字后括号里的位置（§、表、图、式）指原论文。

## 0. 这个方向讨论什么

核心问题：给定一幅目标图像，机器人用实体画具在纸或画布上把它临摹出来。要在仿真中做这类任务，需要回答四件事：

- 目标图怎样拆成画具能执行的笔画；
- 画具在介质上留下什么，仿真要保存哪些状态；
- 怎样衡量临摹得像不像；
- 有哪些目标图、示教和真实笔迹数据。

两个目标场景：

- **素描**：铅笔、炭笔，线条加明暗。明暗来自压力、重复和笔画密度。
- **油画**：不透明的彩色笔画分层覆盖。调色盘上的调色以"直接指定每笔颜色"代替；画布上的湿画混色、涂抹和堆厚仍属于介质问题。

"临摹"有两种含义，本综述都覆盖：

- **结果临摹**：终画与目标图像相似，绝大多数工作属于这一类；
- **过程临摹**：笔画顺序和作画过程也像人，例如 Intelli-Paint、Inverse Painting、Loomis Painter、Draw This First。

包含：

- 目标图到笔画的分解：启发式笔画渲染（SBR）、逐图优化、强化学习、前馈预测、作画过程模型；
- 机器人素描、线描、油画、丙烯、水彩的临摹系统；
- 铅笔、炭笔与油画颜料的仿真和渲染，刷毛模型，颜色合成，以及规划器使用的可微或学习的笔画渲染器；
- 临摹的评测指标与数据。

不包含：

- 控制器侧（VLA、world action model、LLM / VLM agent），见 [vla-drawing-writing](../vla-drawing-writing/survey.md)。两边重复的系统（FRIDA、Spline-FRIDA、IMPASTO、SketcherX、GeminiPainter）在这里只讨论笔画分解、颜色、画布模型和评测；
- 毛笔书法与水墨，只作为相邻工作引用（MoXi）；
- 没有目标图像的创作式作画，只在其笔画分解方法可复用时引用。

规模：四个子方向共核实约 150 条文献与数据集，[papers.md](papers.md) 收录 127 条。

检索范围内没有找到：

- 公开的"机器人指令笔画—实际笔迹"成对数据。FRIDA、Spline-FRIDA、IMPASTO 都采集了这类数据，但没有发布；RealBrush Ink 称计划公开；
- 带笔画矢量或笔刷轨迹的人类油画数据。油画只以作画视频出现，最大的 Loomis Painter 因许可不公开；
- 2010 年以后基于物理的石墨或炭笔沉积模型。近年的工作把铅笔当作样例或风格之一（RealBrush、NBE）；
- 机器人临摹素描或油画的公共基准。最接近的是 IMPASTO 的评测协议（单笔、叠加笔画、整幅画，加权 ℓ1 与 LPIPS）。

## 1. 分类框架

五个正交的轴：

- **轴 1：明暗与颜色的来源**
  - 只有线条：线稿前端加矢量化（AiSketcher、RoboCoDraw）
  - 线或点的密度：排线、点画、TSP 连续线（Lu-Lam-Yam Hatching、WVS、TSP Art、TSP-Bot）
  - 覆盖停留时间：遍历控制（Ergodic Rendering、drozBot）
  - 压力到灰度：铅笔受力（O'Dowd Pencil、Piktor-o-bot）
  - 不透明色块分层：油画、丙烯（Hertzmann98、FRIDA、IMPASTO）
  - 透明罩染或不透明抖动：e-David 2015
- **轴 2：分解方法**
  - 启发式 SBR：Litwinowicz97、Hertzmann98、Im2Oil
  - 逐图梯度优化：SNP、CLIPasso、SketchForge、Birth of a Painting、FRIDA
  - 强化学习：Learning to Paint、Intelli-Paint、CML
  - 前馈预测：Paint Transformer、AttentionPainter、Virtual Sketching、SwiftSketch
  - 作画过程模型：Inverse Painting、ProcessPainter、Loomis Painter
- **轴 3：笔画表示**
  - 折线或航点：AiSketcher、RoboCoDraw、Nasrat 80 s
  - Bézier 曲线加粗细、透明度、颜色：Learning to Paint、CLIPasso、QBS
  - 旋转纹理矩形 {x, y, h, w, θ, r, g, b}：Paint Transformer、Compositional Neural Painter、DQ-Transformer
  - 轨迹隐变量：Spline-FRIDA
  - 带力的参数：IMPASTO 的起点、长度、弯曲、方向、法向力
- **轴 4：画布与介质模型**
  - 二值或灰度印章、alpha 叠加：多数神经画家、FRIDA、Spline-FRIDA
  - 逐像素沉积累积加纸纹：Sousa-Buchanan、Rudolf Crayon
  - 颜料层加体积：IMPaSTo
  - 刷毛级三维：WetBrush
  - 从真机笔画学到的模型：FRIDA、Spline-FRIDA、IMPASTO
- **轴 5：执行回路**
  - 开环：CML、Bidgoli 2020、AiSketcher、RoboCoDraw
  - 分批执行、拍照、重规划：e-David 2013、FRIDA
  - 逐笔视觉闭环：Lu-Lam-Yam Hatching、Paul
  - 滚动时域 MPC：IMPASTO

## 2. 素描：目标图到线条与明暗（P§1）

### 2.1 线稿前端

问题：从照片中取出人会画的线。

- 经典做法是边缘或线条滤波：FDoG（CLD / FDoG，RoboCoDraw 用它提取轮廓）、XDoG（Im2Pencil 的轮廓，CLIPascene 和 SwiftSketch 用它做保真参照）。
- 学习的做法学"人会画的线"，而不是所有边缘：
  - Photo-Sketching 从 5,000 幅众包描摹的轮廓画学习；
  - APDrawingGAN、QMUPD 按面部区域学习肖像风格；
  - Informative Drawings 加深度与 CLIP 损失，让线条携带几何与语义。
- 这些前端都输出没有笔画顺序的栅格。机器人系统还要再做骨架化或矢量化（§3）。

### 2.2 明暗：像素合成与图元密度

- **像素合成**：Lu-Xu-Jia Pencil 和 Im2Pencil 都把画面分成线条层和色调层，分别合成。它们定义了铅笔临摹应该长什么样，但只输出像素，不给工具路径。
- **图元密度**：
  - WVS 用点的密度表现暗度，StippleDiffusion 是以图像为容量约束的学习版本；
  - TSP Art 用一条 TSP 回路连接点，单条连续线靠局部线密度表现明暗，适合不抬笔的机器人。Chitrakar、TSP-Bot、Berio ΣΛ 都采用了这条路线。

### 2.3 图像到矢量笔画

- 主流表示是经可微光栅器优化的 Bézier 曲线：
  - CLIPasso 用 CLIP 损失，笔画数决定抽象程度；
  - CLIPascene 把保真度与简洁度分成两个轴；
  - SketchForge 分开优化轮廓笔画和明暗纹理笔画；
  - DiffDraw 和 Berio ΣΛ 用其他可微光栅器。
- 前馈方法避免逐图优化：Virtual Sketching 用循环网络逐笔作画；SwiftSketch 在控制点上做扩散，不到 1 秒。
- 2026 年出现一笔画生成（SLDgen，均匀有理 B 样条）和带顺序的折线（Draw This First，预测二维顺序场）。
- 评测几乎都在数字画布上：
  - CLIP 识别率（CLIPasso、SwiftSketch）；
  - 对 XDoG 边缘图的 MS-SSIM（CLIPascene、SwiftSketch）；
  - DreamSim、DINO（SwiftSketch、SketchForge）；
  - Chamfer 距离与 Edge F1（Draw This First、SketchForge）；
  - 用户研究（CLIPasso、CLIPascene、SLDgen）。

### 2.4 笔画顺序

顺序影响两件事：

- **执行时间**：RoboCoDraw 把排序写成 GTSP，用随机键遗传算法求解，路径适应度比贪心好 17.34%，实画 43.2 秒（表 2）；抬笔次数是代价的一部分。Piktor-o-bot、GeminiPainter 用快速排序和图启发式。
- **可辨认的先后**：Pixelor 按可识别性学习顺序；SBR Planning 按全景分割和深度排序，让形状尽早出现；Sketch & Paint 用聚类；Draw This First 预测顺序场。

## 3. 机器人素描与线描临摹（P§2）

**通用流水线**：照片 → 风格化线稿（GAN、风格迁移、扩散或 VLM）→ 骨架或矢量提取 → 排序的折线 → 机械臂轨迹。例子有 AiSketcher、RoboCoDraw、Nasrat 80 s、SketcherX、GeminiPainter。

- 折线是机器人侧的通用格式：AiSketcher 骨架化后用 BFS 追踪；RoboCoDraw 输出线段列表；Nasrat 80 s 每条线最多 250 个航点。
- 视觉侧的 Bézier 输出要么被采样成航点（Embodied DIO 导出 G-code），要么由 TSP 路径平滑成曲率有界的 Bézier 样条（TSP-Bot）。
- 接触与线宽：
  - 接触靠柔顺笔架（RoboCoDraw）、阻抗控制（SSK）或画具自身的柔性（Nasrat 80 s、Piktor-o-bot 用的软头笔）；
  - 线宽靠笔高调节：Nasrat 80 s 约 0.1–2.25 mm；SSK 提出从笔压数据推笔高；Berio ΣΛ 用竖直轴控制笔刷宽度。

**明暗的四种机制**：

1. 由视觉或计算反馈放置的排线或线段密度：Lu-Lam-Yam Hatching、Paul、Adamik GA Pencil。Lu-Lam-Yam Hatching 用随目标亮度变大的核模糊当前画面，与目标相减，在差值最大处排下一组线，并按准则函数的最小值停笔。
2. 点画或 TSP 的密度：Chitrakar、TSP-Bot。
3. 遍历覆盖：停留时间正比于暗度（Ergodic Rendering、drozBot），自带定量的遍历度量。
4. 石墨受力：O'Dowd Pencil 用称重传感器控制笔压；Piktor-o-bot 在 2–16 N 之间只能稳定画出约 4 级灰，铅笔硬度、倾角和削尖都有影响，倾斜的 H 铅笔在大力下会断。

**代表数字**：RoboCoDraw 实画 43.2 秒；AiSketcher 约 2 分钟；Nasrat 80 s 约 80 秒。

**评测**：机器人论文很少报告实物画与目标图之间的图像指标，多报告作画时间、用户评分或配对辨认（RoboCoDraw、Nasrat 80 s、GeminiPainter）。例外是 Lu-Lam-Yam Hatching 的准则函数和遍历控制的遍历度量。

**硬件**：UR5 / UR5e（Chitrakar、RoboCoDraw、SBR Planning、TSP-Bot、Piktor-o-bot）、Franka（drozBot、Berio ΣΛ）、KUKA（SketcherX）、3 自由度 uArm（AiSketcher）。AiSketcher 自述低自由度机械臂画不出合成素描里的细节。

**局限**：

- 阴影边界产生多余笔画（AiSketcher）；
- 同一处反复下笔会划破纸，安全速度下要画几个小时（SBR Planning）；
- 排线需要明确的停止准则，否则过暗（Lu-Lam-Yam Hatching）。

## 4. 油画：目标图到笔画（P§3）

### 4.1 经典 SBR

- Paint by Numbers 把图像表示为有序的笔画集合，笔画的颜色、形状、大小和方向可控。
- Litwinowicz97 定下了沿用多年的模板：
  - 网格上播种短笔画，方向沿图像梯度，遇边缘截断；
  - 颜色取笔画中心的源图颜色（双线性插值），长度、颜色、方向加随机扰动；
  - 随机绘制顺序。
- Hertzmann98 加入单色曲线笔画和分层由粗到细：
  - 每种笔刷半径一层，从大到小；
  - 每层与按半径模糊的参考图比较，只在局部误差超过阈值 T 处起笔；
  - 笔画颜色取模糊参考图在起点的颜色。
- 这些方法的笔画颜色都直接读自（模糊的）源图，不涉及调色盘或调色。

### 4.2 神经网络与优化画家

- **笔画参数收敛到两族**：
  - 二次 Bézier 加两端粗细、透明度和 RGB，共 13 维（Learning to Paint 式 5）；
  - 旋转纹理矩形 {x, y, h, w, θ, r, g, b}（Paint Transformer、Compositional Neural Painter、DQ-Transformer）。SNP 的油画笔画允许头尾两种颜色（附录表 4）。
- **规划分三类**：
  - 强化学习：Learning to Paint、Intelli-Paint、Compositional Neural Painter 的组合器；
  - 经神经或解析可微渲染器的逐图梯度优化：SNP、SBP、Birth of a Painting、Dual-Param SBR、QBS；
  - 一次前向的集合预测：Paint Transformer、AttentionPainter。
- **由粗到细**：均匀网格或分块（SNP、Paint Transformer 的 4 级）、语义分层（SBP、Intelli-Paint）、预测区域（Compositional Neural Painter）。Compositional Neural Painter 指出均匀网格会造成块边界不一致（图 2）。
- **颜色**：每种方法都给每笔一个自由的连续 RGB。唯一与颜色相关的正则是 Intelli-Paint 对相邻笔画颜色变化的惩罚（式 14）。
- **非神经的对照**：Im2Oil 按梯度密度采样锚点、做 Voronoi 松弛，颜色取锚点像素，从大到小作画，一个参数控制精细度；115 人、50 幅图的平均意见分 8.26，高于 SNP 7.46、Learning to Paint 7.17、Paint Transformer 6.96（表 1）。
- **代表数字**：
  - 速度：Paint Transformer 512 像素 0.304 秒（表 2）；AttentionPainter 每张 0.08 秒，Compositional Neural Painter 5.21 秒，SNP 约 500 秒（AttentionPainter 表 3）；1024 像素、1,600 笔时 SBP 99.6 秒，SNP 447.1 秒（表 4）。
  - 保真：所有表格都显示保真度随笔画数上升（Compositional Neural Painter 表 1、AttentionPainter 表 2）；基准笔画数在 200–6,000 之间。
  - 像素指标与人的判断可能不一致：512 笔时 Birth of a Painting 的 PSNR 只比 Learning to Paint 高 0.09 dB（23.241 对 23.155），但用户研究偏好前者（表 2、表 4）。
- **局限**：
  - 只有直线、单色笔画，长窄区域缺少跨块上下文（Paint Transformer）；
  - 每块内作画与揉擦的顺序固定，开放 Bézier 表达不了扩散的边界（Birth of a Painting）；
  - 笔画极少时结果抽象、不忠实（DQ-Transformer）。

## 5. 机器人油画与彩绘系统（P§4）

### 5.1 执行回路与笔画模型

- **开环**：先在仿真中规划，再执行（CML、Bidgoli 2020、SBR Planning、Karimov 2021、Cable Mural Robot）。
- **相机闭环**：
  - e-David 2013 每轮仿真候选笔画、执行误差下降最大的约 300 笔、拍照，再循环；
  - FRIDA 执行一批后拍照，重新优化剩余计划（算法 1）；
  - IMPASTO 用学到的像素动力学模型做 5 步时域的滚动 MPC（算法 1）。
- **规划所用的笔画外观模型**：e-David 2013 用带逐色不透明度的 OpenGL 笔刷纹理；FRIDA 学习 param2stroke；Spline-FRIDA 的 Traj2Stroke 让粗细随笔高线性变化；IMPASTO 学 U-Net。
- **笔画必须是机器人能画出来的**：FRIDA 报告，Learning to Paint 不受约束的大而半透明的笔画在机器人上画出的结果与仿真"差别极大"。CML 因此把笔画约束为固定宽度（画布宽的 5%）、不透明、长度不超过画布宽的一半。

### 5.2 颜色处理

- **离散的预混颜料是主流**：
  - FRIDA 最多 12 种预混丙烯；CML 用 k-means 在目标图上选 10 色，由人调配；CoFRIDA 每幅 12 色或固定 4 色；SBR Planning 用 4 支彩笔；Bidgoli 2020 用 5 级灰；
  - e-David 的硬件颜料库有 24 色，但 2013 年的实验只用灰度墨；
  - IMPASTO 的调色盘有 24 格预混油彩，实验中按目标画只用其中一部分；每笔颜色在实测的颜料色块库中做最近邻匹配，学到的动力学模型把颜色当灰度处理。
- **离散化要放进优化循环**：FRIDA 在优化中反复做 k-means 离散，因为事后离散可能毁掉画面内容（附录 C）；Spline-FRIDA 只在 2,000 次迭代的最后 10% 离散（§V-F）。
- **与颜色有关的排序规则**：
  - 由浅到深，减少洗笔，避免深色湿颜料被涂开（FRIDA 附录 C）；
  - 一种颜色画完再清洗（Karimov 2021）；
  - 每种颜色一个轨迹文件，人工换色（Cable Mural Robot）；
  - 惩罚相邻笔画的颜色变化（Intelli-Paint）。
- **物理调色**只在 Karimov 系列中出现：注射泵把丙烯注入带叶轮的混合器，每调一种色就画完该色的所有笔画再清洗。
- **实物颜色与规划颜色的偏差**：SBR Planning 自述实物彩笔与 RGB 中算出的调色板颜色不一致。
- 数字画家里每笔自由 RGB、经典 SBR 从目标图取色，都和"直接指定每笔颜色"一致。

### 5.3 代表数字

- 灰度或墨：e-David 2013 每幅 40×60 cm 画 3–4 万笔，10–15 小时（§5.3）；Karimov 2021 一幅人像约 3.3 万笔。
- 彩色：SBR Planning 2,000 笔、4 色；Bidgoli 2020 250 笔、5 级灰。
- 油画临摹：IMPASTO 临摹画家的 17 笔和 18 笔作品，一幅复杂的画用了 204 步（§IV）。多步规划（Flower）中，IMPASTO-UNet 规划和执行的加权 ℓ1 为 0.0427 和 0.0464，LPIPS 0.1293；FRIDA-CNN 为 0.0597、0.0501 和 0.1619（表 II）。
- 数据量：FRIDA 的笔画模型在约 100 笔校准数据后收益很小（附录 B）；IMPASTO 用 900 笔自对弈数据，预测的 ℓ1 为 0.0285（图 4）；Spline-FRIDA 每种画具采数据约 1 小时、训练约 20 分钟。

### 5.4 局限

- 颜色只有离散选项，笔画彼此独立，不建模湿度和笔上颜料量（FRIDA 称颜料量是最重要的未建模变量），笔刷固定垂直于画布（FRIDA）；
- 规划昂贵：400 笔约 1 小时，显存只够每次优化 80 笔，依赖初始化（Spline-FRIDA）；
- 笔画参数化表达不了衬线式收笔和急转，执行有随机性（IMPASTO）；
- 颜料在画布上的混合比仿真复杂，相机模糊导致反复叠画（e-David 2013）；
- 白色初始画布让像素损失偏向深色（CML）；
- 高质量的颜色再现仍是瓶颈（Karimov 2019）。

## 6. 介质仿真与渲染（P§5）

### 6.1 铅笔、炭笔与其他干性介质

- **基于物理的模型都用纸面高度场，并在每个纸格累积沉积物**：
  - Sousa-Buchanan 每个位置保存石墨、黏土、蜡的量，色调为 Ir = 1 − Gt / TotalLead，TotalLead 约 1000 个单位（GI 1999 §2.3）；沉积取决于笔尖形状、压力和硬度，笔画会磨平纸纹；擦笔把石墨带到工具上再沉积到纸纹低处，橡皮只移除；
  - Rudolf Crayon 每个纸格保存一列蜡层（高度、颜色、透射、散射），由接触轮廓、力和摩擦计算沉积，可涂抹，在 2.4 GHz Pentium 4 上每笔 0.1–4 秒（§5）；
  - Van Haevre Pastel 做粉彩的双向转移、纸面凹陷和工具磨损。
- **验证**只是与扫描的真实色样并排目视比较（Sousa-Buchanan GI 1999 §5、Rudolf Crayon 图 14），没有定量误差。
- **便宜的替代**：Durand Thresholding 用阈值纹理实时生成铅笔、炭笔色调；Majumder-Gopi Charcoal 在噪声纹理上做对比度增强。两者不保存沉积状态，压力和涂抹只是渲染参数。
- 本轮没有找到 2010 年以后基于物理的石墨或炭笔沉积模型。

### 6.2 油画颜料

三种表示层级：

- **二维或 2.5 维网格，每格存颜料与体积**：
  - IMPaSTo 每格最多 8 种颜料浓度和颜料体积，一层湿层加若干干层，守恒平流，每步每格单向转移（沉积或拾取），干燥把湿颜料移入新的干层（§3–5）；
  - 用 8 个波长的 Kubelka–Munk 混色与合成，颜料取实测的真实油彩反射率；
  - 2004 年的 GPU 上，26×26 笔印每秒 116 次，88×88 每秒 68 次（§6）。
- **三维网格**：Baxter Viscous 用 Stokes 流，只能在 32×32×16 上达到 20 fps（§6）；WetBrush 用 4096×4096×64 的像素级密度网格，刷毛附近用粒子，GTX TITAN X 上 30–110 fps（§7）。
- **数据驱动外观**：RealBrush 用拍摄的真实笔画样例合成笔画和涂抹，每笔 0.5–1 秒。

其他要点：

- **涂抹时的细节模糊**：Chu Detail-Preserving 指出模糊主要来自反复的颜料交换和把颜料映射到三维笔刷上。从笔画开始前的画布快照拾取，并用与画布同分辨率的二维拾取图，就能消除，60×60 笔印 145 fps（§4–5）。
- **高度**：要么模拟（IMPaSTo 的每格体积、WetBrush 的密度），要么只为光照伪造（Cockshott Wet&Sticky 的凹凸贴图、Fast Paint Texture 的每笔高度图）。
- **分辨率**：IMPaSTo 称真实颜料的有效分辨率至少 250 DPI，约 0.1 mm / 像素（§1）。
- **验证**：只有 RealBrush 做了与真实笔画的感知对比（2AFC：单笔难以区分，涂抹可以区分）；只有 IMPaSTo 输入了实测颜料反射率。其余是艺术家反馈或合成测试（WetBrush、Chu Detail-Preserving）。

### 6.3 刷毛模型

- Strassmann 把笔刷看作沿位置加压力轨迹演化的一组刷毛。
- dAb 和 IMPaSTo 用弹簧质点骨架加细分曲面。
- Baxter-Lin Brush 用不到 10 根模拟主干插值出数百条刷毛，含各向异性摩擦、塑性和笔尖散开，30–60 Hz。
- WetBrush 模拟 40–600 根刷毛，与颜料双向耦合。
- 与真实笔画的比较只有 Baxter-Lin Brush 对装饰画练习笔画的目视复现，没有定量的笔印误差。机器人侧的模型（§6.6）都跳过刷毛模拟，直接从照片学笔印。

### 6.4 颜色合成

- Kubelka–Munk 由 Haase-Meyer 引入图形学，Curtis Watercolour 用于分层合成，IMPaSTo 在 8 波长空间中混合与合成。代价是每像素更多通道，以及输入要用颜料而不是 RGB。
- Mixbox 用 4 种颜料浓度加 RGB 残差的 7 维隐空间，在隐空间线性混合得到类似 Kubelka–Munk 的结果，中位开销是 RGB 混合的 2.3 倍；只支持不透明颜料的均匀混合，不支持罩染（§4.1、§5）。
- RealPigment 从一张拍摄的色卡拟合叠色行为（RBF 或拟合的 Kubelka–Munk 参数），报告 CIELAB 留一误差。
- 简单的 alpha 混合在涂抹的色相变化（RealBrush §8）和黄叠蓝（RealPigment 图 1）上失败；WetBrush 用保持亮度的 RYB 混合，并自称不符合物理。

### 6.5 学习的与可微的笔画渲染器

两族：

- **神经替代模型**：从程序或物理渲染器学笔画图像。Learning to Paint 学自 CG 渲染程序；Neural Painters 学自 MyPaint；SNP 学自矢量引擎；Wu Oil-GAN 学自离线油画模拟器，输出高度与颜色。
- **显式可微光栅器**：DiffVG、DiffDraw（soft-OR 合成）、Param. Brushstrokes（12 参数笔画）、Birth of a Painting（圆形笔印加揉擦）。Param. Brushstrokes 放弃神经渲染器，因为它显存太大，无法并行渲染大量笔画（§4.2）。

共同点：

- 几乎都用 alpha 叠加或软混合合成到 RGB 画布上，没有颜料高度，也没有湿画交互。例外是 Birth of a Painting 的笔刷状态加画布状态的循环揉擦算子（§3.2.2），以及 Wu Oil-GAN 输出的高度。
- SPIRAL++ 指出流体颜料模拟器有隐藏的速度场，画布图像不是完整状态（附录 G）。
- 这一族渲染器都没有与实体介质做过验证。

### 6.6 机器人回路中的画布模型

- 机器人论文用"从真机笔画照片校准的笔画模型"代替介质物理：
  - FRIDA 学 param2stroke，约 100 笔后收益很小；颜色以 RGBA 叠加；
  - Spline-FRIDA 用 7 个可学参数的解析渲染器：逐段距离图 → 高度图 → 粗细图（粗细与笔高成仿射关系）→ 深浅衰减，逐段取最大，灰度乘 RGB 后 alpha 叠加（§V-D、V-E）；
  - IMPASTO 学 U-Net 画布动力学，输入是当前画布和一张预渲染笔画，预渲染用半径 r(F) = r_min + kF^γ 的圆形笔印（式 12）。
- 这三篇报告了与照片的像素 L1（IMPASTO 另有 LPIPS），是整个介质子方向中仅有的定量仿真—真实验证：FRIDA 的 L1 明显低于 DiffVG（p < .01，图 7）；Spline-FRIDA 在分布外笔画上，Sharpie 的 L1 为 0.00055（CNN 为 0.00107），毛笔为 0.00158（CNN 为 0.00162）（表 II）。
- 它们自述的缺口：不建模湿度与笔上颜料量（FRIDA）；每种画具一个模型（Spline-FRIDA）；动力学里没有涂抹、高度和颜色（IMPASTO）。
- RL 素描与笔刷论文用的是非物理画布：MyPaint（Sim-to-Real Brush，见 vla-drawing-writing）和 42×42 的粗网格，0.5 cm / 像素（From Scratch to Sketch，见 vla-drawing-writing）。

### 6.7 验证方式汇总

- 与真实笔画照片的定量比较：FRIDA、Spline-FRIDA、IMPASTO；
- 感知 2AFC：RealBrush；
- 对真实色卡的 CIELAB 误差：RealPigment；
- 与真实色样并排目视：Sousa-Buchanan、Rudolf Crayon；
- 只输入实测反射率、没有笔画级比较：IMPaSTo；
- 只有艺术家反馈或合成测试：WetBrush、Chu Detail-Preserving。

## 7. 评测指标（P§6）

- **像素 L1 / L2、PSNR**：
  - 使用者：Learning to Paint、Intelli-Paint、FRIDA、Spline-FRIDA、IMPASTO（加权 ℓ1）、ProcessPainter、Birth of a Painting；
  - 弱点：作为训练奖励，判别器奖励优于 L2（Learning to Paint §3.3）；直接最小化像素距离会让中间画布难以看懂（Intelli-Paint）；作画过程是随机的，模糊的"平均"帧反而得到更低的 L1（Timecraft §5.3）。
- **SSIM、MS-SSIM**：
  - 使用者：Birth of a Painting、RealBrush Ink；
  - 弱点：在素描上与人类结构判断的 Spearman 相关只有 0.54 和 0.31，擦掉关键点区域后几乎不变（SketchRef 表 II、图 3）；在人脸素描上失效（Scoot）。
- **LPIPS**：
  - 使用者：Inverse Painting、ProcessPainter、Loomis Painter、IMPASTO、Birth of a Painting；
  - 弱点：在素描上相关只有 0.33（SketchRef 表 II）；在 DreamSim 的人类三元组上，它是学习型指标中一致性最低的；
  - IMPASTO 选它，是因为它对画布颜色和光照差异不敏感。
- **CLIP、DINO、DreamSim**：
  - 使用者：CoFRIDA、Loomis Painter、Painting Change Map、CLIPasso、SwiftSketch、SketchForge；
  - 弱点：FRIDA 直接优化 CLIPScore，所以在 CLIPScore 上比较对它有利（CoFRIDA）；DreamSim 在素描检索中会返回纯色背景（DreamSim 附录 B.1）。
- **线稿几何**：
  - Rough Sketch Bench 在受控错位上比较了几种指标：IoU 对局部错位极敏感，Hausdorff 被离群点主导，固定阈值 F-score 对轻微错位敏感；最后选 Chamfer 距离，但承认是"没有更好的选择"，感知研究规模很小；
  - Cole 2008 用 1 mm 容差的精确率和召回率；画家之间约 75% 的线条像素落在彼此 1 mm 内（§4.1），可作为人与人一致性的上限参照；
  - SketchRef 用关键点 OKS 评结构，与人类判断的相关为 0.66，但需要特定领域的关键点检测器。
- **分布级指标**（FID、FVD、ArtFID）：
  - 使用者：Inverse Painting、Loomis Painter、Compositional Neural Painter、APDrawingGAN、Birth of a Painting；
  - 弱点：评的是分布，不评单幅临摹；有限样本的 FID 有偏（ArtFID §3.2）。
- **过程指标**：
  - Inverse Painting 的 DDC（到目标的 LPIPS 曲线经 DTW 对齐）和 DTS；Loomis Painter 的 PDP（每帧到终画的距离曲线）；
  - 弱点：作画过程是随机的，与唯一的真值过程比较不良定义（Timecraft）。
- **人类研究**：多数论文都做 2AFC、Likert 或 MTurk 研究，样本 14–184 人不等。Rough Sketch Bench 的普通受试者预实验效果弱，认为需要专家或 2AFC。
- **笔画数与效率**：保真度对笔画数的曲线（Learning to Paint 图 8）、固定笔画数下的指标（Birth of a Painting 的 128 / 256 / 512 笔）、数据量曲线（FRIDA 图 15、IMPASTO 图 4）。

## 8. 数据（P§7）

### 8.1 作画过程

- 真实过程数据都来自网上的延时或教程视频，去掉手和工具后提供 RGB 帧，没有笔画参数或笔刷轨迹：
  - Timecraft 233 段（数字与水彩）；
  - Inverse Painting 294 段丙烯风景；
  - Loomis Painter 表 1 中 737 段，含油画 151、铅笔 298，因许可不公开，只发布重建数据的代码；
  - Painting Change Map 161 段丙烯（Loomis 子集）。
- 合成序列：ProcessPainter 3 万条（由 Learning to Paint、SNP、Paint Transformer 等渲染器生成）；Collaborative Neural Painting 10.1 万条（SNP 分解，每条最多 400 笔、8 个参数）。
- PPJudge 记录了约 1.5 万段美术专业学生的真实作画过程，部分是临摹参考画，但没有说明是否发布。

### 8.2 人类示教与真实笔画

- 动作捕捉：Bidgoli 2020 记录 730 多笔，6 自由度、120 fps，与 32×64 的扫描笔迹配对；Spline-FRIDA 用 OptiTrack，每幅 20–200 条轨迹，重采样为 32 点的 x、y、高度，没有压力，并称动作捕捉难以准确测笔高。
- 压力：OpenSketch 是唯一核实的同时记录笔压和时间的素描数据（数位板）。
- 指令—笔迹配对：RealBrush Ink 有 1,818 条机器人墨笔画，路径人工标注并与参考矢量对应，称计划公开；FRIDA、Spline-FRIDA、IMPASTO 的采集数据没有发布。
- IMPASTO 的测试集是 5 位油画家画的 60 笔单笔，只用于评测。

### 8.3 素描与线稿数据集

- 带笔画顺序：
  - QuickDraw：345 类、5,000 万幅，CC BY 4.0，没有目标图像；
  - FS-COCO：凭记忆画 MS-COCO 照片，CC BY-NC 4.0；
  - Photo-Sketching：在照片上描摹，带时间戳的 SVG，CC BY-NC-SA；它是唯一线条与目标图大致对齐的数据集，最接近素描临摹示教；
  - OpenSketch：笔压加时间，项目页没有许可声明；
  - SEVA：限时素描，仓库为 MIT 许可。
- 不带顺序：APDrawingGAN 有 140 对照片与画家线稿；Cole 2008 有 208 幅配准的铅笔线稿；SketchyScene 带分割掩码。
- Sketchy 的规模和时间格式未能核实（ISSUE-008）。

## 9. 横向趋势

- **分解从启发式走向可微优化，再走向前馈预测**：Hertzmann98 → SNP、CLIPasso → Paint Transformer、AttentionPainter、SwiftSketch。单幅用时从 SNP 的约 500 秒降到 AttentionPainter 的 0.08 秒（AttentionPainter 表 3）。
- **机器人侧用学到的笔画模型代替介质物理**：FRIDA（param2stroke）→ Spline-FRIDA（7 参数解析模型）→ IMPASTO（画布动力学）。三者都只要几百到上千笔的真机数据。
- **闭环越来越紧**：e-David 2013 的每轮约 300 笔 → FRIDA 的分批重规划 → IMPASTO 的 5 步 MPC。
- **颜色离散化进入优化循环**：FRIDA、Spline-FRIDA 在优化中离散，IMPASTO 逐笔在颜料库中最近邻匹配。
- **从终图到过程**：Intelli-Paint 的分层与颜色惩罚、Draw This First 的顺序场、Inverse Painting 与 Loomis Painter 的过程重建、PPJudge 的过程评分。
- **力或高度决定笔印**：Spline-FRIDA（粗细与笔高成仿射关系）、IMPASTO（r(F) = r_min + kF^γ）、Piktor-o-bot（力到灰度）、Nasrat 80 s（笔高到线宽）。
- **感知指标取代像素指标，但线稿上仍弱**：油画和过程评测转向 LPIPS、DINO、CLIP；素描上 SketchRef 和 Rough Sketch Bench 显示这些指标与结构判断相关不高。

## 10. 文献自述的开放问题

- 笔上颜料量是最重要的未建模变量；笔画彼此独立，颜色离散，笔刷固定垂直于画布（FRIDA）
- 只建模笔画内的风格，不建模笔画之间的风格；动作捕捉测不准笔高；每种画具要单独训练（Spline-FRIDA）
- 笔画参数化表达不了衬线式收笔和急转；颜色在训练中按灰度处理；采样式规划在动作维度增加时需要更多样本（IMPASTO）
- 只用仿真测量仿真—真实差距，因为采足够的真实样本不可行（CoFRIDA）
- 离散成少数颜色可能让内容无法辨认；频繁换色耗时并涂开深色湿颜料（FRIDA 附录 C）
- 高质量颜色再现是绘画机器人的主要瓶颈（Karimov 2019）
- 仿真分辨率受计算限制，而真实颜料至少约 250 DPI；如何把 RGB 图像转成颜料表示；Kubelka–Munk 只是理想化（IMPaSTo）
- 厚涂、稀释油彩的半透明、用减色或颜料模型代替加色 RGB（Chu Detail-Preserving）
- 颜料混合过于简单，低粒子密度时颜色发脏（WetBrush）
- 只有 4 种原色，只支持不透明的均匀混合，罩染留待以后（Mixbox）
- 神经渲染器常假设画布图像就是完整的模拟状态，对有隐藏速度场的流体颜料不成立（SPIRAL++）
- 机械臂限制细节，建议在机器人约束下联合优化路径规划与素描生成，并加视觉反馈（AiSketcher）
- 铅笔受力只能稳定得到约 4 级灰，铅笔会断，削尖很关键（Piktor-o-bot）
- 同一处反复下笔划破纸，按粗细和颜色选画具仍未解决（SBR Planning）
- 排线需要明确的停止准则（Lu-Lam-Yam Hatching）
- 背景复杂时高抽象度下表现下降（CLIPasso）
- 训练数据只覆盖风景，重建的过程只是合理而非准确（Inverse Painting）
- 手的阴影检测不到，数据偏向铅笔，过程还应反映选色、调色和工具（Loomis Painter）
- 与唯一的真值过程比较不良定义（Timecraft）
- 多份真值线稿之间的对应仍是开放问题，感知研究可能需要专家或 2AFC（Rough Sketch Bench）

## 11. 现有综述的分类对照

- Hertzmann SBR Survey 把笔画渲染分为贪心放置与优化放置。本综述轴 2 中的启发式 SBR 对应贪心，逐图优化对应优化；强化学习、前馈预测和过程模型是 2019 年以后新增的类别。
- SBR Survey 2022（从启发式到深度学习）和 Gülzow 2020（绘画机器人回顾）只核实了元数据或摘要，没有逐项对照。

## 12. 入门阅读顺序

1. Hertzmann98：分层、按误差起笔、单色笔画取自目标图，可以直接映射到印章式画布。
2. Learning to Paint：13 维笔画、神经渲染器和后续论文共同的基线。
3. SNP：经可微渲染器优化、油画笔画参数化和分块渐进细化。
4. CLIPasso：图像到 Bézier 素描的模板，笔画数控制抽象程度。
5. Lu-Lam-Yam Hatching：带停止准则的闭环排线，可直接搬到仿真纸面。
6. RoboCoDraw：完整的机器人线描临摹流水线，有路径排序和时间数字。
7. Sousa-Buchanan GI 与 Sousa-Buchanan CGF：压力 → 石墨沉积 → 色调的参照模型，含擦笔与橡皮。
8. IMPaSTo：最清楚的每格油画画布状态与笔刷—画布转移规则。
9. Chu Detail-Preserving：涂抹为何变糊以及两个便宜的修正。
10. FRIDA：真机采笔画、在优化中离散颜色、由浅到深、拍照重规划。
11. Spline-FRIDA：粗细随笔高变化的少参数可微笔画模型，结构上最接近按压深度决定笔印的模型。
12. IMPASTO：机器人油画临摹的现有最好结果、评测协议和自述缺口。
13. Rough Sketch Bench 与 SketchRef：线稿和素描指标各自为何失效。
14. Photo-Sketching 与 Loomis Painter：最接近素描临摹示教的公开数据，以及油画、铅笔作画过程数据的规模与许可限制。
