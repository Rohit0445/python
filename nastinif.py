salary = int (input("Enter your salary"))

if(salary>0 and salary<=10000):
    print("Nokia=rs.5000 ")
    d=(10*5000)/100
    print("10% gst = ",d)
    print("price after adding gst",5000+d)
    totalprice=5000+d
    emi = totalprice/12
    print("EMI per month = ",emi)

elif(salary>1000 and salary<=50000):
    d=(10*30000)/100
    print("Realme=rs.30000 ")
    print("10% gst = ",d)
    print("price after adding gst",30000+d)
    totalprice=30000+d
    emi = totalprice/24
    print("EMI per month = ",emi)

elif(salary>50000 and salary<=80000 ):
    d=(10*50000)/100
    print("iphone=rs.50000 ")
    print("10% gst = ",d)
    print("price after adding gst",50000+d)
    totalprice=50000+d
    emi = totalprice/36
    print("EMI per month = ",emi)


elif(salary>80000 ):
    d=(10*80000)/100
    print("iphone=rs.80000 ")
    print("10% gst = ",d)
    print("price after adding gst",80000+d)
    totalprice=50000+d
    emi = totalprice/36
    print("EMI per month = ",emi)





else:
    print("Enter valid salary")

