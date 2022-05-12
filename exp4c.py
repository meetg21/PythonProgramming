import re
Substring ='string'
S1 ='''hello'''
S2 ='''hiii'''
print(re.search(Substring, S1, re.IGNORECASE))
print(re.match(Substring, S1, re.IGNORECASE))
print(re.search(Substring, S2, re.IGNORECASE))
print(re.match(Substring, S2, re.IGNORECASE))
