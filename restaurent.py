menu ={1:"burger",
       2:"pizza",
       3:"pasta",
       4:"sandwich",
       5:"biryani" 

       }

print(menu)

def customerorder():
   order = int(input("Enter which number's dish you want to order : "))

   if(order>0 and order<=5):
 
      if(order==1):
          print("you order is and your price will be RS.100")

      elif(order==2):
           print("you order is pizza and your price will be RS.100")

      elif(order==3):
       print("you order is pasta and your price will be RS.100")   
    
      elif(order==4):
           print("you order is sanwich and your price will be RS.100")
    
      elif(order==5):
       print("you order is biryani and your price will be RS.100")
    
    
      else:
        print("this dish is not in our menu")

   else:
      print("please Enter Valid number  ") 

  

customerorder()  

revisedorder=input("you want to add something in your order enter yes") 



while(revisedorder=="yes"):
   customerorder()
   revisedorder=input("you want to add something in your order enter yes") 



