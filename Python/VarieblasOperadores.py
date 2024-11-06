##Declaration and Assignment of Variables
name = "Juan"
age = 25
height = 1.75
is_student = True

"""Arithmetic
Arithmetic operators are used to perform basic mathematical operations. The main arithmetic operators in Python are:

Addition (+): adds two values.
Subtraction (-): subtracts the second value from the first.
Multiplication (*): multiplies two values.
Division (/): divides the first value by the second and returns a floating-point result.
Floor Division (//): divides the first value by the second and returns an integer result (the decimal part is discarded).
Modulus (%): returns the remainder of the division between the first value and the second.
Exponentiation (**): raises the first value to the power of the second."""

a = 10
b = 3 
sum = a + b   # 13
subtraction = a - b    # 7
multiplication = a * b    # 30
division = a / b   # 3.333333333
floor_division = a // b   # 3
modulus = a % b   # 1
exponentiation = a ** b   # 1000

"""
Comparison
Comparison operators are used to compare two values and return a boolean value (True or False) based on the result of the comparison. The comparison operators in Python are:

Equal to (==): returns True if both values are equal.
Not equal to (!=): returns True if the values are different.
Greater than (>): returns True if the first value is greater than the second.
Less than (<): returns True if the first value is less than the second.
Greater than or equal to (>=): returns True if the first value is greater than or equal to the second.
Less than or equal to (<=): returns True if the first value is less than or equal to the second.
"""
a = 10
b = 3


equal = a == b   # False
not_equal = a != b   # True
greater_than = a > b   # True
less_than = a < b   # False
greater_or_equal = a >= b   # True
less_or_equal = a <= b   # False

"""
Logical
Logical operators are used to combine conditional expressions and evaluate multiple conditions. The logical operators in Python are:

AND (and): returns True if both conditions are true.
OR (or): returns True if at least one of the conditions is true.
NOT (not): inverts the value of a condition, returns True if the condition is false and False if the condition is true.
"""

a = 10
b = 3


result_and = (a > 5) and (b < 5)   # True
result_or = (a > 15) or (b < 5)   # True
result_not = not (a > 5)   # False