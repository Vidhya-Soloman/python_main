#SUM OF ALL ITEMS IN A LIST 
#USER INPUT
def func_listsum():
 n=int(input("enter the number of list elements: "))
 l1=[]
 print("enter the elements: ")
 for i in range(0,n):
  ele=int(input())
  l1.append(ele)
 print(l1)
 print("sum=",sum(l1))
func_listsum()
  