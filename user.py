from abc import ABC
from datetime import datetime

class User(ABC):
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    all_customers = []
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.account_number = ( len(name) + len(email) + len(address) )
        self.deposits = []
        self.withdraws = []
        self.loans = []
        self.loan_count = 0
        Customer.all_customers.append(self)
        

    def deposit(self,bank,amount):
        if amount >=0:
            self.balance += amount
            bank.main_balance += amount
            print(f"{amount} is Deposit successfuly!")
            self.deposits.append(f"{amount} is deposit at {datetime.now()}")
        else:
            print("This is Nagative amount!")
    
    def withdraw(self,bank,amount):
        if bank.main_balance == 0:
            print("The bank is bankrupt.")
            return
        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount
                bank.main_balance -= amount
                print(f"{amount} is Withdraw successfuly!")
                self.withdraws.append(f"{amount} is withdraw at {datetime.now()}")
            else:
                print("Withdrawal amount exceeded!")
        else:
            print("This is Nagative amount!")
    
    def check_available_balance(self):
        print(f"Avialable balance is {self.balance}")

    def take_a_loan(self,bank,amount):
        if bank.fag == False:
            print("Now Loan is off")
            return
        if self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            bank.main_balance -= amount
            bank.loan_amount += amount
            self.loans.append(f"{amount} take loan at {datetime.now()}")
        else:
            print("ALL ready you take loan two times !")
            
    def transaction_history(self):
        print("*****Diposit*****")
        for dip in self.deposits:
            print(dip)
        print("*****Withdraw*****")
        for wid in self.withdraws:
            print(wid)
        print("*****Loan*****")
        for ln in self.loans:
            print(ln)


    def transfer_the_amount(self,bank,other,amount):
        if amount <= self.balance:
            if other in bank.customers:
                self.balance -= amount
                other.balance += amount
            else:
                print
                ("Account does not exist")
        else:
            print("Not enough Balance in your account!")

    def find_customer(self,bank,custoner_name):
        for customer in bank.customers:
            if custoner_name == customer.name:
                return customer
        return None

            

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def delete_any_account(self,bank,customer_name):
        for customer in bank.customers:
            if customer_name == customer.name:
                bank.customers.remove(customer)
                print("Delete successfuly! ")
                return
        print("Not Fund")
    
    def show_user(self,bank):
        if len(bank.customers) == 0:
            print("Empty!")
            return
        for customer in bank.customers:
            print(f"Name:> {customer.name}, Email:> {customer.email} and Address:> {customer.address}")

    def total_available_balance_in_bank(self,bank):
        print(f"total available balance in bank is {bank.main_balance}")

    def total_loan_amount(self,bank):
        print(f"Total loan amount is {bank.loan_amount}") 
    
    def is_on(self,bank):
        bank.fag = True
        print("Loan on Successfuly")

    def is_off(self,bank):
        bank.fag = False
        print("Loan off Successfuly")
    



    

        
    