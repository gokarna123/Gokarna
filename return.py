def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=(a-b)
    return c
def multi(a,b):
    c=(a*b)
    return c
def div(a,b):
    c=(a/b)
    return c
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
x=int(input("Choose the number:"))
if x==1:
   ans=add(a,b)
   print("add:",ans)
elif x==2:
  ans=sub(a,b)
  print("sub:",ans)
elif x==3:
  ans=multi(a,b)
  print(" multi:",ans)
if x==4:
    ans=div(a,b)
    print("div:",ans)
else:
   print("sorry you entered invalid option, plz enter valid option as you put!")