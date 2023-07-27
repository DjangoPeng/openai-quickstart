import os
import openai
import gradio as gr
import logging
import tiktoken
import ast

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 代理地址后面需要加 /v1
openai.api_base = os.getenv("OPENAI_PROXY")
openai.api_key = os.getenv("OPENAI_API_KEY")


def ui():
    from theme.winter import Winter
    with gr.Blocks(title="OpenAI Models Study", theme=Winter()) as interface:
        gr.Markdown('''# <span style='color:brown'>OpenAI Models Study</span> ''')
        with gr.Tab(label="对话"):
            api_key = gr.Textbox(label="APIKey", placeholder="请输入API Key", value=openai.api_key)
            api_proxy = gr.Textbox(label="OpenAI代理地址（可选）", placeholder="请输入OpenAI代理地址")

            with gr.Row():
                model_button = gr.Button(value="获取模型", variant='primary')
                model_options = gr.Dropdown(value="gpt-3.5-turbo", label="模型", info="注意所选模型是否支持所选API类型",
                                            interactive=True)
                api_type_options = gr.Dropdown(choices=["/v1/completions", "/v1/chat/completions"],
                                               value="/v1/chat/completions", label="API类型",
                                               info="注意所选模型是否支持所选API类型", interactive=True)
                model_button.click(get_models, inputs=[api_key, api_proxy], outputs=model_options)
            with gr.Row():
                tokens = gr.Textbox(label="Token数量", placeholder="请输入最大Token", value=100)
                temperature = gr.Textbox(label="Temperature", placeholder="请输入Temperature", value=0.5)
            with gr.Row():
                chatbot = gr.Chatbot(label="开启对话吧！")
            with gr.Row():
                with gr.Column():
                    user_input = gr.Textbox(label="请输入要对话的内容", lines=13)
                with gr.Column():
                    identity = gr.Dropdown(choices=["user", "system", "assistant"], value="user", label="对话身份",
                                           info="注意只有API类型为 /v1/chat/completions 时起作用",
                                           interactive=True, visible=True)
                    chat_button = gr.Button(value="发送对话", variant='primary')
                    clear_button = gr.ClearButton(value="清空对话内容", components=[user_input, chatbot])

            completions_history_msg = gr.State([])
            chat_completions_history_msg = gr.State([])
            chat_button.click(chat,
                              inputs=[user_input, completions_history_msg, chat_completions_history_msg, api_key,
                                      api_proxy, model_options, api_type_options, tokens,
                                      temperature, identity],
                              outputs=[chatbot, completions_history_msg, chat_completions_history_msg, user_input])
            clear_button.click(clear_history_msg, inputs=[],
                               outputs=[completions_history_msg, chat_completions_history_msg])
            api_type_options.change(identity_visible, inputs=api_type_options, outputs=identity)
        with gr.Tab(label="模型信息"):
            model_info_button = gr.Button(value="获取选中模型的信息", variant='primary')
            model_info = gr.Json(label="模型信息")
            model_info_button.click(get_model_info, inputs=[api_key, api_proxy, model_options], outputs=model_info)
        with gr.Tab(label="Token计算"):
            gr.Markdown('''## <span style='color:#999966'>注意：将通过当前选中的模型来动态计算模型对应的编码器</span> ''')
            model_encoding = gr.HTML(label="当前模型的分词器")
            encoding_len = gr.HTML(label="计算结果")
            text = gr.Textbox(label="请输入要计算token的内容", lines=15)
            with gr.Row():
                token_result = gr.Textbox(label="Token计算结果", info="计算结果将展示在开头（Token长度）", lines=10)
                token_result_to_text = gr.Textbox(label="Token转文本结果", info="将当前Token计算结果转为文本（Token）", lines=10)
            with gr.Row():
                cal_token_button = gr.Button(value="计算Token", variant='primary')
                token_result_to_text_button = gr.Button(value="还原文本")
            cal_token_button.click(cal_token, inputs=[text, model_options], outputs=[model_encoding, encoding_len, token_result])
            token_result_to_text_button.click(token_result_to_text_fun, inputs=[token_result, model_options], outputs=token_result_to_text)
        interface.queue(max_size=8).launch()


# 将Token计算结果还原为文本
def token_result_to_text_fun(token_result, model):
    encoding = tiktoken.encoding_for_model(model_name=model)
    decode_result = encoding.decode(ast.literal_eval(token_result))
    return decode_result


# 计算token
def cal_token(text, model):
    encoding = tiktoken.encoding_for_model(model_name=model)
    logger.info(f'获取到模型 {model} 对应的编码器：{encoding}')
    encoding_result = encoding.encode(text)
    token_len = len(encoding_result)
    logger.info(f'Token计算：长度：{token_len}，结果：{encoding_result}')
    model_encoding_html = f'''<h2 style='color:#99CCFF'>当前模型编码器：{encoding.name}</h2>'''
    encoding_len_html = f'''<h2 style='color:#669966'>Token长度：{token_len}</h2>'''
    return model_encoding_html, encoding_len_html, encoding_result


# 清除对话内容（包括历史内容）
def clear_history_msg():
    return [], []


# 控制API类型下拉框的可见性
def identity_visible(api_type):
    if api_type == '/v1/completions':
        return gr.Dropdown.update(choices=["user", "system", "assistant"], value="user", label="对话身份",
                                  info="注意只有API类型为 /v1/chat/completions 时起作用",
                                  interactive=True, visible=False)
    else:
        return gr.Dropdown.update(choices=["user", "system", "assistant"], value="user", label="对话身份",
                                  info="注意只有API类型为 /v1/chat/completions 时起作用",
                                  interactive=True, visible=True)


# 对话核心逻辑
def chat(msg, completions_history_msg, chat_completions_history_msg, api_key, api_proxy, model, api_type, tokens,
         temperature, identity):
    tokens = int(tokens)
    temperature = float(temperature)
    if api_proxy:
        openai.api_base = api_proxy
        logger.info(f'OpenAI代理地址：{api_proxy}')
    if not api_key:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        logger.info(f'从系统中获取到 api_key：{api_key}')
    else:
        openai.api_key = api_key

    if not openai.api_key:
        raise gr.Error("api_key 不能为空！")

    if not model:
        raise gr.Error("请选择一个模型！")

    if api_type == '/v1/completions':
        response = openai.Completion.create(model=model, prompt=msg, max_tokens=tokens, temperature=temperature)
        logger.info(f'接收到ChatGPT消息：{response}')
        chat_data = ''
        for chat_result in response['choices']:
            chat_data += chat_result['text']
        completions_history_msg.append((msg, chat_data))
    elif api_type == '/v1/chat/completions':
        chat_completions_history_msg.append({
            "role": identity,
            "content": msg
        })

        response = openai.ChatCompletion.create(model=model, messages=chat_completions_history_msg)
        logger.info(f'接收到ChatGPT消息：{response}')
        chat_data = ''
        for chat_result in response['choices']:
            chat_completions_history_msg.append(chat_result['message'])
            chat_data += chat_result['message']['content']
        completions_history_msg.append((msg, chat_data))

    return completions_history_msg, completions_history_msg, chat_completions_history_msg, ""


# 获取指定模型信息
def get_model_info(api_key, api_proxy, model):
    if not api_proxy:
        openai.api_base = os.getenv("OPENAI_PROXY")
        logger.info(f'从系统中获取到 api_proxy：{api_proxy}')
    else:
        openai.api_base = api_proxy

    if not api_key:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        logger.info(f'从系统中获取到 api_key：{api_key}')
    else:
        openai.api_key = api_key

    if not openai.api_key:
        raise gr.Error("api_key 不能为空！")

    if not model:
        raise gr.Error("请选择一个模型！")

    # 获取模型信息
    model_info = openai.Model.retrieve(model)
    logger.info(f'模型信息：{type(model_info)},{model_info}')
    return model_info


# 获取模型列表
def get_models(api_key, api_proxy):
    if api_proxy:
        openai.api_base = api_proxy
        logger.info(f'OpenAI代理地址：{api_proxy}')
    if not api_key:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        logger.info(f'从系统中获取到 api_key：{api_key}')
    else:
        openai.api_key = api_key

    if not openai.api_key:
        raise gr.Error("api_key 不能为空！")

    # 获取模型列表
    models = openai.Model.list()
    model_list = [model['id'] for model in models['data']]
    logger.info(f'获取到模型：{model_list}')
    # 更新模型下拉框中的值
    return gr.Dropdown.update(choices=model_list)


if __name__ == '__main__':
    ui()
