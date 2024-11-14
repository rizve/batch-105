def my_func(num):
    if num[-1].lower() == 'k':
        return int(float(num[:-1]) * 1000)
    elif num[-1].lower() == 'm':
        return int(float(num[:-1]) * 1000000)
    elif num[-1].lower() == 'b':
        return int(float(num[:-1]) * 1000000000)
    else:
        return int(num)

# print(my_func('100K'))

def my_func_2(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * my_func(num-2)

# print(my_func(4))