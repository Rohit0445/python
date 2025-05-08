a=int(input("enter a number"))
a=a+1
count = 0

for i in range(1,a):
    if(a%i==0):
        count+=1

if(count==2):
    print("It is a prime number")        

else:
    print("It is not a prime number")