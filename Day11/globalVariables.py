x = "Global Variable"

def fun():
    print("Printing "+ x)

fun()

# #modify the global variable
x = "Modified Global Variable"
fun()
# Global Variable
# The function will print the global variable x
# Now we will modify the global variable x
def fun():
    global x
    x = "Modified Global Variable"
    print("Printing "+ x)


