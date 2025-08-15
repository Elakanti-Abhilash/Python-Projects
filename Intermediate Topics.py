# 1. List Comprehension
'''A concise way to create a new list by applying an expression
to each item in an iterable.'''

squares = [x**2 for x in range(5)]
print(squares)

# Output:
'''[0, 1, 4, 9, 16]'''

# 2. Map, Filter, Reduce: Used for functional programming in Python.
'''map(): Applies a function to all items.

filter(): Filters items using a condition.

reduce(): Reduces a list to a single value (from functools).'''

from functools import reduce
nums = [1, 2, 3, 4]
mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
reduced = reduce(lambda x, y: x + y, nums)

print("Mapped:", mapped)
print("Filtered:", filtered)
print("Reduced:", reduced)

# Output:
'''Mapped: [2, 4, 6, 8]
Filtered: [2, 4]
Reduced: 10'''

# 3. OOP - Classes and Objects
'''Object-Oriented Programming allows you to model 
real-world entities using classes.'''

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Abhi")
print(p.greet())

# Output:
'''Hi, I'm Abhi'''
