import re
#collecting input from user i.e the card number to check
txt=input("Enter credit card number: ")
# pattern for checking
valid_pattern="^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"
test=re.findall(valid_pattern,txt)
# final check
if len(test):
   print("Valid")
else:
   print("Not Valid")
