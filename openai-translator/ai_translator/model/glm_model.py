import requests  # 导入requests库，用于发送HTTP请求
import simplejson  # 导入simplejson库，用于处理JSON格式数据

from model import Model  # 导入Model类，用于继承

class GLMModel(Model):  # 定义GLMModel类，继承Model类
    def __init__(self, model_url: str, timeout: int):  # 定义构造函数，传入模型URL和超时时间
        self.model_url = model_url  # 将模型URL赋值给实例变量model_url
        self.timeout = timeout  # 将超时时间赋值给实例变量timeout

    def make_request(self, prompt):  # 定义make_request方法，传入prompt参数,返回翻译结果和是否成功的标志
        try:  # 尝试执行以下代码
            payload = {  # 定义payload字典，包含prompt和history两个键值对
                "prompt": prompt,  # 将prompt参数赋值给payload字典的prompt键
                "history": []  # 将空列表赋值给payload字典的history键
            }
            # 发送POST请求，传入模型URL、payload字典和超时时间，将响应赋值给response变量
            response = requests.post(self.model_url, json=payload, timeout=self.timeout)
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
            response_dict = response.json()  # 将响应的JSON格式数据转换为Python字典，赋值给response_dict变量
            translation = response_dict["response"]  # 从response_dict字典中获取response键对应的值，赋值给translation变量
            return translation, True  # 返回translation和True
        except requests.exceptions.RequestException as e:  # 如果发生requests库的异常，将异常信息赋值给e变量
            raise Exception(f"请求异常：{e}")  # 抛出异常，提示请求异常
        except requests.exceptions.Timeout as e:  # 如果发生请求超时异常，将异常信息赋值给e变量
            raise Exception(f"请求超时：{e}")  # 抛出异常，提示请求超时
        except simplejson.errors.JSONDecodeError as e:  # 如果响应数据不是正确的JSON格式，将异常信息赋值给e变量
            raise Exception("Error: response is not valid JSON format.")  # 抛出异常，提示响应数据不是正确的JSON格式
        except Exception as e:  # 如果发生其他异常，将异常信息赋值给e变量
            raise Exception(f"发生了未知错误：{e}")  # 抛出异常，提示发生了未知错误
        return "", False  # 如果没有返回translation和True，返回空字符串和False