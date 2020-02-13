num=[]
sum=0
for i in range(0,5):
    x=int(input("Enter the number:"))
    num.append(x)
    sum=sum+1
print(num)
d=0
sum=0
for d in range(0,5):
    sum=sum+num[d]
    d=d+1
print(sum)



