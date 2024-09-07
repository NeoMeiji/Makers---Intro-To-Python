# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=726

from lib.helpers import check_that_these_are_equal

# Here's a great use for dictionaries: counting!

# For example, counting how many times each letter appears
# in a string.

# We can use a for loop to iterate over some items, and then
# use a dictionary to keep count of the items we've seen.

# In the process, you'll see a few dictionary functions at
# work, plus the sneaky addition of looping over characters
# in strings.

text = "the quick brush jumped over the lazy crab"

# We'll use a dictionary to keep count of the letters we've
# seen. We'll start with an empty dictionary:

letter_counts = {}
# The keys will be the letters, and the values will be the
# number of that letter we've seen.

# We'll use a for loop to iterate over each letter in the
# string:

for letter in text:
  # We'll check if the letter is already in our dictionary
  # of counts. We can do this using the `not in` operator.
  if letter not in letter_counts:
    # If it isn't, we'll add it to the dictionary with a
    # starting count of 1.
    letter_counts[letter] = 1
    # Note that the syntax for assigning a value to a key in
    # a dict is similar to assigning a variable.
  else:
    # If it is, we'll increment the count for that letter.
    letter_counts[letter] = letter_counts[letter] + 1

# Let's print out the dictionary to see what we've got:
print(letter_counts)

# If you're curious as to why we need to check if the letter
# is in the dictionary, try uncommenting this code and see
# what happens:

# letter_counts = {}
# for letter in text:
  # letter_counts[letter] = letter_counts[letter] + 1

# In the assignment above, our right hand expression tries
# to access the value for a key that has not been added yet.
# This causes an error.

# @TASK: Complete this exercise.

print("")
print("Function: count_words_by_length")

# Write this function that counts the number of words by
# how many letters they have. For example:

# words:  ["hat", "cat", "I", "bird"]
# result: {3: 2, 1: 1, 4: 1}
# Since there are two words of length 3, etc.

def count_words_by_length(words):
  word_length_frequency = {} # This creates an empty dictionary
  for word in words:         # This creates a "for" loop that looks at each word in the list
    word_length = len(word)  # This variable is created and assigned the value of the "len" operator which tells us the length of each word in the list
    if word_length not in word_length_frequency:  # The "if" statement then checks to see if a word of that length has been counted in the dictionary and is a conditional statement.
      word_length_frequency[word_length] = 1 # As is has NOT appeared within the EMPTY dictionary, then a value must be assigned (similarly like a variable) as there is 1 word with 3 characters e.g., "Hat"
    else: word_length_frequency[word_length] = word_length_frequency[word_length] + 1 # If it DOES appear, you have to add a value to the "else" expression otherwise it won't count the rest of the words
  return word_length_frequency #This then counts the number of words by how many letters they have, and calls upon the dictionary named "word_length_frequency"

check_that_these_are_equal(
  count_words_by_length(["hat", "cat", "I", "bird"]),
  {3: 2, 1: 1, 4: 1}
)

check_that_these_are_equal(
  count_words_by_length(["four", "four", "four", "one"]),
  {4: 3, 3: 1}
)

# Once you're done, move on to 039_challenge_1_example.py
