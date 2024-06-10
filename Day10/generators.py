import random

def random_generator():
    for i in range(6):
        yield random.randint(1, 10)
for random_number in random_generator():
    print( "Random number: ", random_number)


# fill in this function
def fib():
    a,b=0,1
    while True:
        yield a
        a,b =b,a+b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break