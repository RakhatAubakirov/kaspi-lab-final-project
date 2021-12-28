from UserAccount.UserAccount import UserAccount


class Refill(UserAccount):
    def __init__(self, id_, currency, balance):
        super().__init__(id_, currency, balance)
        self.balance = 0

    def refill_acc(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated: ", self.balance)