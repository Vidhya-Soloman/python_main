#CO1
#QN 4
#SWAPPING LETTERS OF TWO STRING AT POSITION 1
t1=input("Enter first string: ")
t2=input("Enter second string: ")
print("Before swapping:",t1,t2)
print("After Swapping:",t1[0]+t2[1]+t1[2:],t2[0]+t1[1]+t2[2:])
