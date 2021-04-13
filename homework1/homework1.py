# # 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите
# # у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

peremennaya_odin = "Hello World!"
print(peremennaya_odin)
peremennaya_dva = 2
print(peremennaya_dva)

zapros_peremmennogo_chisla_odin = int(input("Please put the integer >>> "))
zapros_peremmennoi_stroki = input("Please provide the String >>>")
print("{} {}".format(zapros_peremmennoi_stroki, zapros_peremmennogo_chisla_odin))

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Please put the amount of seconds >>> "))
minutes = seconds // 60
hours = minutes // 60
print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

chislo_n = input("Please put the value of N >>> ")
chislo_n = int(chislo_n) + int((chislo_n + chislo_n)) + int((chislo_n + chislo_n + chislo_n))

print(chislo_n)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
chislo = int(input("Please put the number >>> "))
result = 0
while chislo > 0:
    c = chislo % 10
    if c >= result:
        result = c
    chislo //= 10
print(result)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
#                                                                         или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = int(input("Please put the total income here >>> "))
credit = int(input("Please put the total credit here >>> "))

if income > credit:
    hr = int(input("Please put the total number of people >>> "))
    total = income - credit
    print("Firm gained ${}".format(total))
    total = total / hr
    print("Income per person ${}".format(total))

else:
    total = credit - income
    print("Firm lost ${}".format(total))

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_day = int(input("Please put km for the first day >>> "))
check_day = int(input("Please put km for the check day >>> "))

counter_days = 1
print("{}st day: {}".format(counter_days, first_day))

while first_day < check_day:
    first_day = (first_day / 10) + first_day
    counter_days += 1
    print("{}th day: {}".format(counter_days, first_day))
