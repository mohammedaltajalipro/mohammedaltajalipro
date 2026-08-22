import random as rd
import time as t
#trains
nums = [10,11,12,13,14,15,16,27,18,53,34,44,56,89,33,22,21]
Trains = ["Rajdhani", "ExpressShatabdi", "ExpressDuronto", "ExpressTejas", "ExpressGatimaan", "ExpressHumsafar", "Express","duno"]
category = ["sleeper","1st AC","2nd AC","3rd AC","general"]
price = {
    "sleeper":60,
    "1st AC":679,
    "2nd AC":578,
    "3rd AC":366,
    "general":100
    
}
print("<","="*50,">","\n welcome to train booking page","\n<","="*50,">")

def booking():
    print(Trains)
    user_input = input("Enter the train name you want: ")
    if user_input in Trains:
        print("showing categories please wait..")
        t.sleep(2)
    else:
       print("invalid choice")
       return
    for cat, amount in price.items():
     print(cat, "₹", amount)
    user_in = input("\nenter the category you would like to book: ")
    ticket_price = price[user_in]
    gst = 0.25
    rtax = 0.35
    tax = ticket_price*gst + rtax
    total = ticket_price+tax
    if user_in in price:
        print("price:",price[user_in])
        print("calculating everything..")
        t.sleep(2)
        print("checking for available seats")
        t.sleep(2)
        print("ticket price:",ticket_price)
        print("tax:",tax)
        print("total",total)
        print("your seat number is:",rd.choice(nums))
    else:
        print("invalid choie")
        return
    while True:
     user = input("do you want to proceed with booking(yes/no)?")
     if user == "yes":
       print("redirecting....")
       t.sleep(2)
       print("please pay here https://www.paypal.com/paypalme/ali123")
       user1 = input("enter 'paid' after payment: ")
       if user1 != "paid":
         print("booking unsuccessful")
       else:
        print("payment successful")
        break
     else:
        break
    

    

booking()