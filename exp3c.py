data = input()
d=0
a =0
for x in data :
    if x.isdigit():
        d=d+1
    elif x.isalpha():
        a=a+1
    else:
        pass
print("Letters", a)
print("Digits", d)