import random
number = random.randint(1,100)
guess=0
attempt=0
while guess!=number:
    guess= int(input("Guess a number between 1-100"))
    attempt=attempt+1
    if guess>number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Congrats! That's the right number")
        print("total number of attempts is", attempts)
