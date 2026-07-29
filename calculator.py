import math

# Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def square_root(a):
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Factorial not possible"
    return math.factorial(int(a))


# Main Program
while True:
    print("\n******** CALCULATOR ********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 10:
        print("Calculator Closed")
        break

    elif choice >= 1 and choice <= 6:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", add(a, b))
        elif choice == 2:
            print("Result =", sub(a, b))
        elif choice == 3:
            print("Result =", mul(a, b))
        elif choice == 4:
            print("Result =", div(a, b))
        elif choice == 5:
            print("Result =", mod(a, b))
        elif choice == 6:
            print("Result =", power(a, b))

    elif choice == 7:
        a = float(input("Enter a number: "))
        print("Result =", square(a))

    elif choice == 8:
        a = float(input("Enter a number: "))
        print("Result =", square_root(a))

    elif choice == 9:
        a = int(input("Enter a number: "))
        print("Result =", factorial(a))

    else:
        print("Invalid Choice")
