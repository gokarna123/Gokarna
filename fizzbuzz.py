def name(a,b):
    x=int(input("Enter the number:"))
    if x % 3==0 and x % 5 == 0:
        print(a + b)
    elif x%3==0:
        print(a)
    elif x%5==0:
        print(b)
    else:
        print(x)
name("Fizz","Buzz")

