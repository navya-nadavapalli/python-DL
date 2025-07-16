 #calculate Customer Discount by using all concepts
print("------Customer Discount------")
#defining variables
customer_id=int(input("Enter Your Id:"))
customer_name=input("Enter Your Name:")

is_premium_quality=input("premium_customers(Yes/No)")
premium_customers = is_premium_quality == "yes"

years_partnership =int(input("Enter years of partnership:"))

deal_stage=input(f"Enter a string:(proposal,Negotiation,Closed):")
deal_value=float(input("Enter a original value:"))
extra_discount=input("Enter a extra discount stage(proposal,Negotiation,Closed):")

#conditional statements
#applying base discount on customer type and partnership
if  premium_customers:
    discount=10
    print("Premium Customer discount")
elif not premium_customers and years_partnership>=3:
    discount=5
    print("non_premium discount ")
else:
    print("No discount") 


#using match-case statement
#add an extra discount based on deal
match extra_discount:
    case "proposal":
        discount += 2
    case "Negotiation":
        discount += 3
    case "Closed":
        discount += 5
    case _:
        print("Invalid discount stage")    
   #calculate the final price
        
final_price = deal_value-(deal_value * (discount/100))        


#calculation
        
print("------Customer Discount------")
print(f"Enter customer id:{customer_id}")
print(f"Enter customer name:{customer_name}")
print(f"Enter premium quality:{is_premium_quality}")
print(f"Enter years partnership:{years_partnership}")
print(f"Enter extra discount:{extra_discount} ")
print(f"Enter a deal stage:{deal_stage}")
print(f"Enter a deal value:{deal_value}")
print(f"final price after applied discount:{final_price}")






