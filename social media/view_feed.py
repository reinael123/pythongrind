from users import users

def view_feed():
    try:
        username = input("Enter your username: ")
        if username not in users:
            print("Username already exists")
            return
        
        posts = users[username]["posts"]
        if not posts:
            print("Your feed is empty")
        else:
            print("Your feed:")
            for i, posts in enumerate(posts):
                print(f"{i+1}. {posts}")
    except Exception as e:
        print(f"An error occurred: {e}")