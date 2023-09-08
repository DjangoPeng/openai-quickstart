from .content import Content  # 导入 Content 类

class Page:
    def __init__(self):
        self.contents = []  # 初始化 contents 列表为空

    def add_content(self, content: Content):
        self.contents.append(content)  # 将 content 添加到 contents 列表中