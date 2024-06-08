
root_file= "./Day8/BMI.txt"
def bmi_calculator(weight, height):
    return weight / (height * height)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Normal"
    elif bmi >= 25.0 and bmi < 39.9:
        return "Overweight"
    else:
        return "Obese"

def bmi_index(weight, height):
    bmi = bmi_calculator(weight, height)
    category = bmi_category(bmi)
    return bmi, category

def store_bmi_data(filename, name, weight, height, bmi, category):
    try:
        with open(filename, "a") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Weight: {weight} kg\n")
            f.write(f"Height: {height} m\n")
            f.write(f"BMI: {bmi:.2f}\n")
            f.write(f"Category: {category}\n\n")
    except Exception as e:
        print("Error storing data:", e)

def read_bmi_data(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No data found. Please add some BMI records first."

def main_menu():
    print("\n===== BMI Calculator =====")
    print("1. Calculate BMI")
    print("2. View Saved BMI Data")
    print("3. Exit")
    return int(input("Enter your choice: "))

if __name__ == '__main__':
    while True:
        choice = main_menu()
        if choice == 1:
            name = input("Enter your name: ")
            weight = float(input("Enter your weight (in kg): "))
            height = float(input("Enter your height (in m): "))
            bmi, category = bmi_index(weight, height)
            print(f"Your BMI: {bmi:.2f}")
            print(f"Category: {category}")
            store_bmi_data(root_file, name, weight, height, bmi, category)
        elif choice == 2:
            print(read_bmi_data(root_file))
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")