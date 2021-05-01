def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Input numbers \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in file')
    except ValueError:
        print('Incorrect number')


summary()
