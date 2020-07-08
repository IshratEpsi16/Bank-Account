#base class
class Account:
    def __init__(self,filepath):    #constructor
        self.filepath=filepath    
        with open(filepath,'r') as file:
            self.balance=int(file.read()) 
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def deposit(self,amount):
        self.balance=self.balance+amount
    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))
#inherited class
class Checking(Account):
  
    def __init__(self,filepath,fee):        #fee which the bank charged
        Account.__init__(self,filepath)
        self.fee=fee
    def transfer(self,ammount):
        self.balance=self.balance-ammount-self.fee
account=Account('balance.txt')
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(200)
print(account.balance)
account.commit()
#Inherited class
checking=Checking("balance.txt",10)
checking.transfer(100)
print(checking.balance)
checking.commit()

