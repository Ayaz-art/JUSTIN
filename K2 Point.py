# RESTURENT ORDER SETUP
# Define MENU
Menu = {
    "pizza":1200,
    "burger":300,
    "fries":150,
    "coffee":100,
    "salad":50,
    "pasta":300,
}

# Greetings
print('HI WELCOME TO K2 RESTURENT POINT')
print('HOW MAY I HELP YOU WE ARE OFFERING THESE ITEMS')
print("pizza: Rs1200\nburger:Rs300\nfries :Rs150\ncoffee:Rs100\nsalad :Rs50\npasta:Rs300")

Order_Total = 0
#  90 + 30 - 120
Item_1 = input("Enter The Name Of The Item You Want To Order = ")
if Item_1 in Menu:
    Order_Total += Menu[Item_1]# 0 + 1200 = 1200
    print(f"Your item {Item_1} has been added to your order")

else:
      print(f"Ordered item {Item_1} is not avaialable yet please order something else")

print(f"So Your Total Is Rs.{Order_Total}") 

Another_Order = input("Are you want to add another item? (yes/no) ")    
if Another_Order =='yes':
    Item_2 = input("Please enter the name of your next item = ")
    if Item_2 in Menu:
         Order_Total += Menu[Item_2]
         print(f"ITEM {Item_2} has been added to order")
    else:
          print(f"Order Item {Item_2} is not available yet please order something else ")        

print(f"So Your Total Is Rs.{Order_Total}") 

Another_Order = input("Are you want to add another item? (yes/no) ")    
if Another_Order =='yes':
    Item_3 = input("Please enter the name of your next item = ")
    if Item_3 in Menu:
         Order_Total += Menu[Item_3]
         print(f"ITEM {Item_3} has been added to order")
    else:
          print(f"Order Item {Item_3} is not available yet please order something else ")       

print(f"So Your Total is Rs.{Order_Total}") 

Another_Order = input("Are you want to add another item? (yes/no) ")    
if Another_Order =='yes':
    Item_4 = input("Please enter the name of your next item = ")
    if Item_4 in Menu:
         Order_Total += Menu[Item_4]
         print(f"ITEM {Item_4} has been added to order")
    else:
          print(f"Order Item {Item_4} is not available please order something else ")        

print(f"So Your Total is Rs.{Order_Total}") 

Another_Order = input("Are you want to add another item? (yes/no) ")    
if Another_Order =='yes':
    Item_5 = input("Please enter the name of your next item = ")
    if Item_5 in Menu:
         Order_Total += Menu[Item_5]
         print(f"ITEM {Item_5} has been added to order")
    else:
          print(f"Order Item {Item_5} is not available please order something else ")        

print(f"So Your Total is Rs.{Order_Total}") 

Another_Order = input("Are you want to add another item? (yes/no) ")    
if Another_Order =='yes':
    Item_6 = input("Please enter the name of your next item = ")
    if Item_6 in Menu:
         Order_Total += Menu[Item_6]
         print(f"ITEM {Item_6} has been added to order")
    else:
          print(f"Order Item {Item_6} is not available please order something else ")        

print(f"So Your Total is Rs.{Order_Total}") 
    


