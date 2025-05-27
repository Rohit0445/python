# def hello(): #Declaration
#     print("hello") #statement

# hello() #calling

#non-return without argument

# def factorial():
#     a=int(input("Enter a number : "))
#     ans = 1
#     for i in range(1,a+1):
#         ans*=i
#     print(ans)

# factorial() 

# def sum():
#     num = int (input("Enter a number : "))
#     ans = 0
#     for i in range(1,num+1):
#         ans+=i
#     print(f"sum of n natural numbers is {ans}")

# sum()

# def fibonacci():
#     num1 = int(input("Enter a number : "))
#     a =0
#     b=1
#     next = b
#     count = 1

#     while (count<=num1):
#         print(next, end=" ")
#         count += 1
#         a, b = b, next
#         next = a + b
#     print()

# fibonacci()
#--------------------------------------------------------------------------------------------------------------

#return without argument -------Return ko function bahar bhi use kr sakte hai

# def sum():
#     num1 = int(input("Enter a first number : "))
#     num2 = int(input("Enter a second number : "))

#     return(num1+num2)

# a = sum()
# print(a)

#factorial 

# def factorial():
#     num = int(input("Enter a number : "))
#     ans = 1
#     for i in range (1,num+1):
#         ans*=i
#     return(ans)
    
# a= factorial()
# print(a)

#  using yield keyword i uses for multiple value return in a object form

# def square():
#     for i in range (1,11):
#         yield(i*i)

# a = square()
# for i in a :
#     print(i,end=" ")

#prime number 

# def isprime():
#     num = int (input("Enter a number : "))
#     count = 0
#     for i in range(1,num+1):
#         if(num%i==0):
#             count+=1
#     if (count==2):
#         return("Prime")
#     else:
#         return("not a prime")

# a =isprime()
# print(a)

# b = isprime()
# print(b)

#perfect number 

# def perfectnum():
#     num = int (input("Enter a number : "))
#     sum = 0
#     for i in range(1,num):
#         if(num%i==0):
#             sum+=i
        

#     if(num==sum):
#         return("perfect number")
    
#     else:
#         return("not a perfect number")
    
# x = perfectnum()
# print(x)


#nonreturn type with argument  -------------------------------------------------------------------------------+

# def sum(a,b):  #parametre
#     print(a+b)

# sum(7,8) # argument 

# def sum(a,b):  
#     print(a+b)

# num1 = 12
# num2 = 11
# # sum(num1,num2)

# def perfect_num(num):
#     ans=0
#     for i in range(1,num):
#        if (num%i==0):
#            ans+=i
#     if(ans==num):
#         print("perfect num")

#     else:
#         print("not perfect")



# a = int(input("Enter a number : "))
# perfect_num(a)

# b = int(input("Enter a number : "))
# perfect_num(b)


# while(1):
#     c=int(input("Enter 1 for exit enter 2 for continue : "))
#     if(c==1):
#         break
#     elif(c==2):
#         perfect_num(a)

#-----------------------------------------------------------------------------------------

#  types of arguments
#   
#-----------------------------------------------------------------------------------------


# 1= positinal argument 

# def student(name,rollno):
#     print(f"The name is {name} and the roll no is {rollno}")

# student("rohit",101) 


#-----------------------------------------------------------------------------------------
#default argument perameter k santh ek default value initialize kr denge taki koi argumnet na ho to bbhi funtion chl jae default values k thorugh

# def sum(a=0,b=0):
#     return a+b
# sum()

#-----------------------------------------------------------------------------------------
#variable length multiple arguments de sakte hai 

# def sum(*a):
#     ans=0
#     for i in a:
#        for j in i:
#         ans += j
#     print(ans)

# li=[1,2,3,4,5]
# sum(li)

#-----------------------------------------------------------------------------------------
#keyword variable length

def view_data(**kvarg):
    print(kvarg)

dic = {
    "name" : "rohit",
    "rollno":102,    
    "name1" : "sourav",
    "rollno1":103,   
    "name2" : "ajay",
    "rollno2":104,   
    }

view_data(**dic)


view_data(rollno = 201,rollno1 = 202,rollno3 = 203)
