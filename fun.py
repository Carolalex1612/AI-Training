color = ["red", "blue", "deep blue","green","olive green"]
def findcolor(col,fun=None):
    newcolor = []
    for x in color:
        if fun == "==":
            if col == x:
                newcolor.append(x)
        elif fun == "!=":
            if col != x:
                newcolor.append(x)
        elif fun == "":
            if col.lower() in x.lower():
                newcolor.append(x)
        else:
            return "Invalid operator"
    return newcolor
print(findcolor(input("Enter the color:"),input("Enter function:")))
