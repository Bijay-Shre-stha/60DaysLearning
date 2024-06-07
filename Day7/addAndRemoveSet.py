set1 ={1,2,3,4,5}
set2 = {4,5,6,7,8}

#loop through set1
for x in set1:
    print(x)
    

# Add items
set1.add(6)
print(set1)

# Add sets
fruit = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruit.update(tropical)

print(fruit)

# Add any iterable
myListSet= [1,2,3]
fruit.update(myListSet)
print(fruit)

# Remove items
fruit.remove("banana")
print(fruit)

# Discard items
fruit.discard("banana")
print(fruit)

# Pop items
x = fruit.pop()
print(x)
print(fruit)

# Clear items
clear = fruit.clear()
print(clear)
print(fruit)

# Delete items
del fruit

