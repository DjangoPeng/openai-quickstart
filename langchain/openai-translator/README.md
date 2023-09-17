# OpenAI-Translator

## Introduction

OpenAI Translator is an AI-powered translation tool designed to translate English PDF books to Chinese. The tool leverages large language models (LLMs) like ChatGLM and OpenAI's GPT-3 and GPT-3.5 Turbo for translation. It's built in Python and has a flexible, modular, and object-oriented design. 

## Why this project
Langchain prac cause I like programming

### Sample Results

## Features

- [X] Translation  PDF books to MarkDown by using LLMs.
- [X] Support for [OpenAI](https://platform.openai.com/docs/models) models.
- [X] Flexible configuration through a YAML file or gradios building UI.
- [X] Timeouts and error handling for robust translation operations.
- [X] Modular and object-oriented design for easy customization and extension.
- [x] Add support for translation styles.
- [X] able to add images into MarkDown file 


## Getting Started

### Environment Setup

1.Clone the repository `https://github.com/ycAlex11/langchain-examples-.git`.

2.The `OpenAI-Translator` requires Python 3.10 or later. Install the dependencies with `pip install -r requirements.txt`.

3.Set up your OpenAI API key(`$OPENAI_API_KEY`). You have to specify it in the config.yaml file.

### Usage

You can use OpenAI-Translator either by specifying a configuration file .

#### Using a configuration file:

Adapt `config.yaml` file with your settings:

```yaml
model_name: "gpt-3.5-turbo"
input_file: "tests/test.pdf"
output_file_format: "markdown"
source_language: "English"
target_language: "Chinese"
api_key: "your OpenAI API key"
style:""
```

Then run the tool:

```bash
python ai_translator/main.py
```