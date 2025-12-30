# class new:
#     def __init__(self,x):
#         print(id(x))
#         print("Constructor Called")

# obj = new(10)

# n number of constructor bana sakte hai pr last bala call hota hai automatiacally
# kyunki same name k function overload hota hai jo python support nAHI karta 

# ____________________instance variable-----------------

class info:
    def __init__(self,name,age):
        self.name = name #INSTANCE VARIABLE -------------------- left side ka veriable hota hai right side value 
        self.age = age
        print(name)
        print(age)


obj = info("Rohit",24)
obj1 = info("Ajay",24)