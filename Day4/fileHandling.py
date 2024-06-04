import os
fileRoot = "./Day4"

def create_file(filename):
    try:
        with open(os.path.join(fileRoot, filename), "w") as file:
            file.write("Hello from File Handling Write.\n")
            file.write("This is the second line.\n")
            file.write("This is the third line.\n")
            print("Data written successfully")
            file.close()
    except Exception as e:
        print("Enter a valid filename. Please try again.")



def read_file(filename):
    try:
        with open(os.path.join(fileRoot, filename), "r") as file:
            for each in file:
                print(each)
            file.close()
    except Exception as e:
        print("File not found. Please try again.")

def append_file(filename ,text):
    try:
        with open(os.path.join(fileRoot, filename), "a") as f:
            print("File: " + filename + " opened successfully" )
            f.write(text)
            print("Data appended successfully")
            f.close()
    except Exception as e:
        print("File not found. Please try again.")


def rename_file(oldname, newname):
    try:
        os.rename(os.path.join(fileRoot, oldname), os.path.join(fileRoot, newname))
        print("File: " + oldname + " renamed to " + newname + " successfully.")
    except Exception as e:
        print("File not found. Please try again.")

def delete_file(filename):
    try:
        os.remove(os.path.join(fileRoot, filename))
        print("File: " + filename + " deleted successfully.")
    except Exception as e:
        print("File not found. Please try again.")


if __name__ == '__main__':
    while True:
        try:
            print("1. Create File")
            print("2. Read File")
            print("3. Append File")
            print("4. Rename File")
            print("5. Delete File")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                filename = input("Enter the filename: ")
                create_file(filename)
            elif choice == 2:
                filename = input("Enter the filename: ")
                read_file(filename)
            elif choice == 3:
                filename = input("Enter the filename: ")
                text = input("Enter the text to append: ")
                append_file(filename, text)
            elif choice == 4:
                oldname = input("Enter the old filename: ")
                newname = input("Enter the new filename: ")
                rename_file(oldname, newname)
            elif choice == 5:
                filename = input("Enter the filename: ")
                delete_file(filename)
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")
                continue
        except Exception as e:
            print("Please enter a valid input. Please try again.")

    print("Thank you for using the program.")

