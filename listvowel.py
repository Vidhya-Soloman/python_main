#list comprehension
#vowels in list
vowels=['a','A','e','E','i','I','o','O','u','U']
word=input("enter a word").split()[0]
vowelinword=[alphabet for alphabet in word if alphabet in vowels]
print("Vowels in the entered word",vowelinword) 