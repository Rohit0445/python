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

#--------------------------------------------------------------- # default constructor ----------------------------------------------
# class student :
#     def __init__(self):
#         print("Constructor is activated ")

# s1 = student()


# =-----------------------------------------------------------# parametarised constructor -------------------------------------------------

# class student1 :
#     college = "cybrom"
#     def __init__(self,name):
#         self.sname = name
#         print(f"welcome {name} from {self.college} ")


# s2 = student1("Rohit")

# s3 = student1("Keshav")
 
# s4 = student1("Ajay")



# --------------------------------------------------------inharitence-----------------------------------------------------------------------

class sbi:

    def withdrawl(self):
        amount=20000
        withdraw=int(input("Enter withdrwal amount : "))
        if(withdraw<=amount):
           print(f"withdwarl succesfull {withdraw}remaining amount {amount-withdraw}")

        else:
            print("not sufficient amount")

    
    def deposit(self):
        amount=20000
        deposit = int(input("Enter deposit amount : "))
        print(f"deposit succesfull total amount{amount+deposit}")

    def balance(self):
        amount= 20000
        print(f"balance{amount}")

    
pin=1234
your_pin=int(input("Enter your pin : "))

if(pin==your_pin):
    operation=input("choose an option from withdraw , deposit, check balance : ")
    s1= sbi()
    if(operation=="withdraw"):
        s1.withdrawl()

    elif(operation=="deposit"):
        s1.deposit()

    elif(operation=="check balance"):
        s1.balance()

else:
    print("incorrect pin")
        



