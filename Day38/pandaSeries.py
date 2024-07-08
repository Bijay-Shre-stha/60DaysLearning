import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
print(a)

# printing first value
print(a[0])

# creating labels
b = ([1, 2, 3, 4, 5])
labels = pd.Series(b,['a', 'b', 'c', 'd', 'e'])
print(labels)

# key/values Objects
print('\n');
calories = {"day1": 420, "day2": 380, "day3": 390}
calories_series = pd.Series(calories)
print(calories_series)

# Accessing elements using index
print("\n")
indexCalories = pd.Series(calories, index=["day1", "day2"])
print(indexCalories)
