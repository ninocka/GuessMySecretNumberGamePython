# This Python file uses the following encoding: utf-8
#TEST za čžš
import random
a = "č, ž, š"
print "To je le test: " + a

print "Welcome! It is nice to see you! Let\'s play and have fun!"
name = raw_input("But first, what is your name?")
print "Hello, %s!" % name
print "Let's play GUESS MY SECRET NUMBER!"
def play(): #saving play for reuse
    number = random.randrange (1,10)
    guess = ""
    attempt = 0
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
        else: #guess == number
            print "Mindreader! You have entered the correct number!! That took you %d attempts. Let\'s play again!" % attempt
            break
     except ValueError:
            print "ONLY NUMBERS between 1 and 10 please!"

while True:
        answer = input("Do you want to play? Please, write number 1 to play or number 2 to exit ")
        if answer == 1:
         play()
        elif answer == 2:
            print "Goodbye and see you soon!"
            break
        else:
            print "Input numbers 1 or 2 only"

