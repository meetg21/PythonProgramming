
import re

a = " Hi my name__ is meetabbbbb"
b = " my age is 18.My phone number is 56789"

c = a+b 
# for letters 4<
find =(re.findall(r"\b\w{4,}\b", c))
# print(find)

# abbbbb
final2 = re.search('ab+?',c)
# print(final2)

# lowercase__
final3 = re.search('[a-z]+[_]',c)
# print(final3)

final4= re.search('m',c)
# print(final4)


final5= re.search("5",c)
print(final5)


