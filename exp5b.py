x=list(map(int,input().split()))
evennumbers=[]
oddnumbers=[]

f=lambda y: y%2==1
oddnumbers=filter(f,x)
print("Odd numbers: ", list(oddnumbers))

h=lambda y: y%2==0
evennumbers=filter(h,x)
print("EVen Numbers: ", list(evennumbers))
