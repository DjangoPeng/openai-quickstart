# 定义一个类，来给python做反射
import requests


class WeatherHandler:
    GAODE_API = "08e9348f9e3eb90b535fe556158c2c6d"
    @staticmethod
    def get_current_weather(city_code):
        url = f"https://restapi.amap.com/v3/weather/weatherInfo?key={WeatherHandler.GAODE_API}&city={city_code}&extensions=all"
        response = requests.get(url)
        # print(response.json())
        return response.json()


import json
import openai
import requests
from tenacity import retry, wait_random_exponential, stop_after_attempt
from termcolor import colored

GPT_MODEL = "gpt-3.5-turbo"


def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "function": "magenta",
    }

    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(f"assistant[function_call]: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(f"assistant[content]: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "function":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))


@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, functions=None, function_call=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + "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"
    }

    json_data = {"model": model, "messages": messages}

    if functions is not None:
        json_data.update({"functions": functions})

    if function_call is not None:
        json_data.update({"function_call": function_call})

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        # execute_function_call 可以直接作用在这里 这样外层就不需要处理了
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

# # 定义一个函数chat_completion_api，通过 OpenAI Python 库调用 Chat Completions API
# @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
# def chat_completion_request(messages, functions=None, function_call=None, model=GPT_MODEL):
#     try:
#         openai.api_key = "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"
#         if functions != None:
#             data = openai.ChatCompletion.create(
#               model=model,
#               messages = messages,
#               functions = functions,
#             )
#             new_message = data.choices[0].message
#             result_message = {"role": new_message.role, "content": new_message.content,"function_call":json.loads(str(new_message.function_call))}
#         else:
#             data = openai.ChatCompletion.create(
#               model=model,
#               messages = messages,
#             )
#             new_message = data.choices[0].message
#             result_message ={"role": new_message.role, "content": new_message.content}
#
#         return result_message
#     # 如果发送请求或处理响应时出现异常，打印异常信息并返回
#     except Exception as e:
#         print("Unable to generate ChatCompletion response")
#         print(f"Exception: {e}")
#         return e

# 第一个字典定义了一个名为"get_current_weather"的功能
functions = [
    {
        "name": "get_current_weather",  # 功能的名称
        "description": "Get the current weather",  # 功能的描述
        "parameters": {  # 定义该功能需要的参数
            "type": "object",
            "properties": {  # 参数的属性
                "city_code": {  # 地点参数
                    "type": "string",  # 参数类型为字符串
                    "description": "The city code, e.g. 110000",  # 参数的描述
                },
            },
            "required": ["city_code"],  # 该功能需要的必要参数
        },
    }
]


def execute_function_call(message):
    # 这里先打印一下， 因为当GPT响应可以调用对应的function的时候，日志中会有体现，这个时候我们就可以通过解析role为function，来获取函数名称和参数， 进而就可以使用python的反射方式来屌用function
    # 这里解析最新的返回中有function call时， 就可以调用反射了
    # message = response.json()["choices"][0]["message"]
    if message['role'] == "assistant" and message.get("function_call"):
        function_name = message["function_call"]["name"]
        function_arguments = json.loads(message["function_call"]["arguments"])
        function = getattr(WeatherHandler, function_name, function_arguments.keys())
        if function and callable(function):
            result = function(**function_arguments)
            return result
    else:
        return ""

if __name__ == "__main__":
    # 定义一个空列表messages，用于存储聊天的内容
    messages = []

    # 使用append方法向messages列表添加一条系统角色的消息
    messages.append({
        "role": "system",  # 消息的角色是"system"
        "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."
        # 消息的内容
    })
    messages.append({
        "role": "system",  # 消息的角色是"system"
        "content": "format weather info like date: {date}\n weather: {weather}"  # 消息的内容
    })
    messages.append({
        "role": "system",  # 消息的角色是"system"
        "content": "when user give a place name, can get the city code from data/citycode.xlsx"  # 消息的内容
    })
    messages.append({
        "role": "user",  # 消息的角色是"user"
        "content": "I'm in Beijing, China. what's the weather today?"  # 用户的消息内容
    })

    # 使用定义的chat_completion_request函数发起一个请求，传入messages和functions作为参数
    chat_response = chat_completion_request(
        messages, functions=functions
    )
    assistant_message = chat_response.json()["choices"][0]["message"]
    messages.append(assistant_message)

    if assistant_message.get("function_call"):
        results = execute_function_call(assistant_message)
        # 将功能的结果作为一个功能角色的消息添加到消息列表中
        messages.append({"role": "function", "name": assistant_message["function_call"]["name"], "content": str(results)})

    chat_response = chat_completion_request(
        messages, functions=functions
    )

    assistant_message = chat_response.json()["choices"][0]["message"]
    messages.append(assistant_message)
    pretty_print_conversation(messages)




