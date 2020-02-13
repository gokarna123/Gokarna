x= int(input("Enter the numbers:"))
for G in range(1, x + 1):
    print(G, "- Gokarna Adhikari")

y=int(input("Enter the numbers:"))
count=0
for B in range(1, y + 1):
    if B % 2==0:
     count += 1
    print(B)
print(f"(we have {count} even number)")

def name(a,b):
    print(f"Hi {a} {b}")
    print("Welcome to softwarica college   ")
name("Gokarna", "Adhikari")


x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
def number(x,y):
    return x + y


ans= G(x, y)
print(ans)