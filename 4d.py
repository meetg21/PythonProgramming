import re

a = " Hi my name__ is meetabbbbb"
b = " my age is 18.My phone number is 56789"

c = a+b 
# lowercase__
final3 = re.search('[a-z]+[_]',c)
print(final3)