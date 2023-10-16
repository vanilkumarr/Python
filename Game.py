import random

while True:
    choices = ["rock","paper","scissors"]
    player=None
    while player not in choices:
        player=input("choice: Rock,paper or scissors :")
        player=player.lower()
    BOT= random.choice(choices)

    if player == 'rock':
        if BOT == "scissors":
            print("your choice:", player)
            print("BOT choice:", BOT)
            print("you won")
        if BOT == "paper":
            print("your choice:", player)
            print("BOT choice:", BOT)
            print("you lose")
    elif player == 'scissors':
        if BOT == "rock":
            print("your choice:", player)
            print("BOT choice:", BOT)
            print("you won")
        if BOT == "paper":
            print("your choice:", player)
            print("BOT choice:", BOT)
            print("you lose")
    elif player == 'paper':
        if BOT == "scissors":
            print("your choice:", player)
            print("BOT choice:", BOT)
            print("you won")
        if random == "rock":
            print("your choice:", player)
            print("BOT choice:", random)
            print("you lose")
    elif player == BOT:
        print("your choice:", player)
        print("BOT choice:", BOT)
        print("you tie")

    exit=input("you want to play again: Yes/no?").lower()
    if exit !="yes" and exit !="y":
        break
print("thank you for playing")





