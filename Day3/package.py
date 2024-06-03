import re

find_members = []
print(dir(re))
for member in dir(re):
    if 'find' in member:
        find_members.append(member)
print(find_members)