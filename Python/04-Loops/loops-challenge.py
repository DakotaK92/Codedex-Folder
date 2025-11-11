# ============= Challenge 1 =============
"""
  Instructions
  “Are we there yet?” is a phrase that has existed for as long as there are children, vehicles, and road trips.

  First, ask the user “Are we there yet?” using the input() function and store it in an answer variable.

  Then, create a while loop that asks the user “Are we there yet?” again. Keep asking them this over and over until they respond with “Yes”.

  The output could look something like this:

  Are we there yet? One more hour
  Are we there yet? Almost there
  Are we there yet? Don't make me pull over
  Are we there yet? Yes
"""

answer = input("Are we there yet? ")

while answer != "Yes":
  answer = input("Are we there yet? ")

print("Finally! We are there!")

# ============= Challenge 2 =============

"""
  Instructions
  Ring in the New Year! A New Year's Eve party doesn't feel complete without a countdown from 10 to 1.

  Use a for loop that counts down by using the "step" value in range().

  Inside the loop, print the numbers from 10 to 1, each on its own line.

  When the loop finishes the countdown, print this exact string Happy New Year! 🥳.

  The output should look like this:

  10
  9
  8
  7
  6
  5
  4
  3
  2
  1
  Happy New Year! 🥳
  Counting down from 10 to 1 on each line and then a Happy New Year message at the end.

  Note: Feel free to end your message with any emoji you want!
"""

for i in range (10, 0, -1):
  print(i)

print ("Happy New Year! 🥳")

# ============= Challenge 3 =============

"""
  Instructions
  Suppose we have a pair of dice. 🎲 🎲

  In dice games, "snake eyes" means rolling two 1s. Why is it called that? Because two small dots look like a pair of snake eyes. 🐍👀

  It’s the lowest possible roll (1 + 1 = 2) and is seen as bad luck. 😅

  Let's keep rerolling two dice until we get snake eyes.

  Nope
  Nope
  Nope
  Nope
  Snake eyes!

  First, use the random module to “roll” the two dice.

  Each die (named die1 and die2) should have an integer value from 1 to 6.

  Store the sum of the two random values in variable named total.

  Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.

  Let the loop run until the total is 2, then print 'Snake eyes!
"""

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

while total != 2:
  print("Nope")
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  total = die1 + die2

print("Snake eyes!")

# ============= Challenge 4 =============

"""
    Instructions
    Use only a for loop with range() and print() to display a staircase of asterisks in the terminal like this:

    *
    * *
    * * *
    * * * *
    * * * * *
    # ... and so on

    Be sure you start with a single * in the first line and end with 24 total asterisks on the last line.

    Note: Each * should have a space after it so they're spread out.
"""

for i in range(1, 25):
  print("* " * i)

# ============= Challenge 5 =============

"""
  Instructions
  A number is "squared" when it is either multiplied by itself or taken to the second power (e.g., 4² = 4 x 4 = 16).

  First, ask the user for an integer with int(input()) and store it in a number variable. Then, define a total variable with an initial value of 0.

  Note: You can pass a string prompt to int(input()).

  Next, use a for loop and range() function to calculate the total of the squares of all integers from 1 to that number.

  Last, print the output as an integer value.

  For example, if number is 5, the total should be 55 because:

  1 
  2
  +2 
  2
  +3 
  2
  +4 
  2
  +5 
  2
  
  =1+4+9+16+25
  =55
"""

number = int(input("Enter an integer: "))

total = 0

for i in range(1, number + 1):
  total += i ** 2

  print(total)
