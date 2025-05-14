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

li = [1,8,6,9,4,3,7,2,5 ]

for i in range(len(li)):
    
    for j in range(i+1, len(li)):
        if(li[j] > li[i]):
            temp = li[i]
            li[i] = li[j]
            li[j] = temp    

print(li)
