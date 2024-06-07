set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# union() method
set3 = set1.union(set2)
print("Print using union():",set3)
set4 = set1 | set2
print("Print using | operator:",set4)

# Join multiple sets
set5 = set1.union(set2, set3)
print("Print using union() with multiple sets:",set5)

# join set and tuple
set6 = set1.union(("apple", "banana", "cherry"))
print("Print using union() with tuple:",set6)

# join set and list
set7 = set1.union(["apple", "banana", "cherry"])
print("Print using union() with list:",set7)

# using update() method
set1.update(set2)
print("Print using update():",set1)

# using intersection() method
set8 = set1.intersection(set3)
print("Print using intersection():",set8)

# using symmetric_difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
