import re
x = input()

# final = re.sub("([^aeiou])y",r"\1ies",x)
final = re.sub("([aeiou]y)$",r"\1s",x)
# final = re.sub()
print(final)


