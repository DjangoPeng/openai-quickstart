import requests
import time
import os
from typing import Generator

import jwt

from data_types import TextMsg, ImageMsg, TextMsgList, MsgList, CharacterMeta


# 智谱开放平台API key，参考 https://open.bigmodel.cn/usercenter/apikeys
os.environ["API_KEY"] = "04559ca20c345d282e76d07238d03ad9.PfCA5xBWPWBGHnzY"
API_KEY: str = os.getenv("API_KEY", "c175ae7f0ba6a73eb22e4ec0cddcdcc9.55fbjTiX2iacE9wG")


class ApiKeyNotSet(ValueError):
    pass


def verify_api_key_not_empty():
    if not API_KEY:
        raise ApiKeyNotSet


def generate_token(apikey: str, exp_seconds: int) -> str:
    # reference: https://open.bigmodel.cn/dev/api#nosdk
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)
 
    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }
 
    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )


def get_characterglm_response(messages: TextMsgList, meta: CharacterMeta) -> Generator[str, None, None]:
    """ 通过http调用characterglm """
    # Reference: https://open.bigmodel.cn/dev/api#characterglm
    verify_api_key_not_empty()
    url = "https://open.bigmodel.cn/api/paas/v3/model-api/charglm-3/sse-invoke"
    resp = requests.post(
        url,
        headers={"Authorization": generate_token(API_KEY, 1800)},
        json=dict(
            model="charglm-3",
            meta=meta,
            prompt=messages,
            incremental=True)
    )
    resp.raise_for_status()
    
    # 解析响应（非官方实现）
    sep = b':'
    last_event = None
    for line in resp.iter_lines():
        if not line or line.startswith(sep):
            continue
        field, value = line.split(sep, maxsplit=1)
        if field == b'event':
            last_event = value
        elif field == b'data' and last_event == b'add':
            yield value.decode()


def get_characterglm_response_via_sdk(messages: TextMsgList, meta: CharacterMeta) -> Generator[str, None, None]:
    """ 通过旧版sdk调用characterglm """
    # 与get_characterglm_response等价
    # Reference: https://open.bigmodel.cn/dev/api#characterglm
    # 需要安装旧版sdk，zhipuai==1.0.7
    import zhipuai
    verify_api_key_not_empty()
    zhipuai.api_key = API_KEY
    response = zhipuai.model_api.sse_invoke(
        model="charglm-3",
        meta= meta,
        prompt= messages,
        incremental=True
    )
    for event in response.events():
        if event.event == 'add':
            yield event.data


def get_chatglm_response_via_sdk(messages: TextMsgList) -> Generator[str, None, None]:
    """ 通过sdk调用chatglm """
    # reference: https://open.bigmodel.cn/dev/api#glm-3-turbo  `GLM-3-Turbo`相关内容
    # 需要安装新版zhipuai
    from zhipuai import ZhipuAI
    verify_api_key_not_empty()
    client = ZhipuAI(api_key=API_KEY) # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-3-turbo",  # 填写需要调用的模型名称
        messages=messages,
        stream=True,
    )
    for chunk in response:
        yield chunk.choices[0].delta.content


def generate_role_appearance(role_profile: str) -> Generator[str, None, None]:
    """ 用chatglm生成角色的外貌描写 """
    
    instruction = f"""
请从下列文本中，抽取人物的外貌描写。若文本中不包含外貌描写，请你推测人物的性别、年龄，并生成一段外貌描写。要求：
1. 只生成外貌描写，不要生成任何多余的内容。
2. 外貌描写不能包含敏感词，人物形象需得体。
3. 尽量用短语描写，而不是完整的句子。
4. 不要超过50字

文本：
{role_profile}
"""
    return get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
    )


def generate_chat_scene_prompt(messages: TextMsgList, meta: CharacterMeta) -> Generator[str, None, None]:
    """ 调用chatglm生成cogview的prompt，描写对话场景 """
    instruction = f"""
阅读下面的角色人设与对话，生成一段文字描写场景。

{meta['bot_name_1']}的人设：
{meta['bot_info_1']}
    """.strip()
    
    if meta["bot_info_2"]:
        instruction += f"""

{meta["bot_name_2"]}的人设：
{meta["bot_info_2"]}
""".rstrip()

    if messages:
        instruction += "\n\n对话：" + '\n'.join((meta['bot_name_1'] if msg['role'] == "user_1" else meta['bot_name_2']) + '：' + msg['content'].strip() for msg in messages)
    
    instruction += """
    
要求如下：
1. 只生成场景描写，不要生成任何多余的内容
2. 描写不能包含敏感词，人物形象需得体
3. 尽量用短语描写，而不是完整的句子
4. 不要超过50字
""".rstrip()
    print(instruction)
    
    return get_chatglm_response_via_sdk(
        messages=[
            {
                "role": "user",
                "content": instruction.strip()
            }
        ]
    )


def generate_cogview_image(prompt: str) -> str:
    """ 调用cogview生成图片，返回url """
    # reference: https://open.bigmodel.cn/dev/api#cogview
    from zhipuai import ZhipuAI
    client = ZhipuAI(api_key=API_KEY) # 请填写您自己的APIKey
    
    response = client.images.generations(
        model="cogview-3", #填写需要调用的模型名称
        prompt=prompt
    )
    return response.data[0].url

