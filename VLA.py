# def add(*args):
#     # print(args)
#     # print(type(args))
#     # sum=0
#     # for i in args:
#     #     sum+=i
#     # print(sum)
#     print(args)
#     print(type(args))
    

# x=eval(input("Enter a value"))
# y=eval(input("Enter a value"))
# add(x,y)


# def sub(*substract):
     
#     sub=0
#     for i in substract:
#         sub=i-sub
#     print(sub)

# sub(10,5,2,1)



def add(*args):
    sum = 0
    for i in args:
        for j in i:
            sum = sum+j

    print(sum)
    print(type(args))
    print(type(i))

x = eval(input("Enter any tuple : "))

add(x)