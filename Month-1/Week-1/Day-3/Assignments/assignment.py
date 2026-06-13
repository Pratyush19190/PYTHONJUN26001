#1
name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")

print("\n----- User Information -----")
print("Name:", name)
print("Age:", age)
print("City:", city)

#2
age = int(input("Enter Age: "))

if age >= 18:
    print("\nYou are eligible to vote.")
else:
    print("\nYou are not eligible to vote.")
    
#3
num = int(input("Enter Number: "))

if num % 2 == 0:
    print(f"\n{num} is an Even Number")
else:
    print(f"\n{num} is an Odd Number")
    
#4
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("\nGrade A")
elif marks >= 70:
    print("\nGrade B")
elif marks >= 40:
    print("\nGrade C")
else:
    print("\nFail")
    
#5
emp_id = input("Is Employee ID valid? (yes/no): ")
wifi = input("Connected to Office Wi-Fi? (yes/no): ")

if emp_id == "yes":
    if wifi == "yes":
        print("Access Granted")
    else:
        print("Connect to Office Wi-Fi")
else:
    print("Access Denied")
    
#6
marks = int(input("Enter Marks: "))
income = int(input("Enter Family Income : "))

if marks >= 85:
    if income < 500000:
        print("Scholarship Approved")
    else:
        print("Scholarship Rejected")
else:
    print("Scholarship Rejected")
    
#7
for i in range(1, 21):
    print(i)
    
#8
for i in range(2, 51, 2):
    print(i)
    
#9
num = int(input("Enter Number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
#10
for i in range(20, 0, -1):
    print(i)
    
#11
i = 1

while i <= 10:
    print(i)
    i += 1
    
#12
i = 10

while i >= 1:
    print(i)
    i -= 1
    
#13
sum = 0

for i in range(1, 101):
    sum = sum + i

print("Sum =", sum)

#14
count = 0

for i in range(1, 101):
    if i % 5 == 0:
        count += 1

print("Total Numbers Divisible by 5 =", count)

#15
balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("\nEnter Choice: "))

if choice == 1:
    print("\nCurrent Balance: ", balance)

elif choice == 2:
    amount = int(input("Enter Amount to Deposit: "))
    balance = balance + amount
    print("Updated Balance: ", balance)

elif choice == 3:
    amount = int(input("Enter Amount to Withdraw: "))
    
    if amount <= balance:
        balance = balance - amount
        print("Updated Balance: ", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")