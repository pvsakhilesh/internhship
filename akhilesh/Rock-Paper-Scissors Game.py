import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def play_round():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    print(result)
    return result
def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Choose 'rock', 'paper', or 'scissors' to play.")
    while True:
        result = play_round()
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        print(f"\nCurrent Scores: You - {user_score} | Computer - {computer_score}")
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThank you for playing!")
            break
play_game()
\