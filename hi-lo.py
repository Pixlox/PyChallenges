import random

secret = random.randint(1,10)
count = 0

guess = int(input("Guess a number between 1 and 10: "))
print(guess)

while guess != secret:
    if guess > secret:
        print("LOWER")
    
    elif guess < secret:
        print("HIGHER")

    guess = int(input("Guess again: "))  

print("CORRECT")