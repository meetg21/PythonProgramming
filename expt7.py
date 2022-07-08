class account:
    rate=0.05
    minimum_amount=500
    balance=0
    def __init__ (self,name,account_type,account_number):
        self.name=name
        self.account=account_type 
        self.account_number=account_number
    def details(self):
        print("Name: ",self.name)
        print("Account Type: ",self.account_type)
        print("Account Number: ",self.account_number)
        print("Balance",self.balance)

class sav_acc(account):
    def withdraw(self,amount):
      
        if self.balance==0:
            print("Error can't withdraw account empty !!") 
        else:
            self.balance-=amount
            print("The current balance is: ",self.balance)

    def deposit(self,amount):
        
        time=int(input("Enter the time you want to deposit: ")) 
        self.balance+=(self.balance+amount)*(1+self.rate*time) 
        print("The current balance is: ",self.balance)

class curr_acc(account): 
    def display(self):
       
        print("The current account only provides checkbook facility")
        self.balance = 500
        print(self.balance)

    def withdraw(self,amount):
        
        print(self.balance)        

        if self.balance<=500:
            print("Your balance is only 500 .... if you withdraw then service charge of 2% will be imposed on you!...")
            a = int(input("Press 1 to confirm"))
            if a==1:
                self.balance =self.balance-amount
                if((self.balance) <0):
                    print("Cant proceed as your balance is not suffiecient")
                    self.balance = self.balance + amount
                else:
                    self.balance -= self.balance*0.02
                    print("The current balance is: ",self.balance)
            else:
                self.balance =self.balance-amount
                print("The current balance is: ",self.balance)

        else:
            self.balance-=amount
            print("The current balance is: ",(self.balance-(self.balance*0.02)))
    
    def deposit(self,amount):
      
        self.balance += amount
        if(self.balance < 500):
            print("Your balance is lower than 500 please add more money or else ervice charge of 2% will be imposed on you!...PLease enter 1 to enter more money ")
            choice = int(input("Enter your choice"))
            if choice == 1:
                self.balance = self.balance - amount
                amount = int(input("Enter the amount you want to add"))
                print("The current balance is: ",self.balance+amount)
        else:
            print("The current balance is: ",self.balance)


name=input("Enter name: ") 
account_number=input("Enter account number: ")
account_type=input("Enter type of account 'saving' or 'current': ")
if account_type=='saving':    
    obj=sav_acc(name,account_type,account_number)
else:
    obj=curr_acc(name,account_type,account_number) 
    obj.display()

while(True):
    task=input("Enter 'deposit' to deposit or 'withdraw' for withdrawing:")
    if task=='deposit':
        amount=int(input("Enter amount: "))
        obj.deposit(amount)
    if task=='withdraw':
        amount=int(input("Enter amount: ")) 
        obj.withdraw(amount)
    if task == '0':
        break