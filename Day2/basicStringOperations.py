string_I= "Hello world!"
string_II= 'Hello world!'

double_quote_string= "Hello world!"
print("Single quotes are ''")
print(len(double_quote_string))

# Indexing
print(double_quote_string.index("o"))
# Count
print(double_quote_string.count("l"))
# Slicing
print(double_quote_string[3:7])
# Slicing with step
print(double_quote_string[:7])
# Slicing with step
print(double_quote_string[3:])
# Slicing with step [start:stop:step]
print(double_quote_string[3:7:2])
# Reverse string
print(double_quote_string[::-1])
# Uppercase
print(double_quote_string.upper())
# Lowercase
print(double_quote_string.lower())
# Startswith
print(double_quote_string.startswith("Hello"))
# Endswith
print(double_quote_string.endswith("John!"))
# Split
print(double_quote_string.split("l"))
# Join
print(":".join(double_quote_string))
# Replace
print(double_quote_string.replace("world", "John"))
# Strip
print("    Hello world!    ".strip())
# Lstrip
print("    Hello world! ".lstrip())
# Rstrip
print(" Hello world!    ".rstrip())
# Find
print(double_quote_string.find("world"))
# Center
print(double_quote_string.center(20, "*"))
# Ljust
print(double_quote_string.ljust(20, "*"))
# Rjust
print(double_quote_string.rjust(20, "*"))
# Title
print(double_quote_string.title())
# Capitalize
print(double_quote_string.capitalize())
# Swapcase
print(double_quote_string.swapcase())
# Isalnum
isalnum_string= "Hello123"
print(isalnum_string.isalnum())
print(double_quote_string.isalnum())
# Isalpha
isalpha_string= "Hello"
print(isalpha_string.isalpha())
print(double_quote_string.isalpha())

#Triple quotes
triple_quote_string= """Hello"""
print(triple_quote_string)