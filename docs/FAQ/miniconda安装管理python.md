# 说明
本文介绍如何安装miniconda
并且基于miniconda安装python环境

# 官方介绍
https://docs.anaconda.com/free/miniconda/
## windows安装
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe
```
## mac安装
```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

```
安装完毕之后, 以下命令针对 bash 和 zsh shell 进行初始化
```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
## linux安装
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
安装完毕之后, 以下命令针对 bash 和 zsh shell 进行初始化
```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```


# 使用MiniConda管理python环境
- 安装python3.10.13
假设我需要有一个环境叫myenv(你也可以叫其他名字), 并且指定python版本为3.10.13
```bash
conda create --name myenv python=3.10.13
```

- 激活环境, 并安装依赖文件requirement.txt
```bash
conda activate myenv
pip install -r requirements.txt
```
ps: 如果遇到下载超时或者失败, 更换源
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 解除激活环境
```bash
conda deactivate
```

- 删除环境
```bash
conda remove --name myenv --all
```





