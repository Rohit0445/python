n=input("Enter Your NAme")
if((n.replace(' ','')).isalpha()) and (len(n) >=3 and len(n) < 21):
    print(n)

else:
    print("not Alpha")


    # if len(n)<3:
    #     print(n)
    # elif len(n)>20:
    #     print(n)
    # elif(len(n)>=3 and len(n)<=20):
    #     print(n)