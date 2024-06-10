# def transmit_to_space(message):
#     "This is to transmit the space for the messages!"
#     def data_transmitter():
#         "The data transmitter! A nested function!"
#         print(message)
#     return data_transmitter
#     # data_transmitter()

# print(transmit_to_space("Test message!"))

# Here, the data_transmitter() function is a closure. The nested function data_transmitter() can access the non-local variable message. Therefore, the message variable is remembered even after the outer function transmit_to_space() has finished executing.

# using nonlocal keyword
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)
print_msg(9)

def transmit_to_space(message):
    "This is the enclosing function!"
    def data_transmitter():
        "The nested function!"
        print(message)
    return data_transmitter
# Here, we have a closure data_transmitter() that takes a message and returns a function. The returned function can be assigned to another variable. This variable can be called to invoke the nested function within it.

fun2 = transmit_to_space("Burn the Sun!")
fun2()

def multiplier_of(n):
    def multiply(x):
        return x*n
    return multiply
multiplywith5 = multiplier_of(5)
print(multiplywith5(9))