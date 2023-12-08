class Bank:
 def __init__(self,accno,accname,acctype,balance):
   self.accno=accno
   self.accname=accname
   self.acctype=acctype
   self.balance=balance

 def deposit(self,amount):
  self.balance+=amount
  print(amount,"Deposited successfully")
  print("Available Balance:",self.balance )
 def withdraw(self,amount):
  if amount>self.balance: 
   print("Insufficient balance")
  else:
   self.balance-=amount
   print(amount,"withdrawn successfully")
   print("Available Balance:",self.balance )

accno=int(input("Enter account number:"))
accname=input("Enter account name:")
acctype=input("Enter account type:")
balance=0
obj=Bank(accno,accname,acctype,balance)
while(True):
 choice=int(input("Enter your choice \n 1.Deposit \n 2.Withdraw\n 3.Exit\n"))
 if choice==1:
  obj.deposit(int(input("Enter amount to deposit:")))
 if choice==2: 
  obj.withdraw(int(input("Enter amount to withdraw:")))
 if choice==3:
  exit()



 


