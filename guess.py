import random 
def guessNumber(n, target):
    lo,hi = 1, len(n) - 1
    steps = 0
    while lo <= hi:
        mid = (lo + hi)//2
        steps+=1
        if target == mid:
            return 'correct'
        elif target < mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def playGuessNumberGame():
    # Set the range of numbers
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Guess the Number game! Guess a number between {lower_bound} and {upper_bound}.")

    # Let the player guess the number
    player_guess = guessNumber(upper_bound, target_number)
if __name__ == "__main__":
    playGuessNumberGame()