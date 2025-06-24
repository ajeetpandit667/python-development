class Account:
    def __init__(self, acc, bal):  # fixed __init__
        self.account = acc
        self.balance = bal
        print("initial balance is :",self.balance)

    def debited(self, amount):
        self.balance -= amount  # fixed balance update
        print("Debited amount is {}".format(amount))  # fixed print
        print("Available balance is {}".format(self.get_bal()))  

    def credited(self, amount):
        self.balance += amount  # fixed balance update
        print("Credited amount is {}".format(amount))  # fixed print
        print("Available balance is {}".format(self.get_bal()))   

    def get_bal(self):
        return self.balance   

# test
acc1 = Account(10000, 12345)
acc1.debited(1000)  
acc1.credited(500)
