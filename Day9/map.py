numbers = [1,2,3,4,5,6,7,8,9,10]

mapResult = list(map(lambda x: x*2, numbers))

print(mapResult)


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
circle_result = list(map(round, circle_areas, range(1,3)))
print(circle_result)

#zip function
a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
zipResult = list(zip(a,b))
print(zipResult)

#custom zip function
strings = ['a', 'b', 'c', 'd']
numbers = [1,2,3,4]
custom_zip=map(lambda x,y: (x,y), strings, numbers)
print(list(custom_zip))