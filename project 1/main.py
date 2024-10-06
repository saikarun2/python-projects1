import random
# snake,water and gun
def game(comp, you):
    # if two values are equal  return tie
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("computer turn: Snake(s) Water(w) or Gun(g)?: ")
randNo = random.randint(1,3)
if randNo == 1:
    comp ='s'
elif randNo == 2:
    comp ='w'
elif randNo == 3:
    comp = 'g'

you= input("yours turn: Snake(s) Water(w) or Gun(g)?: ")
a= game(comp,you)

print(f"computer chose: {comp}")
print(f"you chose: {you}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("computer win")