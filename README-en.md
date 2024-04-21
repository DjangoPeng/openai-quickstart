# OpenAI Quickstart

<p align="center">
    <br> English | <a href="README.md">中文</a>
</p>


This project is designed as a one-stop learning resource for anyone interested in large language models and their application in Generative AI(GenAI) scenarios. By providing theoretical foundations, development basics, and hands-on examples, this project offers comprehensive guidance on these cutting-edge topics.

## Features

- **Theory and Development Basics of Large Language Models**: Deep dive into the inner workings of large language models like BERT and GPT Family, including their architecture, training methods, applications, and more.

- **OpenAI-based Development**: tutorial and best practices for OpenAI's Embedding, GPT-3.5, GPT-4, as well as practical development such as Function Calling and **ChatGPT Plugin**.

- **GenAI Application Development with LangChain**: Hands-on examples and tutorials using LangChain to develop GenAI applications, demonstrating the practical application of large language models(**AutoGPT, RAG-chatbot, Machine Translation**)

- **LLM Tech Stack and Ecosystem**: Data privacy and legal compliance, GPU Technology Selection Guide, Hugging Face quick start, ChatGLM usage.

## Getting Started

You can start by cloning this repository to your local machine:

```shell
git clone https://github.com/DjangoPeng/openai-quickstart.git
```

Then navigate to the directory and follow the individual module instructions to get started.


## Setting Up the Development Environment

This project is developed using Python v3.10. For a complete list of Python dependency packages, see [requirements.txt](requirements.txt).

Official documentation for key dependencies is as follows:

- Python environment management with [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
- Interactive Python development environment [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
- Large model application development framework [LangChain](https://python.langchain.com/docs/get_started/installation)
- [OpenAI Python SDK](https://github.com/openai/openai-python?tab=readme-ov-file#installation)


**Below are detailed installation instructions (using Ubuntu OS as an example):**

### Installing Miniconda

```shell
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

After installation, it is recommended to create a new Python virtual environment named `langchain`.

```shell
conda create -n langchain python=3.10

# Activate the environment
conda activate langchain 
```

This environment needs to be activated each time before use.


### Installing Python Dependency Packages

```shell
pip install -r requirements.txt
```

### Configuring OpenAI API Key

Depending on the command-line tool you use, set the `OPENAI_API_KEY` environment variable in `~/.bashrc` or `~/.zshrc`:

```shell
export OPENAI_API_KEY="xxxx"
```

### Installing and Configuring Jupyter Lab

After the above development environment setup, use Miniconda to install Jupyter Lab:

```shell
# Generate a Jupyter Lab configuration file
jupyter lab --generate-config
```

Open the configuration file and make the following changes:

```python
# Allowing Jupyter Lab to start as a non-root user (no need to modify if starting as root)
c.ServerApp.allow_root = True
c.ServerApp.ip = '*'
```

Use `nohup` to start Jupyter Lab in the background:

```shell
$ nohup jupyter lab --port=8000 --NotebookApp.token='replace_with_your_password' --notebook-dir=./ &
```

Jupyter Lab's output log will be saved in the `nohup.out` file (which is already filtered in the `.gitignore` file).


## Schedule

| Lesson     | Description                                                                                                                                                                                                        | Course Materials                                                                          | Events                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Lesson 1   | Fundamentals of Large Models: Evolution of Theory and Technology <br/> - An Initial Exploration of Large Models: Origin and Development <br/> - Warm-up: Decoding Attention Mechanism <br/> - Milestone of Transformation: The Rise of Transformer <br/> - Taking Different Paths: The Choices of GPT and Bert | Suggested Readings:<br/>- [Attention Mechanism: Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)<br/>- [An Attentive Survey of Attention Models](https://arxiv.org/abs/1904.02874)<br/>- [Transformer: Attention is All you Need](https://arxiv.org/abs/1706.03762)<br/>- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | [[Homework](docs/homework_01.md)] |
| Lesson 2   | The GPT Model Family: From Start to Present <br/> - From GPT-1 to GPT-3.5: The Evolution <br/> - ChatGPT: Where It Wins <br/> - GPT-4: A New Beginning <br/>Prompt Learning <br/> - Chain-of-Thought (CoT): The Pioneering Work <br/> - Self-Consistency: Multi-path Reasoning <br/> - Tree-of-Thoughts (ToT): Continuing the Story | Suggested Readings:<br/>- [GPT-1: Improving Language Understanding by Generative Pre-training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)<br/>- [GPT-2: Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)<br/>- [GPT-3: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)<br/><br/><br/>Additional Readings:<br/>- [GPT-4: Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE](https://www.semianalysis.com/p/gpt-4-architecture-infrastructure)<br/>- [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models](https://arxiv.org/abs/2303.10130)<br/>- [Sparks of Artificial General Intelligence: Early experiments with GPT-4](https://arxiv.org/abs/2303.12712)<br/><br/> | [[Homework](docs/homework_02.md)] |
| Lesson 3   | Fundamentals of Large Model Development: OpenAI Embedding <br/> - The Eve of General Artificial Intelligence <br/> - "Three Worlds" and "Turing Test" <br/> - Computer Data Representation <br/> - Representation Learning and Embedding <br/> Embeddings Dev 101 <br/> - Course Project: GitHub openai-quickstart <br/> - Getting Started with OpenAI Embeddings                      | Suggested Readings:<br/>- [Representation Learning: A Review and New Perspectives](https://arxiv.org/abs/1206.5538)<br/>- [Word2Vec: Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)<br/>- [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)<br/><br/>Additional Readings:<br/><br/>- [Improving Distributional Similarity with Lessons Learned from Word Embeddings](http://www.aclweb.org/anthology/Q15-1016)<br/>- [Evaluation methods for unsupervised word embeddings](http://www.aclweb.org/anthology/D15-1036) | [[Homework](docs/homework_03.md)]<br/>Code:<br/>[[embedding](openai_api/embedding.ipynb)] |
| Lesson 4   | OpenAI Large Model Development and Application Practice <br/> - OpenAI Large Model Development Guide <br/> - Overview of OpenAI Language Models <br/> - OpenAI GPT-4, GPT-3.5, GPT-3, Moderation <br/> - OpenAI Token Billing and Calculation <br/>OpenAI API Introduction and Practice <br/> - OpenAI Models API <br/> - OpenAI Completions API  <br/> - OpenAI Chat Completions API <br/> - Completions vs Chat Completions <br/>OpenAI Large Model Application Practice <br/> - Initial Exploration of Text Completion <br/> - Initial Exploration of Chatbots | Suggested Readings:<br/><br/>- [OpenAI Models](https://platform.openai.com/docs/models)<br/>- [OpenAI Completions API](https://platform.openai.com/docs/guides/gpt/completions-api)<br/>- [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) | Code:<br/>[[models](openai_api/models.ipynb)] <br/>[[tiktoken](openai_api/count_tokens_with_tiktoken.ipynb)] |
| Lesson 5   | Best Practices for Applying Large AI Models <br/> - How to Improve the Efficiency and Quality of GPT Model Use <br/> - Best Practices for Applying Large AI Models <br/>   - Text Creation and Generation<br/>   - Article Abstract and Summary <br/>    - Novel Generation and Content Supervision <br/>    - Executing Complex Tasks Step by Step <br/>    - Evaluating the Quality of Model Output <br/>    - Constructing Training Annotation Data <br/>    - Code Debugging Assistant <br/> - New Features： Function Calling Introduction and Practical Application | Suggested Readings <br/> - [GPT Best Practices](https://platform.openai.com/docs/guides/gpt-best-practices) <br/> - [Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling) | Code： <br/> [Function Calling](openai_api/function_call.ipynb) |
| Lesson 6   | Practical: OpenAI-Translator <br/> - Market demand analysis for OpenAI-Translator <br/> - Product definition and feature planning for OpenAI-Translator <br/> - Technical solutions and architecture design for OpenAI-Translator <br/> - OpenAI module design <br/> - OpenAI-Translator practical application <br/> | | Code: <br/> [pdfplumber](openai-translator/jupyter/pdfplumber.ipynb) |
| Lesson 7   | ChatGPT Plugin Development Guide <br/> - Introduction to ChatGPT Plugin <br/> - Sample project: Todo management plugin <br/> - Deployment and testing of practical examples <br/> - ChatGPT developer mode <br/> - Practical: Weather Forecast plugin development <br/> - Weather Forecast Plugin design and definition <br/> - Weather Forecast function service <br/> - Integration with third-party weather query platform <br/> - Practical Weather Forecast Plugin | | Code: <br/> [[todo list](chatgpt-plugins/todo-list)] <br/> [[weather forecast](chatgpt-plugins/weather-forecast)]  |
| Lesson 8   | LLM Application Development Framework LangChain (Part 1) <br/> - LangChain 101  <br/> - What is LangChain <br/> - Why LangChain is Needed <br/> - Typical Use Cases of LangChain <br/> - Basic Concepts and Modular Design of LangChain <br/> - Introduction and Practice of LangChain Core Modules <br/> - Standardized Large-Scale Model Abstraction: Mode I/O <br/> -  Template Input: Prompts <br/> -  Language Model: Models <br/> - Standardized Output: Output Parsers  | | Code: <br/> [[model io](langchain/jupyter/model_io)] |
| Lesson 9   | LLM Application Development Framework LangChain (Part 2) <br/> - Best Practices for LLM Chains <br/> - Getting Started with Your First Chain: LLM Chain <br/> - Sequential Chain: A Chained Call with Sequential Arrangement <br/> - Transform Chain: A Chain for Processing Long Texts <br/> - Router Chain: A Chain for Implementing Conditional Judgments <br/> - Memory: Endowing Applications with Memory Capabilities <br/> - The Relationship between Memory System and Chain <br/> - BaseMemory and BaseChatMessageMemory: Memory Base Classes <br/> - Memory System for Service Chatting <br/> - ConversationBufferMemory <br/> - ConversationBufferWindowMemory <br/> - ConversationSummaryBufferMemory  |  | Code: <br/> [[chains](langchain/jupyter/chains)] <br/> [[memory](langchain/jupyter/memory)] |
| Lesson 10  | LLM Application Development Framework LangChain (Part 3)  <br/> - Native data processing flow of the framework: Data Connection <br/> - Document Loaders <br/> - Document Transformers <br/> - Text Embedding Models <br/> - Vector Stores <br/> - Retrievers <br/> - Agent Systems for Building Complex Applications: Agents <br/> - Theoretical Foundation of Agents: ReAct <br/> - LLM Reasoning Capabilities: CoT, ToT <br/> - LLM Operation Capabilities: WebGPT, SayCan <br/> - LangChain Agents Module Design and Principle Analysis <br/> - Module: Agent, Tools, Toolkits <br/> - Runtime: AgentExecutor, PlanAndExecute, AutoGPT <br/> - Getting Started with Your First Agent: Google Search + LLM <br/> - Practice with ReAct: SerpAPI + LLM-MATH |  | Code: <br/> [[data connection](langchain/jupyter/data_connection)] <br/> [[agents](langchain/jupyter/agents)] |
| Lesson 11  | Practical: LangChain version OpenAI-Translator v2.0 <br/> - In-depth understanding of Chat Model and Chat Prompt Template <br/> - Review: LangChain Chat Model usage and process <br/> - Design translation prompt templates using Chat Prompt Template <br/> - Implement bilingual translation using Chat Model <br/> - Simplify Chat Prompt construction using LLMChain <br/> - Optimize OpenAI-Translator architecture design based on LangChain <br/> - Hand over large model management to LangChain framework <br/> - Focus on application-specific Prompt design <br/> - Implement translation interface using TranslationChain <br/> - More concise and unified configuration management <br/> - Development of OpenAI-Translator v2.0 feature <br/> - Design and implementation of graphical interface based on Gradio <br/> - Design and implementation of Web Server based on Flask | | Code:  <br/> [[openai-translator](langchain/openai-translator)] |
| Lesson 12  | Practical: LangChain version Auto-GPT <br/> - Auto-GPT project positioning and value interpretation <br/> - Introduction to Auto-GPT open source project <br/> - Auto-GPT positioning: an independent GPT-4 experiment <br/> - Auto-GPT value: an attempt at AGI based on Agent <br/> - LangChain version Auto-GPT technical solution and architecture design <br/> - In-depth understanding of LangChain Agents <br/> - LangChain Experimental module <br/> - Auto-GPT autonomous agent design <br/> - Auto-GPT Prompt design <br/> - Auto-GPT Memory design <br/> - In-depth understanding of LangChain VectorStore <br/> - Auto-GPT OutputParser design <br/> - Practical LangChain version Auto-GPT | | Code: <br/> [[autogpt](langchain/jupyter/autogpt)] |
| Lesson 13  | Sales-Consultant business process and value analysis <br/> - Technical solution and architecture design of Sales-Consultant <br/> - Use GPT-4 to generate sales pitches <br/> - Store sales Q&A pitches in FAISS vector database <br/> - Retrieve sales pitches data using RetrievalQA <br/> - Implement chatbot graphical interface using Gradio <br/> - Practical LangChain version Sales-Consultant | | Code： <br/> [[sales_chatbot](langchain/sales_chatbot)] |
| Lesson 14  | Era of large models: Open source and data protocols <br/> - What is open source? <br/> - Widely used open source and data protocols <br/> - Is Llama pseudo-open source? <br/> - Open source protocol of ChatGLM2-6B <br/> Interpretability of large language models <br/> - Enhancing transparency in model decision-making <br/> - Related research of Stanford Alpaca <br/> Regulatory compliance of large language model applications <br/> - Mainland China: Registration of generative AI services <br/> - International: Data privacy and protection (taking GDPR as an example) <br/> - Key points of corporate compliance | | |
| Lesson 15  | Github in the era of large models: Hugging Face <br/> - What is Hugging Face? <br/> - Hugging Face Transformers library <br/> - Hugging Face open community: Models, Datasets, Spaces, Docs <br/> - Comparative analysis of large models <br/> - Open LLM Leaderboard (Large Model Ladder) <br/> Graphics card selection guide <br/> - GPU vs Graphics card <br/> - GPU Core vs AMD CU <br/> - CUDA Core vs Tensor Core <br/> - Evolution of Nvidia architectures <br/> - Graphics card performance ladder | | |
| Lesson 16  | Tsinghua GLM large model family <br/> - Strongest base model GLM-130B <br/> - Enhanced dialogue capability ChatGLM <br/> - Open source chat model ChatGLM2-6B <br/> - Internet search capability WebGLM <br/> - Initial exploration of multimodal VisualGLM-6B <br/> - Code generation model CodeGeex2 <br/> Application development of ChatGLM2-6B large model <br/> - Private deployment of ChatGLM2-6B <br/> - HF Transformers Tokenizer <br/> - HF Transformers Model <br/> - Synchronize the model to Hugging Face <br/> - Empower ChatGLM2-6B graphical interface using Gradio <br/> - Fine-tuning of ChatGLM2-6B model <br/> - Practical assignment: Implement graphical interface of openai-translator based on ChatGLM2-6B | | |



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have any suggestions or feature requests, please open an issue first to discuss what you would like to change.

<a href='https://github.com/repo-reviews/repo-reviews.github.io/blob/main/create.md' target="_blank"><img alt='Github' src='https://img.shields.io/badge/review_me-100000?style=flat&logo=Github&logoColor=white&labelColor=888888&color=555555'/></a>

## License

This project is licensed under the terms of the Apache-2.0 License . See the [LICENSE](LICENSE) file for details.

## Contact

Django Peng - pjt73651@email.com

Project Link: https://github.com/DjangoPeng/openai-quickstart
