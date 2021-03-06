import random
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess

if guess == secret_number:
    print('Good job! You guessed in my number {} guesses'.format(guesses_taken))
else:
    print('Nope.  The number I was thinking of was ' + str(secret_number))
