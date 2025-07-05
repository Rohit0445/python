# def my_data(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# my_data(x=10,y=20,z=30,p=40) 

# d = {'x':10, 'y':20, 'z':30}

# for k,v in d.items():
#     print('key is = ',k,'value is = ',v)


# def func_name(**kwargs):

#     print(kwargs)
#     print(type(kwargs))

#     for k,v in kwargs.items():
#        print('key is = ',k,'value is = ',v)


# x =eval(input("Enter data"))

# func_name(**x)


# -------------------------combine all arguments ------------------------------------

def example(a,b=10, *c,d,e='py',**f):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    

example(5,6,7,8,d=9,x=10,y=20,z=30)
