# Program 1(a)
# Write a program to print the multiplication table for the given
# number?

num1 = int(input("Enter a number:"))
for i in range(1, 11):
    print(i*num1)

# Program 1(b)
# Write a program to find factorial of a number

def fact(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact

num2 = int(input("Enter a num:"))
print(fact(num2))

# Program 1(c)
# Write a program to check whether the given number isprime
# or not?

def check(n):
    for i in range(2, n):
        if n % 2 == 0:
            print("Not a prime")
            break
    else:
            print("Prime Number")

num3 =int(input("Enter a num:"))
check(num3)



