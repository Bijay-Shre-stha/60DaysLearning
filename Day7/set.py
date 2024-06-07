set_1 = {1,"Hello",3,4,5,1}
print(set_1)

thisSet = {"apple", "banana", "cherry", True, 1, 2,0, False}
print(thisSet)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

print("Length of set1: ", len(set1))
print("Length of set2: ", len(set2))
print("Length of set3: ", len(set3))

print("Type of set1: ", type(set1))

set4 = set(("apple", "banana", "cherry"))
print(set4)

# Access items
set5 = set(("apple", "banana", "cherry", "apple", "banana", "cherry"))
for x in set5:
    print(x)

# Check if item exists
print("banana" in set5)

# If not exits
print("banana" not in set5)