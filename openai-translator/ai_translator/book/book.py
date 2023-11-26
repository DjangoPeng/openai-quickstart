from .page import Page  # 导入 Page 类

class Book:  # 定义 Book 类
    def __init__(self, pdf_file_path):  # 定义构造函数，传入 pdf 文件路径
        self.pdf_file_path = pdf_file_path  # 将 pdf 文件路径赋值给实例变量
        self.pages = []  # 初始化页面列表

    def add_page(self, page: Page):  # 定义添加页面方法，传入 Page 类型的参数
        self.pages.append(page)  # 将页面添加到页面列表中