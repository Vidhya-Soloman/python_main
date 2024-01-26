a=input("Enter a string:")
r=a[::-1]
if(r==a):
 print("String is palindrome")
else:
 print("Not Palindrome")
l=len(a)
#print(l)
mid=l//2
#print(mid)
if(a[:mid]==a[mid:]):
 print("String is Symmetrical")
else:
 print("Not Symmetrical")