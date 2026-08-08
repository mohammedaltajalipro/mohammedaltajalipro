import time as t
class inventory:
    def __init__(self,category,name,quantity,price):

        self.category = category
        self.name = name
        self.quantity = quantity
        self.price = price
#claculate gst and total price
    def calculate(self):
     gst = 0.18 * self.price
     total_price = self.price + gst
     print("Price:", self.price)
     print("GST:", gst)
     print("Total Price:", total_price)
category = {"Electronics":[inventory("Electronics","Mobile",10,10000), inventory("Electronics","Laptop",5,50000), inventory("Electronics","Headphones",20,2000)],
            "Furniture":[inventory("Furniture","Sofa",5,15000), inventory("Furniture","Bed",3,25000), inventory("Furniture","Dining Table",2,20000)],
            "utensils":[inventory("utensils","Pan",10,500), inventory("utensils","Pot",8,400)],
            "stationary":[inventory("stationary","Pencil",20,10), inventory("stationary","Book",15,50)],
            "Medicine":[inventory("Medicine","Tablets",100,10), inventory("Medicine","Syrup",50,20) ]}
category_list = list(category.keys())
while True:
 print("="*50,"\n WELCOME TO ALI INVENTORY MANAGEMENT SYSTEM\n","="*50)
 print("choose the category:")
 print("1. Electronics\n2. Furniture\n3. Utensils\n4. Stationary\n5. Medicine")
 choice = int(input("Enter your choice(1-5): "))
 if 1 <= choice <= len(category_list):
    selected_category = category_list[choice - 1]
    print("\nopening", selected_category, "section...")
    t.sleep(2)
    print("\ncategory\tname\tquantity\tprice")
    print("-"*50)
    for i in range(len(category[selected_category])):
     item = category[selected_category][i]
     print(f"{i+1}\t{item.category}\t{item.name}\t\t{item.quantity}\t\t{item.price}")
    product = int(input(f"\nEnter Product Number (1-{len(category[selected_category])}): "))

    if 1 <= product <= len(category[selected_category]):

        selected_product = category[selected_category][product - 1]

        print("\nYou Selected")
        print("Category :", selected_product.category)
        print("Product  :", selected_product.name)
        print("Stock    :", selected_product.quantity)
        print("Price    :", selected_product.price)
        
        buy = input("\nDo you want to buy this product? (yes/no): ").lower()
        print("\nProcessing your request...")
        t.sleep(2)
        if buy == "yes":
            if selected_product.quantity > 0:
                print("\nCalculating Bill...")
                t.sleep(2)
                selected_product.calculate()
                print("pay here https://www.paypal.com/paypalme/ali123")
                t.sleep(2)
                payment = input("\nEnter 'paid' after payment: ").lower()
                if payment == "paid":
                    selected_product.quantity -= 1
                    print("\nPayment Successful!")
                    print("Purchase Successful!")
                    print("Remaining Stock:", selected_product.quantity)
                else:
                    print("Payment Failed!")
            else:
                print("Sorry! Product is Out of Stock.")
        else:
            print("Purchase Cancelled.")
    else:
        print("Invalid Product Number!")
 else:
    print("Invalid Category!")
 print("Do you want to keep shopping(yes/no)?")
 choice = input("Enter you choice: \n")
 if choice != "yes":
    break





