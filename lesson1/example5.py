max_count = int(input("Max number >>> "))
delimeter = int(input("Number for deletion >>> "))

current_count = 0

while True:
    if current_count == max_count:
        break

    current_count += 1

    if current_count % delimeter == 0:
        continue

    print(current_count)
