
LIST_FILE_FINAL = 'listfile3.txt'
LIST_FILE = 'listfile.txt'
LIST_F ='list_f.txt'
def task():
    data = ['Ivanov', 'Petrov', 'Sidorov', 'Smirnov']
    with open('listfile.txt', 'w') as f:
        for listfile in data:
            f.write('%s' ' ' % listfile)
    f.close()


    data_2 = ['400000$', '54800000$', '1000000$', '155415$']
    with open('list_f.txt', 'w') as f:
        for list_f in data_2:
            f.write('%s'' ' % list_f)
    f.close()

    with open('listfile3.txt', "w") as listfile3:
        with open(LIST_FILE, 'r') as listfile:
            for f in listfile:
                listfile3.write(f)
        with open(LIST_F, 'r') as listfile:
            for f in listfile:
                listfile3.write(f)
    listfile3.close()

if __name__ == "__main__":
    task()
    with open(LIST_FILE_FINAL) as file:
        for line in file:
            print(line, end='')