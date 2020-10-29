import random

def main():
    p_1 = input(str("Enter name for player 1: "))
    p_2 = input(str("Enter name for player 2: "))
    player_1 = 0
    player_1_wins = 0
    player_2 = 0
    player_2_wins = 0
    rounds = 1

    while rounds != 10:
       print("Round " + str(rounds))
       player_1 = dice_roll()
       player_2 = dice_roll()
       print( p_1, "Roll's:", player_1)
       print(p_2, "Roll:'s", player_2 )

       if player_1 == player_2:
           print("Draw!\n")
       elif player_1 > player_2:
           player_1_wins = player_1_wins + 1
           print(p_1, "wins!\n")
       else:
           player_2_wins = player_2_wins + 1
           print(p_2, "wins!\n")

       rounds = rounds + 1

    if player_1_wins == player_2_wins:
        print("Draw!")
    elif player_1_wins > player_2_wins:
        print(p_1, "- rounds won: " + str(player_1_wins))
    else:
        print(p_2, "- rounds won: " + str(player_2_wins))


def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()
