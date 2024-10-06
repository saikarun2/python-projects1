import random
randNumber = random.randint(1,100)
# print(randNumber)
userGusess = None
guesses = 0

while(userGusess!=randNumber):
    userGusess = int(input("enter your guess: "))
    guesses += 1
    if(userGusess == randNumber):
        print("you guessed it right!")
    else:
        if(userGusess>randNumber):
            print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed is wrong! enter a larger number")

print(f"you guessed the number in {guesses} guessed")
with open("highscore.txt","r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("you have just broken the high score!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))