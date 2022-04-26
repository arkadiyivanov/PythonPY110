def geom(base: int):
    n = 0
    while True:
        yield base * n
        n += 1


if __name__ == "__main__":
    numbers = geom(10)

    for _ in range(9):
        print(next(numbers))
