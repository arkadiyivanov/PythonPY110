
# LIST_FILE_FINAL = 'listfile3.txt'
# LIST_FILE = 'listfile.txt'
# LIST_F ='list_f.txt'
def task():
    places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
    with open('listfile.txt', 'w') as f:
        for listfile in places:
            f.write('%s\n' % listfile)
    f.close()
    # places = ['100', '200', '300', '400']
    # with open('list_f.txt', 'w') as f:
    #     for listitem in places:
    #         f.write('%s\n' % listitem)
    # f.close()
    # LIST_FILE_FINAL = 'listfile3.txt'
    # LIST_FILE = 'listfile.txt'
    # LIST_F ='list_f.txt'
    # with open('listfile3.txt', "w") as listfile3:
    #     with open(LIST_FILE, 'r') as listfile:
    #         for f in listfile:
    #             listfile3.write(f)
    #     with open(LIST_F, 'r') as listfile:
    #         for f in listfile:
    #             listfile3.write(f)
    # listfile3.close()

if __name__ == "__main__":
    task()
    # with open(LIST_FILE_FINAL) as file:
    #     for line in file:
    #         print(line, end="")