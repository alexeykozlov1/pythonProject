from itertools import count

for el in count(int(input('Beginning number '))):
    # forever loop
    print(el)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    # forever loop
    print(el)
