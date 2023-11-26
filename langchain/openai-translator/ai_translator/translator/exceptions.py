# 一个异常类，用于处理获取页数超出范围的情况
class PageOutOfRangeException(Exception):
    def __init__(self, book_pages, requested_pages):
        self.book_pages = book_pages  # 书籍总页数
        self.requested_pages = requested_pages  # 请求的页数
        super().__init__(f"Page out of range: Book has {book_pages} pages, but {requested_pages} pages were requested.")