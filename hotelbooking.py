import time
class hotel:
    def __init__(self,name,price,rating):
        self.name = name
        self.price = price 
        self.rating = rating
    def payment(self):
        gst = 0.27 * float(self.price.split('/')[0])
        total_price = float(self.price.split('/')[0]) + gst
        print("Room Price: ",self.price)
        print("Total Price (including GST): ", total_price)
print("===== Welcome to the Hotel Booking System =====\n")
hotel1 = hotel("The Grand Palace","500/hr",4.5)
hotel2 = hotel("Ocean View Resort","700/hr",4.8)
hotel3 = hotel("Mountain Retreat","600/hr",4.6)
hotel4 = hotel("City Lights Hotel","550/hr",4.3)
available_hotels = [hotel1, hotel2, hotel3, hotel4]
print("Available Hotels:")

for hotel in available_hotels:
    print(f"- {hotel.name}")
    
#booking function
def display():
    user_choice = input("\nEnter the hotel number (1-4): ")

    if user_choice == "1":
        print("Hotel Name:", hotel1.name)
        print("Price:", hotel1.price)
        print("Rating:", hotel1.rating)
        hotel1.payment()

    elif user_choice == "2":
        print("Hotel Name:", hotel2.name)
        print("Price:", hotel2.price)
        print("Rating:", hotel2.rating)
        hotel2.payment()

    elif user_choice == "3":
        print("Hotel Name:", hotel3.name)
        print("Price:", hotel3.price)
        print("Rating:", hotel3.rating)
        hotel3.payment()

    elif user_choice == "4":
        print("Hotel Name:", hotel4.name)
        print("Price:", hotel4.price)
        print("Rating:", hotel4.rating)
        hotel4.payment()

    else:
        print("Hotel not found.")
        return
    print("Do you want to proceed with the booking? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print("please wait...")
        time.sleep(3)
        print("Loading...")
        time.sleep(2)
        print("Done!")
        print("pay here https://www.phonepay.com/phonepayme/yourusername")
        payment = input("Enter 'paid' after payment: ").lower()
        if payment == "paid":
            print("Payment successful! Enjoy your stay.")
        else:
            print("Payment not received. Booking cancelled.")
    else:
        print("Thank you for visiting!")
while True:
    display()

    another_booking = input("\nDo you want to book another hotel? (yes/no): ").lower()

    if another_booking == "no":
        print("Thank you for using the Hotel Booking System!")
        break

    elif another_booking != "yes":
        print("Invalid choice! Please enter yes or no.")


