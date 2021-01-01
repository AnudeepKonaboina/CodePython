# context manager

class ContextManager:
    def __init__(self):
        print("constructor")

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


if __name__ == '__main__':
    with ContextManager() as c:
        print("within context manager block")
