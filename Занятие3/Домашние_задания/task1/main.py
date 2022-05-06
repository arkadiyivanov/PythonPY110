
def task():
    places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
    with open('listfile.txt', 'x') as listfile1:
        for listitem in places:
            f.write('%s\n' % listitem)
    listfile1.close()
    places = ['100', '200', '300', '400']
    with open('list_f.txt', 'x') as f:
        for listitem in places:
            f.write('%s\n' % listitem)
    f.close()
    LIST_FILE = 'listfile.txt'
    LIST_F ='list_f.txt'
    with open('listfile3.txt', "x") as listfile3:
        with open(LIST_FILE, 'r') as listfile:
            for f in listfile:
                listfile3.write(f)
        with open(LIST_F, 'r') as listfile:
            for f in listfile:
                listfile3.write(f)

    listfile3.close()
if __name__ == "__main__":
     task()



