#  Write a program to read the numbers until -1 is encountered. Also, count the number of prime numbers and composite numbers entered by the user

# initial count (defining variables)
count = 0
com_count = 0
prm_count = 0
while True:    
    num =int(input("Enter a number\n"))
    # condition for -1
    if num == -1:
        print("Break")
        break    
    elif num == 1:
        print("neither composite nor prime")
        # 1 being exception
    elif num == 2:
        prm_count += 1
        print("2 is a prime number")    
    else:
        for a in range(2,num):
            # prime checking
            if num%a==0:
                count+=1
        if count>=1:
            # else composite 
            print(num, "is Composite Number")
            com_count += 1
        else:
            print(num, "is Prime Number")    
            prm_count += 1    
            
# printing final count
print("No of composite numbers till now are: ",com_count)
print("No of prime numbers till now are: ",prm_count)