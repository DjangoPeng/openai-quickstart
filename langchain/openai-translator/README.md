# OpenAI-Translator

<p align="center">
    <br> English | <a href="README-CN.md">中文</a>
</p>

<p align="center">
    <em>Google Cloud credits are provided for this project. #AISprint</em>
</p>

## Introduction

OpenAI Translator is an AI-powered translation tool designed to translate English PDF books to Chinese. The tool leverages large language models (LLMs) like `Gemma`, `ChatGLM` and `gpt-3.5-turbo-instruct` for translation. It's built in Python and has a flexible, modular, and object-oriented design. 

## Why this project

In the current landscape, there's a lack of non-commercial yet efficient PDF translation tools. Many users have PDF documents with sensitive data that they prefer not to upload to public commercial service websites due to privacy concerns. This project was developed to address this gap, providing a solution for users who need to translate their PDFs while maintaining data privacy.

### Sample Results

The OpenAI Translator is still in its early stages of development, and I'm actively working on adding more features and improving its performance. We appreciate any feedback or contributions!

![The_Old_Man_of_the_Sea](images/sample_image_0.png)

<p align="center">
    <em>"The Old Man and the Sea"</em>
</p>

## Features

- [X] Translation of English PDF books to Chinese using LLMs.
- [X] Support for both [Gemma 2](https://ai.google.dev/gemma/docs/model_card_2), [ChatGLM](https://github.com/THUDM/ChatGLM-6B) and [OpenAI](https://platform.openai.com/docs/models) models.
- [X] Flexible configuration through a YAML file or command-line arguments.
- [X] Timeouts and error handling for robust translation operations.
- [X] Modular and object-oriented design for easy customization and extension.
- [x] Add support for other languages and translation directions.
- [x] Implement a graphical user interface (GUI) for easier use.
- [x] Create a web service or API to enable usage in web applications.
- [X] Improve translation quality by using custom-trained translation models.


## Getting Started

### Environment Setup

1.Clone the repository `git clone git@github.com:DjangoPeng/openai-translator.git`.

2.Checkout into the `gemma` branch `git checkout gemma`.

3.The `OpenAI-Translator` requires Python 3.10 or later. Install the dependencies with `pip install -r requirements.txt`.

### Usage

You can use OpenAI-Translator either by specifying a configuration file or by providing command-line arguments.

#### Using a configuration file:

Adapt `config.yaml` file with your settings:

```yaml
model_name: "gemma2:2b"
input_file: "tests/test.pdf"
output_file_format: "markdown"
source_language: "English"
target_language: "Chinese"
```

Then run the tool:

```bash
python ai_translator/main.py
```

![sample_out](images/sample_image_1.png)

#### Using Gradio (Graphical Interface):

For a more user-friendly experience, you can launch the OpenAI-Translator with a graphical interface using Gradio. This allows you to interact with the translator through a web-based GUI:

```bash
python ai_translator/gradio_server.py
```

This will open a local web interface where you can upload your PDF, select the model, and configure the translation settings.

![gradio_demo](./images/gradio_demo.png)

#### Using Flask Web Server (REST API):

To integrate the translation service into a web application or to interact with it programmatically, you can start the Flask web server:

```bash
python ai_translator/flask_server.py
```

This launches a REST API where you can send requests to translate documents, allowing for integration with other web services or applications.

#### Using command-line arguments:

You can also specify the settings directly on the command line. Here's an example of how to use the `Gemma-2-2B` model:

```bash
# Set your api_key as an env variable
python ai_translator/main.py --model_name "gemma2:2b" --input_file "your_input.pdf" --output_file_format "markdown" --source_language "English" --target_language "Chinese"
```

### Learning Notebook

The project also includes a [Jupyter Notebook](./jupyter/translation_chain.ipynb) for learning purposes. This notebook demonstrates how to use the translation chain of OpenAI Translator, providing detailed code annotations and examples to help users better understand and utilize the tool. By working through this notebook, you can gain a deeper insight into each step of the translation process and experiment with modifications according to your needs.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.
