def div(*args):

    try:
        arg1 = int(input("Input one"))
        arg2 = int(input("Input two "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong"

    return res


print(f'result  {div()}')