a = [1, 5, 7, 4, "Apple"]
b = [{"fruit": "Apple"}, {"Veg": "Carrot"}]
c = "Apple"
result = []
unique = []
d = False

for item in a:
    result.append(item)
    if item == c:
        d = True

e = False
for item in b:
    for value in item.values():
        result.append(value)
        if c in item.values():
            e = True

# print(result)
if d and e:
    for item in result:
        if item != c:
            unique.append(item)
            results = set(unique)
        # elif item == c:
        #     print()
    
    print(results)
else:
    print(c)

