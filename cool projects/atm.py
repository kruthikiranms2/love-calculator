balance = 200
pin = 1996
choice=0
def view_balance():
    print("Your current balance is €", balance)
def withdraw():
    global balance
    x= int(input("Enter amount to withdraw: "))
    if x>balance:
        print("Insufficient funds, try again:")
    else:
        balance = balance-x
        print(f"Please collect {x} cash and remove card")
        print(f"your new balance is {balance}")

    























def show_menu():
    while True:
        print("\nWelcome to the ATM")
        print("1. View Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_balance()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            deposit()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you. Goodbye!")
            break
show_menu()