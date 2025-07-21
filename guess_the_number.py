import random

top_of_range = input("Type a number: ")

# Validate input
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a valid number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number.")
        continue

    if guess == random_number:
        print("You got it!")
        break
    elif guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in", guesses, "guesses.")