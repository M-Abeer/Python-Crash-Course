# Ctrl+Shift+F10-> to run

print("Hello World")
print("Abeer")

# Variable
age = 20
print(age)

# input

name = input("What is your name?")
print("Hello " + name)

# Type Conversion
birth_year = input("Enter your Birth Year: ")
# input will generate string
age = 2024 - int(birth_year)
print(age)

first = (float(input("Enter first num")))
second = int(input("Enter second num"))
sum = first+second
print("Sum is ", sum)

# String
course = 'Python for Beginner'
print(course.upper())
print(course)
print(course.find('n'))
print('Python' in course)

# Arithmetic Operator
print(10//3)

# Operator Precendance
print(10+3*2)

# Logical Operator
price = 20
print (price > 18 and price < 25)

# if else
temperature = 32
if temperature > 40:
    print("It is hot day!")
    print("Drink more Water")
elif temperature < 40:
    print("Nice Day")
else:
    print("It is cold day!")

# Quiz
weight = int(input("Enter Weight"))
unit = input("Kg(K) or Lbs(L)")
if unit == 'K':
    print("Weight in kg is:", weight/0.45)
elif unit == 'L':
    print("Weight in Lbs is:", weight*0.45)
else:
    print("Enter Correct option")

# While Loop
i=1
while i<5:
    print("Abeer")
    i=i+1

# Lists
names=['abeer','arreb','ali','uneeb']
print(names[0:3])
print(names)
print('abeer' in names)
(names.insert(0 , -1))
print(names)

# for loop
for item in names:
    print(item)

# range function
numbers= range(10)
for i in numbers:
    print(i)
# range(0,10,2)

# Tuples
# immutable objects

number=(1,2,3,4,5,6)
print(number.index(2))
# we cannot mutate objects