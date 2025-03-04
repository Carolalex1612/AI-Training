x = ("apple", "banana", "cherry", "Kivi", "banana")
y = list(x)
y.insert(2, "apple")

unique = set()
duplicate = set()
seen = set()

for i in y:
    if i in seen:

        duplicate.add(i)
        if i in unique:
            unique.remove(i)
    else:
        seen.add(i)
        unique.add(i)

fruits = {
    "unique": unique,
    "duplicate": duplicate
}

print(fruits)
