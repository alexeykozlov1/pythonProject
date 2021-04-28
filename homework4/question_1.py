from sys import argv

file, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Salary is ${res}')
except ValueError:
    print('Not a number')
    exit()
