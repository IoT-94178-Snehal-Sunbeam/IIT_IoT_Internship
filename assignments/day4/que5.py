#n=int(input("Enter value:"))

list=[lambda n:n*1000,
      lambda n:n*1000,
      lambda n:n*1000,
      lambda n:n*0.00000220462]

n=float(input("Enter value:"))

kg=list[0](n)
gm=list[1](kg)
mg=list[2](gm)
ibs=list[3](mg)

print("tonns to kilograms:",kg)
print("kilograms to grams:",gm)
print("grams to miligrams:",mg)
print("miligrams to pounds:",ibs)


