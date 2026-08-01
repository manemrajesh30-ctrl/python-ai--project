# ============================================================
# CODOMAX DIGITAL SOLUTIONS
# TASK 2 - INTRODUCTION TO AI AND PYTHON
# ============================================================

print("=" * 60)
print("CODOMAX DIGITAL SOLUTIONS")
print("TASK 2 - INTRODUCTION TO AI AND PYTHON")
print("=" * 60)


# ------------------------------------------------------------
# 1. VARIABLES AND DATA TYPES
# ------------------------------------------------------------

print("\n1. VARIABLES AND DATA TYPES")

name = "Student"
age = 20
height = 5.7
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("Name type:", type(name))
print("Age type:", type(age))
print("Height type:", type(height))
print("Is Student type:", type(is_student))


# ------------------------------------------------------------
# 2. ARITHMETIC OPERATORS
# ------------------------------------------------------------

print("\n2. ARITHMETIC OPERATORS")

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# ------------------------------------------------------------
# 3. CONDITIONAL STATEMENTS
# ------------------------------------------------------------

print("\n3. CONDITIONAL STATEMENTS")

marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# ------------------------------------------------------------
# 4. FOR LOOP
# ------------------------------------------------------------

print("\n4. FOR LOOP")

for i in range(1, 11):
    print(i)


# ------------------------------------------------------------
# 5. WHILE LOOP
# ------------------------------------------------------------

print("\n5. WHILE LOOP")

count = 1

while count <= 5:
    print(count)
    count += 1


# ------------------------------------------------------------
# 6. LIST
# ------------------------------------------------------------

print("\n6. LIST")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)
print("First fruit:", fruits[0])

fruits.append("Grapes")

print("After adding Grapes:", fruits)


# ------------------------------------------------------------
# 7. TUPLE
# ------------------------------------------------------------

print("\n7. TUPLE")

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)
print("First element:", numbers[0])
print("Length:", len(numbers))


# ------------------------------------------------------------
# 8. DICTIONARY
# ------------------------------------------------------------

print("\n8. DICTIONARY")

student = {
    "name": "Student",
    "age": 20,
    "course": "AI and ML"
}

print("Student Details:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# ------------------------------------------------------------
# 9. FUNCTIONS
# ------------------------------------------------------------

print("\n9. FUNCTIONS")


def add_numbers(a, b):
    return a + b


def greet(name):
    return "Hello " + name


result = add_numbers(10, 20)

print("Sum:", result)
print(greet("Student"))


# ------------------------------------------------------------
# 10. EVEN OR ODD
# ------------------------------------------------------------

print("\n10. EVEN OR ODD")

number = 15

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# ------------------------------------------------------------
# 11. FACTORIAL
# ------------------------------------------------------------

print("\n11. FACTORIAL")

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of", number, "is", factorial)


# ------------------------------------------------------------
# 12. FIBONACCI SERIES
# ------------------------------------------------------------

print("\n12. FIBONACCI SERIES")

n = 10
first = 0
second = 1

print("Fibonacci Series:")

for i in range(n):
    print(first, end=" ")
    first, second = second, first + second

print()


# ------------------------------------------------------------
# 13. PRIME NUMBER
# ------------------------------------------------------------

print("\n13. PRIME NUMBER")

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")


# ------------------------------------------------------------
# 14. SIMPLE CALCULATOR
# ------------------------------------------------------------

print("\n14. SIMPLE CALCULATOR")

a = 20
b = 5
operator = "+"

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"

print("First number:", a)
print("Second number:", b)
print("Operator:", operator)
print("Result:", result)


# ------------------------------------------------------------
# 15. FIND LARGEST NUMBER
# ------------------------------------------------------------

print("\n15. FIND LARGEST NUMBER")

numbers = [25, 10, 45, 30, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number:", largest)


# ------------------------------------------------------------
# 16. COUNT VOWELS
# ------------------------------------------------------------

print("\n16. COUNT VOWELS")

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"
vowel_count = 0

for character in text:
    if character in vowels:
        vowel_count += 1

print("Text:", text)
print("Number of vowels:", vowel_count)


# ------------------------------------------------------------
# 17. REVERSE A STRING
# ------------------------------------------------------------

print("\n17. REVERSE A STRING")

text = "Python"

reverse_text = text[::-1]

print("Original:", text)
print("Reversed:", reverse_text)


# ------------------------------------------------------------
# 18. SUM OF LIST
# ------------------------------------------------------------

print("\n18. SUM OF LIST")

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    total += number

print("Numbers:", numbers)
print("Sum:", total)


# ------------------------------------------------------------
# 19. CLASS AND OBJECT
# ------------------------------------------------------------

print("\n19. CLASS AND OBJECT")


class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Student", "AI and ML")

student1.display()


# ------------------------------------------------------------
# 20. FINAL MESSAGE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TASK 2 COMPLETED SUCCESSFULLY!")
print("=" * 60)