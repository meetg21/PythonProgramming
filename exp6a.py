class student:
    def __init__(name,self,roll,member1,member2,member3,member4):
        self.roll = roll
        self.name = name
        self.m2 = member2
        self.m1 = member1
        self.m3 = member3
        self.m4 = member4
name = input("Enter your full name >>")
roll = int(input("Enter the roll number of the student >>"))
member1 = int(input("Enter marks in subject No.1 >>"))
member2 = int(input("Enter marks in subject No.2 >>"))
member3 = int(input("Enter marks in subject No.3 >> "))
member4 = int(input("Enter marks in subject No.4 >> "))

stu1 = student
setattr(stu1,'name',name)
setattr(stu1,'roll',roll)
setattr(stu1,'m1',member1)
setattr(stu1,'m2',member2)
setattr(stu1,'m3',member3)
setattr(stu1,'m4',member4)


print("MARK LIST")
print("Name :",getattr(stu1,'name'))
print("Roll Number : ",getattr(stu1,'roll'))
print("Marks in Subject1 : ",getattr(stu1,'m1'))
print("Marks in Subject2 : ",getattr(stu1,'m2'))
print("Marks in Subject3 : ",getattr(stu1,'m3'))
print("Marks in Subject4 : ",getattr(stu1,'m4'))

totalMarks = 0

for i in range(1,5):
    totalMarks = totalMarks + getattr(stu1,'m'+str(i))
    i = i+1

print("Total marks scored by the student : ",totalMarks) 

percentage = totalMarks*0.25

print("Percentage scored by the student : ",percentage,"%")


