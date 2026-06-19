#1
def welcome_user(name):
    print("Welcome,", name + "!")

welcome_user("Prakash")

#2
def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

number = int(input("Enter a number: "))

check_even_odd(number)

#3
def check_even_odd(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

number = int(input("Enter a number: "))

check_even_odd(number)

#4
def check_voting_eligibility(age):
    if age >= 18:
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

age = int(input("Enter your age: "))

check_voting_eligibility(age)

#5
def calculate_discount(price):
    if price > 5000:
        discount = price * 0.10
    else:
        discount = 0

    print("Discount Amount: ", discount)

price = float(input("Enter product price: "))

calculate_discount(price)

#6
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

number = int(input("Enter a number: "))

print_numbers(number)

#7
def print_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i)

number = int(input("Enter a number: "))

print_even_numbers(number)

#8
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number: "))

multiplication_table(number)

#9
def reverse_countdown(num):
    while num > 0:
        print(num)
        num -= 1

number = int(input("Enter a number: "))

reverse_countdown(number)

#10
def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

number = int(input("Enter a number: "))

result = sum_numbers(number)

print(result)

#11
def square_number(num):
    return num * num

number = int(input("Enter a number: "))

result = square_number(number)

print(result)

#12
def count_positive_numbers(numbers):
    count = 0

    for num in numbers:
        if num > 0:
            count += 1

    return count

numbers = [1, -2, 3, -4, 5]

result = count_positive_numbers(numbers)

print(result, "Positive Numbers")

#13
def calculate_grade(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    else:
        print("Fail")

marks = int(input("Enter marks: "))

calculate_grade(marks)

#14
def print_odd_numbers(n):
    for i in range(1, n + 1, 2):
        print(i)

number = int(input("Enter a number: "))

print_odd_numbers(number)

#15
def login(username, password):
    if username == "admin":
        if password == "1234":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("Invalid User")

username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)

#Bonus Questions
#1
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

number = int(input("Enter a number: "))

result = factorial(number)

print(result)

#2
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

number = int(input("Enter a number: "))

result = reverse_number(number)

print(result)

#3
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

string = input("Enter a string: ")

result = count_vowels(string)

print(result)

#4
def guess_number(guess):
    secret_number = 7

    if guess == secret_number:
        print("Correct Guess")
    else:
        print("Try Again")

number = int(input("Enter your guess: "))

guess_number(number)

#5
def print_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

number = int(input("Enter a number: "))

print_pattern(number)

#Challenge question
def employee_bonus(name, salary, experience):
    bonus_percent = 0

    # If-Else + Nested If
    if experience >= 5:
        if salary < 50000:
            bonus_percent = 0.20
        else:
            bonus_percent = 0.10
    elif experience >= 3:
        bonus_percent = 0.10
    else:
        bonus_percent = 0.05

    bonus_amount = salary * bonus_percent
    final_salary = salary + bonus_amount

    for _ in range(1):
        print("Employee Name:", name)
        print("Salary:", salary)
        print("Bonus Amount:", bonus_amount)

    i = 1
    while i <= 1:
        print("Final Salary:", final_salary)
        i += 1

    return final_salary

emp_name = input("Enter employee name: ")
emp_salary = float(input("Enter salary: "))
emp_exp = int(input("Enter years of experience: "))

employee_bonus(emp_name, emp_salary, emp_exp)