from my_functions import my_pow


def my_func(x, y):

    if x < 0:
        raise ValueError('incorrect x')

    if int(y) != float(y) or y >= 0:
        raise ValueError('incorrect y')

    return my_pow(x, y)


if __name__ == '__main__':
    try:
        print(my_func(2, -4))
    except (ValueError, TypeError) as e:
        print(e)
