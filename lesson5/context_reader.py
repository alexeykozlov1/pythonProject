with open("data.txt") as my_file:
    print(my_file.read())

print(type(my_file))
# print(my_file.read())

#  Exception Handler

try:
    with open('data.txt')as file:
        print(file.read())
except IOError:
    print("Some error")
