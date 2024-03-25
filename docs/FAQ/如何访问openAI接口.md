# 如何访问openAI接口
本文只提供学习用.商用请使用正规国内代理, 代理商提供的服务

## 解法1. 使用国内代理api
使用国内代理api即可. 将域名替换即可. api.openai.com -> api.openai-proxy.com
风险提示: 由于是第三方代理, 因此可以作为测试学习用. !!!不要作为生产用以防key被盗用!!!!!!

```python
client = OpenAI(
  base_url='https://api.openai-proxy.com/v1'
)
```

## 解法2. 自购代理, 使用socks5代理
第二种: 已购买代理的socks5代理
设置为全局代理可以直接使用, 如果不是设置为全局代理, 查看你代理的端口, 诸如18080

先安装库
```bash
pip install PySocks
```

在代码开头设置socks5代理
```python
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 18080)
socket.socket = socks.socksocket
```



