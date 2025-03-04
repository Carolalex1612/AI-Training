x = ("apple","banana","cherry","Kivi","apple")
y = list(x)
y.insert(2,"apple")
y.append("papaya")
print(y)
 
b = []
a = []
for i in y:  
    if i in a:
        b.append(i)
        # a.remove(i)
        print("The B list has:",b)     
    else:        
        a.append(i)
        print("The A list has:",a)
# print(a)
# print(b)
fruits = dict(unique = set(a), duplicate = set(b))
print(fruits)