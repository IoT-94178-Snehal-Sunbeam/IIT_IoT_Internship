import geometry as gm

r=int(input("Enter value of radius:"))
l=int(input("Enter value of length:"))
b=int(input("Enter value of breadth:"))

circle=gm.area_circle(r)
print(f"Area of circle:{circle}")

react=gm.area_reactangle(l,b)
print("Area of reactangle:",react)

