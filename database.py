# database.py
class Database:
    def __init__(self):
        self.users = []
        self.posts = []

    def add_user(self, user):
        self.users.append(user)

    def add_post(self, post):
        self.posts.append(post)

    def get_users(self):
        return self.users

    def get_posts(self):
        return self.posts
