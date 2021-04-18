products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Item title: ')
        if not tmp.isalnum():
            print('Empty, Please put some value')
            continue

        title = tmp

    if price is None:
        tmp = input('Price: ')
        if not tmp.isdigit():
            print('The price should be an integer')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Amount: ')
        if not tmp.isdigit():
            print('Amount should be an integer')
            continue

        amount = int(tmp)

    tmp = input('Measurement: ')
    if not tmp.isalpha():
        print('Measurement should not be empty')
        continue

    unit = tmp

    products.append((
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Finished? (Y/N)) ')
    if q.lower() == 'y':
        break

analyze = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    analyze['title'].append(item['title'])
    analyze['price'].append(item['price'])
    analyze['amount'].append(item['amount'])
    analyze['unit'].add(item['unit'])

print(analyze)
