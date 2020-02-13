a =int(input("Enter the marks of physics: "))
b =int(input("Enter the marks of chemistry: "))
c =int(input("Enter the marks of mathematics: "))
d =int(input("Enter the marks of English: "))
e =(a+b+c+d)
x =400
print("Total marks of 4 subjects is:", e)
p =(e/x)*100
print("percentages:", p)
if p>=70 and p<=100:
    print("distinction:")
elif p>=60 and p<=70:
    print("first division:")
elif p>=40 and p<=60:
    print("pass:")
if p<=40:
    print("fail:")
if p>=90 and p<=100:
    print("A+")
elif p>=80 and p<90:
    print("A")
elif p>=70 and p<=80:
    print("B+")
if p>=60 and p<=70:
    print("B")
if p>=50 and p<=60:
    print("C+")
elif p>=40 and p<=50:
    print("C")
elif p>=30 and p<=40:
    print("D+")
if p>=20 and p<=30:
    print("D")
if p<=20:
    print("E")
