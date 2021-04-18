raiting = []

while True:
    item = input('Put some number: ')
    if not item.isdigit():
        print("Incorrect values")
        continue
    else:
        item = int(item)

    index = None

    for i, num in enumerate(raiting):
        if item > num:
            index = i
            break

    if index is None:
        raiting.append(item)
    else:
        raiting.insert(index, item)

    print(raiting)

    q = input('Did you finished? (y/N)) ')
    if q.lower() == 'y':
        break
