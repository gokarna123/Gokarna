def value():
    limit=int(input("Enter the number which are multiply of 3 & 5 :"))
    for i in range(1,limit+1):
        if i%3==0 or i%5==0:
            print(i)


value()
