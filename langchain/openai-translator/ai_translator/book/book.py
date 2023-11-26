from .page import Page  # 导入 Page 类，用于添加页面

class Book:
    def __init__(self, pdf_file_path):  # 初始化函数，传入 pdf 文件路径
        self.pdf_file_path = pdf_file_path  # 将 pdf 文件路径存储到实例变量中
        self.pages = []  # 初始化一个空的页面列表

    def add_page(self, page: Page):  # 添加页面的方法，传入一个 Page 类的实例
        self.pages.append(page)  # 将传入的页面实例添加到页面列表中