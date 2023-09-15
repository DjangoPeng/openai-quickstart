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

## 课程表

| 课表 | 描述                                                                                                                                                                                                        | 课程资料                                                                           | 任务                                                                   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 第1节   | 大模型基础：理论与技术的演进 <br/> - 初探大模型：起源与发展 <br/> - 预热篇：解码注意力机制 <br/> - 变革里程碑：Transformer的崛起 <br/> - 走向不同：GPT与BERT的选择 | 建议阅读：<br/>- [Attention Mechanism: Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)<br/>- [An Attentive Survey of Attention Models](https://arxiv.org/abs/1904.02874)<br/>- [Transformer：Attention is All you Need](https://arxiv.org/abs/1706.03762)<br/>- [BERT：Pre-training of Deep Bidirectional Transformers for Language Understanding(https://arxiv.org/abs/1810.04805) | [[作业](docs/homework_01.md)] |
| 第2节   | GPT 模型家族：从始至今 <br/> - 从GPT-1到GPT-3.5：一路的风云变幻 <br/> - ChatGPT：赢在哪里 <br/> - GPT-4：一个新的开始 <br/>提示学习（Prompt Learning） <br/> - 思维链（Chain-of-Thought, CoT）：开山之作 <br/> - 自洽性（Self-Consistency）：多路径推理 <br/> - 思维树（Tree-of-Thoughts, ToT）：续写佳话 | 建议阅读：<br/>- [GPT-1: Improving Language Understanding by Generative Pre-training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)<br/>- [GPT-2: Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)<br/>- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)<br/><br/><br/>额外阅读：<br/>- [GPT-4: Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE](https://www.semianalysis.com/p/gpt-4-architecture-infrastructure)<br/>- [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130)<br/>- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712)<br/><br/> | [[作业](docs/homework_02.md)] |
| 第3节   | 大模型开发基础：OpenAI Embedding <br/> - 通用人工智能的前夜 <br/> - "三个世界"和"图灵测试" <br/> - 计算机数据表示 <br/> - 表示学习和嵌入 <br/> Embeddings Dev 101 <br/> - 课程项目：GitHub openai-quickstart <br/> - 快速上手 OpenAI Embeddings                     | 建议阅读：<br/>- [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538)<br/>- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)<br/>- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)<br/><br/>额外阅读：<br/><br/>- [Improving Distributional Similarity with Lessons Learned from Word Embeddings](http://www.aclweb.org/anthology/Q15-1016)<br/>- [Evaluation methods for unsupervised word embeddings](http://www.aclweb.org/anthology/D15-1036) | [[作业](docs/homework_03.md)]<br/>代码：<br/>[[embedding](openai_api/embedding.ipynb)] |
| 第4节   | OpenAI 大模型开发与应用实践 <br/> - OpenAI大型模型开发指南 <br/> - OpenAI 语言模型总览 <br/> - OpenAI GPT-4, GPT-3.5, GPT-3, Moderation <br/> - OpenAI Token 计费与计算 <br/>OpenAI API 入门与实战 <br/> - OpenAI Models API <br/> - OpenAI Completions API  <br/> - OpenAI Chat Completions API <br/> - Completions vs Chat Completions <br/>OpenAI 大模型应用实践 <br/> - 文本内容补全初探（Text Completion） <br/> - 聊天机器人初探（Chat Completion） | 建议阅读：<br/><br/>- [OpenAI Models](https://platform.openai.com/docs/models)<br/>- [OpenAI Completions API](https://platform.openai.com/docs/guides/gpt/completions-api)<br/>- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) | 代码：<br/>[[models](openai_api/models.ipynb)] <br/>[[tiktoken](openai_api/count_tokens_with_tiktoken.ipynb)] |
| 第5节   | AI大模型应用最佳实践 <br/> - 如何提升GPT模型使用效率与质量 <br/> - AI大模型应用最佳实践 <br/>   - 文本创作与生成<br/>   - 文章摘要和总结 <br/>    - 小说生成与内容监管 <br/>    - 分步骤执行复杂任务 <br/>    - 评估模型输出质量 <br/>    - 构造训练标注数据 <br/>    - 代码调试助手 <br/> - 新特性： Function Calling 介绍与实战 | 建议阅读 <br/> - [GPT Best Practices](https://platform.openai.com/docs/guides/gpt-best-practices) <br/> - [Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling) | 代码： <br/> [Function Calling](openai_api/function_call.ipynb) |
| 第6节   | 实战：OpenAI-Translator <br/> - OpenAI-Translator 市场需求分析 <br/> - OpenAI-Translator 产品定义与功能规划 <br/> - OpenAI-Translator 技术方案与架构设计 <br/> - OpenAI 模块设计 <br/> - OpenAI-Translator 实战 <br/>  |  | 代码： <br/> [pdfplumber](openai_translator/jupyter/pdfplumber.ipynb) |
| 第7节   | 实战：ChatGPT Plugin 开发 <br/> - ChatGPT Plugin 开发指南 <br/> - ChatGPT Plugin 介绍 <br/> - ChatGPT Plugin 介绍 <br/> - 样例项目：待办（Todo）管理插件 <br/> - 实战样例部署与测试 <br/> - ChatGPT 开发者模式 <br/> - 实战：天气预报（Weather Forecast）插件开发 <br/> - Weather Forecast Plugin 设计与定义 <br/> - 天气预报函数服务化 <br/> - 第三方天气查询平台对接 <br/> - 实战 Weather Forecast Plugin <br/> - Function Calling vs ChatGPT plugin <br/>  | | 代码： <br/> [[todo list](openai_plugins/todo-list)]  <br/> [[Weather Forecast](openai_plugins/weather-forecast)] |
| 第8节   | 大模型应用开发框架 LangChain (上) <br/> - LangChain 101  <br/> - LangChain 是什么 <br/> - 为什么需要 LangChain <br/> - LangChain 典型使用场景 <br/> - LangChain 基础概念与模块化设计 <br/> - LangChain 核心模块入门与实战 <br/> - 标准化的大模型抽象：Mode I/O <br/> -  模板化输入：Prompts <br/> -  语言模型：Models <br/> - 规范化输出：Output Parsers  | | 代码： <br/> [[model io](langchain/jupyter/model_io)] |
| 第9节   | 大模型应用开发框架 LangChain (中) <br/> - 大模型应用的最佳实践 Chains <br/> - 上手你的第一个链：LLM Chain <br/> - 串联式编排调用链：Sequential Chain <br/> - 处理超长文本的转换链：Transform Chain <br/> - 实现条件判断的路由链：Router Chain <br/> - 赋予应用记忆的能力： Memory <br/> - Momory System 与 Chain 的关系 <br/> - 记忆基类 BaseMemory 与 BaseChatMessageMemory <br/> - 服务聊天对话的记忆系统 <br/> - ConversationBufferMemory <br/> - ConversationBufferWindowMemory <br/> - ConversationSummaryBufferMemory |  | 代码： <br/> [[chain](langchain/jupyter/chain)] <br/> [[memory](langchain/jupyter/memory)] |
| 第10节  | 大模型应用开发框架 LangChain (下) <br/> - 框架原生的数据处理流 Data Connection <br/> - 文档加载器（Document Loaders） <br/> - 文档转换器（Document Transformers） <br/> - 文本向量模型（Text Embedding Models） <br/> - 向量数据库（Vector Stores） <br/> - 检索器（Retrievers） <br/> - 构建复杂应用的代理系统 Agents <br/> - Agent 理论基础：ReAct <br/> -  LLM 推理能力：CoT, ToT <br/> -  LLM 操作能力：WebGPT, SayCan <br/> - LangChain Agents 模块设计与原理剖析 <br/> -  Module: Agent, Tools, Toolkits, <br/> -  Runtime: AgentExecutor, PlanAndExecute , AutoGPT, <br/> - 上手第一个Agent：Google Search + LLM <br/> - 实战 ReAct：SerpAPI + LLM-MATH |  | 代码： <br/> [[data connection](langchain/jupyter/data_connection)] <br/> [[agents](langchain/jupyter/agents)] |
| 第11节  | 实战： LangChain 版 OpenAI-Translator v2.0 <br/> - 深入理解 Chat Model 和 Chat Prompt Template <br/> - 温故：LangChain Chat Model 使用方法和流程 <br/> - 使用 Chat Prompt Template 设计翻译提示模板 <br/> - 使用 Chat Model 实现双语翻译 <br/> - 使用 LLMChain 简化构造 Chat Prompt <br/> - 基于 LangChain 优化 OpenAI-Translator 架构设计 <br/> - 由 LangChain 框架接手大模型管理 <br/> - 聚焦应用自身的 Prompt 设计 <br/> - 使用 TranslationChain 实现翻译接口 <br/> - 更简洁统一的配置管理 <br/> - OpenAI-Translator v2.0 功能特性研发 <br/> - 基于Gradio的图形化界面设计与实现 <br/> - 基于 Flask 的 Web Server 设计与实现 |  | 代码： <br/> [[openai-translator](langchain/openai-translator)] |
| 第12节  | 实战： LangChain 版Auto-GPT  <br/> - Auto-GPT 项目定位与价值解读 <br/> - Auto-GPT 开源项目介绍 <br/> - Auto-GPT 定位：一个自主的 GPT-4 实验 <br/> - Auto-GPT 价值：一种基于 Agent 的 AGI 尝试 <br/> - LangChain 版 Auto-GPT 技术方案与架构设计 <br/> - 深入理解 LangChain Agents <br/> - LangChain Experimental 模块 <br/> - Auto-GPT 自主智能体设计 <br/> - Auto-GPT Prompt 设计 <br/> - Auto-GPT Memory 设计 <br/> - 深入理解 LangChain VectorStore <br/> - Auto-GPT OutputParser 设计 <br/> - 实战 LangChain 版 Auto-GPT |    | 代码： <br/> [[autogpt](langchain/jupyter/autogpt)] |
| 第13节  | Sales-Consultant 业务流程与价值分析 <br/> - Sales-Consultant 技术方案与架构设计 <br/> - 使用 GPT-4 生成销售话术 <br/> - 使用 FAISS 向量数据库存储销售问答话术 <br/> - 使用 RetrievalQA 检索销售话术数据 <br/> - 使用 Gradio 实现聊天机器人的图形化界面 <br/> - 实战 LangChain 版 Sales-Consultant | | 代码： <br/> [[sales_chatbot](langchain/sales_chatbot)] |
| 第14节  | 大模型时代的开源与数据协议 <br/> - 什么是开源？ <br/> - 广泛使用的开源协议和数据协议 <br/> - Llama 是不是伪开源？ <br/> - ChatGLM2-6B 的开源协议 <br/> 大语言模型的可解释性 <br/> - 提高模型决策过程的透明度 <br/> - Stanford Alpaca 的相关研究 <br/> 大语言模型应用的法规合规性 <br/> - 中国大陆：生成式人工智能服务备案 <br/> - 国际化：数据隐私与保护（以 GDPR 为例） <br/> - 企业合规性应对要点 | | |
| 第15节  | 大模型时代的Github：Hugging Face <br/> - Hugging Face 是什么？ <br/> - Hugging Face Transformers 库 <br/> - Hugging Face 开源社区：Models, Datasets, Spaces, Docs <br/> - 大模型横向对比 <br/> - Open LLM Leaderboard（大模型天梯榜） <br/> 显卡选型推荐指南 <br/> - GPU vs 显卡 <br/> - GPU Core vs AMD CU <br/> - CUDA Core vs Tensor Core <br/> - N卡的架构变迁 <br/> - 显卡性能天梯榜 | | |
| 第16节  | 清华 GLM 大模型家族 <br/> - 最强基座模型 GLM-130B  <br/> - 增强对话能力 ChatGLM <br/> - 开源聊天模型 ChatGLM2-6B <br/> - 联网检索能力 WebGLM <br/> - 初探多模态 VisualGLM-6B <br/> - 代码生成模型 CodeGeex2 <br/> ChatGLM2-6B 大模型应用开发 <br/> - ChatGLM2-6B 私有化部署 <br/> - HF Transformers Tokenizer <br/> - HF Transformers Model <br/> - 将模型同步至 Hugging Face <br/> - 使用 Gradio 赋能 ChatGLM2-6B 图形化界面 <


## 贡献

贡献是使开源社区成为学习、激励和创造的惊人之处。非常感谢你所做的任何贡献。如果你有任何建议或功能请求，请先开启一个议题讨论你想要改变的内容。

<a href='https://github.com/repo-reviews/repo-reviews.github.io/blob/main/create.md' target="_blank"><img alt='Github' src='https://img.shields.io/badge/review_me-100000?style=flat&logo=Github&logoColor=white&labelColor=888888&color=555555'/></a>

## 许可证

该项目根据Apache-2.0许可证的条款进行许可。详情请参见[LICENSE](LICENSE)文件。

## 联系

Django Peng - pjt73651@email.com

项目链接: https://github.com/DjangoPeng/openai-quickstart

