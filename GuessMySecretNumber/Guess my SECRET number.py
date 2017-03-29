# -*- coding: utf-8 -*-
name = raw_input("What is your name?")
print "Hello, %s!" % name
print "Let's play GUESS MY SECRET NUMBER!"
import random
number = random.randrange (1,10)
guess = ""
tries = 0

while guess != number:
    try:
        guess = int(raw_input("Please enter the number between 1 and 10: "))
        tries = tries + 1
        if guess < number:
            print "Sorry this is not the correct answer - try again! Little higher."
        elif guess > number:
            print "Sorry this is not the correct answer  - try again! Little lower."
        else: #guess == number
            print "Mindreader! You have entered the correct number!! That took you %d attempts" % tries
            break
    except ValueError:
            print "ONLY NUMBERS between 1 and 10 please!"

