import re

a = " Hi my name__ is meetabbbbb"
b = " my age is 18.My phone number is 56789"

c = a+b 
# for letters 4<
find =(re.findall(r"\b\w{4,}\b", c))
print(find)