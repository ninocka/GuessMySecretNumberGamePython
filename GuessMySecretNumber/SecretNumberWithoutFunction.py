# utf--*- coding: utf8 -*-
#TEST za čžš
a = "č, ž, š"
print "To je le test: " + a

import random
number = random.randrange(1, 10)
guess = ""
attempt = 0

print "Welcome! It is nice to see you! Let\'s play and have fun!"
name = raw_input("But first, what is your name?")
print "Hello, %s!" % name
print "Let's play GUESS MY SECRET NUMBER!"
while True:
    try:
        guess = int(raw_input("Please enter the number between 1 and 10: "))
        attempt = attempt + 1
        if guess < number:
            print "Sorry this is not the correct answer - try again! Little higher."
        elif guess > number:
            print "Sorry this is not the correct answer  - try again! Little lower."
        else: #guess == number
            print "Mindreader! You have entered the correct number!! That took you %d attempts. Let\'s play again!" % attempt
            answer = input("Do you want to play? Please, write number 1 to play or number 2 to exit ")
            if answer == 1:
                while True:
                    try:
                        guess = int(raw_input("Please enter the number between 1 and 10: "))
                        attempt = attempt + 1
                        if guess < number:
                            print "Sorry this is not the correct answer - try again! Little higher."
                        elif guess > number:
                            print "Sorry this is not the correct answer  - try again! Little lower."
                        else:  # guess == number
                            print "Mindreader! You have entered the correct number!! That took you %d attempts. Let\'s play again!" % attempt
                            answer = raw_input("Do you want to play? Please, write number 1 to play or number 2 to exit ")
                    except ValueError:
                        print "ONLY NUMBERS between 1 and 10 please!"
            elif answer == 2:
                print "Goodbye and see you soon!"
                break
            else:
                print "Input numbers 1 or 2 only"
            break
    except ValueError:
            print "ONLY NUMBERS between 1 and 10 please!"
