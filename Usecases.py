'''A.Python is an indent based programming language
The following program throws an indentation error. Correct it and make sure it prints properly.'''

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
    print('Keep Learning and Exploring!')

'''B. Commented line in Python
Use Case 1:
Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.'''

#below are the student and trainer count of Data engineering batch in Inceptez
students = 100
trainers = 2
'''getting the total memmber count by adding student and trainer
Finally printing the total count'''
total = students + trainers
print(total)

'''Use Case 2:
Convert the below block into a “dead code” using comments, then re-activate it later to print'''

#print("Welcome to Inceptez Python Learning")

'''C. Playing with Quotes
Use Case 1:
Create three string variables that correctly store and print:

This is Inceptez's "Python" class for Data Engineers & AI Engineers
→ Use single, double, and triple quotes appropriately.'''

s1='This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'
s2="This is Inceptez's \"Python\" class for Data Engineers & AI Engineers"
s3='''This is Inceptez's "Python" class for Data Engineers & AI Engineers'''
print(s1)
print(s2)
print(s3)

'''Use Case 2:
Write a multiline string using triple quotes that prints:

Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.'''

multiline_str='''Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.'''
print(multiline_str)

'''D. Let's learn all about VARIABLES
Use Case 1:
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)

Then print a formatted message:

Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologie'''
Student_Name='Divya'
Course_Name='Python Fundamentals'
Training_Institute_Name='Inceptez Technologies'
print(f'Name: {Student_Name} is learning the course {Course_Name} at the institute {Training_Institute_Name}')

'''Use Case 2:
Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing character also by operating it with Eighteen percent gst
'''
fee = 45000
print(type(fee))
fee=fee+fee*0.18
print(fee,type(fee))
#print(fee+'Eighteen percent gst')

'''E. Variables Naming Conventions
Use Case 1:
Identify which variable names below are invalid for Inceptez’s student database:
'''
#2student = 'Ravi' #invalid
_student_id = 1001 #valid
studentName = 'Priya' #valid
#class name = 'Python' #invalid
inceptez_batch = 'Morning' #valid


'''Use Case 2:
Declare 3 variables following naming styles for Inceptez projects:

PascalCase: DataEngineeringBatch
camelCase: dataEngineeringBatch
snake_case: data_engineering_batch'''

Pascal_Case= 'DataEngineeringBatch'
camel_Case= 'dataEngineeringBatch'
snake_case= 'data_engineering_batch'

'''F. Type identification & Casting
Use Case 1:
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
Example:
Enter your age: 40
You will retire in 20 years at Inceptez Technologies.'''

age=input('Enter your age: ')
print(isinstance(age,str))
age=int(age)
retirement=60-age
print(f'You will retire in {retirement} years at Inceptez Technologies')

'''Use Case 2 (Debug):
Fix the type error in the following code for salary calculation:

salary = '50000'
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)'''

salary = 50000
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

'''G. Data types and casting
Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
employee_name (string)
base_salary (float)
hra_percent (integer)
bonus_amount (float)
B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount
C. Print the output like this:
'''
employee_name=input('Enter your employee name: ')
base_salary=float(input('Enter your base salary in : '))
hra_percent=int(input('Enter your hra percentage: '))
bonus_amount=float(input('Enter your bonus amount: '))
HRA = base_salary * (hra_percent / 100)
Total_Salary = base_salary + HRA + bonus_amount
print(f'Employee : {employee_name}\nBase Salary: {base_salary}\nHRA @ {hra_percent}%:{HRA}\nBonus: {bonus_amount}\nTotal Salary Payable: {Total_Salary}' )

'''Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify (try using if condition with the help of AI, however we will learn about if condition soon):
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.'''

while True:
    mark=input('Enter your marks: ')
    try:
        mark=float(mark)
        if mark >= 90:
            print('Outstanding')
        elif mark >= 75:
            print('Excellent')
        elif mark >= 50:
            print('Pass')
        elif mark<50:
            print('Fail')
        break
    except ValueError as e:
        print('Invalid marks entered — Please provide numeric input')
    except Exception as e:
        print(f'error message is :{e}')

'''Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)'''
item_name = input("Enter product name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))
total_cost = price * quantity
print(f'You purchased {quantity} units of {item_name}')
print(f'Total payable: {total_cost} INR')

'''H. Python Operators Usecases
Use Case 1: Internet Data Usage Calculator
Write a program that asks the user for:
Total monthly data limit (in GB)
Data used so far (in GB)
Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
Remaining data
Usage percentage rounded to 2 decimals
If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."'''
data_limit=int(input('Enter the Total monthly data limit in GB: '))
data_used=float(input('Enter the Data used so far in GB : '))
Remaining_data = data_limit - data_used
Usage_percentage = round((data_used / data_limit) * 100,2)
print(f'Remaining data available: {Remaining_data} GB\nso far used data percentage:{Usage_percentage}%')
if Usage_percentage >=80:
    print('Warning: High usage, consider upgrading your plan.')

'''Use Case 2: Shopping Discount Calculation
Write a program that takes:
Original price (float)
Discount percent (int)
Using assignment and arithmetic operators, calculate:
 Discount amount = (price * discount_percent) / 100
 Final price = price - discount_amount
Print:
 Original price, discount applied, and final payable amount'''
original_price=float(input('Enter the Original price : '))
discount_percent=int(input('Enter the Discount percent : '))
discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount
print(f'Original price:{original_price}\ndiscount applied:{discount_amount}\nfinal payable amount:{final_price}')

'''Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")
Expected behavior:
Convert age to integer before comparison.
Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).
'''
age = int(input("Enter age: "))
citizen = input("Are you an Indian citizen? (yes/no)")
if age >= 18 and citizen.lower() == "yes":
 print("Eligible to vote")
else:
 print("Not eligible")

 '''Use Case 1: Banking Eligibility Check
 Write a program that asks the user for:
     Age, Monthly income
 Conditions:
 If age < 18: print "Not eligible for a bank account."
 If age >= 18 and income < 15000: print "Eligible for basic savings account."
 If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
 If age >= 18 and income > 50000: print "Eligible for premium account."
'''
age = int(input("Enter age: "))
monthly_income = int(input("Enter the Monthly income: "))
if age < 18:
 print("Not eligible for a bank account.")
elif age >= 18 and monthly_income < 15000:
    print("Eligible for basic savings account.")
elif age >= 18 and (monthly_income >= 15000 and monthly_income <= 50000):
    print("Eligible for savings + salary account.")
elif age >= 18 and monthly_income > 50000:
    print("Eligible for premium account.")
#Use Case 2: Check room availability
room_availability = input("Enter whether the room is available yes/no: ")
guest_status= input("Enter you are a VIP/member: ")
if room_availability.lower() =='yes' and guest_status.upper()=='VIP':
 print("As you are a VIP complimentary upgrade is available")
elif room_availability.lower() =='yes' and guest_status.lower() =='member':
    member_years=int(input("Enter the years you were a member: "))
    if member_years >=5:
        print(f"As you are a member for {member_years}years We are Offering discount")
    else:
        print(f"As you are a member for {member_years}years only Standard price")
else:
    print('No rooms available')

'''Use Case 3 (Bug Fixing): Nested Condition Logic Issue
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")'''

temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
 print("Normal temperature")
elif temp >= 37 and temp <= 39:
 print("Fever")
else:
 print("High fever")

'''J. Looping Constructs
Use Case 1: Table Generator
 Write a program that takes a number from the user and prints the multiplication table from 1 to 10 for that number.
'''
num = int(input("Enter any number: "))
for i in range(1,11):
    mul=num*i
    print(f'{num}x{i}={mul}')

'''Use Case 3 (Bug Fixing): Infinite Loop Issue
 Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed.'''
i = 1
while i<= 10:
     print(i)
     i=i+1

'''K. Collection Types
Use Case 1: Product Price Lookup
Create a dictionary with at least 5 products and their prices.
Ask the user to enter a product name.
If found, print the price.'''

'''Use Case 3 (Bug Fixing): List Index Error
 Fix the following code so that it prints all items correctly without an index error:
Incorrect code:
items = ["Pen", "Book", "Mouse", "Keyboard"]
 i = 0
 while i <= len(items):
 print(items[i])
 i = i + 1
Expected behavior:
 The loop should print all the items exactly once and exit without an error.'''

items = ["Pen", "Book", "Mouse", "Keyboard"]
i = 0
while i < len(items):
    print(items[i])
    i = i + 1

'''L. Exception Handling
Use Case 1: Division Safe Calculator
 Ask the user for two numbers.
 Perform division and print the result.
 If the user tries to divide by 0, print:
 "Error: Division by zero is not allowed."'''

try:
    a=int(input('Enter the number: '))
    b=int(input('Enter the number: '))
    c=a/b
    print(f'{a}/{b} is {c}')
except Exception as e:
    print('Error: Division by zero is not allowed.')

'''Use Case 2: Safe Integer Input
Ask the user to enter a number.
Try converting it to an integer.
If conversion fails, print:
"Invalid input. Please enter a numeric value."'''

try:
    a=input('Enter the number: ')
    b=int(a)
    print(f'Entered number is {b}')
except ValueError as e:
    print('Invalid input. Please enter a numeric value.')
except Exception as e:
    print(e)

'''Use Case 3 (Bug Fixing): Multiple Exception Handling
 Fix the below code so it handles both invalid input and division by zero correctly.
Incorrect code:
num1 = int(input("Enter number 1: "))
 num2 = int(input("Enter number 2: "))
 result = num1 / num2
 print("Result:", result)
Expected behavior:
If user enters non-numeric values → print "Invalid input"
If num2 is zero → print "Cannot divide by zero."
Otherwise print the result.'''

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1 / num2
    print("Result:", result)
except ValueError as e:
    print('Invalid input. Please enter a numeric value.')
except ZeroDivisionError as e:
    print('Cannot divide by zero.')
except Exception as e:
    print(e)





