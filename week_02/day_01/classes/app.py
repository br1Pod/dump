from modules.bank_accounts import *

# account = {
#     "holder_name": "John",
#     "balance": 500,
#     "type": "business"
# }

# print(get_account_name(account))

bank_account = BankAccount("John", 500, "business")
bank_account2 = BankAccount("Hannah", 1000, "personal")

bank_account.holder_name = "Ada"

# print(bank_account.holder_name)

# bank_account.pay_in(50)
# print(bank_account.balance)

# bank_account.pay_monthly_fee()
# print(bank_account.balance)

bank_account2.pay_monthly_fee()
print(bank_account.balance)
print(bank_account2.balance)