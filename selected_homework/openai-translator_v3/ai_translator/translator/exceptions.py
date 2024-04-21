class PageOutOfRangeException(Exception):
    def __init__(self, book_pages, requested_pages):
        self.book_pages = book_pages
        self.requested_pages = requested_pages
        super().__init__(f"Page out of range: Book has {book_pages} pages, but {requested_pages} pages were requested.")
