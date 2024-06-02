numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
print("\n")


#xrange is not available in Python 3
# for i in xrange(5):

#range
print("After ranges: \n")
for numbers in range(5):
    print(numbers)
print("\n")
#range with start and end
print("After ranges with start and end: \n")
for numbers in range(1, 5):
    print(numbers)
print("\n")

#range with start, end and step
print("After ranges with start, end and step: \n")
for numbers in range(1, 10, 2):
    print(numbers)
print("\n")


#while loop
print("After while loop: \n")
count = 0
while count < 5:
    print(count)
    count += 1
print("\n")

#break
print("After break: \n")
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
print("\n")

#continue
print("After continue: \n")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
print("\n")

#continue using for loop
print("After continue using for loop: \n")
for count in range(5):
    if count % 2 != 0:
        continue
    print(count)

