#CO4
#QN 1
class Bank:
 def __init__(self,num,name,type,balance):
  self.num=num
  self.name=name
  self.type=type
  self.balance=balance
 def deposit(self):
  amount=int(input("Enter the amount to deposit: "))
  self.balance+=amount
  print("Amount After deposit:",self.balance)
 def withdraw(self):
  amount=int(input("Enter the amount to withdraw: "))
  if(amount>self.balance):
   print("Insufficient balance")
  else:
    self.balance-=amount
    print("Amount after withdraw: ",self.balance)
b1=Bank(101,"john","savings",0)
while(1):
 print("1.Deposit\n2.Withdraw\n3.Exit")
 choice=int(input("Enter your choice: "))
 if choice==1: 
   b1.deposit()
 elif choice==2:
   b1.withdraw()
 else:exit(0)
 