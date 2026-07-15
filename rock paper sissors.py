import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

while True:
    # User input
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.\n")
        continue

    # Computer choice
    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    # Determine winner
    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("💻 Computer wins!")

    # Play again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThanks for playing!")
        break

    print()