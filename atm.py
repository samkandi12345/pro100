class Atm(object):
    def __init__(self,creditcardinseted,passwordcorrect,withdrawamount):
        self.creditcardinseted = creditcardinseted,
        self.passwordcorrect = passwordcorrect,
        self.withdrawamount = withdrawamount

    def cash(self):
        print("you have correctly inserted your credit card")

    def password(self):
        print("your password is correct")

    def cashout(self):
        print("you have recieved your entered amount")

cashout = Atm("true",123456789,2500)
print(cashout.withdrawamount)