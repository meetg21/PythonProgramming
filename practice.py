x = input("Enter your id\n")
y = input("Enter password\n")
dairymilk = 0
kitkat = 0 
snicker = 0
if y == "bbb"and x =="XYZ":
    while True:

        print("dairy milk 10 rs")
        print("kit kat 15 rs")
        print("snicker 10 rs")

        bol = int(input("You can proceed and enter from menu"))

        if bol == 1:
            dairymilk += 1
        elif bol == 2:
            kitkat += 1
        elif bol == 3:
            snicker += 1
        else:
            print("invalid")
            break
else:
    print("bhak sale")

dairymilk_cost = 10*dairymilk
kitkat_cost = 15*kitkat
snicker_cost = 10*snicker

print("Name   Quantity   Price")
print(f"Dairymilk   {dairymilk}   {dairymilk_cost}")
print(f"Kitkat   {kitkat}   {kitkat_cost}")
print(f"Snicker   {snicker}   {snicker_cost}")    
