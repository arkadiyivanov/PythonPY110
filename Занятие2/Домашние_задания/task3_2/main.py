import functools
def decorator(*args):
    def wrapper(*args):
        if args== int:
            print("Аргументы являются INT")
    return wrapper

@decorator
def f(*args):
    args
    print(f)
# Применяем декоратор с параметрами


if __name__ == "__main__":
    # Write your solution here
    pass
