from armstrong import armstrong
from evens import evens

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)

N=int(input("Enter the Three Digit number: "))
C=armstrong(N)
if C:
    print(N,"It is an armstrong number")
else:
    print(N,"It is not an armstrong number")    