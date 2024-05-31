# This functions `evens` will list first 
# n even numbers
def evens(num):
    even = []
    for n in range(0, num+1, 2):
        even.append(n)
    return even

