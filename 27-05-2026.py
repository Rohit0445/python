#reverse string on its possition 

# name = "Rohit Meena"

# temp= ""
# rev = ""

# for i in name:
#     if i !=" ":
#         temp=i+temp

#     else:
#         rev= rev+temp+" "
#         temp=""
# rev=rev+temp
# print(rev)

# Fibonacci series

a=0
b=1
list=[]
for i in range(10):
   
    # print(a,end=" ")
    list.append(a)
    
    c=a+b
    a=b
    b=c
print(list)