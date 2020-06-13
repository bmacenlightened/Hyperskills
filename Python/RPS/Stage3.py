import random

choices = ["paper", "scissors", "rock"] 

def user_pick():
    pick = input()
    return pick
    
def computer_choice():
    return random.choice(choices)
    
def second_win(a, b):
    if a == "paper" and b == "scissors":
        return True
    if a == "rock" and b == "paper":
        return True
    if a == "scissors" and b == "rock":
        return True


def play_game(user, computer):
    if user == computer:
        return f"There is a draw {user}"
    elif second_win(user, computer):
        return f"Sorry, but computer chose {computer}"
    else:
        return f"Well done.  Computer chose {computer} and failed"
    

def game():
    while True:
        user = user_pick()
        if user == "!exit":
            break
        elif user in choices:
            computer = computer_choice()
            print(play_game(user, computer))
        else:
            print("Invalid input")
    
game()