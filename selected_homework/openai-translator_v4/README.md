### 作业需求
基于 ChatGLM2-6B 实现带图形化界面的 openai-translator

### 作业总结
+ [openai_api_demo](openai_api_demo)

利用的chatGLM中的api_demo进行调整为server项，故没有采用ChatGLM2-6b，而是ChatGLM3-6b

运行起来需要：
1. git clone https://www.modelscope.cn/ZhipuAI/chatglm3-6b.git
2. 确保机器有足够的资源【俺没有。。。故暂未实现。。。】

+ [ai_translator](ai_translator)

将历史的 
from langchain_openai import ChatOpenAI 
替换为
from langchain.llms import ChatGLM
并针对ChatGLM做参数匹配
