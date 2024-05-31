# This function will check whether the given number is armstrong or not
def armstrong(N):
    S = 0
    M=N
    while M>0:
       V= M % 10
       S += V ** 3
       M //= 10
    if (N==S):
        return True
    else:
        return False