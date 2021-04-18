my_int = 2
my_float = 2.2
my_str = "dfdfgdfgd"
my_list = ['a', '4']
my_tuple = ('b', '7')
my_dict = {'address': '140 Main St', 'phone': '123456789'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')