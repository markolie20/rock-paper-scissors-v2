import random

options = ["scissors", "paper", "rock"]

i = random.randint(0, (len(options) - 1))

playedHand = input("PLay rock, paper or scissors please: ")

computerPlayedHand = options[i]

if playedHand == "rock":
    if computerPlayedHand == "scissors":
        print("the computer had scissors, you win")
    elif computerPlayedHand == "paper":
        print("the computer had paper, you lose")
    elif computerPlayedHand == "rock":
        print("the computer also had rock, its a tie")
elif playedHand == "paper":
    if computerPlayedHand == "rock":
        print("the computer had rock, you win")
    elif computerPlayedHand == "scissors":
        print("the computer had scissors, you lose")
    elif computerPlayedHand == "paper":
        print("the computer also had paper, its a tie")
elif playedHand == "scissors":
    if computerPlayedHand == "paper":
        print("the computer had paper, you win")
    elif computerPlayedHand == "scissors":
        print("the computer also had scissors, its a tie")
    elif computerPlayedHand == "rock":
        print("the computer had rock, you lose")
else:
    print("please only state rock, paper or scissors")

