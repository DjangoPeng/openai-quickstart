# OpenAI Quickstart

![GitHub stars](https://img.shields.io/github/stars/DjangoPeng/openai-quickstart?style=social)
![GitHub forks](https://img.shields.io/github/forks/DjangoPeng/openai-quickstart?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/DjangoPeng/openai-quickstart?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/DjangoPeng/openai-quickstart)
![GitHub language count](https://img.shields.io/github/languages/count/DjangoPeng/openai-quickstart)
![GitHub top language](https://img.shields.io/github/languages/top/DjangoPeng/openai-quickstart)
![GitHub last commit](https://img.shields.io/github/last-commit/DjangoPeng/openai-quickstart?color=red)
![GitHub last commit](https://img.shields.io/github/last-commit/DjangoPeng/openai-quickstart?color=red)

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


## Course Schedule

For the complete documentation, please refer to the [Quick Start Guide for Large Language Models (LLMs) Application Development - Course Outline](docs/schedule.md#schedule)


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated. If you have any suggestions or feature requests, please open an issue first to discuss what you would like to change.

<a href='https://github.com/repo-reviews/repo-reviews.github.io/blob/main/create.md' target="_blank"><img alt='Github' src='https://img.shields.io/badge/review_me-100000?style=flat&logo=Github&logoColor=white&labelColor=888888&color=555555'/></a>

## License

This project is licensed under the terms of the Apache-2.0 License . See the [LICENSE](LICENSE) file for details.

## Contact

Django Peng - pjt73651@email.com

Project Link: https://github.com/DjangoPeng/openai-quickstart

## Star History

<a href="https://star-history.com/#DjangoPeng/openai-quickstart&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=DjangoPeng/openai-quickstart&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=DjangoPeng/openai-quickstart&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=DjangoPeng/openai-quickstart&type=Date" />
  </picture>
</a>