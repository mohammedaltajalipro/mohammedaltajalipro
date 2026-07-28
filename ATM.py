import time as t
balance = 50000

while True:

    options = (
        "\n======= ATM =======\n"
        "1. Withdraw\n"
        "2. Deposit\n"
        "3. Check Balance\n"
        "4. Exit"
    )

    print(options)

    choice = input("Choose any option = ")

    if choice == "1":

        withdraw = int(input("Enter the amount to withdraw = "))

        if withdraw <= balance:

            # Check the balance after withdrawal
            remaining_balance = balance - withdraw

            if remaining_balance <= 1:

                print("Warning! Your balance will become very low.")

                opt = input(
                    "Do you still want to withdraw? 1. Yes 2. No = "
                )

                if opt == "2":
                    print("Withdrawal cancelled")
                    continue

            # Withdraw the money only once
            balance -= withdraw

            print("You have withdrawn your amount successfully!")
            print("Your balance is =", balance)

        else:
            print("Insufficient balance")

    elif choice == "2":

        deposit = int(input("Enter the amount to deposit = "))

        balance += deposit

        print(deposit, "deposited successfully")
        print("Your new balance is =", balance)

    elif choice == "3":

        print("Your Balance is =", balance)

    elif choice == "4":

        print("Exit successful")
        break
    else:

        print("Invalid choice")
    print("Do you want recipt\n yes?/no?")
    choice = ("yes","no")
    choice = input("Enter your choice =")
    if choice == "yes":
        print("printing recipt......")
        t.sleep(2)
        print("Here is your recipt \n ==========XXXBANK===========\n withdrawed amt:",withdraw,"\n your balance =",balance,"\n<=============================>")