from tokenizer.tokenizer import tokenize


function = "2x^3 + 3x - 1"
function_tokens = tokenize(function)
print(function_tokens)