my_file = open(r"data.txt", "r")

# for line in my_file.readlines():
#     print(line.replace("\n", ""))

print(my_file.closed)
print(my_file.mode)
print(my_file.name)

for data in my_file.read(1024):
    print(data)

# print(my_file.tell())
# my_file.seek(0, 0)
# print(my_file.tell())
#
# print(my_file.read(18))

my_file.close()
