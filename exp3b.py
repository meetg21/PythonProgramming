# Write a program to check whether a number is Armstrong or not.

# taking input from user
number = input("enter number\n ")
# length
dig = len(number)
sum = 0 

for i in range(dig):
    # condition for number to be armstrong
    sum += int(number[i])**3  

if int(number) == sum: 
    print("yes")

else :
    print("no")

