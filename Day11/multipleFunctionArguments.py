def test(first, second, third, *the_rest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(the_rest)))

test(1, 2, 3, 4, 5)

def bar(first,second, third, **options):
    if options.get("action")=="sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number")=="first":
        return first
    
result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" %(result))


# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7



# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")