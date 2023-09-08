import openai  # 导入 OpenAI API
import requests  # 导入 requests 库，用于发送 HTTP 请求
import simplejson  # 导入 simplejson 库，用于处理 JSON 数据
import time  # 导入 time 库，用于处理时间

from model import Model  # # 导入Model类，用于继承
from utils import LOG  # 导入自定义的 LOG 函数，用于日志记录

# 继承 Model 类，实现 OpenAIModel
class OpenAIModel(Model):
    # 初始化函数，传入模型名称和 API 密钥
    def __init__(self, model: str, api_key: str):
        self.model = model
        openai.api_key = api_key

    # 发送请求函数，传入请求的 prompt，返回翻译结果和是否成功的标志
    def make_request(self, prompt):
        attempts = 0
        while attempts < 3:
            try:
                # 如果模型是 gpt-3.5-turbo，则使用 openai.ChatCompletion.create() 方法
                if self.model == "gpt-3.5-turbo":
                    response = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role": "user", "content": prompt}
                        ]
                    )
                    # 获取 response 中的翻译结果
                    translation = response.choices[0].message['content'].strip()
                # 如果模型不是 gpt-3.5-turbo，则使用 openai.Completion.create() 方法
                else:
                    response = openai.Completion.create(
                        model=self.model,
                        prompt=prompt,
                        max_tokens=150,
                        temperature=0
                    )
                    # 获取 response 中的翻译结果
                    translation = response.choices[0].text.strip()

                return translation, True
            # 捕获openai.error.RateLimitError异常
            except openai.error.RateLimitError:
                attempts += 1
                # 如果尝试次数小于3，则等待60秒后重试
                if attempts < 3:
                    LOG.warning("Rate limit reached. Waiting for 60 seconds before retrying.")
                    time.sleep(60)
                # 如果尝试次数大于等于3，则抛出异常
                else:
                    raise Exception("Rate limit reached. Maximum attempts exceeded.")
            # 如果请求异常，则抛出异常
            except requests.exceptions.RequestException as e:
                raise Exception(f"请求异常：{e}")
            # 如果请求超时，则抛出异常
            except requests.exceptions.Timeout as e:
                raise Exception(f"请求超时：{e}")
            # 如果 response 不是 JSON 格式，则抛出异常
            except simplejson.errors.JSONDecodeError as e:
                raise Exception("Error: response is not valid JSON format.")
            # 如果发生未知错误，则抛出异常
            except Exception as e:
                raise Exception(f"发生了未知错误：{e}")
        return "", False