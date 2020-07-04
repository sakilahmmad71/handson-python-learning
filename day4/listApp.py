myList = []

myList.append('Bangladesh')
myList.append('America')
myList.append('Norway')
myList.append('Uruguye')
myList.append('Uganda')
myList.append('Barishal')
myList.append('Noakhali')

print(myList)

myList.insert(4, 'Canada')

myList[6] = "Barishailla Barishal"

print(myList)

myList.pop()

print(len(myList))

myList.remove("Uganda")

print(myList)

if "Bangladesh" in myList :
    country = "My country {} is beautiful"
    print(country.format(myList[myList.index("Bangladesh")]))
else:
    print("This is not my country")

myList.reverse()

print(myList)

myList.sort()

print(myList)