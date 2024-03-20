class Bankaccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        return f"Баланс на счете номер {self.account_number} владельца {self.owner} составляет {self.balance}"


account = Bankaccount("Иванов Иван", "23613578192", 1000)
print(account.show_balance())
