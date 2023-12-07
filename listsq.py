#list comprehension
#square of n numbers
lis=[]
n=int(input("enter the size of the list"))
for i in range (n):
 lis.append(int(input(f"lis[{i}]")))
square=[x*x for x in lis]
print("squares",square)