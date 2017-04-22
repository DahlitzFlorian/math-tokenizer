"""
Includes a self-made tokenizer to split the function into tokens
"""
import re


def tokenize(function: str) -> dict:
    operators = ["+", "-", "*", "/", "^"]
    result = {}

    # remove spaces
    function = re.sub("\s", "", function)

    for i, char in enumerate(function):
        if char.isdigit():
            result[i] = ("Literal", char)
        elif char.isalpha():
            result[i] = ("Variable", char)
        elif char in operators:
            result[i] = ("Operator", char)
        elif char == "(":
            result[i] = ("Left Parenthesis", char)
        elif char == ")":
            result[i] = ("Right Parenthesis", char)
    
    return result

print(tokenize("2x^2+4x-3"))