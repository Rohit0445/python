#  higher order functions are takes a function as an argument at the time of calling 
 
#  Map(),Filter(),reduce(),decorator,generator,lambda all thease are higher order functions 


#------------------MAP()-------------------------- gives all the values same number of output element as an input element------
#syntex------
# map(functionname,collection)
# return  a object
#-----------------------------------------------------------------------------------------------------

#q1------ square all elements in a list 

# li = [1,2,3,4,5]

# def sqr(n):
#     return n**2

# result = map(sqr,li)

# print(result)
# # print(list(result))
# print(tuple(result))
#--------------------------------------------------------------------------------

#q2------ Add 5 in  all elements in a list 


# li = [1,2,3,4,5]

# def add(n):
#     return (n+5)

# result = map(add,li)

# print(result)
# print(tuple(result))

#--------------------------------------------------------------------------------------


#q1------ square root of   all elements in a list 
#square root formula ---- **0.5
#cube root formula ---- **0.33



# li = [1,2,3,4,5]

# def add(n):
#     return (n**0.33)

# result = map(add,li)

# print(result)
# print(tuple(result))



#------------------FILTER()--------------------------give elements which setisfying the conditions------
#syntex------
# filter(functionname,collection)
#return object  


#q = 1 = even numbers in a list 

# li = [1,2,3,4,5,6,7,8,9]


# def even(n):
#     if n%2 == 0:
#         return n

# result  = filter(even,li)
# print(result)
# print(list(result)) 




#------------------REDUCE()--------------------------------gives only one element or value 
 
# direct use nahi kr sakte sabse pehle functools ko import krna padega 
# import functools
#  functool.reduce(functionname,collection,initial_value)

#syntex------
# functool.reduce(functionname,collection,initial_value)
# gives  two parameter to a function 


#q---add all elemnt of list 

# import functools


# li = [1,2,3,4,5,6]

# def add_all(x,y):
#     return x+y

# result = functools.reduce(add_all,li)

# print(result)



li1 = [1,2,3,4]
li2 = [1,2,3]
li3 = [1,2,3,4]

def add(x,y,z):
    return x+y+z

result = map(add,li1,li2,li3)

print(result)
print(list(result))












