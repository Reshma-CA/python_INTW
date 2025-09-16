# 1. Bank Account System

# Problem: Create a BankAccount class with methods to deposit, withdraw, and check balance.

# Account created with balance 1000
# Deposit 500
# Withdraw 200
# Check Balance

# Deposited: 500
# Withdrawn: 200
# Current Balance: 1300

class Bank:
    def __init__(self, d,w):
        self.c= 1000
        self.d = d
        self.w = w
        
    
    def deposited(self):
        print(f"Deposited: {self.d}")
        
    
    def withdrawn(self):
        print(f"Withdrawn: {self.w}")
        
    def current_balance(self):
        print(f"Current balance :{self.c+self.d-self.w}")
        
d = int(input("Enter your deposited amount: "))
w = int(input("Enter your withdrawal amount: "))
        
obj = Bank(d,w)
obj.deposited()
obj.withdrawn()
obj.current_balance()


# Name: Alice
# Roll No: 101
# Marks: 85, 90, 80


# Sample Output:

# Student: Alice (101)
# Average: 85.0
# Grade: A

class Student:
    def __init__(self,name,roll_num,english_mark,science_mark,math_mark):
        self.name = name
        self.roll_num = roll_num
        self.english_mark = english_mark
        self.science_mark = science_mark
        self.math_mark = math_mark
        
    def display_average_grade(self):
        average =  (self.english_mark+self.science_mark+self.math_mark)/3
        print("Average: ",average)
        if average>=85:
            print(f" Grade : A")
            
        
obj = Student("Alice",101,85, 90, 80)
obj.display_average_grade()


# 3. Rectangle Area & Perimeter

# Problem: Create a Rectangle class with length and width. Add methods to calculate area and perimeter.
# Sample Input:

# Length = 5
# Width = 3


# Sample Output:

# Area: 15
# Perimeter: 16

class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
        
    def Area(self):
        print(f"Area : {self.l*self.w}")
        
    def Perimeter(self):
        perimeter = 2*(self.l+self.w)
        print(f"Perimeter: {perimeter}")
        
obj = Rectangle(5,3)
obj.Area()
obj.Perimeter()

# 4. Employee Salary Slip

# Problem: Create an Employee class with attributes: name, position, and base salary. Add a method to calculate net salary after tax (10%).
# Sample Input:

# Name: John
# Position: Developer
# Base Salary: 50000


# Sample Output:

# Employee: John (Developer)
# Net Salary: 45000

class Employee:
    def __init__(self,name,position,base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary
        
    def Salary(self):
        net_salary = self.base_salary - (self.base_salary*0.10)
        print(f"Employee: {self.name} ({self.position})")
        print(f"Net Salary: {net_salary}")
        
obj = Employee("John","Developer",50000)
obj.Salary()


# 5. Library Management

# Problem: Create a Book class with title, author, and availability status. Add methods to issue and return a book.
# Sample Input:

# Book: Python Basics by Mark
# Issue Book
# Return Book


# Sample Output:

# Book issued successfully
# Book returned successfully

class Book:
    def __init__(self,title,author,issue,returnd):
        self.title = title
        self.author = author
        self.issue = issue
        self.returnd =returnd
        
    def Issue(self):
        print(f"{self.title} by {self.author} {self.issue} Successfully")
        
    def Return(self):
        print(f"{self.title} by {self.author} {self.returnd} Successfully")
obj = Book("Python Basics","Mark","issued","returned")
obj.Issue()
obj.Return()


# 6. Car Speed Tracker

# Problem: Create a Car class with attributes model and speed. Add methods to accelerate and brake.
# Sample Input:

# Car: Tesla Model 3
# Accelerate by 20
# Brake by 5


# Sample Output:

# Current speed: 20
# Current speed: 15

class Car:
    def __init__(self, model,speed):
        self.model = model
        self.speed = speed
        self.break_power = 5
        
    def Accelerate(self):
        print(f"{self.model} Current speed: {self.speed}")
        
    def Brake(self):
        print(f"{self.model} Current speed: {self.speed - self.break_power}")
        
obj = Car("Tesla Model 3",20)
obj.Accelerate()
obj.Brake()

        
        