# r = "Rohit Meena"

# print(r[0::])
# print(r[0:5:])
# print(r[0:8:2])
# print(r[::-1])
# print(r[-1:-8 :-1])




# li = [1,2,1,2,3,1]
# print(li)
# x = int(input("Enter en element from the list "))
# count = 0

# for i in li:
#     if(i==x):
#         count += 1

# print(f'{x} is present {count} times in a list')



# li = [1,2,3,4,5]
# print(li)
# x = int(input("Enter en element from the list  "))
# count = 0

# for i in li:
#     count=count+1
#     if(i==x):
#         count=(count+1)-2
#         break
        

# print(f'{x} is present  at the index of {count} in a list')


li = [1, 2, 3, 4, 5]
i = 0
j = len(li) - 1

while i < j:
    li[i] ,li[j] = li[j], li[i]
    i += 1
    j -= 1
print(li)