li = [10,20,56,35,94,85,74,63,12]

num = int (input("Enter which largest number you want : "))

li.sort()
print(li)
print(num,"rd largest number is ", li[-(num)])