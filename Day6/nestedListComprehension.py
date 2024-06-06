matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]	,
]
#without using list comprehension
print("Without using list comprehension: ", [[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range (4):
    transposed.append([row[i] for row in matrix])
print("Using list comprehension: ", transposed)
