import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

print(json.loads(json_string))

#Dumps() method

json_dump = json.dumps({"name": "John", "age": 30, "city": "New York"})
print(json_dump)


import pickle

pickle_string = pickle.dumps([1, 2, 3, 4, 5, "a", "b", "c", "d", "e"])
print(pickle_string)
# print(pickle_string), will print a binary string which is not human readable
print(pickle.loads(pickle_string))


import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name]=salary
    salaries_json=json.dumps(salaries)

    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])