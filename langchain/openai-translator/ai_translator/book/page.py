# 导入 Content 类，用于创建页面内容
from .content import Content

class Page:
    def __init__(self):
        # 初始化一个空列表，用于存储页面内容
        self.contents = []

    def add_content(self, content: Content):
        # 将传入的内容添加到页面内容列表中
        self.contents.append(content)