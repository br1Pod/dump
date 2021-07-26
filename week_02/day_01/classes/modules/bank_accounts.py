class BankAccount:
    def __init__(self, holder_name, balance, type):

        # initialise instance variables
        self.holder_name = holder_name
        self.balance = balance
        self.type = type
        self.rates = {   
            "personal" : 10,
            "business" : 50
        }


    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
        self.balance -= self.rates[self.type]