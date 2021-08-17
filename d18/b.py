operandStack = []
operatorStack = []

def process():
    operandA = operandStack.pop()
    operandB = operandStack.pop()
    operator = operatorStack.pop()

    if operator == '+':
        operandStack.append(operandA + operandB)
    elif operator == '*':
        operandStack.append(operandA * operandB) 
    else:
        raise NotImplementedError("Invalid Operator passed: {}".format(operator))

def evaluateInfix(expression):
    for token in expression:
        if token.isdigit():
            operandStack.append(int(token))
        
        elif token == '+' or token == '(':
            operatorStack.append(token)

        elif token == '*':
            # Multiplication has less precedence than addition.
            while(len(operatorStack) != 0 and len(operatorStack)!= 0 and operatorStack[-1] != '('):
                process()
            operatorStack.append(token) 

        elif token == ')':
            # Token is a right parentheses, evaluate till corresponding left parentheses
            while(operatorStack[-1] != '('):
                process()
            
            # Discard right parentheses
            operatorStack.pop()

    # Perform remaining operations
    while(len(operatorStack) != 0):
        process()

    return operandStack.pop()


def tokenize(expressionString):
    expressionString = expressionString.replace(" ", "")
    return [char for char in expressionString]

if __name__ == "__main__":
    lines =  open('input.txt', 'r').readlines()
    sum = 0
    for expr in lines:
        sum += evaluateInfix(tokenize(expr))
    print(sum)