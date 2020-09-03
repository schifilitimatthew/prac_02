import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# It produced a random number between 5 and 20
#
# What was the smallest number you could have seen, what was the largest?
# Smallest - 5 Largest - 20
#
# What did you see on line 2?
# It produced a random number between 3 and 10 however they had to increments of 2 from 3
#
# What was the smallest number you could have seen, what was the largest?
# Smallest - 3 Largest - 9
#
# Could line 2 have produced a 4?
# No
#
# What did you see on line 3?
# It produced a random number between 2.5 and 5.5 with up to 16 decimals places (may of been default)
#
# What was the smallest number you could have seen, what was the largest?
# Smallest - 2.5 Largest - 5.5
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))