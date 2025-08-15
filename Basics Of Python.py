# 1. Variables and Data Types:Variables are containers to store data. Data types define the type of data like numbers, text, or true/false.

name = "Abhi"         # str (string)
age = 25               # int (integer)
height = 5.6           # float (decimal)
is_student = True      # bool (boolean)

print(name)
print(age)
print(height)
print(is_student)
# Output:
'''Abhi
25
5.6
True'''

# 2. Conditional Statements (if, elif, else): Used to make decisions. It runs different code based on whether conditions are true or false.

age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
# Output:
'''You just became an adult!'''

# 3. Loops (for and while): Loops are used to repeat code. `for` loops go through a sequence. `while` loops run as long as a condition is true.

# for loop
for i in range(3):
    print("Hello")

# while loop
count = 1
while count <= 3:
    print("Bye")
    count += 1
# Output:
'''Hello
Hello
Hello
Bye
Bye
Bye'''

# 4. Functions: Functions are reusable blocks of code that perform a specific task.

def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")
# Output:

'''Hello, Alice
Hello, Bob'''

# 5. Lists and Dictionaries:

'''List: Ordered, changeable collection (like an array).
Dictionary: Key-value pairs for storing related data.'''

# List example
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # banana

# Dictionary example
person = {"name": "Alice", "age": 25}
print(person["name"])

# Output:

'''banana
Alice'''

