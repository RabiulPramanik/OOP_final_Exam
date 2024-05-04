from user import Customer
class Bank:
    def __init__(self,bank_name) -> None:
        self.bank_name = bank_name
        self.customers = Customer.all_customers
        self.main_balance = 0
        self.loan_amount = 0
        self.fag = True
