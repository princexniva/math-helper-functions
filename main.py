from evens import evens
from palindrome import palindrome

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)

c=input()
if palindrome(c):
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")

    