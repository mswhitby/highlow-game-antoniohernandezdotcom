import random

def mystery_number_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the maximum number of guesses
    max_guesses = 7
    guesses_used = 0
    
    print("✨ Welcome to **Mystery Number Quest**! ✨")
    print("I've chosen a secret number between 1 and 100.")
    print(f"Can you uncover it in just {max_guesses} guesses? Let's find out!\n")
    
    while guesses_used < max_guesses:
        # Ask the user for their guess
        try:
            guess = int(input("🔮 Enter your guess: "))
        except ValueError:
            print("🚫 Oops! That's not a valid number. Try again!")
            continue
        
        guesses_used += 1
        
        # Check if the guess is correct
        if guess < secret_number:
            print("📈 Too low! Aim higher!")
        elif guess > secret_number:
            print("📉 Too high! Bring it down!")
        else:
            print(f"🎉 **Congratulations!** You've uncovered the mystery number {secret_number} in {guesses_used} guesses!")
            print("You're a true number detective! 🕵️‍♂️")
            return
    
    # If the user runs out of guesses
    print(f"😢 Oh no! You've used all {max_guesses} guesses.")
    print(f"The mystery number was {secret_number}. Better luck next time!")

# Run the game
mystery_number_game()
