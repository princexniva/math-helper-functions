from evens import evens

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)


   
from squares import squares

a=int(input("Enter the number:"))
r=squares(a)
for i in range(a):
    print(i**2)