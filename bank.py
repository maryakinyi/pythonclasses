class Account:
    def __init__(self,phonenumber,name,loan_limit):
        self.phonenumber=phonenumber
        self.balance=0
        self.name=name
        self.loan_limit=loan_limit
        self.loan=loan
        
# Requirement bank to increament a
    def deposit(self,amount): 
        if amount<=0:
            return f"amount must be greater than 0"
        else:    
        self.balance +=amount
        return f"Dear, {self.name},you have deposited {amount} and your {self.balance}"

   # 
    def withdraw(self,amount):
        if amount<=0:
            return f"Hello,{self.name} you have withdrawn {amount}"
        elif amount>self.balance:
            return f"Amount must be greater than 0"
        else:
            self.balance-=amount
            return f"{self.name}.Your balance is {self.balance}"

    def borrow(self,amount):
        if amount>self.loan_limit:
            print(f"You can borrow")  
        elif self.loan>0:
            print(f"kindly ,you clear your debt balance") 
        else:
            self.loan+=1
            self.balance+=amount
            return f"You have successesfully borrowed "             
            


        
        #Account accepts amount,amount must be more than 0 amount must be less than balance,amount reduces the balance  
