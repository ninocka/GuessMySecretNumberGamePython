# utf--*- coding: utf8 -*-
import random
number = random.randrange (1,10)
guess = ""
attempt = 0
print "Welcome! It is nice to see you! Let\'s play and have fun!"
name = raw_input("But first, what is your name?")
print "Hello, %s!" % name
print "Let's play GUESS MY SECRET NUMBER!"
while True:
    try:
        answer = raw_input("Do you want to play? Please, write  'p' to play or  'e' to exit ")
        if answer == 'p':
            while True:
                try:
                    guess = int(raw_input("Please enter the number between 1 and 10: "))
                    attempt = attempt + 1
                    if guess < 1:
                        print "ONLY NUMBERS between 1 and 10 please!"
                    elif guess < number:
                        print "Sorry this is not the correct answer - try again! Little higher."
                    elif guess > 10:
                        print "ONLY NUMBERS between 1 and 10 please!"
                    elif guess > number:
                        print "Sorry this is not the correct answer  - try again! Little lower."
                    else:  # guess == number
                        print "Mindreader! You have entered the correct number!! That took you %d attempts. Let\'s play again!" % attempt
                        answer = raw_input("Do you want to play? Please, write  'yes' to play or  'no' to exit ")
                        number = random.randrange(1, 10)
                        guess = ""
                        attempt = 0
                        attempt = attempt + 1
                except ValueError:
                    print "ONLY NUMBERS between 1 and 10 please!"
        elif answer == "e":
            print "Goodbye and see you soon!"
            break
        else:
            print "Input p or e only"
            answer = raw_input("Do you want to play? Please, write  'yes' to play or  'no' to exit ")
    except: ValueError
    print "Only 'p' or 'e' please"
    answer = raw_input("Do you want to play? Please, write  'yes' to play or  'no' to exit ")

