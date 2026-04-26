import random

num1 = random.randint(1, 101)

while True:
    guess = int(input('Guess a number between 1 and 101:'))
    if guess == num1:
        print("you guessed the number!")
        num1 = random.randint(1, 101)
    elif guess < num1:
        print('Too Low!')
    elif guess > num1:
        print('Too High!')
