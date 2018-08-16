import random
lives = 20
n = random.randint(1, 99)
guess = int(input("Enter a number from 1 to 99: "))
while lives > 0:
    if guess < n:
        print ("You're a little too low.")
        print ("You have", lives, "lives")
        guess = int(input("Enter a number from 1 to 99: "))
        lives = lives - 1
    elif guess > n:
        print ("You're a little too high.")
        print ("You have", lives, "lives")
        guess = int(input("Enter a number from 1 to 99: "))
        lives = lives - 1
    else:
        print ("OMG,YOU GOT THE ANSWER!")
        break
