import random
import os


def main():
    print "The Number Game  \n ========================"
    print "I am guessing a number between 0 and 200. Can you guess it?"

    user_name = raw_input("What's your name?: ")

    random_number = random.randrange(200)
    print random_number
    user_guess = ""

    message_file = open("Motivation.txt", "r")
    motivation_list = message_file.read().splitlines()
    message_file.close()

    user_motivations = map(lambda motivation: "** " + motivation + ", " + user_name + "! **", motivation_list)

    while user_guess != random_number:
        # get the users guess
        # compare guess against random_number
        user_guess = int(raw_input("Your Guess:"))
        if user_guess < random_number:
            print random.choice(user_motivations)
            print "Your guess was too low"
        elif user_guess > random_number:
            print random.choice(user_motivations)
            print "Your guess was too high"
    print "*** You Did it!!!!!! ****"

    raw_input()


main()
