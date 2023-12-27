#CO1
#QN 8
l1=[]
n=int(input("Enter the size of list:"))
print("Enter the elements:")
for i in range(0,n):
 ele=int(input())
 l1.append(ele)
print("Original list: ",l1)
print("Numbers in list that are not even:")
for i in l1:
 if i%2!=0:
  print(i)