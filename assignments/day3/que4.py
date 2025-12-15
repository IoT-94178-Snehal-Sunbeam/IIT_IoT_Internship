
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        print("invalid operation!")


a= int(input("Enter number one: "))
b= int(input("Enter number two: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("result:",add(a,b))
elif choice == 2:
    print("result:",sub(a,b))
elif choice == 3:
    print("result:",mul(a,b))
elif choice == 4:
    print("result:",div(a,b))
else:
    print("Invalid choice!")
