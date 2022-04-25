# importing lib
import string
# string
edic = {}

# taking input from the user to be stored in a string
estring = input("Enter a string: ").lower()

# creating for loop
for char in string.ascii_lowercase:
    x = estring.count(char)
    if x!= 0:
        #print(f'"{char}" : {x}')
        edic[char] = x

# printing 
print(edic)
