import configparser
import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_bot(message):
    """
    :param message: eg: {"role": "system", "content": "you are a translation assistant"})
    :return: eg: {"role": "assistant", "content": "...."})
    """
    # ChatCompletion
    conversation_3 = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message,
        max_tokens=50,
        temperature=0.2,
    )
    answer = conversation_3['choices'][0]["message"]
    new_message_dict = {"role": answer.role, "content": answer.content}
    print(answer.content)
    return new_message_dict


def start_chat():
    """
    第一次开始会话时：需要给一个role
    后面每次会话时将前面的内容加载到message里（后面可以优化，如何控制那些内容需要加载进去）
    :return:
    """
    message = []
    start = 0
    while True:
        if not start:
            content = input("首次开始会话，请定义角色以及简单描述：如：翻译助手，请帮我将下面的内容翻译成中文\nbot: ")
            message.append({"role": "system", "content": content})
        else:
            content = input("user: ")
            message.append({"role": "user", "content": content})
        if content == 'q':
            break
        # print('message:',message) # 可以看到每次输入的message
        res = chat_with_bot(message)
        message.append(res)
        start += 1


if __name__ == '__main__':
    start_chat()
