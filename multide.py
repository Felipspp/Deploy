def multide(num:int):
    if num % 5 == 0 and num % 7 == 0:
        return 1
    elif num % 5 == 0:
        return 2
    elif num % 7 == 0:
        return 3
    else:
        return 4
