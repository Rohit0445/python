# def hello(): #Declaration
#     print("hello") #statement

# hello() #calling

#non-return without argument

def factorial():
    a=int(input("Enter a number : "))
    ans = 1
    for i in range(1,a+1):
        ans*=i
    print(ans)

factorial() 

def sum():
    num = int (input("Enter a number : "))
    ans = 0
    for i in range(1,num+1):
        ans+=i
    print(f"sum of n natural numbers is {ans}")

sum()

def fibonacci():
    num1 = int(input("Enter a number : "))
    a =0
    b=1
    next = b
    count = 1

    while (count<=num1):
        print(next, end=" ")
        count += 1
        a, b = b, next
        next = a + b
    print()

fibonacci()