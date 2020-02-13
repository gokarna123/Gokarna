def maximum(a,b,c):
    x=a>b>c
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print("the max nbr is:",a)
elif b>=a and b>=c:
    print("The max nbr is:",b)
elif c>=a and c>=b:
    print("The max nbr is:",c)
