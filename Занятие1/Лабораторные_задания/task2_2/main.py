def task() -> int:
    list_numbers = [8, -8, 5, 5, -4, -7, -1, -3, 4, 8, -8, -3, -3, 4, 5, -5, 1, -7, 3, -2]

    return sum(filter(lambda x: x < 0, list_numbers))  # TODO заменить list comprehension на filter


if __name__ == "__main__":
    print(task())
