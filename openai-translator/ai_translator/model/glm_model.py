import requests
import simplejson

from model import Model

class GLMModel(Model):
    def __init__(self, model_url: str, timeout: int):
        self.model_url = model_url
        self.timeout = timeout

    def make_request(self, prompt):
        try:
            payload = {
                "prompt": prompt,
                "history": []
            }
            response = requests.post(self.model_url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            response_dict = response.json()
            translation = response_dict["response"]
            return translation, True
        except requests.exceptions.RequestException as e:
            raise Exception(f"请求异常：{e}")
        except requests.exceptions.Timeout as e:
            raise Exception(f"请求超时：{e}")
        except simplejson.errors.JSONDecodeError as e:
            raise Exception("Error: response is not valid JSON format.")
        except Exception as e:
            raise Exception(f"发生了未知错误：{e}")
        return "", False
