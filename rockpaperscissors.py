import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice}

    return choices

def check_win(player, computer):
    print(f"Player chose: {player} Computer chose: {computer}")
    if player == computer:
        return "Tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock beats scissors! You win."
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win."
        else:
            return "Scissors cut paper! You lose."
    elif player == "scissors":
            if computer == "paper":
                return "Scissors cut paper! You win."
            else:
                return "Rock beats scissors! You lose."


choices = get_choices()


print(check_win(choices["player"],choices["computer"]))

