x=int(input("Enter the number:"))
c=0
a=1
while a<=x:
    if(x%a==0):
        c=c+1
    a=a+1
if c==2:
    print(x," is a Prime number")
else:
    print(x," is the composite number")