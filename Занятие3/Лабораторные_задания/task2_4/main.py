import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)# TODO считать содержимое JSON файла

    gen_exr = (item["contains_improvement_appeals"]  for item in json_data) # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
