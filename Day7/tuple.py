tuple = (1, 2, 3, 4, 5)
print(tuple)

# Tuple with mixed data types
tuple = (1, "Hello", 3.4)
print(tuple)

# Nested tuple
tuple = (1, (2, 3, 4), [5, 6, 7])
print(tuple)

# Duplicate elements
tuple = (1, 2, 3, 4, 1, 2)
print(tuple)

# Length of tuple
tuple = (1, 2, 3, 4, 5)
print(len(tuple))

# Tuple with one element
tuple = (1,)
print(tuple)

# Parentheses are optional
tuple = 1, 2, 3, 4, 5
print(tuple)

# Accessing elements
tuple = (1, 2, 3, 4, 5)
print(tuple[0])
print(tuple[1])
# print(tuple[5]) # IndexError: tuple index out of range
print(tuple[-1])

# Type of tuple
tuple = (1, 2, 3, 4, 5, "Hello")
print(type(tuple))

# Changing tuple elements
# tuple = (1, 2, 3, 4, 5)
# tuple[0] = 10 # TypeError: 'tuple' object does not support item assignment
# print(tuple)

# Adding elements

#1. Converting into a list
# my_tuple = (1, 2, 3, 4, 5)
# my_list = list(my_tuple)
# my_list.append(6)
# my_tuple = tuple(my_list)
# print(my_tuple)

# 2. Adding two tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, )
tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 =(True , False, 1 , 0)
print(" Printing: ", tuple4)

# Removing elements
delete_tuple = ("apple", "banana", "cherry")
del delete_tuple
print("Tuple deleted successfully")


# unpacking tuple
my_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = my_tuple
print(a)
print(d)
print(e)

# using * to catch multiple values
fruits = ("apple", "banana", "cherry", "kiwi", "strawberry", "raspberry")

(*green, yellow, red, blue) = fruits

print(green)
print(yellow)
print(red)


# Loop through a tuple
my_tuple = (1, 2, 3, 4, 5)
for i in my_tuple:
    print(i)

# Loop through the index numbers
my_tuple = (1, 2, 3, 4, 5)
for i in range (len(my_tuple)):
    print("Indexing: ", my_tuple[i])


# Multiplying tuples
tuple = (1, 2, 3, 4, 5)
new_tuple = tuple * 2
print(new_tuple)

# count() method
tuple = (1, 2, 3, 4, 1, 2, 1)
print(tuple.count(1))

# index() method
tuple = (1, 2, 3, 4, 1, 2, 1)
print("Printing index value: ",tuple.index(3)) 