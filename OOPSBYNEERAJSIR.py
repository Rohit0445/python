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

# class Student :
#     def __init__(self,name):
#         self.n = name   #decleration of instance variable
    
#     def addnow(self,age):
#         self.a = age   #decleration

#     def show(self):
#         print(self.n,self.a,self.city)  #calling

# obj = Student('Rohit')

# obj.addnow(24)

# obj.city='bhopal'  #decleration

# obj.show()  


# print(obj.n,obj.a,obj.city)    #calling 


# ============================Static Veriable ==================


# class Student :
#     school = 'SHSS'

#     def __init__(self,name):
#         self.n = name   #decleration of instance variable
#         Student.gread = "10th"


    
#     def addnew(self):
#         Student.principal= 'python'   #decleration

#     def show(self):
#         print(Student.school,Student.gread,Student.principal)  

# Student.city = 'bhopal'

# obj = Student('Rohit')

# obj.addnew() 
# obj.show() 
# print(f'name = {obj.n}, School = {obj.school} , city = {obj.city}, class = {obj.gread} , principal = {obj.principal}')



#============================local Variable==================

# class Student :
#     school = 'SSRHSS'
#     def __init__(self):
#         x = 10

#     def new(self):
#         print(x) # x is not defined beacause x is a loccal variable 

# obj = Student()
# obj.new()


#---------------------------------------   METHODS   ----------------------------------------------

class Student:
    school = "SAKET SHISHU RRANJAN HIGHER SECONDARY SCHOOL VIDISHA"
    greade = "12th"

    def __init__(self,name):
        self.n=name

    @classmethod 
    def update(cls,x,y):   #update class Variable or create new variable
        cls.greade=x
        cls.principle=y

obj = Student('Rohit')
print(obj.greade)

obj.update('10th','RAGINI PANDEY') #update class Variable or create new variable
print(obj.greade)
print(obj.principle)

print(obj.school)
print(obj.n)

 