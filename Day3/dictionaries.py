phoneBook1= {}
phoneBook1["John"] = 938477566
phoneBook1["Jack"] = 938377264
phoneBook1["Jill"] = 947662781
print(phoneBook1)

#Alternatively, a dictionary can be initialized with the same values in the following notation:
# phoneBook2 = {
    # "John" : 938477566,
    # "Jack" : 938377264,
    # "Jill" : 947662781
# }
# print(phoneBook2)

# Iterating over a dictionary
for name , number in phoneBook1.items():
    print("Phone number of",name)

# Removing a value
del phoneBook1["John"]
print(phoneBook1)

# Updating a dictionary
# phoneBook1["Jake"] = 938273443
# print(phoneBook1)

# Exercise

# phoneBook = {  
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }  
# # your code goes here
# phoneBook["Jake"] = 938273443
# del phoneBook["Jill"]

# # testing code
# if "Jake" in phoneBook:  
#     print("Jake is listed in the phoneBook.")
    
# if "Jill" not in phoneBook:      
#     print("Jill is not listed in the phoneBook.")