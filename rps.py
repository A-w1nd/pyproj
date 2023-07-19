import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game Tied"
    elif player_choice == "Rock":
        return "You Win" if computer_choice == "Scissors" else "You Lose"
    elif player_choice == "Paper":
        return "You Win" if computer_choice == "Rock" else "You Lose"
    elif player_choice == "Scissors":
        return "You Win" if computer_choice == "Paper" else "You Lose"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        player_choice = input("Enter your choice (Rock/Paper/Scissors) or type 'I quit' to end the game: ").capitalize()
        if player_choice == "I quit":
            print("Thank you for playing.")
            break

        if player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose from Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)


main()