# 1.	Write a  program to find maximum between two numbers.
# a = 10
# b= 20

# if(a>b):
#     print("a is maximum")

# else:
#     print("b is maximum")
#-------------------------------------------------------------------------
# 2.	Write a  program to find maximum between three numbers.

# a = 10
# b= 40
# c =30

# if(a> (b and c)):
#     print("a is maximum")

# elif(b>(a and c)):
#     print("b is maximum")

# else:
#     print("c is maximum")

#---------------------------------------------------------------------------------------------
# 3.	Write a  program to check whether a number is negative, positive or zero.
# num = int (input("Enter a number : "))

# if(num > 0):
#     print("number is Positive")


# elif(num < 0):
#     print("number is Negative")

# else:
#     print("Number is Zero")

#---------------------------------------------------------------------------------------------------
# 4.	Write a program to check whether a number is divisible by 5 and 11 or not.
# num = int (input("Enter a number : "))

# if(num%5==0 and num%11==0):
#     print("number is Divisible by 5 and 11")

# else: 
#     print("number is not Divisible by 5 and 11")

#-----------------------------------------------------------------------------------------
# 5.	Write a  program to check whether a number is even or odd.
# num = int (input("Enter a number : "))

# if(num%2==0 ):
#     print("number is Even")

# else: 
#     print("number is Odd")
#-----------------------------------------------------------------------------------------
# 6.	Write a  program to check whether a year is leap year or not.
# year = int(input("Enter a year: "))

# if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#     print(year , "is a leap year.")

# else:
#     print(year ,"is not a leap year.")
#-----------------------------------------------------------------------------------------------
# 7.	Write a program to check whether a character is alphabet or not.

# char = input("Enter any character : ")
# check = char.isalpha()

# if(check==True):
#     print("this is an Alphabet")

# else:
#     print("This is not an alphabet")
#--------------------------------------------------------------------------------------------------------
# 8.	Write a  program to input any alphabet and check whether it is vowel or consonant.

#alpha= input("Enter a Alphabet : ")
#vowel = ["a","e","i","o","u"]

#if (alpha in vowel):
#    print("vowel")

#else:
#    print("consonant")

#-----------------------------------------------------------------------------------------------------------
# 9.	Write a  program to input any character and check whether it is alphabet, digit or special character
# char = input("Enter a character : ")
# length = len(char)

# if(length==1):

#     if(char.isalpha()==True):
#         print("This is an alphabet")
    
#     elif(char.isdigit==True):
#         print("This is a Digit")
    
#     else:
#         print("This is an Special character")

# else:
#     print("Please enter only one character ")
#---------------------------------------------------------------------------------------------------------
# 10.	Write a program to check whether a character is uppercase or lowercase alphabet.

# char = input("Enter a character : ")

# if(char.isalpha()==True):
#     if(char.isupper()==True):
#       print("This is an uppercase character")

#     else:
#      print("This is an Lowercase character")

# else:
#   print("please enter a valid aplhabet as character")

#---------------------------------------------------------------------------------------------------------------------------
 # 11.	Write a  program to input week number and print week day.

number = int(input("Enter week number (1-7): "))
days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

print(days[number-1])

# if (number == 1):
#     print("Monday")
# elif (number == 2):
#     print("Tuesday")
# elif (number == 3):
#     print("Wednesday")
# elif (number == 4):
#     print("Thursday")
# elif (number == 5):
#     print("Friday")
# elif (number == 6):
#     print("Saturday")
# elif (number == 7):
#     print("Sunday")
# else:
#     print("Invalid week number! Please enter a number between 1 and 7.")



#---------------------------------------------------------------------------------------------------------- 
# 12.	Write a  program to input month number and print number of days in that month.

# m = [3,5,7,8,10,12]
# m2 = [1,4,6,9,11]
# month_num = int(input("Enter month number between 1-12 : "))

# if(month_num>=0 and month_num<=12):
#     if(month_num in m):
#         print("31 Days in this month ")

#     elif(month_num in m2):
#         print("30 Days in this month ")

#     else:
#         print("28 Days in this month ")

# else:
#     print("Invalid month number , Please enter month number between 1-12")
#----------------------------------------------------------------------------------------------------------------------------

# 13.	Write a  program to count total number of notes in given amount.

# amount = int (input("Enter an amount : "))
# notes = [2000,1000,500,200,100,50,20,10,5,2,1]
# count = 0
# for note in notes:
#     if (amount>=note):
#         count1 = amount//note
#         amount %= note
#         print(f"{note} x {count1} = {note*count1}")
#         count += count1
# print("Total number of notes is" , count  )

#------------------------------------------------------------------------------------------------------------------------------------
# 14.	Write a  program to input angles of a triangle and check whether triangle is valid or not.

# a = float(input("Enter first angle: "))
# b = float(input("Enter second angle: "))
# c = float(input("Enter third angle: "))

# if (a + b + c == 180) :
#     print("The triangle is valid.")
# else:
#     print("The triangle is not valid.")

#--------------------------------------------------------------------------------------------------------------------------------------
# 15.	Write a  program to input all sides of a triangle and check whether triangle is valid or not.

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if (a + b > c and b + c > a and a + c > b):
#     print("The triangle is valid.")
# else:
#     print("The triangle is not valid.")

#-------------------------------------------------------------------------------------------------------------------------------------------
# 16.	Write a  program to check whether the triangle is equilateral, isosceles or scalene triangle.

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if (a == b == c):
#     print("Equilateral triangle")
# elif (a == b or b == c or a == c):
#     print("Isosceles triangle")
# else:
#     print("Scalene triangle")

#----------------------------------------------------------------------------------------------------------------------------------
# 17.	Write a  program to calculate profit or loss.

# cost_price = int(input("Enter Cost Price: "))
# selling_price = int(input("Enter Selling Price: "))

# if selling_price > cost_price:
#     print(f"Profit = {selling_price - cost_price}")
# elif selling_price < cost_price:
#     print(f"Loss = {cost_price - selling_price}")
# else:
#     print("No Profit No Loss")

#-----------------------------------------------------------------------------------------------------------------------------------------

# 18.	Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

# chemistry = int(input("Enter marks in Chemistry: "))
# physics = int(input("Enter marks in Physics: "))
# biology = int(input("Enter marks in Biology: "))
# math = int(input("Enter marks in Mathematics: "))
# computer = int(input("Enter marks in Computer: "))

# total = physics + chemistry + biology + math + computer
# percentage = total*100 / 500

# print(f"Percentage: {percentage}%")

# if percentage >= 90:
#     print("Grade A")
# elif percentage >= 80:
#     print("Grade B")
# elif percentage >= 70:
#     print("Grade C")
# elif percentage >= 60:
#     print("Grade D")
# elif percentage >= 40:
#     print("Grade E")
# else:
#     print("Grade F")

#-------------------------------------------------------------------------------------------------------------------------------------
# 19.	Write a  program to input basic salary of an employee and calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

# basic_salary = float(input("Enter basic salary: "))

# if basic_salary <= 10000:
#     hra =   basic_salary * 20//100
#     da = basic_salary * 80//100
# elif basic_salary <= 20000:
#     hra = basic_salary * 25//100
#     da =  basic_salary * 90//100
# else:
#     hra = basic_salary * 30//100
#     da =  basic_salary *95//100

# gross_salary = basic_salary + hra + da
# print(f"Gross Salary: {gross_salary}")

#-------------------------------------------------------------------------------------------------------------------------------------

# 20.	Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill 

# units = int(input("Enter electricity units consumed: "))

# if units <= 50:
#     bill = units * 0.50
# elif units <= 150:
#     bill = 50 * 0.50 + (units - 50) * 0.75
# elif units <= 250:
#     bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
# else:
#     bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

# surcharge = bill * 20/100
# total_bill = bill + surcharge

# print(f"Total Electricity Bill: Rs. {total_bill}")

