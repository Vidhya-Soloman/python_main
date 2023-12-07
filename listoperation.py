#LIST OPERATIONS
l1=[1,2]
l2=[1,3]
if len(l1)==len(l2):
 print("same length")
else:
 print("not same")
if sum(l1)==sum(l2):
 print("same sum")
else:
 print("not same")
common=set(l1) & set(l2)
if common:
 print("common element ",common)
else:
 print("no common")