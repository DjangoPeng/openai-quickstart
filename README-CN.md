# OpenAI 快速入门

<p align="center">
    <br> <a href="README.md">English</a> | 中文
</p>


本项目旨在为所有对大型语言模型及其在人工智能治理和控制（AIGC）场景中应用的人们提供一站式学习资源。通过提供理论基础，开发基础，和实践示例，该项目对这些前沿主题提供了全面的指导。

## 特性

- **大型语言模型的理论和开发基础**：深入探究像 GPT-4 这样的大型语言模型的内部运作，包括其架构，训练方法，应用等。

- **用 LangChain 开发 AIGC 应用**：使用 LangChain 开发 AIGC 应用的实践示例和教程，展示了大型语言模型的实际应用。

## 入门

你可以通过克隆此仓库到你的本地机器来开始：

```shell
git clone https://github.com/DjangoPeng/openai-quickstart.git
```

然后导航至目录，并按照单个模块的指示开始操作。

## 进度表

| 日期       | 描述                                                                                                                                                                                                        | 课程资料                                                                           | 任务                                                                   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 周一 7月12日 **第1周** | 大型模型基础：理论与技术的演变 <br/> - 大型模型的初步探索：起源与发展 <br/> - 热身：解码注意力机制 <br/> - 变革里程碑：Transformer的崛起 <br/> - 走向不同的道路：GPT和Bert的选择 | 建议阅读：<br/>- [注意力机制：通过联合学习对齐和翻译进行神经机器翻译](https://arxiv.org/abs/1409.0473)<br/>- [注意力模型的细心调查](https://arxiv.org/abs/1904.02874)<br/>- [Transformer：注意力是你所需要的](https://arxiv.org/abs/1706.03762)<br/>- [BERT：对语言理解的深度双向Transformer的预训练](https://arxiv.org/abs/1810.04805) | [[作业](docs/homework_01.md)] |
| 周四 7月16日 | GPT模型家族：从开始到现在 <br/> - 从GPT-1到GPT-3.5：演变 <br/> - ChatGPT：它的胜利之处 <br/> - GPT-4：新的开始 <br/>提示学习 <br/> - 思维链（CoT）：先驱作品 <br/> - 自我一致性：多路径推理 <br/> - 思维树（ToT）：继续故事 | 建议阅读：<br/>- [GPT-1：通过生成性预训练改进语言理解](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)<br/>- [GPT-2：语言模型是无监督的多任务学习者](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)<br/>- [GPT-3：语言模型是少量学习者](https://arxiv.org/abs/2005.14165)<br/><br/><br/>额外阅读：<br/>- [GPT-4：架构，基础设施，训练数据集，成本，愿景，MoE](https://www.semianalysis.com/p/gpt-4-architecture-infrastructure)<br/>- [GPT是GPT：大型语言模型的劳动力市场影响潜力的初步观察](https://arxiv.org/abs/2303.10130)<br/>- [人工智能泛用性的火花：GPT-4的早期实验](https://arxiv.org/abs/2303.12712)<br/><br/> | [[作业](docs/homework_02.md)] |
| 周二 7月19日 **第2周** | 大型模型开发基础：OpenAI嵌入 <br/> - 通用人工智能的前夜 <br/> - "三个世界"和"图灵测试" <br/> - 计算机数据表示 <br/> - 表示学习和嵌入 <br/> 嵌入Dev 101 <br/> - 课程项目：GitHub openai-quickstart <br/> - 从OpenAI嵌入开始                     | 建议阅读：<br/>- [表示学习：回顾和新视角](https://arxiv.org/abs/1206.5538)<br/>- [Word2Vec：高效估计词在向量空间中的表示](https://arxiv.org/abs/1301.3781)<br/>- [GloVe：全局向量词表示](https://nlp.stanford.edu/pubs/glove.pdf)<br/><br/>额外阅读：<br/><br/>- [利用词嵌入学到的经验改进分布式相似性](http://www.aclweb.org/anthology/Q15-1016)<br/>- [无监督词嵌入的评估方法](http://www.aclweb.org/anthology/D15-1036) | [[作业](docs/homework_03.md)]<br/>代码：<br/>[[嵌入](openai_api/embedding.ipynb)] |
| 周六 7月23日 | OpenAI大型模型开发和应用实践 <br/> - OpenAI大型模型开发指南 <br/> - OpenAI语言模型概述 <br/> - OpenAI GPT-4，GPT-3.5，GPT-3，审核 <br/> - OpenAI令牌计费和计算 <br/>OpenAI API介绍和实践 <br/> - OpenAI模型API <br/> - OpenAI补全API  <br/> - OpenAI聊天补全API <br/> - 补全vs聊天补全 <br/>OpenAI大型模型应用实践 <br/> - 文本完成的初步探索 <br/> - 聊天机器人的初步探索 | 建议阅读：<br/><br/>- [OpenAI模型](https://platform.openai.com/docs/models)<br/>- [OpenAI补全API](https://platform.openai.com/docs/guides/gpt/completions-api)<br/>- [OpenAI聊天补全API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) | 代码：<br/>[[模型](openai_api/models.ipynb)] <br/>[[tiktoken](openai_api/count_tokens_with_tiktoken.ipynb)] |


## 贡献

贡献是使开源社区成为学习、激励和创造的惊人之处。非常感谢你所做的任何贡献。如果你有任何建议或功能请求，请先开启一个议题讨论你想要改变的内容。

## 许可证

该项目根据Apache-2.0许可证的条款进行许可。详情请参见[LICENSE](LICENSE)文件。

## 联系

Django Peng - pjt73651@email.com

项目链接: https://github.com/DjangoPeng/openai-quickstart

