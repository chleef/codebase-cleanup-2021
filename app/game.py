
from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    Params:
        choice1 and choice2 are both strings - either rock, paper, or scissors
    """
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock"
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors"
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None
        }
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice


if __name__ == '__main__':

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    winner = determine_winner(u, c)

    if winner == u:
        print("You won!")
    elif winner == c:
        print("Computer won")
    elif winner == None:
        print("It's a tie")

    #could do nested ifs obviously
    #write a function to determine
    #dictionary approch - make a win, tie, lose dictionary - or a tuple?