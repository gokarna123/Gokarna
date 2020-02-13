num=int(input("Enter the number:"))
i=0
while i<num:
    j=0
    while j<num-1:
        if num[j]>num[j + 1]:
            a=num[j]
            num[j]=num[j + 1]
            num[j + 1]=a
        j=j+1
    i=i+1
print(num)





