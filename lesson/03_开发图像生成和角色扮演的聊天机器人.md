[streamlit](https://streamlit.io/)是一个开源Python库，可以轻松创建和共享用于机器学习和数据科学的漂亮的自定义web应用程序。即使开发者不擅长前端开发，也能快速的构建一个比较漂亮的页面。

`characterglm_api_demo_streamlit.py`展示了一个具备图像生成和角色扮演能力的聊天机器人。它用`streamlit`构建了界面，调用CogView API实现文生图，调用CharacterGLM API实现角色扮演。执行下列命令可启动demo，其中`--server.address 127.0.0.1`是可选参数。
```bash
streamlit run --server.address 127.0.0.1 characterglm_api_demo_streamlit.py
```

作业3：改进代码，为文生图功能加上风格选项，在页面上加上一个可指定图片风格的选项框。
