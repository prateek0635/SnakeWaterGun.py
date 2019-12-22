import random #Imported the random so that Bot can choose the Random S W G
import time # To pause the game between some commands so that it will feel smooth
def check(n,k):
    global u,c #Global 
    if n=='S':
        if k=='G':
            c=c+1
            print("Bot Won This chance")
        elif k=='W':
            u=u+1
            print(f"{name} won This game")

    elif n=='W':
        if k=='G':
            u=u+1
            print(f"{name} won This game")
        elif k=='S':
            c=c+1
            print("Bot Won This chance")
    elif n=='G':
        if k=='S':
            u=u+1
            print(f"{name} won This game")
        elif k=='W':
            c=c+1
            print("Bot Won This chance")

u=0
c=0
print("Welcome to this Snake Water and Gun game")
name=input("Please enter your good name Please!!! ")
time.sleep(1)  #this will sleep the game for 1 second So that it will feel like a game
print(f"Welcome {name}")
time.sleep(1)
for i in range(10):
    print(f"Your chance no.{i+1}")
    time.sleep(1)
    n=input('Chosse S,G,W: ')
    a=['S','G','W']
    k=random.choice(a)
    check(n,k)
    print(f"Bot choses {k}")
    time.sleep(1)
    print(f"Current Score is\n {name}={u}\n Bot={c}")
    time.sleep(1)
time.sleep(1)
print(f"Overall score is \n {name}={u}\n Bot={c}")
time.sleep(1)
if c>u:
    print("Better Luck Next time BOT won")
elif c==u:
    print(f"Uff {name} It's a Tie   . Try again")
else:
    print(f"Congratulations!! {name} Its a victory .. You Won")
