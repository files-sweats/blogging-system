# main.py
from user import User
from post import Post
from database import Database

# Create users
user1 = User('john_doe', 'john@example.com')
user2 = User('jane_doe', 'jane@example.com')

# Create posts
post1 = Post('First Post', 'This is the content of the first post.', user1)
post2 = Post('Second Post', 'This is the content of the second post.', user2)

# Create a database and add users/posts
database = Database()
database.add_user(user1)
database.add_user(user2)
database.add_post(post1)
database.add_post(post2)

# Display users and posts
print("Users:")
for user in database.get_users():
    print(f"Username: {user.get_username()}, Email: {user.get_email()}")

print("\nPosts:")
for post in database.get_posts():
    print(f"Title: {post.get_title()}")
    print(f"Content: {post.get_content()}")
    print(f"Author: {post.get_author().get_username()}\n")
