squares = []
for i in range(10):
    squares.append(i**2)
print("Squares: ", squares)

# The above code snippet can be written in a single line using list comprehension as follows:

print("Using list comprehension: ")
squares = [i**2 for i in range(10)]
print("Squares: ", squares)

# using clauses in list comprehension
# List comprehensions can contain multiple clauses:

evenNumbers = [i for i in range(20) if i % 2 == 0]
print("Even numbers: ", evenNumbers)

combs = []
for x in [1,2,3]:
    for y in [4,5,6]:
        if x != y:
            combs.append((x,y))
print("Combinations: ", combs)
