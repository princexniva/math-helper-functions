#This function tell you if the given number is palindrome or not
def palindrome(num):
    revnum=num[::-1]
    if revnum==num:
      return True
    else:
      return False

