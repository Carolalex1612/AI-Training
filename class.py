name = ["Carol", "Sherly"]
age = [30, 25]
namedict = dict(zip(name, age))
print(namedict)

class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def names(self):
        print("Hello " + self.name)
    
    def add_to_dict(self, dict_obj):
        dict_obj[self.name] = self.age

x = myclass("Alex", 35)  
x.names()
x.add_to_dict(namedict)
print(namedict)











# name = ["Carol","Sherly"]
# age = [30,25]
# namedict = dict(zip(name,age))
# print(namedict)

# class myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def names(self):
#         print("Hello"+self.name)

# x= myclass("Alex",35)
# x.names()

