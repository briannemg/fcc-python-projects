"""
Module Name: arithmetic_arranger.py
Author: briannemg
Date: 2025-08-18
Description:
    A Python module containing a function to format arithmetic problems vertically.
    Example: converts "235 + 52" to:

      235
    +  52
    ----- 

Usage:
    Import the module and call the `arithmetic_arranger` function.

Notes:
    - Supports addition and subtraction only.
    - Limits to a maximum of five problems.
    - Returns formatted string for printing.

"""

from typing import List

def arithmetic_arranger(problems: List[str], show_answers: bool = False) -> str:
    """
    Arrange and format a list of arithmetic problems vertically.

    Args:
        problems (List[str]): Each string is an arithmetic problem, e.g., "32 + 698".
        show_answers (bool, optional): If True, include the solutions in the output. Default is False.

    Returns:
        str: A string containing the vertically arranged problems, ready to print.

    Raises:
        ValueError: If there are more than five problems, unsupported operators,
                    numbers with more than four digits, or non-digit inputs.

    Example:
        >>> arithmetic_arranger(["32 + 698", "3801 - 2"])
           32      3801
        + 698     -   2
        -----     -----
    """

    if len(problems) > 5:
        raise ValueError("Error: Too many problems.")
    
    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            raise ValueError("Error: Each problem must contain two operands and an operator.")
        
        num1, operator, num2 = parts

        if operator not in ("+", "-"):
            raise ValueError("Error: Operator must be '+' or '-'.")
        
        if not (num1.isdigit() and num2.isdigit()):
            raise ValueError("Error: Numbers must only contain digits.")
        
        if len(num1) > 4 or len(num2) > 4:
            raise ValueError("Error: Numbers cannot be more than four digits.")
        
        width = max(len(num1), len(num2)) + 2  # 2 spaces for operator and at least one space

        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes.append("-" * width)

        if show_answers:
            result = str(eval(problem))
            results.append(result.rjust(width))

    arranged_problems = "    ".join(first_line) + "\n" + \
                        "    ".join(second_line) + "\n" + \
                        "    ".join(dashes)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


# Main testing block to allow running this script directly
if __name__ == "__main__":
    example_problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    
    print("Arithmetic problems arranged without answers: \n")
    print(arithmetic_arranger(example_problems))

    print("\nArithmetic problems arranged with answers:\n")
    print(arithmetic_arranger(example_problems, show_answers=True))