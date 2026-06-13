# 1
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sum = x + y
print("The sum is:", sum)

#2
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sub = x - y
print("The subtraction result is:", sub)

#3
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

mul = x * y
print("The multiplication result is:", mul)

#4
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

div = x / y
print("The division result is:", div)

#5
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

mod = x % y
print("The remainder result is:", mod)

#6
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: ")) 

result = x // y
print("The floor division result is:", result)

#7
base = int(input("Enter the base number: "))
power = int(input("Enter the power number: "))

result = base ** power
print("The result is:", result)

#8
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x == y)

#9
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x != y)

#10
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x > y)

#11
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x < y)

#12
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x >= y)

#13
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(x <= y)

#14
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (True/False): ") == "True"

print((age >= 18) and citizen)

#15
student = input("Are you a student? (True/False): ") == "True"
premium = input("Do you have a premium membership? (True/False): ") == "True"

print(student or premium)

#16
experience = int(input("Enter years of experience: "))
rating = int(input("Enter performance rating: "))

print((experience >= 5) and (rating >= 4))

#17
marks = int(input("Enter your marks: "))
sports_quota = input("Sports quota? (True/False): ") == "True"

print((marks >= 80) or sports_quota)

#18
x = int(input("Enter a number: "))

print((x >= 1) and (x <= 100))

#19
x = int(input("Enter a number: "))

print(x % 2 == 0)

#20
value = input("Enter True or False: ") == "True"

print(not value)


