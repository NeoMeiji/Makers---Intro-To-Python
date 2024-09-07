# Video alternative: https://vimeo.com/954334376/0c486313d0#t=625

# Here's a mindbender for you:

a = 10
b = 20
a = b
print(f"a is {a}")
print(f"b is {b}")

# @TASK: What does that output? And why? Take a guess, then
# run the code and see.

# I guess that "a" will be printed as 20 and "b" will be printed as 20 as the state of the program has been changed by the "a = b" statement, which will disregard the previous value of "a". 

# Was it what you expected?
# Yes it was exactly what I expected.

# My own example below:
anaconda = 25
batman = 10
charlie = 5

anaconda = batman
batman = charlie

print(f"anaconda is {anaconda}")
print(f"batman is {batman}")
print(f"charlie is {charlie}")

# Try to puzzle it out, and then move on to
# 020_state_tables.py
