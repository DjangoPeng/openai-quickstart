# OpenAI 快速入门指南

<p align="center">
    <br> <a href="README.md">English</a> | 中文
</p>

本项目旨在指导你进行使用 OpenAI API 的应用开发的初始步骤。它将帮助你设置开发环境，理解如何使用API，并为你提供一个用于交互式开发的Jupyter Lab记事本。

## 开始使用

这里是让你的开发环境做好准备的步骤：

### 1. 设置环境变量

为了使用OpenAI API，你需要从OpenAI控制台获取一个API密钥。一旦你有了密钥，你可以将其设置为环境变量：

对于基于Unix的系统（如Ubuntu或MacOS），你可以在终端中运行以下命令：

```bash
export OPENAI_API_KEY='你的-api-key'
```

对于Windows，你可以在命令提示符中使用以下命令：

```bash
set OPENAI_API_KEY=你的-api-key
```

请确保将`'你的-api-key'`替换为你的实际OpenAI API密钥。

### 2. 克隆OpenAI快速入门存储库

你可以使用以下命令将OpenAI快速入门存储库克隆到你的本地机器上：

```bash
git clone https://github.com/DjangoPeng/openai-quickstart.git
```

这将在你的当前目录下创建一个名为'openai-quickstart'的目录。

### 3. 安装Jupyter Lab

我们将使用Jupyter Lab作为我们的交互式开发环境。你可以使用pip进行安装：

```bash
pip install jupyterlab
```

### 4. 启动Jupyter Lab

导航到'openai-quickstart'目录并通过运行以下命令启动Jupyter Lab：

```bash
cd openai-quickstart
jupyter lab
```

这将启动Jupyter Lab并在你的默认网络浏览器中打开它。

现在，你已经准备好开始使用OpenAI API进行开发了！
