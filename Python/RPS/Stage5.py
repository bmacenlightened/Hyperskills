import random



def get_rating(user):
    file = open("rating.txt", 'r')
    for line in file:
        if line.split()[0] == user:
            return int(line.split()[1])
    return 0

def user_pick():
    pick = input()
    return pick
    
def computer_choice(choices):
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
        print(f"There is a draw {user}")
        return 50
    elif second_win(user, computer):
        print(f"Sorry, but computer chose {computer}")
        return 0
    else:
        print(f"Well done.  Computer chose {computer} and failed")
        return 100
    

def game():
    name = input("Enter your name:")
    print(f"Hello {name}")
    rating = get_rating(name)
    options = input()
    print("Okay, let's start")
    choices = []
    if options == "":
        choices = ["paper", "scissors", "rock"]
    else:
        choices = [list(options)] 
    while True:
        user = user_pick()
        if user == "!exit":
            break
        elif user == "!rating":
            print(f"Your rating: {rating}")
        elif user in choices:
            computer = computer_choice(choices)
            rating_change = play_game(user, computer)
            rating = rating + rating_change
        else:
            print("Invalid input")
    
game()