with open('data.txt', 'w') as printik:
    strings = ["Alex", "Sveta"]
    for names in strings:
        print(names, file=printik)
