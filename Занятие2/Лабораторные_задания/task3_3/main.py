def header_footer(fn):
    def wrapper():
        print("========")
        fn()
        print("========")
    return wrapper()# TODO написать декоратор



@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
