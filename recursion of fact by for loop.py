x=int(input("Enter the number:"))
def fact(x):
    if x==0:
       return 1
    else:
      return x*fact(x-1)


y=fact(x)
print(y)
