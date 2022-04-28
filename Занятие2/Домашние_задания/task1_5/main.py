from string import ascii_lowercase, ascii_uppercase, digits
import random


def random_pasw(n):
    pasw_ = ascii_lowercase + ascii_uppercase + digits
    indx = random.randint(n, n)
    yield ''.join(random.choice(pasw_) for x in range(indx))


if __name__ == "__main__":
    # print(next(pasw_func))
    # print(ascii_lowercase)
    # print(ascii_uppercase)
    # print(digits)
    n = 8
    count = 0
    for f in range(n):
        print(next(random_pasw(n)))
        if count >= 4:
            break
