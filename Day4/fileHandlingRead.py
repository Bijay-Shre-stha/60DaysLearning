#read
file = open("Day4/file.txt", "r")
for each in file:
    print(each)

# read with With statement
# with open("Day4/file.txt", "r") as file:
#     for each in file:
#         print(each)

# read with readline
file = open("Day4/file.txt", "r")
print(file.read(5))

#split
file = open("Day4/file.txt", "r")
data = file.readlines()
for each in data:
    words = each.split()
    print(words)
