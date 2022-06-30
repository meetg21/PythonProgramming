class store:
    def __init__(self,code,price):
        self.code = code
        self.price = price

st1 = []

st1.append(store("AB12345",195))
st1.append(store("AB14567",350))
st1.append(store("AB09375",100))
st1.append(store("AB98734",250))
st1.append(store("AB09998",185))
st1.append(store("AB45346",190))

print("Product and Price list")

for i in range(len(st1)):
    print(st1[i].code,"  ",st1[i].price)

dict1 = {}

while True:
    pq = input("Enter the product code : ")
    qty = int(input("Enter the quantity : "))
    dict1[pq] = qty

    x = input("Do you want to continue[yes/no] : ")
    if x == "no" or x == "No":
        break
    else:
        continue

print("\nProduct and Quantity purchased")
print(dict1)

totalPrice = 0

for x in dict1.keys():
    for i in range(len(st1)):
        if x == st1[i].code:
            totalPrice = totalPrice + (dict1[x]*st1[i].price)

print("Total cost = ",totalPrice)
