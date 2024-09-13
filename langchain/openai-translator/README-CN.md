
# OpenAI-Translator

<p align="center">
    <br> <a href="README.md">English</a> | 中文
</p>

## 介绍

OpenAI Translator 是一个由 AI 驱动的翻译工具，旨在将英文 PDF 书籍翻译成中文。该工具利用了如 `Gemma`、`ChatGLM` 和 `gpt-3.5-turbo-instruct` 等大语言模型（LLMs）进行翻译。它是用 Python 构建的，具有灵活、模块化和面向对象的设计。

## 项目缘由

在当前的环境中，缺乏非商业化但高效的 PDF 翻译工具。许多用户拥有包含敏感数据的 PDF 文档，他们不希望将这些文档上传到公共商业服务网站以保持隐私。本项目旨在解决这一问题，为需要翻译 PDF 的用户提供一个能够维护数据隐私的解决方案。

### 示例结果

OpenAI Translator 仍处于开发的早期阶段，我正在积极添加更多功能并提高其性能。我们欢迎任何反馈或贡献！

![老人与海](images/sample_image_0.png)

<p align="center">
    <em>"老人与海"</em>
</p>

## 功能

- [X] 支持任意语言对之间的 PDF 电子书翻译。
- [X] 支持 [Gemma 2](https://ai.google.dev/gemma/docs/model_card_2), [ChatGLM](https://github.com/THUDM/ChatGLM-6B) 和 [OpenAI](https://platform.openai.com/docs/models) 模型。
- [X] 通过 YAML 文件或命令行参数进行灵活配置。
- [X] 超时和错误处理功能确保翻译操作的稳健性。
- [X] 模块化和面向对象的设计，便于定制和扩展。
- [x] 支持其他语言和翻译方向。
- [x] 实现图形用户界面（GUI），便于使用。
- [x] 创建一个 Web 服务或 API，以便在 Web 应用中使用。
- [X] 通过使用自定义训练的翻译模型提高翻译质量。

## 入门指南

### 环境设置

1. 克隆仓库 `git clone git@github.com:DjangoPeng/openai-translator.git`。

2. 切换到 `gemma` 分支 `git checkout gemma`。

3. OpenAI-Translator 需要 Python 3.10 或更高版本。使用 `pip install -r requirements.txt` 安装依赖。

### 使用方法

您可以通过指定配置文件或提供命令行参数来使用 OpenAI-Translator。

#### 使用配置文件：

根据您的设置修改 `config.yaml` 文件：

```yaml
model_name: "gemma2:2b"
input_file: "tests/test.pdf"
output_file_format: "markdown"
source_language: "English"
target_language: "Chinese"
```

然后运行工具：

```bash
python ai_translator/main.py
```

![示例输出](images/sample_image_1.png)

#### 使用 Gradio （图形界面）：

为了更便捷的用户体验，您可以使用 Gradio 启动 OpenAI-Translator 图形界面。这允许您通过 Web 界面与翻译器进行交互：

```bash
python ai_translator/gradio_server.py
```

这将打开一个本地 Web 界面，您可以在其中上传 PDF，选择模型并配置翻译设置。

#### 使用 Flask Web Server （REST API）：

要将翻译服务集成到 Web 应用中或以编程方式与之交互，您可以启动 Flask Web 服务器：

```bash
python ai_translator/flask_server.py
```

这将启动一个 REST API，您可以发送请求以翻译文档，允许与其他 Web 服务或应用程序集成。

#### 使用命令行参数：

您还可以直接在命令行上指定设置。以下是如何使用 `Gemma-2-2B` 模型的示例：

```bash
# 将您的 api_key 设置为环境变量
python ai_translator/main.py --model_name "gemma2:2b" --input_file "your_input.pdf" --output_file_format "markdown" --source_language "English" --target_language "Chinese"
```

### 学习笔记本

项目中还包含一个用于学习的 [Jupyter Notebook](./jupyter/translation_chain.ipynb)。此 Notebook 演示了如何使用 OpenAI Translator 的翻译链，并提供了详细的代码注释和示例，帮助用户更好地理解和使用该工具。通过此 Notebook，您可以更深入地了解翻译过程的每个步骤，并根据自己的需求进行实验和修改。


## 许可证

本项目采用 Apache-2.0 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
