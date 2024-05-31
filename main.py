from evens import evens
from factorial import factorial

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)


a=int(input("Enter the number: "))
print(factorial(a))