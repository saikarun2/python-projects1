import random

def game(comp,you):
    if comp == you:
        return None
    elif comp =='r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp =='p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp =='s':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("computer choice: rock(r) parer(p) siscor(s): ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo ==2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("user choice: rock(r) parer(p) siscor(s): ")
a = game(comp,you)

print(f"compurter choise is: {comp}")
print(f"user choice is: {you}")

if a==None:
    print("its a tie")
elif a:
    print("you win")
else:
    print("you lost")