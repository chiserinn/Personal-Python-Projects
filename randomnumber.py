import random

def guess(x):
    random_no = random.randint(1,x)
    guess = 0

    while guess != random_no: #to initialise guess as a variable (0), and that this will LOOP until you give the correct input
        guess = int(input("Guess the Random Number (1 - {}): ".format(x)))
        if 1 < guess < x:
            if guess > random_no:
                print("Try again, you're too high.")
            elif guess < random_no:
                print("Try again, you're too low.")
        else:
            print("Out of bounds error.")
    print("You did it! You have guessed the number: {}".format(random_no))


def computer_guess(y):
    low = 1
    high = y
    feedback = ''
    print("Hi! I'm going to guess a random number!")
    while feedback != 'c' : #while main input = null, loop getting input
        if low!=high:
            guess = random.randint(low, high) 
        else:
            guess = low

        print(guess)
        feedback = str(input("Is it too high (H), to low (L) or correct (C)? ".lower()))
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("Yay I did it! I guessed the number {}!!".format(guess))

computer_guess(1000)