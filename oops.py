# class and object 


# class student:      #classs 
#     name = "Rohit"
#     def myfunc(self):
#         print(self.name)


# s1 = student()     #object
# s1.myfunc()  


# class student1 :
#     college = "cybrom"
#     def sdata(self,name):
#         self.sname = name
#         print(f"welcome {name} from {self.college} ")


# s1 = student1()
# s1.sdata("Rohit")

# s2 = student1()
# s2.sdata("Suryansh")

# s3 = student1()
# s3.sdata("keshav")

# default constructor
class student :
    def __init__(self):
        print("Constructor is activated ")

s1 = student()


# parametarised constructor 

class student1 :
    college = "cybrom"
    def __init__(self,name):
        self.sname = name
        print(f"welcome {name} from {self.college} ")


s2 = student1("Rohit")

s3 = student1("Keshav")
 
s4 = student1("Ajay")




