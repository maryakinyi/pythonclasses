class Account:
    def __init__(self,id,phonenumber,amount):
        self.id=id
        self.phonenumber=phonenumber
        self.amount=amount
    def  deposit(self):
        return f"For your to get update of your account you must have {self.phonenumber}"

    def withhdraw(self):
        return f"For you to be able to withdraw money for your in a bank you must have {self.amount},{self.id} "