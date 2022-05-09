import re

a = " Hi my name__ is meetabbbbb"
b = " my age is 18.My phone number is 56789"

c = a+b 
# abbbbb
final2 = re.search('ab+?',c)
print(final2)