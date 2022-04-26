def task() -> list:
    temp_tuple = (0, 36.6, 100)

    return list(map(lambda temp: temp * (9 / 5) + 32, temp_tuple))  # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
