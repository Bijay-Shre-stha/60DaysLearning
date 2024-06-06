stack = []
print("Enter the n'th number of value to insert on stack: ")
n = int(input())
for i in range(n):
    print("Enter the value: ")
    stack.append(input())
print("Stack: ", stack)
print("Pop the value from stack: ", stack.pop())
print("Stack: ", stack)
print("Pop the value from stack: ", stack.pop())
print("Stack: ", stack)
stack.append("Hello")
print("Stack: ", stack)