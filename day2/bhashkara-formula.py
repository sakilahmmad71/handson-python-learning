import math

a = 2
b = 3
c = 1

x1 = (-b + math.sqrt((b * b) - 4 * a * c)) / 2 * a
x2 = (-b - math.sqrt((b * b) - 4 * a * c)) / 2 * a

z = x1 + x2

print(z)

print(type(z))
