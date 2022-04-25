# creating a list X
X = []
# taking input from the user
n = int(input("Enter number of terms: "))
# for loop
for i in range(n):
    X.append(int(input("Enter a number to add in the list: ")))
X.sort()
# printing the list
print("The list is as follows: ",X)
# creatring a list Y for cross verification to x
Y = []
for x in X:
    if x not in Y:
        Y.append(x)

# printing the list w/o duplicates
print("New list without duplicates: ",Y)
