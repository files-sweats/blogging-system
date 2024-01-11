# post.py
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_author(self):
        return self.author
