num = int(input("Enter a nmber : "))

if(num==1):
    next = int(input("enter your next destination from 2,3 and 4")) 

    if(next==2):
        next = int(input("enter your next destination from 3 and 4")) 
 
        if(next==3):
            next = int(input("enter your next destination is 4")) 

            if(next==4):
                print("reached")

            else:
                print("Invalid") 

        elif(next==4):
            print("reached") 
 

    elif(next==3):
        next = int(input("enter your next destination form 2 and 4")) 

        if(next==2):
            next = int(input("enter your next destination is  4")) 

            if(next==4):
                print("reached")

            else:
                print("Invalid") 

        
        elif(next==4):
            print("reached")

        else:
            print("Invalid")    

    elif(next==4):
        print("reached")

    else:
        print("Invalid input")    


else:
    print("Invalid")        