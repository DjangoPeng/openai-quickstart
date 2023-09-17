# OpenAI-Translator

## 简介

OpenAI Translator 是一个基于人工智能的翻译工具，旨在将英文PDF书籍翻译成中文。该工具利用了大型语言模型（LLMs）如ChatGLM以及OpenAI的GPT-3和GPT-3.5 Turbo进行翻译。它是用Python构建的，具有灵活、模块化和面向对象的设计。

## 为什么选择这个项目
喜欢敲敲代码，顺便熟悉langchain
### 示例结果

## 特点

- [X] 使用LLMs将PDF书籍翻译成Markdown。
- [X] 支持[OpenAI](https://platform.openai.com/docs/models)模型。
- [X] 通过YAML文件或Gradio构建界面进行灵活的配置。
- [X] 强大的超时和错误处理功能，确保翻译操作的稳健性。
- [X] 模块化和面向对象的设计，便于自定义和扩展。
- [x] 添加对翻译风格的支持。
- [X] 能够将图片插入到Markdown文件中。

## 入门指南

### 环境设置

1. 克隆仓库 `https://github.com/ycAlex11/langchain-examples-.git`。

2. `OpenAI-Translator` 需要Python 3.10或更高版本。使用 `pip install -r requirements.txt` 安装依赖项。

3. 设置你的OpenAI API密钥（`$OPENAI_API_KEY`）。你需要在config.yaml文件中指定它。

### 使用方法

你可以通过指定一个配置文件来使用OpenAI-Translator。

#### 使用配置文件：

根据你的设置修改`config.yaml`文件：

```yaml
model_name: "gpt-3.5-turbo"
input_file: "tests/test.pdf"
output_file_format: "markdown"
source_language: "English"
target_language: "Chinese"
api_key: "你的OpenAI API密钥"
style:""
```

然后运行工具：

```bash
python ai_translator/main.py
```