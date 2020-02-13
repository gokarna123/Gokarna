x=int(input("Enter a number:"))
y=0
a=x
while x>0:
    v= x % 10
    x=x//10
    y= y * 10 + v
print(y)
if a==y:
    print(a," is palindrome")
else:
    print(a," is not palindrome")
