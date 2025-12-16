
n=int(input("Enter distance:"))

meter=lambda n: n*1000
centimeter1=lambda n: n*100
milimeter=lambda n: n*10
inches=lambda n:n*12
centimeter2=lambda n:n*2.54


print(f"kilometers to meter={meter(n)}")
print(f"meters to centimeter={centimeter1(n)}")
print(f"centimeters to milimeter={milimeter(n)}")
print(f"feets to inches ={inches(n)}")
print(f"inches to centimeter={centimeter2(n)}")

