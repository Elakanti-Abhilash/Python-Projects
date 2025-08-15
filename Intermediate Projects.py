# 1. Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# output
'''Enter a number: 17
17 is a prime number.'''

# 2. Fibonacci Number
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

terms = int(input("How many terms? "))
print("Fibonacci Series:")
for num in fibonacci(terms):
    print(num, end=' ')

# output
'''How many terms? 6
Fibonacci Series:
0 1 1 2 3 5'''

# 3. Palindrome Number
def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# output
'''Enter a number: 121
121 is a palindrome.'''

# 4. Reverse a Number
def reverse_number(n):
    is_negative = n < 0
    n = abs(n)
    reversed_str = str(n)[::-1]
    reversed_num = int(reversed_str)
    return -reversed_num if is_negative else reversed_num

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))

# output
'''Enter a number: 12345
Reversed number: 54321'''

# 5. Sorting a Numbers
def sort_ascending(numbers):
    return sorted(numbers)

def sort_descending(numbers):
    return sorted(numbers, reverse=True)

def sort_even_then_odd(numbers):
    return sorted(numbers, key=lambda x: (x % 2, x))

def sort_by_digits(numbers):
    return sorted(numbers, key=lambda x: len(str(abs(x))))

def sort_by_closeness(numbers, target):
    return sorted(numbers, key=lambda x: abs(x - target))

def display_menu():
    print("\nSorting Options:")
    print("1. Ascending Order")
    print("2. Descending Order")
    print("3. Even Numbers First, Then Odd")
    print("4. Sort by Number of Digits")
    print("5. Sort by Closeness to Target Number")

# Input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
display_menu()
choice = input("Choose an option (1-5): ")

# Process based on choice
if choice == '1':
    result = sort_ascending(numbers)
    print("Ascending:", result)
elif choice == '2':
    result = sort_descending(numbers)
    print("Descending:", result)
elif choice == '3':
    result = sort_even_then_odd(numbers)
    print("Even first, then odd:", result)
elif choice == '4':
    result = sort_by_digits(numbers)
    print("Sorted by digit count:", result)
elif choice == '5':
    target = int(input("Enter target number: "))
    result = sort_by_closeness(numbers, target)
    print(f"Sorted by closeness to {target}:", result)
else:
    print("Invalid choice.")
# output
'''Enter numbers separated by spaces: 14 3 78 5 900 21 1
Sorting Options:
1. Ascending Order
2. Descending Order
3. Even Numbers First, Then Odd
4. Sort by Number of Digits
5. Sort by Closeness to Target Number
Choose an option (1-5): 3
Even first, then odd: [14, 78, 900, 1, 3, 5, 21]
'''