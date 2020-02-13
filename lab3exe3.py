def show_numbers():
 limit=int(input("Enter the number:"))
 for i in range(0,limit):
        if i%2==0:
            print(i,"EVEN")
        elif i%2==1:
            print(i,"ODD")


show_numbers()
