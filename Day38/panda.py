import pandas as pd

data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'location': ['New York', 'Paris', 'Berlin', 'London'],
    'age': [24, 13, 53, 33]
}

data_pandas = pd.DataFrame(data)
print(data_pandas)

