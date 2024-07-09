dict = {}

dict[1] = 10
dict.setdefault(1, 0)

print(dict)

for key, value in dict.items():
    print(type(key))