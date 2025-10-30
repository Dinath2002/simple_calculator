# simple_calculator.py

print("Simple Calculator")
print("------------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator."

print("Result:", result)
