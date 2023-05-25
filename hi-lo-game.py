import random

def grabDifficulty():
    difficultyWord = input("Choose a difficulty (easy / medium / hard) ")

    if difficultyWord == "easy":
        return 10
    elif difficultyWord == "medium":
        return 20
    elif difficultyWord == "hard":
        return 30
    else:
        print("Invalid answer.")
        print("Defaulting to difficulty - easy")
        return 10

difficulty = grabDifficulty()
secret = random.randint(1, difficulty)
count = 1

name = input("What is your name? Enter: ")
guess = int(input("Guess a number between 1 and " + str(difficulty) + ":"))
print(guess)

while guess != secret:
    if guess > secret:
        count = count + 1
        print("Lower...")
    
    elif guess < secret:
        count = count + 1
        print("Higher...")

    guess = int(input("Guess again: "))

    if guess == secret:
        print("Correct!")
        print("Guessing took you " + str(count) + " tries, " + name + "!")
