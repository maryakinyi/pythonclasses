from datetime import datetime, time


class Account:
      bank_name="Stanbic Bank"


      def __init__(self,name,phone,loan_limit):
          self.name=name
          self.phone=phone
          self.transation=[]
          self.loan_limit=loan_limit
          self.balance=0
          self.loan=0
      def  deposit(self,amount):
          try:
              10+amount
          except TypeError:
              return f"The amount must be in figures"
          if amount<=0:
              return f"{self.name} you must have amount that is greater than 0"
          else:
            self.balance+=amount
            transation={
             "amount":amount,
             "balance":self.balance,
             "time":datetime.now(),
             "narration":"Deposit"

           }
            self.transation.append(transation)
          return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
      def  show_balance(self):
          return self.balance

      def withdraw(self,amount):
          try :
              10 + amount
          except TypeError:
              return f"The amount must be in figures"    
          if amount<0:
              return f"Dear{self.name} with {self.phone}  your balance is {self.balance}"
          elif amount>self.balance:
             return f"Your can't withraw"

          else :
              self.balance-=amount
              return f"Dear {self.name} with {self.phone} Your balance is {self.balance}"

      def borrow(self,amount):
          if amount>=self.loan:
              return f"You can't borrow the money, your expectation is above the limits"
          elif  self.loan>=1:
              return f" Pay your first loan to borrow again"

          else:
             self.loan=0
             self.balance+=amount
             return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"

      def get_statement(self):
          for transation in self.transation:
              narration=transation["narration"]
              amount=transation["amount"]
              balance=transation["balance"]
              time=transation["time"]
              print(f"For the time of Transation {time.strftime('%D')} your statement {narration} the money you have{amount}Balance {balance}")


      def withdraw(self,amount):
          if amount<0:
              return f"Dear{self.name} with {self.phone}  your balance is {self.balance}"
          elif amount>self.balance:
             return f"Your can't withraw"

          else :
              self.balance-=amount
              return f"Dear {self.name} with {self.phone} Your balance is {self.balance}"

      def borrow(self,amount):
          if amount<=self.loan_limit:
              return f"You can't borrow the money, your expectation is above the limits"
          elif  amount>=1:
              return f" Pay your first loan to borrow again"

          else:
             self.loan=0
             self.balance+=amount
             return f"Dear {self.name} you had {amount} amount and now it has increased to  balance now is {self.balance}"

      def repay_loan(self,amount):
          if amount<0:
              return f"Dear {self.name} you had paid KSH. {amount} amount and  your  balance is {self.balance}"

          elif amount<self.loan:
              self.loan-=amount
              return f"You have paid {amount} and the remaning loan is{self.loan} "
          else:
              difference=amount-self.loan
              self.balance+=difference
              self.loan=0
              return f"Dear {self.name}, you have successfully paid your loan which is {self.loan}, your new balance is{self.balance}"
      def transfer(self,amount,account):
          try:
              10 + amount
          except TypeError:
             return f"amount must be integer" 
          if amount<0:
              return f"try again"
          fees=amount*0.05
          if amount+fees>self.balance:
              return f"Your balance is {self.balance} and you need {amount+fees}"
          else:
              self.balance-=amount+fees
              account.deposit(amount)
              return f"Your balance is {self.balance},the fee deducted was {fees}"
          #Inheritance
class MobileMoneyAccount(Account):
    def __init__(self,name,phone,service_provider,loan_limit=10000):
        super().__init__(name,phone,loan_limit)
        self.service_provider=service_provider
        
    def buy_airtime(self,amount):
       self.balance-=amount
       return f"you have successfully bought {amount} "
