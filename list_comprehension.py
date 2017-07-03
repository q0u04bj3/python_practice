def fun(begin, end):
    return sum([x ** 2 if x % 2 == 1 else -x ** 2 for x in range(begin, end)])