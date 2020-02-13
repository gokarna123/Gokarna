words=input("Enter the words;")
length=len(words)
string=""
counter=-1
while counter>(length-1):
    string1=words[counter]
    string1=string+string1
    counter=counter-1
if string==words:
    print("the number is palindrome")
else:
    print("The number is not palindrome")