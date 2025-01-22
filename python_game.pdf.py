import random

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'stone' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'stone'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Stone, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (stone, paper, scissors) or 'quit' to exit: ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        elif player_choice not in ['stone', 'paper', 'scissors']:
            print("Invalid choice. Please choose stone, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice() 
        print(f"Computer chose: {computer_choice}")
        print(get_winner(player_choice, computer_choice))
        print("-" * 30)

if __name__ == "__main__":
    main()
