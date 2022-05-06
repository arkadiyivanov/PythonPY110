def decorator(some_obj):
    def wrapper(*args, **kwargs):
        print("Смотри, что я получил:", args, kwargs)
        for _ in some_obj:
            raise TypeError("Объект <название или номер позиционного аргумента>"
                            " <значение аргумента> не является итерируемым")




    return wrapper

@decorator
def f(*args, **kwargs):
    return args, kwargs

# Применяем декоратор с параметрами


if __name__ == "__main__":
    # Write your solution here

    f(5)
