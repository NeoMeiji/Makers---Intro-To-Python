# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=0

from lib.helpers import check_that_these_are_equal

# Mapping is going through a list and converting ('mapping')
# each item to another item. This is useful when you want
# to perform the same operation across a list of items.

# For example:

# * Getting the price of each item in a list of products
# * Making each item in a list of words uppercase
# * Finding the first letter of each item in a list of words

# Here's an example:

words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again

for word in words: # We go through each word
  first_letter = word[0] # Get the first letter
  # And append it to our accumulator list:
  first_letters.append(first_letter)

print(words)
print(first_letters)

# @TASK: run this program to see what it does.

# @TASK: Complete this exercise.

print("")
print("Function: add_one_hundred_to_numbers")

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
  added_numbers = []
  for number in numbers:
    added_numbers.append(number + 100)
  return added_numbers

check_that_these_are_equal(
  add_one_hundred_to_numbers([1, 2, 3, 4]), [101, 102, 103, 104])
check_that_these_are_equal(
  add_one_hundred_to_numbers([2, 3, 4, 5]), [102, 103, 104, 105])

# My own example below:

def add_two_hundred_and_fifty_five_to_numbers(list_of_numbers):
  numbers_added = []
  for parameters in list_of_numbers:
    numbers_added.append(parameters + 255)
  return numbers_added

check_that_these_are_equal(
  add_two_hundred_and_fifty_five_to_numbers([1, 2, 3, 4]), [256, 257, 258, 259])
check_that_these_are_equal(
  add_two_hundred_and_fifty_five_to_numbers([2, 3, 4, 5]), [257, 258, 259, 260])

# Accumulator Variable > "[]" = It's where we put our summary value + It starts off blank.

# Cannot use just ANY accumulator variable such as "" as it does not work and returns the following error:
# AttributeError: 'str' object has no attribute 'append'

# When you're done, move on to 036_filtering.py