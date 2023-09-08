# 定义一个名为PageOutOfRangeException的异常类
class PageOutOfRangeException(Exception):
    # 定义构造函数，接收两个参数：book_pages和requested_pages
    def __init__(self, book_pages, requested_pages):
        # 将book_pages参数赋值给self.book_pages属性
        self.book_pages = book_pages
        # 将requested_pages参数赋值给self.requested_pages属性
        self.requested_pages = requested_pages
        # 调用父类的构造函数，传入异常信息字符串
        super().__init__(f"Page out of range: Book has {book_pages} pages, but {requested_pages} pages were requested.")