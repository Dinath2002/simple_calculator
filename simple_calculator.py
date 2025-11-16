#!/usr/bin/env python3
"""
Simple Calculator - A command-line calculator for basic arithmetic operations.

Supported operations:
    + : Addition
    - : Subtraction
    * : Multiplication
    / : Division
    ** : Exponentiation
    % : Modulo (remainder)
"""

from typing import Union


def get_number(prompt: str) -> float:
    """
    Get a valid number from user input.
    
    Args:
        prompt: The input prompt to display to the user.
        
    Returns:
        A float number entered by the user.
        
    Raises:
        ValueError: If the input is not a valid number.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_operator() -> str:
    """
    Get a valid operator from user input.
    
    Returns:
        A valid operator string (+, -, *, /, **, %).
    """
    valid_operators = {'+', '-', '*', '/', '**', '%'}
    while True:
        op = input("Enter operator (+, -, *, /, **, %): ").strip()
        if op in valid_operators:
            return op
        print("❌ Invalid operator! Please choose from: +, -, *, /, **, %")


def calculate(num1: float, num2: float, operator: str) -> Union[float, str]:
    """
    Perform the calculation based on the given operator.
    
    Args:
        num1: The first number.
        num2: The second number.
        operator: The operator to apply.
        
    Returns:
        The result of the calculation, or an error message string.
    """
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "❌ Error: Division by zero!"
            return num1 / num2
        elif operator == '**':
            return num1 ** num2
        elif operator == '%':
            if num2 == 0:
                return "❌ Error: Modulo by zero!"
            return num1 % num2
    except Exception as e:
        return f"❌ Error: {str(e)}"


def format_result(result: Union[float, str]) -> str:
    """
    Format the result for display.
    
    Args:
        result: The calculation result.
        
    Returns:
        A formatted string representation of the result.
    """
    if isinstance(result, str):
        return result
    
    # Remove trailing zeros and unnecessary decimal point
    if isinstance(result, float):
        if result == int(result):
            return str(int(result))
        return f"{result:.10g}"
    
    return str(result)


def main() -> None:
    """Main function to run the calculator."""
    print("\n" + "="*40)
    print("✨ Simple Calculator ✨")
    print("="*40 + "\n")
    
    try:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operator = get_operator()
        
        result = calculate(num1, num2, operator)
        formatted_result = format_result(result)
        
        print(f"\n{'─'*40}")
        print(f"{num1} {operator} {num2} = {formatted_result}")
        print(f"{'─'*40}\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Calculator closed by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
