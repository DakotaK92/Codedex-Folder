""" ================ Challenge 1 =================="""

"""
    Every year at the Oscars, the Academy Award for Best Picture is awarded to a single film. It's usually the last award presented and is considered to be the most prestigious.

    Let's use a Python list to document the recent winners!

    Start with the following list:

    best_pictures = [
    '2019 - Parasite',
    '2018 - Green Book',
    '2017 - The Shape of Water',
    '2016 - Moonlight',
    '2015 - Spotlight',
    '2014 - Birdman',
    '2013 - 12 Years a Slave',
    '2012 - Argo',
    '2011 - The Artist'
    ]
    Google the Best Picture winners from 2020, 2021, 2022, 2023, and 2024. Then, add them to the front of the best_pictures list.

    Lastly, print the best_pictures list. Make sure that the updated list starts with the winner for 2024, then 2023, then 2022, then 2021, then 2020, and so on.

    Note: Make sure to match the format of the existing list. And remember, it's the year of the movie, not the year of the ceremony.
"""

best_pictures = [
  '2024 - Anora',
  '2023 - Oppenheimer',
  '2022 - Everything Everywhere All at Once',
  '2021 - CODA',
  '2020 - Nomadland',
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist'
]

print(best_pictures)

""" ================ Challenge 2 =================="""

"""
    Suppose you and three of your friends all went out for a meal together. The bill comes due, and all of you decide to split the bill evenly.

    Here is a Python list of prices for what was ordered:

    bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

    Using this bill list, calculate the total amount and then divide it four ways.

    Initialize the total with zero and loop through the bill list to add everything up.

    With the total, store what each person has to pay in a my_share variable and then print the result to the terminal.
"""

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

for item in bill:
  total += item

my_share = total / 4

print(my_share)

""" ================ Challenge 3 =================="""

"""
    DNA is made of the following four pieces:

    Adenine (A)
    Cytosine (C)
    Guanine (G)
    Thymine (T)
    A DNA sequence is made of three-letter combinations of these pieces, such as 'ACG', TCA', and 'CGT'.

    Let's use a Python list to find a specific three-letter combination, starting with the following:

    dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

    Next, define two variables:

    item_to_find string that is set as a three-letter combination of your choice, with no spaces (e.g. 'TGA' or 'CAT').
    item_found boolean, initialized to False.
    Loop through each item in the dna_sequence list. Inside, use an if statement to test if a given item is equal to the item_to_find. If so, set item_found to True.

    Outside the loop, use an if/else statement to check if item_found is True:

    If so, print something like "Item Found!"
    Else, print something like "Item not found."
"""

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = "CAT"

item_found = False

for item in dna_sequence:
  if item == item_to_find:
    item_found = True

if item_found:
  print("Item Found!")
else:
  print("Item not found.")

""" ================ Challenge 4 =================="""
"""
    Many folks, especially around the holidays, carry a wishlist of things they've always wanted. Use Python lists to make your own wishlist!

    Create a list called wishlist and add three items to the list. Each item should be a string of something you've always wanted.

    Print the wishlist to the terminal to see all your wishes in one place!
"""
wishlist = ["A Baby", "A Career in Design", "House"]

print(wishlist)

""" ================ Challenge 5 =================="""
"""
    Are you feeling lucky? Let's replicate a small lottery that decides a winner based on random numbers. This challenge will use the random module.

    Create two empty lists called my_numbers and winning_numbers.

    Loop over a range of 5 steps (i.e., range(0,5)) and populate both lists with a random number between 1 and 69.

    Outside the loop, add one more number to each list that is between 1 and 26.

    Lastly, print the my_numbers and winning_numbers lists to the terminal. The output could look like this:

    My Numbers: [59, 66, 28, 52, 10, 12]
    Winning Numbers: [26, 27, 37, 35, 47, 8]
""" 

import random

my_numbers = []
winning_numbers = []

for i in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))

my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

print("My Numbers:", my_numbers)
print("Winning Numbers:", winning_numbers)