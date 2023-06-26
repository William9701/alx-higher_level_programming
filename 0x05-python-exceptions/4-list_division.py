#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    b = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
        except IndexError:
            print('out of range')
            x = 0

        try:
            y = my_list_2[i]
        except IndexError:
            print('out of range')
            y = 0

        try:
            result = x / y
        except TypeError:
            print('wrong type')
            result = 0
        except ZeroDivisionError:
            print('division by 0')
            result = 0
        finally:
            b.append(result)

    return b
