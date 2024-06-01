list = []
list.append(1)
list.append(2)
list.append(3)
print(list[0])
print(list[1])
print(list[2])

for x in list:
    print("This is from the list:", x)

stringList=[]
stringList.append("Hello")
stringList.append("World")
print(stringList[0])
print(stringList[1])

for x in stringList:
    print("This is from the stringList:", x)
    

#Nested List
nestedList = []
nestedList.append([1,2,3])
nestedList.append([4,5,6])

print(nestedList[0])
print(nestedList[1])

for x in nestedList:
    print("This is from the nestedList:", x)
    for y in x:
        print("This is from the nestedList:", y)
