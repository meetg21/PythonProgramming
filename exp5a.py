def PalindromeNumber(str):
   if len(str) <= 1:
       return True
   elif str[0] == str[-1]:
       return PalindromeNumber(str[1:-1])
   else:
       return False
if PalindromeNumber(input()):
   print("Palindrome")
else:
   print('Not a palindrome')

