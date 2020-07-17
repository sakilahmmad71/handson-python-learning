

# def sqare(n): return n * 2


# newArray = [sqare(number) for number in numbers]

# print(newArray)


numbers = [2, 4, 6, 8, 12]

newNumbers = map(lambda n: n * 2, numbers)

print(list(newNumbers))
