from .content import Content

class Page:
    def __init__(self):
        self.contents = []

    def add_content(self, content: Content):
        self.contents.append(content)
    
    def sort_contents(self):
        self.contents.sort(key=lambda content: content.coordinates[1])
