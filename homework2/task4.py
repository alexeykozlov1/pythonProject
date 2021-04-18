while True:
    var_str = input('Please put some words: ')
    if len(var_str) < 3 or var_str.count(' ') < 1:
        print('Incorrect values')
        continue

    break

for idx, word in enumerate(var_str.split()):
    print(idx + 1, (word, word[:11])[len(word) > 10])
