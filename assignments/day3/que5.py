
def greet(name="sunbeam"):
    print(f"Hello, {name}!")

def info(name, age=20, city="mumbai"):
    print(f"Name: {name}, Age: {age}, City: {city}")

def apply_function(func, value=5):
    result = func(value)
    print(f"Result: {result}")


def square(a):
    return a * a

def cube(a):
    return a * a * a

greet()           
greet("dkte")     

info(name="iot", city="pune")  
info("snehal", age=20)          

apply_function(square)          
apply_function(cube, value=3)  
apply_function(lambda x: x+10)  
