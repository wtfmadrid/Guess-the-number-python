import random

def guessNumberGame():
    lower_bound = 1
    upper_bound = 10
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Guess the Number game! Guess a number between {lower_bound} and {upper_bound}.")

    steps = 0

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            steps += 1
            if not lower_bound <= player_guess <= upper_bound:
                print(f"Out of bounds, please stay inbound. Range is {lower_bound} to {upper_bound}")
            if player_guess == target_number:
                print(f"Congratulations! You guessed the number {target_number} in {steps} steps.")
                break
            elif player_guess < target_number:
                print("Try for a higher number.")
            else:
                print("Try for a lower number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        

if __name__ == "__main__":
    guessNumberGame()
