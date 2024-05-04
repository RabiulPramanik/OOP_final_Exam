from bank import Bank
from user import Customer, Admin

bank = Bank("ABC")

def customer_only():
    name = input("Enter you name: ")
    email = input("Enter you email: ")
    address = input("Enter you address: ")
    account_type = input("Enter you account type: ")
    customer = Customer(name=name,email=email,address=address,account_type=account_type)
    while True:
        print("1. Deposit.")
        print("2. Withdraw.")
        print("3. Check available balance.")
        print("4. Check transaction history.")
        print("5. Take a loan .")
        print("6. Transfer.")
        print("7. Exit.")
        op = int(input("Enter yor option: "))

        if op == 1:
            amount = int(input("Enter your amount: "))
            customer.deposit(bank,amount)

        elif op == 2:
            amount = int(input("Enter your amount: "))
            customer.withdraw(bank,amount)

        elif op == 3:
            customer.check_available_balance()

        elif op == 4:
            customer.transaction_history()

        elif op == 5:
            amount = int(input("Enter your amount: "))
            customer.take_a_loan(bank,amount)

        elif op == 6:
            name = input("Enter ohter customer name: ")
            other = customer.find_customer(bank,name)
            if other:
                amount = int(input("Enter your amount: "))
                customer.transfer_the_amount(bank,other,amount)
            else:
                print("Account does not exist")

        elif op == 7:
            break
        else:
            print("Wrong option!")

def admin_only():
    name = input("Enter you name: ")
    email = input("Enter you email: ")
    address = input("Enter you address: ")

    admin = Admin(name=name,email=email,address=address)  

    while True:
        print("1. Delete any user account.")
        print("2. Show all user accounts list.")
        print("3. Check the total available balance of the bank.")
        print("4. Check the total loan amount.")
        print("5. On or off the loan feature of the bank.")
        print("6. Exit.")
        op = int(input("Enter yor option: "))

        if op == 1:
            name = input("Enter name: ")
            admin.delete_any_account(bank,name)

        elif op == 2:
            admin.show_user(bank)

        elif op == 3:
            admin.total_available_balance_in_bank(bank)

        elif op == 4:
            admin.total_loan_amount(bank)

        elif op == 5:
            print("1. Loan on.")
            print("2. Loan off.")
            ch = int(input("Enter choice: "))
            if ch == 1:
                admin.is_on(bank)
            elif ch == 2:
                admin.is_off(bank)
            else:
                print("Wrong option!")

        elif op == 6:
            break
        else:
            print("Wrong option!")


while True:
    print(f"*****Welcome to  {bank.bank_name} ******")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    op = int(input("Enter your option: "))
    if op == 1:
        admin_only()
    elif op == 2:
        customer_only()
    elif op == 3:
        break
    else:
        print("Wrong option! ")


    