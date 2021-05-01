my_file = open(r"/Users/alexeykozlov/PycharmProjects/pythonProject/lesson5/data.txt", "w")
if my_file.writable():
    my_file.write("Update\n")

    strings = ["Alex\n", "Sveta\n"]
    my_file.writelines(strings)
else:
    print("Can not write")

my_file.close()
