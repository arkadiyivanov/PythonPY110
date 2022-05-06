
def task():
    places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
    with open('listfile.txt', 'x') as filehandle:
        for listitem in places:
            filehandle.write('%s\n' % listitem)
    filehandle.close()
    places = ['100', '200', '300', '400']
    with open('list_f.txt', 'x') as f:
        for listitem in places:
            f.write('%s\n' % listitem)
    f.close()
def task_3():
    with open(listfile, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            for upper_line in map(str.upper, input_file):
                output_file.write(upper_line)

if __name__ == "__main__":



