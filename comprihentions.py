# convert multiline code into single line is called comprihension
# 
# 1 = list comprehenssion = it returns a list --------------------------------------------------------------

# SYNTEX ====   1 
# for loop == x = [item for item in collection ]:
                #    print([i for i in range(1,11)])

# print([i for i in range(1,11)])

# # Even nummber
# print([i for i in range(2,101,2)])

# # odd number
# print([i for i in range(1,11,2)])

#--------list comprehenssion = it returns a list---------------------------------------------------

# SYNTEX ====   2

# for loop + if 

# Even number 
# print([i for i in range(1,11) if i%2==0])


# SYNTEX ====   3

# for loop + if + else 

# print([i  if i%2==0 else None for i in range(1,11)])



#--------Dictionary comprehenssion = it returns a Dictionary or KEY : Value Pair ---------------------------------------------------

# print({ i:i**2 for i in range (1,6)})


# square of EVEN NUMBER 

# print({ i:i**2 for i in range (1,11) if i%2==0})


# print({ i:i**2 if i %2==0 else None for i in range (1,11) })

li = [35,65,12,45,31,25,]

print({ i:"pass" if i>=33 else "fail" for i in li  })











