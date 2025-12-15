
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b!= 0:
        return a/b
    else:
        return "Invalid operation!"

def calculate(operand1, operand2, operation_func):
    result = operation_func(operand1, operand2)
    return result

a=int(input("Enter number one:"))
b=int(input("Enter number two:"))

print("Addition:", calculate(a, b, add))       
print("Subtraction:", calculate(a, b, subtract)) 
print("Multiplication:", calculate(a, b, multiply)) 
print("Division:", calculate(a, b, divide))      

