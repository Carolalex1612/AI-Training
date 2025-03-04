def myFun(fruit, veg):
    newDict = {}
    i = 0 
    
    for j in fruit:
    
        newDict[fruit[i]] = veg[i]  
        i = i+1  
    
    print(newDict)
    
myFun(["Apple", "Orange"], ["Carrot", "Beans"])


# def myFun(fruit , veg):
#     newDict = dict(fruit = veg)
#     print(newDict)
    
# myFun (["Apple", "Orange"], ["Carrot", "Beans"])