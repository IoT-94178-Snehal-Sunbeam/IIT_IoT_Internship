n1 = int(input("Enter number one: "))
n2 = int(input("Enter number two: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(f"{n1} + {n2} = {n1 + n2}")
elif choice == 2:
    print(f"{n1} - {n2} = {n1 - n2}")
elif choice == 3:
    print(f"{n1} * {n2} = {n1 * n2}")
elif choice == 4:
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Invalid choice!")
