# for i in range (1,11):
#     print(i)


# li = [1,2,3,4,5,6]

# # for i in li:
# #     print(i)


# for i in range(len(li)):
#     print(i,li[i]


#---------------------------------------------maximum num in list -----------------------------------------------------------------------------


# li = [1,3,8,4,6]

# maximum = li[0]

# for i in range(1, len(li)):
#     if maximum < li[i]:
#         maximum = li[i]

# print(maximum)


#--------------------------------------------------------minimum num in list -----------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------------------------------------------
#greatest digit 

# num = 2413
# digit = 0
# while(num > 0):
#     lastdigit = num % 10
#     num = num//10
#     if(lastdigit > digit):
#         digit = lastdigit
    


# print(digit)

#--------------------------------------------------------------------------------------------------------------------------------
#smallest digit 

# num = 2146
# digit = 9

# while(num > 0):
#      digit1 = num%10
#      if(digit1 < digit):
#         digit = digit1
#      num = num//10
        

# print(digit)
    
#------------------------------------------------------------------------------------------------------------------------
#list in assending order.


# li = [1,8,6,9,4,3,7,2,5 ]

# for i in range(len(li)):
    
#     for j in range(i+1, len(li)):
#         if(li[j] < li[i]):
#             temp = li[i]
#             li[i] = li[j]
#             li[j] = temp    

# print(li)

#----------------------------------------------------------------------------------------------------------------------------------
#dessanding order 

# li = [1,8,6,9,4,3,7,2,5 ]

# for i in range(len(li)):
    
#     for j in range(i+1, len(li)):
#         if(li[j] > li[i]):
#             temp = li[i]
#             li[i] = li[j]
#             li[j] = temp    

# print(li)

#----------------------------------------------------------------------------------------------------------------------------------------------
#PALINDROME


# num =  int(input("enter a number : " ))
# temp = num
# rev = 0
# while(num > 0):
#     digit = num%10
#     num = num //10
#     rev = rev * 10 +  digit


# if(digit == temp ):
#     print("palindrom")

# else:
#     print("not a palindrome")


# num =  (input("enter a number : " ))

# print("palindrome") if num == num[::-1] else print("not a palindrome")


# num =  (input("enter a number : " ))
# length = len(num)
# num = int(num)
# amstrong = num
# ans = 0

# while(num > 0):
    
#     digit = num%10
#     num = num//10
#     ans += digit**length


# if (ans == amstrong):
#     print("Amstrong")

# else:
#     print(" Not a amstrong")

#reverse list -------------------------------------------------------------

# li = [1,2,38,4,51,68,7,18,9 ]

# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         temp = li[i]
#         li[i] = li[j]
#         li[j] = temp    
# print(li)

#or reverse list

# li = [1,2,38,4,51,68,7,18,9 ]

# i =0
# j = len(li)-1

# while(i<j):
#     temp = li[i]
#     li[i] = li[j]
#     li[j] = temp
#     i+=1
#     j-=1

# print(li)

#PRIME NUMBER ---------------------------------------------------------------------------------------------------


# num = int (input("Enter a number : "))
# count = 0
# i=1
# while(i<=num):
#     if(num%i ==0):
#           count+= 1
#     i+= 1      

# if(count==2):
#      print("prime")

# else:
#      print("not a prime")  



#-----------------------------------------------------------------------------------------------------------

#kth largest number
 
# li = [10,20,56,35,94,85,74,63,12]

# num = int (input("Enter which largest number you want : "))

# li.sort()
# print(li)
# print(num,"rd largest number is ", li[-(num)])

#---------------------------------------------------------------------------------------------------------

#second largest number 

# li1 = [10,20,56,35,94,85,74,63,12]

# li1.sort()

# print("second largest number is ", li1[-2])

#---------------------------------------------------------------------------------------------------------

#perfect number

# num = int(input ("Enter a number :  "))
# x=0  
# for i in range(1,num):
#     if(num%i==0):
#         x += i 

# if(num==x):
#     print(f"{num } is a  perfect number")

# else:
#    print (f"{num } not a perfect number")

#----------------------------------------------------------------------------------------------------------

#fibonacci

num = int(input("Enter a number : "))

first = 0
second = 1

for i in range (num):
    if (i==0):
        print(first,end= " ")
        continue
    if (i==1):
        print(second,end= " ")
        continue

    next = first+second
    first = second
    second = next
    print(next,end=" ")