x=int(input("Enter the number:"))
sum=0
a=x
while x>0:
    y=x%10
    sum=sum+y**3
    x=x//10
if a==sum:
    print("The number is an Armstrong")
else:
    print("The number is not an Armstrong")