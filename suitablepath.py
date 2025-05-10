# num = int(input("Enter a nmber : "))

# if(num==1):
#     next = int(input("enter your next destination from 2,3 and 4"))  

#     if(next==2):
#         next = int(input("enter your next destination from 3 and 4")) 
 
#         if(next==3):
#             next = int(input("enter your next destination is 4")) 

#             if(next==4):
#                 print("reached")

#             else:
#                 print("Invalid") 

#         elif(next==4):
#             print("reached") 
 

#     elif(next==3):
#         next = int(input("enter your next destination form 2 and 4")) 

#         if(next==2):
#             next = int(input("enter your next destination is  4")) 

#             if(next==4):
#                 print("reached")

#             else:
#                 print("Invalid") 

        
#         elif(next==4):
#             print("reached")

#         else:
#             print("Invalid")    

#     elif(next==4):
#         print("reached")

#     else:
#         print("Invalid input")    


# else:
#     print("Invalid")    

#-------------------------------------------------------------Q1-ATM ------------------------------------------------------------------------------------

card = input("Enter your card is from which bank").lower()
balance=10000

if(card == "sbi"):
    password=1234
    pin = int(input("Enter your pin : "))

    if(pin==password):
        print("choose one of them Withdraw , Deposit , Balance")
        opption = input("Enter what would you choose : ").lower()

        if(opption=="withdraw"):
            amount=int(input("Enter withdraw Amount" ))
            if(amount>0 and amount<=balance):
                print("withdraw succesfull")
                balance -= amount
                print(balance , "Remaining balance")
            else:
                print("Not sufficient balance")   
            

        elif(opption=="deposit"):
            
            amount=int(input("Enter  deposit Amount" ))
            if(amount>0):
               balance += amount
               print(balance , "Your balance ")
            
            else:
                print("you gave the negative value ")
                print("your balance is " , balance)
            

        elif(opption=="balance"):
            print(balance)

        else:
            print("Invalid input")


    else:
        print("Invalid PIN")

else:
    print("INvalid Company Card")


#------------------------------------------------------- Q2 = email / password ------------------------------------------------------------------


# email = "student@gmail.com"
# password = 1234

# mail = input("Enter your Email : ").lower()


# if(email == mail):
#    pin = int(input("Enter Your password"))
#    if(pin==password):
#       print("correct")
    
#    else:
#       print("Invalid password")

# else:
#    print("Invalid Email ")


#--------------------------------------Q3 = mobile ---------------------------------------------------------------------------------------------


# brand = input("Enter which company mobile you want : ").lower()

# if(brand == "realme"):
#     print("we have realme13 and realme 14")
#     model = input("Enter which model you want : ").lower()
#     if(model == "realme13"):
#         print( "price of this model is 25000")

#     elif(model == "realme14"):
#         print( "price of this model is 30000")

#     else:
#         print("not available")    


# elif(brand == "iphone"):
#     print("we have iphone14 and iphone 15")
#     model = input("Enter which model you want : ").lower()
#     if(model == "iphone14"):
#         print( "price of this model is 70000")

#     elif(model == "iphone15"):
#         print( "price of this model is 80000")

#     else:
#         print("not available")

# elif(brand == "oneplus"):
#     print("we have oneplusnode2 and oneplusnode3")
#     model = input("Enter which model you want : ").lower()
#     if(model == "oneplusnode2"):
#         print( "price of this model is 35000")

#     elif(model == "oneplusnode3"):
#         print( "price of this model is 30000")

#     else:
#         print("not available")

# else:
#     print("Not Available")            