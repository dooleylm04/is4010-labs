import random

def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""

    return (
        f"The {adjective} Cincinnati Bengals {verb} over the Tampa Bay Buccaneers."  
        f"{noun} had the {adjective} catch of the game to seal the win. "
        f"This was a great step towards {verb} the {noun}."
    )

def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")