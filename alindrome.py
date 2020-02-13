
import time
raw_input=1
name=raw_input("what is your name?")
print("Hello, " + name, "Time to play hangman!")

print(""
"")


time.sleep(1)

print("Start guessing...")
time.sleep(0.5)


word = "secret"


guesses = ''

turns = 10
while turns>0:
      failed=0
    if character in guesses:
    print("char")
    else:
           print("_"),
            failed +=1
           if failed ==0:
               print("you won")
               break
               print()
               guess = raw_input("guess a character:")
               guesses += guess
               if guess not in word:
               turns -= 1
               print("wrong")
            Print("You have", + turns, 'more guesse')
            if turns ==0:
              print("You Lose")



