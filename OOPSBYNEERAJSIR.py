# class A:
#     pass
# print(id(A))

# obj = A()
 
# print(id(obj))

# print(dir(A))


# ---------------------------------------------------------Constructor--------------------------------------------


# class A :  
#     def __init__(self):
#         print(id(self))  #address of self
#         print("Constructor Called")

 
# obj = A()
# print(id(A))    #address of class
# print(id(obj)) #address of object


# class student :
#     def  __init__(self,name,age,city):
#         self.n=name
#         self.a=age
#         self.c=city

# obj = student('rohit',24,'vidisha')

# print(obj.n,obj.a,obj.c,sep=',')


# -----------------------------example of instance variable or class vareable----------=----------

# class student:
#     school = 'SHSS'
#     principal = 'python'

#     def __init__(self,name,age,city):
#         self.n=name
#         self.a=age 
#         self.c=city

# obj1 = student('rohit',24,'vidisha')        
# obj2 = student('rohit',24,'vidisha')
# obj3 = student('rohit',24,'vidisha')

# print(id (obj1),id (obj2))
# print(id (obj1.n),id (obj2.n),id(obj3.n))
# print(obj1.school, obj2.school)



# class student:
#     school = 'SHSS'
#     principal = 'python'

#     def __init__(self,name,age,city):
#         self.n=name
#         self.a=age 
#         self.c=city

# obj1 = student('rohit',24,'vidisha')        
# obj2 = student('ajay',25,'narmadapuram')
# obj3 = student('vijay',23,'bhopal')

# print(obj1.n,obj2.n,obj3.n,sep=',')
# print(obj1.a,obj2.a,obj3.a,sep=',')
# print(obj1.c,obj2.c,obj3.c,sep=',')

# print(obj1.school, obj2.school)



# ============================instence Veriable ==================

class Student :
    def __init__(self,name):
        self.n = name   #decleration of instance variable
    
    def addnow(self,age):
        self.a = age   #decleration

    def show(self):
        print(self.n,self.a,self.city)  #calling

obj = Student('Rohit')

obj.addnow(24)

obj.city='bhopal'  #decleration

obj.show()  


print(obj.n,obj.a,obj.city)    #calling 





