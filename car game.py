x= ""
while x!= "quit":
    x=input(">").lower()
    if x== "start":
        print("car started..")
    elif x== "stop":
        print("car stoped.")
    elif x== "help":
        print(""""
        Start - to start the  car
        stop - to stop the car
        quit - to quit
        """)
    elif x == "quit":
        continue
else:
    print("Sorry, i don't understand that!")