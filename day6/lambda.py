def myfunc(n):
    return lambda a: lambda b: n * a * b


print(myfunc(5)(7)(2))
