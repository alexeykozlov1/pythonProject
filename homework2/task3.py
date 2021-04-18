seasons_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]

seasons_dict = {
    'Winter': ['12', '1', '2'],
    'Spring': ['3', '4', '5'],
    'Summer': ['6', '7', '8'],
    'Autumn': ['9', '10', '11']
}

while True:
    month_number = input('Number of month: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Incorrect number')
        continue

    break

for season, months in seasons_list:
    if month_number in months:
        print(f'The number {month_number} is {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'The number {month_number} is {season}')
