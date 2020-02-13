'''i=0
while i<4 :
    j=0
    while j<3:
        print(f"({i},{j})")
        j+=1
    i+=1'''


a=True
while a==True:
    name= input('enter your name:')
    print(" do you want to repeat?")
    c=input()
    if c=='yes':
        print("my name is", name)
    else:
        a= False
print("The process is finished by user")
