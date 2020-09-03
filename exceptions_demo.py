"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input to either the numerator or denominator is not a integer.

2. When will a ZeroDivisionError occur?
When the input to the denominator is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
You could use a while loop to varify that the denominator isn't 0.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")