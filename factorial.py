## To find the factorial of the given number.
def factorial(z) :
    c=1
    for i in range(1,z+1):
        c*=i
    return c
