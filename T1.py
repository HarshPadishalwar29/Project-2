# T1.py
def greet(name):
    """Function to greet the user"""
    return f"Hello, {name}! Welcome to Python programming."

if __name__ == "__main__":
    user_name = input("Can you please tell your name: ")
    print(greet(user_name))
