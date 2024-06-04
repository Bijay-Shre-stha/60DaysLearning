file = open ("Day4/writeFile.txt", "w")
if file:
    print("File is opened")
    file.write("Hello from File Handling Write.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")
    print("Data written successfully")
else:
    print("File is not opened")
file.close()