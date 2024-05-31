from evens import evens
from cubes import cubes

num = int(input("Enter a number: "))
even_nmbers = evens(num)
for i in even_nmbers:
    print(i)

n=int(input("Enter a number: "))

t=cubes(n)

for i in t:
    print(i)
