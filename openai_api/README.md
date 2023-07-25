# OpenAI Quickstart Guide

<p align="center">
    <br> English | <a href="README-CN.md">中文</a>
</p>

This project guides you through the initial steps of developing applications using the OpenAI API. It will help you setup your development environment, understand how to use the API, and provide you with a working Jupyter Lab notebook for interactive development.

## Getting Started

Here are the steps to get your development environment ready:

### 1. Setting Up Environment Variables

In order to use the OpenAI API, you need to have an API key which can be obtained from the OpenAI dashboard. Once you have the key, you can set it as an environment variable:

For Unix-based systems (like Ubuntu or MacOS), you can run the following command in your terminal:

```bash
export OPENAI_API_KEY='your-api-key'
```

For Windows, you can use the following command in the Command Prompt:

```
set OPENAI_API_KEY=your-api-key
```

Make sure to replace `'your-api-key'` with your actual OpenAI API key.

### 2. Clone the OpenAI Quickstart Repository

You can clone the OpenAI Quickstart repository to your local machine using the following command:

```bash
git clone https://github.com/DjangoPeng/openai-quickstart.git
```

This will create a directory named 'openai-quickstart' in your current directory.

### 3. Install Jupyter Lab

We will be using Jupyter Lab as our interactive development environment. You can install it using pip:

```bash
pip install jupyterlab
```

### 4. Start Jupyter Lab

Navigate to the 'openai-quickstart' directory and start Jupyter Lab by running the following command:

```bash
cd openai-quickstart
jupyter lab
```

This will start Jupyter Lab and open it in your default web browser.

Now, you are ready to start developing with the OpenAI API!
