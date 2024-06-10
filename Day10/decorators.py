def multiply(multiplier):
    def multiply_generator(old_fun):
        def new_fun(*args, **kwargs):
            return multiplier * old_fun(*args, **kwargs)
        return new_fun
    return multiply_generator  # it returns the new generator function

@multiply(9) # multiply(9) returns multiply_generator function

def return_num(num):
    return num # return_num is passed to multiply_generator function

print(return_num(3))  

def type_check(correct_type):
    def check(old_fun):
        def new_fun(arg):
            if isinstance(arg, correct_type):
                return old_fun(arg)
            else:
                print ("Bad Type")
        return new_fun
    return check


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])