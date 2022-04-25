
# thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(len(thislist))
# print(type(thislist))
# print(thislist[1])
# print(thislist[-1])
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])


# thislist = ["orange", "mango", "kiwi", "pineapple", "apple"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")
# for x in thislist:
#      print(x)
# for i in range(len(thislist)):
#       print(thislist[i])
# thislist.sort()


# thislist=["apple","banana","cherry"]
# # thislist.append("orange")
# # print(thislist)
# tropical=["mango", "pineapple"]
# thislist.extend(tropical)
# print(thislist)


# del thislist
# print(thislist)

# thislist.clear()
# # print(thislist)


# x=thislist
# y= thislist.copy()
# thislist.clear()
# print(x)
# print(y)


# list1 = [5, 6, 7]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)


# x = ("apple",)
# y = ("apple")
# print(type(x))
# print(type(y))


# thistuple=("apple","banana","cherry")
# print(thistuple[-1])

# x = ("apple", "banana", "cherry")
# x[1] = "kiwi"
# print(x)
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)



# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
# print(type(red))
# print(red)
# print(type(red))



thisdict={"brand":"Ford","model": "Mustang","year": 1964, "year": 2020}
# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))
# print(thisdict["brand"])
# print(thisdict["year"])
# # x = thisdict.get("model")
# print(x)
# y = thisdict.keys()
# print(y)
# z = thisdict.values()
# print(z)
# thisdict["color"] = "white"
# print(thisdict)
# if "model" in thisdict:
#     print("yes")
# thisdict["year"] = 2018
# print(thisdict)
# thisdict.pop("model")
# print(thisdict)

# for x in thisdict:
#     print(x)
#     print(thisdict[x])

for x, y in thisdict.items():
    print(x, y)	
