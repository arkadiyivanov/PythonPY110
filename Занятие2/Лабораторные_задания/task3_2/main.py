def min_len_check(fn):
    def wrapper(str_arg):
        if len(str_arg) < 10:
            raise ValueError("Строка слишком короткая")# TODO записать обертку для исходной функции

    return wrapper


@min_len_check# TODO задекорировать функцию
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
