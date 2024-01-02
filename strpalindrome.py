#checking whether a string is palindrome or not
txt=input("Enter a string: ")
rev=txt[::-1]
if(txt==rev):
 print("Palindrome")
else:
 print("Not palindrome")