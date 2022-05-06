
def decorator(f):
    def wrapper(*args):
        print("Смотри, что я получил:", *args)
        if type(*args) is int:
            print('Позиционный аргумент является типом int')
        if type(*args) is not int:
            print("Позиционный аргумент не является int")
    return wrapper

@decorator
def f(*args):
    return args

# Применяем декоратор с параметрами


if __name__ == "__main__":
    # Write your solution here

    f(2000)