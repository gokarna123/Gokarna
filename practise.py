num=[]
x=1500
for i in range(1500,2701):
    if (i%7==0) and (i%5==0):
       num.append(i)
print(num)

x=(1,2,3,4,5,4,3,2,1)
for i in x:
   print("X"*i)

numbers=(0,1,2,3,4,5,6,7,8,9,10)
for i in numbers:
    if (i%2==0):
        print("The number is even")
    elif (i%2==1):
        print("The number is odd")

num=[0,1,2,3,4,5,6]
for i in num:
    num.remove(5)
    print(num)

