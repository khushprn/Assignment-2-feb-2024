
import random
n = random.randint(1, 10)
g = None

while g != n:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < n:
        print("Too low!")
    elif guess > n:
        print("Too high!")
    else:
        print("Correct! You guessed it!")
