import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]

    word_pattern = re.compile(r"\w+")  # TODO записать регулярное выражение для поиска слова любой длин

    for word in word_list:
        print(word_pattern.search(word).group())  # TODO вызвать от регулярного выражения методы search и group


if __name__ == "__main__":
    task()
