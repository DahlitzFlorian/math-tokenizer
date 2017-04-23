"""
Includes a self-made tokenizer to split the function into tokens
"""
import re


def tokenize(function: str) -> dict:
    operators = ["+", "-", "*", "/", "^"]
    r = 0
    result = {}
    intermediate_result1 = [0,]
    intermediate_result2 = []

    # remove spaces
    function = re.sub("\s", "", function)

    for char in function:
        # dedicate a type to each value (char)
        # and allocate it to intermediate_result2
        if char.isdigit():
            intermediate_result2.append("Literal")
            intermediate_result2.append(char)
        elif char.isalpha():
            intermediate_result2.append("Variable")
            intermediate_result2.append(char)
        elif char in operators:
            intermediate_result2.append("Operator")
            intermediate_result2.append(char)
        elif char == "(":
            intermediate_result2.append("Left Parenthesis")
            intermediate_result2.append(char)
        elif char == ")":
            intermediate_result2.append("Right Parenthesis")
            intermediate_result2.append(char)
        
        # checks if values of same type occur in a row
        # and have to be put together
        # e.g. '2' and '3' have to be handled as '23'
        # therefore intermediate_result1 exists
        # if they don't match put intermediate_result1 into
        # finished result
        if intermediate_result1[0] == intermediate_result2[0]:
            intermediate_result1[1] += intermediate_result2[1]
            intermediate_result2 = []
        elif intermediate_result1[0] == 0:
            intermediate_result1 = []
            intermediate_result1.append(intermediate_result2[0])
            intermediate_result1.append(intermediate_result2[1])
            intermediate_result2 = []
        else:
            result[r] = (intermediate_result1[0], intermediate_result1[1])
            intermediate_result1 = []
            intermediate_result1.append(intermediate_result2[0])
            intermediate_result1.append(intermediate_result2[1])
            intermediate_result2 = []
            r += 1
    
    # append last type and value to result
    if intermediate_result1 != []:
        result[r] = (intermediate_result1[0], intermediate_result1[1])
    
    return result
