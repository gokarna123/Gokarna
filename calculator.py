from mymodule import add,sub,multi,div
a=int(input("Enter the number of a:"))
b=int(input("Enter the number of b:"))
x=int(input("Choose the option:"))
if x==1:
   add(a,b)
elif x==2:
    sub(a,b)
elif x==3:
    multi(a,b)
elif x==4:
    div(a,b)
