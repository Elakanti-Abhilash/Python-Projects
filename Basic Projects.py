# 1. Simple Calculator
'''Create a game where the program randomly selects a
number between 1 and 100. The user has to guess the number. 
After each guess, the program should tell the user whether 
the guess was too low, too high, or correct. Limit the
number of guesses to 7.'''
import random

number_to_guess = random.randint(1, 100)
attempts = 7

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100. You have 7 attempts.")

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}: Your guess: "))
    if guess == number_to_guess:
        print("🎉 Congratulations! You guessed the number!")
        break
    elif guess < number_to_guess:
        print("Too low.")
    else:
        print("Too high.")
else:
    print("Sorry, you've used all your attempts. The number was", number_to_guess)
    
 # output:
'''Welcome to the Number Guessing Game!
Guess a number between 1 and 100. You have 7 attempts.
Attempt 1: Your guess: 40
Too low.
Attempt 2: Your guess: 70
Too high.
Attempt 3: Your guess: 55
🎉 Congratulations! You guessed the number!'''

# 2. Basic Calculator
'''Create a calculator that performs addition, 
subtraction, multiplication, and division. The 
user should enter two numbers and an operator. 
Based on the operator, the correct operation 
is performed.'''
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if a == 0:
            return "Cannot divide by zero!"
        return a / b
    else:
        return "Invalid operator."
# Input
n1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

# Output
result = calculator(n1, n2, op)
print("Result:", result)
'''Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 2
Result: 5.0'''

# 3. Student Grade Checker
'''Write a program that takes marks of 5 subjects
from a student. Calculate the total, average, and
assign a grade based on the average:

A: 90+
B: 80-89
C: 70-79
D: 60-69
F: <60'''
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = []

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: "))
    marks.append(score)

total = sum(marks)
average = total / len(subjects)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\n--- Report Card ---")
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)

# Output:
'''Enter marks for Math: 85
Enter marks for Science: 90
Enter marks for English: 88
Enter marks for History: 80
Enter marks for Computer: 95

--- Report Card ---
Total Marks: 438.0
Average Marks: 87.6
Grade: B
'''