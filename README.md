

# CROSSTALK-DATASETS

🤗 我们提供了一个中文相声和小品相关的数据集，并使用Seq2Seq，GPT，UniLM，GPT3分别测试了其在相声生成上的效果，通过Belu和distinct衡量了每种模型生成的效果，并且抽选了15位被试进行模型生成段落效果的排序（真实样本，RNN，GPT，UniLM，GPT3），此处提供我们base方案的各种评估指标，以及我们使用的训练集与测试集，还有部分的原始数据（如需全部，请联系我们）。（持续更新中）



------



### 1.1. 数据集概况

| 篇章统计                                     | 数值 |
| -------------------------------------------- | ---- |
| 单口相声数量                                 | 168  |
| 对口相声数量                                 | 3685 |
| 群口相声数量                                 | 256  |
| 小品数量                                     | 5222 |
| 纯对话文本数量(包括对口，群口，纯对话的小品) | 4859 |
| 全文本数量                                   | 9331 |



| 数值统计              | 数值     |
| --------------------- | -------- |
| 数据集全字数          | 16481376 |
| 数据集全句数          | 663305   |
| 长句数（长度大于128） | 8717     |
| 短句数（长度小于24）  | 446756   |
| 句长中位数            | 16       |
| 篇章平均句子数        | 71       |





------



### 1.2. 示例数据集

| 路径                | 描述                 |
| ------------------- | -------------------- |
| demo_data/GPT_Train | base方案训练时的语料 |
| demo_data/ORI_Data  | 抽样出的原始语料格式 |

**meta格式说明：**

```
{
		"isAllDialog":true,                                       #是否为纯对话格式
		"charSize":526,                                           #本篇字数
		"filePath":"u399dy/蔡少芬李菁相声《学说普通话》台词完整版",     #相对路径
		"roles":[                                                 #角色
			"李菁:",
			"蔡少芬:"
		],
		"sentenceSize":25,                                        #句子数
		"source":"https://www.399dy.com/xiangsheng/11176.html",   #来源网站
		"idx":28,                                                 #索引
		"title":"蔡少芬李菁相声《学说普通话》台词完整版",               #篇章标题
		"type":"对口相声"                                          #类型
	},
```

**文本内格式实例：**

```
甲:现在的商业都讲究实事求是，公约上写着:“百问不烦，百拿不厌。”
乙:那是呀!
甲:旧社会做买卖就不一样，宣传得蛮好，实际净骗人，门口都写两块大牌子。
乙:写的什么?
甲:写着“货真价实，公平交易”。
乙:写得蛮好看!
甲:实际是货不真，价不实，大秤买，小秤卖，想尽一切办法多赚钱。大买卖讲究宣传，门口弄一份儿洋鼓洋号吹吹打打。还有的在电台登广告。广告都这样。
乙:您给学学。
甲:“各位先生，各位女士，早晨起来您不喝茶吗?您要想喝好茶叶的话，报告您一个好消息，××茶庄备有专人到南省产茶名区，采办各种红绿花茶，加花熏制，西湖龙井，铁叶儿大方，清香适口，气味芬芳，馈送亲友最为相宜。他家的地址:××大街往北路西一百七十三号，电话三局六二九四号。”
乙:是这样儿!
甲:这是那时候的大买卖。小买卖儿可报不起，做一天买卖连本带利将够一家子吃饭的，花不起广告费呀。像卖烤地瓜的也这么登广告就不行了。
乙:是吗?
甲:那稿子念起来也不受听啊!不信我给您念念。
乙:好。
```



------



### 1.3. base方案评估指标

|       | BLEU2(字) | BLEU4(字) | dist_1 | dist_2 |
| ----- | --------- | --------- | ------ | ------ |
| Seq2Seq   | 0.12 | 0.01 | 90.46 | 78.15 |
| GPT   | 6.01      | 2.19      |    91.27    | 83.98 |
| GPT3  | 7.42 | 2.48 | 82.94 | 75.96 |
| UniLM | 6.64 | 2.65 | 90.37 | 74.13 |

*TIP:所有的生成任务都没有加重复惩罚。*



**人工检验方式：**

截取50篇相声的前10句作为输入，有历史记忆的生成后10句，一共20句作为一个评估对象。

将每个篇章的Seq2Seq,GPT,GPT3,UniLM生成的句子拼接在输入句后面，合上原始篇章的20句，一共5个评估对象作为一个评估单元。

挑选了不同职业，不同地域，不同年龄，不同性别的14名被试，告诉他们需要对每个评估对象进行评价（0-不好，1-好），然后对每个评估单元中的5个评估对象由好到不好的顺序进行排序。被试被告知每个评估对象都是由不同的模型生成的。

最终我们得到每个模型的平均认可度 **(得到好的个数/总个数)** 分别为：

| 原始篇章 | UniLM | GPT3  | GPT   | Seq2Seq   |
| -------- | ----- | ----- | ----- | ----- |
| 89.14    | 46.14 | 45.14 | 30.57 | 16.14 |

每个模型的平均排序得分分别为：

| 原始篇章 | UniLM  | GPT3   | GPT    | Seq2Seq   |
| -------- | ------ | ------ | ------ | ----- |
| 222.07   | 151.71 | 147.64 | 126.07 | 102.5 |


fleiss_kappa : 0.3657753225075188

------



### 1.4.base方案



GPT使用的预训练模型：

https://huggingface.co/thu-coai/CDial-GPT_LCCC-base

GPT使用的训练代码：

https://github.com/yangjianxin1/GPT2-chitchat

GPT3地址（需自行申请）：

https://beta.openai.com/

UniLM的地址：

https://github.com/YunwenTechnology/Unilm

Seq2Seq的地址：

https://github.com/IBM/pytorch-seq2seq



------

### 1.5.生成例子

**交互式生成**

```
demo 1:

user:大家好
chatbot:大家好
user:今天我们两个和大家说段相声
chatbot:对，这是全国有名的主持人曹云金
user:不敢不敢
chatbot:首先我们两个人说的头一回合作
user:是，第一回
chatbot:我们两个人说相声，有名
user:全国老少爷们都知道
chatbot:我一个人说相声，有名啊
user:感情您这是要夸自己呀
chatbot:谢我干吗呀
user:谢您夸自个儿的时候带上我了
chatbot:对您有好处啊


demo 2:

user:谢谢大家热烈的掌声
chatbot:谢大伙儿
user:我们哥俩儿今天来给大家说段相声
chatbot:对，这个相声主要讲究的是说、学。
user:还有逗唱
chatbot:相声主要讲究说、学表演
user:你还和我杠上了是么
chatbot:怎么就我不是一个人
user:那你是什么呀
chatbot:我不是一个人

demo 3:

user:大家好呀，掌声很热烈
chatbot:是
user:我们哥俩今天来给大伙说短相声
chatbot:别说了
user:啊，为什么呀
chatbot:这个相声是我最重要的朋友?怕您各位不认识，有可能还在暗地里面呢
user:什么跟什么呀这是
chatbot:怕您各位不认识我们
user:那我们先来做一下自我介绍
chatbot:做个说明
user:我是anon
chatbot:我叫韩雪松，谢大家听个话

```

**剧本式生成**

```
demo 1
我们首先看一下，其他剧场相声的报价。
那我们来听一听。
国家大剧院一千五百块，农业展览馆二千块，北京动物园五千块。
跟猴儿一块说相声啊?
那么我们今天的相声卖多少钱呢?
卖多少钱哪?
八毛钱，比其他剧场足足便宜了三百块呀!
这都什么账头啊这是?
赶快拨打我们的销售热线，二百五加三八加十三点加二。
全是傻数啊。
========================以下为生成内容===========================
你拨了?
拨了啊。
你说什么?
我说，我是一个人，一个人来。
这么小的数目，我们还是先报给你吧。
好啊。
一共十五块钱，您有现金吗?
有呀!您给我十五块钱。
不用给十五块钱了，跟我来吧!


demo 2
谢谢大伙儿，谢谢大伙儿。
感谢您各位。
这次啊回到北京说相声，我这心里是特别的高兴。
诚惶诚恐。
尤其见着下面几位还是我们的老街坊。
老街坊。
看见您那我就想起我小时候住的那骆驼湾胡同来。
骆驼湾那儿。
可不是嘛，过去有个北京的小曲。
叫什么呀?
========================以下为生成内容===========================
叫做《满江红》。
《满江红》。
这首歌是我们老街坊常唱的。
小时候我们还在上海呢，我们小时候也常听到这首歌。
小时候听到这首歌，我们都会跟着一起唱。
那个时候，你说的是北京人，你说的是北京人，北京人都会一起唱的。
对对对对对对！
不要只有北京人会一起唱，全国各地的人都会一起唱。
全国各地的人都会一起唱。

demo 3
人人都有爱好。
是
有爱好听歌的，有爱好看书的，有爱好玩游戏的，你的爱好就很好，很高雅。
什么啊
他爱踢毽子
对
踢毽子好啊
是么
促进血液循环，血液循环有规律对身体很好
有这么大用处?
========================以下为生成内容===========================
对啊
那是
但是也有高雅之风
哦?
有时候踢得动人
是吗
尤其是在春晚上
踢得动人
是
我跟朋友们说
```

------



### 1.6 同context不同模型生成示例


**demo 1**

```


======================================
原始篇章：

谢谢大家。
唉。
刚才是郭老师带着他的爱徒，岳云鹏。
嗯。
两个人合说一段歪唱太平歌词。
嗯。
2700多位观众啊，乐的都累了。
是。
把我们换上来，让您休息休息。
对。
-----------------------------------本线之前是context,之后为基于context的剧本生成
岳云鹏，有人缘。
嗯。
长的也漂亮嘛。
好啊!
浓眉小眼，大屁股圆脸。
您还什么都见过。
这是他的一个艺术特点。
这是艺术特点。
郭德纲，大家更熟悉了。
嗯。
======================================
UNILM:

甲:谢谢大家。
乙:唉。
甲:刚才是郭老师带着他的爱徒，岳云鹏。
乙:嗯。
甲:两个人合说一段歪唱太平歌词。
乙:嗯。
甲:2700多位观众啊，乐的都累了。
乙:是。
甲:把我们换上来，让您休息休息。
乙:对。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我们两个人合作这么长时间。
乙:嗯。
甲:刚才主持人叫郭麒麟。
乙:哦。
甲:他也给大家表演一段传统相声。
乙:对。
甲:后边那位老师。
乙:嗯。
甲:就是孙越老师。
乙:对。

======================================
GPT

甲:谢谢大家。
乙:唉。
甲:刚才是郭老师带着他的爱徒，岳云鹏。
乙:嗯。
甲:两个人合说一段歪唱太平歌词。
乙:嗯。
甲:2700多位观众啊，乐的都累了。
乙:是。
甲:把我们换上来，让您休息休息。
乙:对。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我们这一场换将上来。
乙:我跟您说这正经的咱们。
甲:是。
乙:由于压力比较大。
甲:哦。
乙:正经的多了。
甲:嗯。
乙:四门功课，绕口令您怎么样?
甲:我会数数来宝，其实学这东西好啊。
乙:学习数来宝。

======================================
GPT3

甲:谢谢大家。
乙:唉。
甲:刚才是郭老师带着他的爱徒，岳云鹏。
乙:嗯。
甲:两个人合说一段歪唱太平歌词。
乙:嗯。
甲:2700多位观众啊，乐的都累了。
乙:是。
甲:把我们换上来，让您休息休息。
乙:对。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:现在我们请来了一位新人，让大家给他欢呼。
乙:嗯。
甲:这个新人是谁呢？
乙:嗯。
甲:这个新人是谁呢？
乙:嗯。
甲:刚才我们在这里说了一句话，不知道大家听懂了没有？
乙:对。你说的是什么呢？
甲:我们在这里说了一句话——“好的”，不知道大家听懂了没有？
乙:嗯。我听懂了。

======================================
Seq2Seq

甲:谢谢大家。
乙:唉。
甲:刚才是郭老师带着他的爱徒，岳云鹏。
乙:嗯。
甲:两个人合说一段歪唱太平歌词。
乙:嗯。
甲:2700多位观众啊，乐的都累了。
乙:是。
甲:把我们换上来，让您休息休息。
乙:对。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我们俩是两个人。
乙:嗯。
甲:咱们俩演员一块栾云平方休息，先生在艺术家里边站着。
乙:对。
甲:相声界的艺术家。
乙:哎。
甲:京剧水平高峰。
乙:是。
甲:今天我们哥俩表演艺术家。
乙:是。

======================================



```

**demo 2**

```




======================================
原始篇章：

甲:相声演员李伟建。
乙:刘洪沂。
甲:今天呢我们给您说段相声。
乙:刘老师。
甲:啊。
乙:先问问您。
甲:啊。
乙:中国这么多传统的节日，您最爱过哪个节啊?
甲:爱过哪个节?
乙:啊。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我最爱过的是那个……
乙:您这么羞涩干嘛呀。
甲:那我最爱过的是春节。
乙:春节。
甲:啊。
乙:为什么呀?
甲:你想啊，新年伊始，万象更新，中国的传统节日大伙都这么过嘛。
乙:您今年多大岁数?
甲:我今年六十五岁。
乙:难怪。
======================================
UNILM:

甲:相声演员李伟建。
乙:刘洪沂。
甲:今天呢我们给您说段相声。
乙:刘老师。
甲:啊。
乙:先问问您。
甲:啊。
乙:中国这么多传统的节日，您最爱过哪个节啊?
甲:爱过哪个节?
乙:啊。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:寒食节。
乙:对呀。
甲:中国有句话叫"吃粽子怕死"。
乙:哦。
甲:而且呢也要过。
乙:是啊。
甲:尤其是端午节。
乙:诶。
甲:吃粽子。
乙:吃粽子怕死?

======================================
GPT

甲:相声演员李伟建。
乙:刘洪沂。
甲:今天呢我们给您说段相声。
乙:刘老师。
甲:啊。
乙:先问问您。
甲:啊。
乙:中国这么多传统的节日，您最爱过哪个节啊?
甲:爱过哪个节?
乙:啊。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:爱过传统节日。
乙:这回你打算表演什么节目?
甲:我找一下好节目啊，让您开眼。
乙:等会儿。
甲:民主席是谁啊?
乙:哈利波特。
甲:好啊。
乙:他在美国还给安排了。
甲:怎么没有选项啊?
乙:你们也去呗!

======================================
GPT3

甲:相声演员李伟建。
乙:刘洪沂。
甲:今天呢我们给您说段相声。
乙:刘老师。
甲:啊。
乙:先问问您。
甲:啊。
乙:中国这么多传统的节日，您最爱过哪个节啊?
甲:爱过哪个节?
乙:啊。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:嗯。
乙:啊。
甲:爱过哪个节?
乙:啊。
甲:我觉得，爱过的节日，是农历新年。
乙:哦。
甲:因为我们中国人，最重要的一个节日，就是农历新年。
乙:那么您呢，您最爱过的一个人呢?
甲:我最爱过的一个人?
乙:啊。
======================================
Seq2Seq

甲:相声演员李伟建。
乙:刘洪沂。
甲:今天呢我们给您说段相声。
乙:刘老师。
甲:啊。
乙:先问问您。
甲:啊。
乙:中国这么多传统的节日，您最爱过哪个节啊?
甲:爱过哪个节?
乙:啊。
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:喜欢听节日。
乙:对。
甲:喜欢相声。
乙:喜欢。
甲:喜欢健美。
乙:喜欢。
甲:喜欢看。
乙:喜欢看。
甲:喜欢看。
乙:喜欢看。

======================================


```

**demo 3**

```

======================================
原始篇章：

甲:今天呢我给大家表演相声。
乙:像您这个相声演员都讲究什么。
甲:讲究说学逗唱。
乙:说学逗唱。
甲:对。
乙:唱你能唱什么。
甲:唱我们各地方的地方戏，评戏，梆子，京剧，尤其我们相声演员对京剧非常有研究。
乙:这么说您对京戏非常有研究。
甲:那是啊。
乙:那您会整出戏吗?
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:经常跟这个京剧演员在一块唱。
乙:是吗?
甲:那是。
乙:那行，今儿个我帮帮您。
甲:帮，甭帮，经不住帮。
乙:我打算帮您唱一出。
甲:您帮我唱一出戏。
乙:啊。
甲:没问题。
乙:那咱俩唱一出。
======================================
UNILM:

甲:今天呢我给大家表演相声。
乙:像您这个相声演员都讲究什么。
甲:讲究说学逗唱。
乙:说学逗唱。
甲:对。
乙:唱你能唱什么。
甲:唱我们各地方的地方戏，评戏，梆子，京剧，尤其我们相声演员对京剧非常有研究。
乙:这么说您对京戏非常有研究。
甲:那是啊。
乙:那您会整出戏吗?
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我会。
乙:整出戏你唱什么呀?
甲:整出戏叫<<西河调>。
乙:哎哟喂。
甲:怎么着?
乙:打算学谁呢?
甲:我呀。
乙:打算学谁呀?
甲:我呀。
乙:打算学谁呀?

======================================
GPT

甲:今天呢我给大家表演相声。
乙:像您这个相声演员都讲究什么。
甲:讲究说学逗唱。
乙:说学逗唱。
甲:对。
乙:唱你能唱什么。
甲:唱我们各地方的地方戏，评戏，梆子，京剧，尤其我们相声演员对京剧非常有研究。
乙:这么说您对京戏非常有研究。
甲:那是啊。
乙:那您会整出戏吗?
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:不会我干嘛你说废话，我还没学会。
乙:是啊。
甲:要不咱来点个别的。
乙:看出什么呀。
甲:来也没有唱过，我唱过什么京剧。
乙:那可不一定。
甲:您能找一个能人吗?
乙:哪儿的事情啊。
甲:您跟我唱就行了，来这苏三。
乙:苏三?
======================================
GPT3

甲:今天呢我给大家表演相声。
乙:像您这个相声演员都讲究什么。
甲:讲究说学逗唱。
乙:说学逗唱。
甲:对。
乙:唱你能唱什么。
甲:唱我们各地方的地方戏，评戏，梆子，京剧，尤其我们相声演员对京剧非常有研究。
乙:这么说您对京戏非常有研究。
甲:那是啊。
乙:那您会整出戏吗?
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:我整出戏。
乙:那您整出什么戏?
甲:啊，我整出《绣花大盗》。
乙:《绣花大盗》。
甲:对，《绣花大盗》。
乙:那您整出什么地方的戏?
甲:啊，这个是关于一个叫王家卫的人。
乙:王家卫。
甲:对，王家卫，这个人有一天他去看电影，看到电影里的女主角带了一个小鸟，小鸟叫做小白兔，小白兔是一只很懒惰的小鸟，因此王家卫急于想要这只小鸟。
======================================
Seq2Seq

甲:今天呢我给大家表演相声。
乙:像您这个相声演员都讲究什么。
甲:讲究说学逗唱。
乙:说学逗唱。
甲:对。
乙:唱你能唱什么。
甲:唱我们各地方的地方戏，评戏，梆子，京剧，尤其我们相声演员对京剧非常有研究。
乙:这么说您对京戏非常有研究。
甲:那是啊。
乙:那您会整出戏吗?
-----------------------------------本线之前是context,之后为基于context的剧本生成
甲:戏剧不少。
乙:还没有?
甲:哎。
乙:您怎么回事?
甲:我也没耽误工夫。
乙:您别提这个忙活动。
甲:您这话说得很丰富。
乙:噢。
甲:您看我们这些个社会最近常用的。
乙:噢，您可以参加各种曲艺协会来解放的。

======================================




```