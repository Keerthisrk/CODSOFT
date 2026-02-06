import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Instructions:")
    print("Type rock, paper, or scissors to play.")
    print("Type exit to quit the game.\n")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice == "exit":
            print("\nThanks for playing!")
            break

        if user_choice not in choices:
            print("❌ Invalid choice. Please try again.\n")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"\nScore:")
        print(f"You: {user_score} | Computer: {computer_score}\n")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("👋 Goodbye!")
            break

play_game()