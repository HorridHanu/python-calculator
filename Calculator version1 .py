# CODE LANGUAGE IS PYTHON
# CODE BY HANU
# EDUCATIONAL PURPOSE ONLY!
# PROGRAME DATE : 20-JUNE-2021
# CODE FOR BASIC FAULTY CALCULATOR.
def addtion(num1, num2):
    print("After Addtion ", num1 + num2)


def substraction(num1, num2):
    print('After Substaction', num1 - num2)


def multiply(num1, num2):
    print('After Multiply', num1 * num2)


def divide(num1, num2):
    print('After Divide', num1 / num2)


print("\tPRESS")
print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Divide")
print("5.Exit!")
choice = int(input("enter your choice: "))
num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))
if choice == 1:
    addtion(num1, num2)
if choice == 2:
    substraction(num1, num2)
if choice == 3:
    multiply(num1, num2)
if choice == 4:
    divide(num1, num2)
