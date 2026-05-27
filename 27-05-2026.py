#reverse string on its possition 

name = "Rohit Meena"

temp= ""
rev = ""

for i in name:
    if i !=" ":
        temp=i+temp

    else:
        rev= rev+temp+" "
        temp=""
rev=rev+temp
print(rev)
