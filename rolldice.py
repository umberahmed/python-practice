"""This program will roll a dice and ask the user to guess the sum."""

from random import randint      # importing randit from random for number to guess
from time import sleep          # importing sleep to delay output and build player suspense

def get_user_guess():
    """Ask user to guess a number"""
    guess = int(raw_input("Guess a number: "))
    return guess

def roll_dice(number_of_sides = 6):

      first_roll = randint(1, number_of_sides)

      second_roll = randint(1, number_of_sides)

      max_val = number_of_sides * 2

      print "The maximum possible value is: %d" % max_val

      guess = get_user_guess()

      if guess > max_val:
          print "No guessing higher than the maximum possible value!"
      else:
          print "\nRolling..."
          sleep(2)
          print "The 1st roll is: %d" % first_roll
          sleep(1)
          print "The 2nd roll is: %d" % second_roll
          sleep(1)
          total_roll = first_roll + second_roll
          print "Result..."
          sleep(1)
          print "\n %d" % total_roll

          if guess == total_roll:
              print "You guessed correctly! You win!"
          else:
              print "You lose :-("

roll_dice(20)
