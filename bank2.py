class Bank:
 def __init__(self,accno,name,type,balance):
  self.accno=accno
  self.name=name
  self.type=type
  self.balance=balance
 def deposit(self):
  amount=int(input("Enter the amount to deposit:"))
  self.balance+=amount
  print("Balance=",self.balance)
 def withdraw(self):
  amount=int(input("Enter the amount to withdraw:"))
  if(self.balance<amount):
   print("**Insufficient balance**")
  else:
   self.balance-=amount
   print("Available balance:",self.balance)
 def display(self):
  print("******************************")
  print("Acc no:",accno,"\nName:",self.name,"\nAccount Type:",self.type)
  print("******************************")

accno=int(input("Enter account number:"))
name=input("Enter name:")
type=input("Enter account type:")
p=Bank(accno,name,type,0)
p.display()
while(1): 
 print("1.Deposit\n2.Withdraw\n3.Exit\n")
 choice=int(input("Enter your choice:"))
 if(choice==1):
  p.deposit()
 elif(choice==2):
  p.withdraw()
 elif(choice==3):
  exit(0)