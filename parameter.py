def add():
    c= a+b
    print("add is:", c)
def sub():
    c= a-b
    print("sub is:", c)
def div():
    c= a/b
    print("div is:", c)
def multi():
    c =a*b
    print("multi is:", c)
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
x=int(input("choose the your option:"))
if x==1:
    add()
elif x==2:
    sub()
elif x==3:
    div()
if x==4:
    multi()
