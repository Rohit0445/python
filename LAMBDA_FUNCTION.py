#lambda function 








# LAMBDA + MAP -------------------------

# square of all element-------------------------------------------------

# l = [1,2,3,4,5,6]

# print(list(map(lambda x:x**2,l)))

# --------------------------------------------------------------
# add 5 in all elements 

# l = [1,2,3,4,5,6]

# print(list(map(lambda x:x+5,l)))

#--------------------------------------------------------------
# l1 = [1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]

# print(list(map(lambda x,y,z:x+y+z,l1,l2,l3))) 


# LAMBDA + FiltEr

# Even number 

l = [1,2,3,4,5,6,7,8,9]

print(list(filter(lambda x: x if(x%2==0) else (None),l)))




