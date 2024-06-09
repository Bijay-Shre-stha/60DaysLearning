a = 1
b = 2
sum = lambda x,y :x+y
print(sum(a,b))


l = [2,4,7,3,14,19]
for i in l:
    odd = lambda x: x%2!=0
    print(odd(i))

def function(x):
    return lambda y: x*y

double = function(2)
print(double(11))
