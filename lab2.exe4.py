a =int(input("Enter the first number:"))
b =int(input("Enter the second number:"))
c =int(input("Enter the third number:"))
if a<b and a<c:
    print("the lowest number:",a)
elif b<a and b<c:
    print("The lowest number:",b)
else:
    print("The lowest number:",c)