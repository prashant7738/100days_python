# *args takes unlimited argument as tuples meanwhile **kwargs takes unlimited args as dictionary

def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum


print(add(2,3,4,5))