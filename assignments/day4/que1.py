
k=int(input("enter distance:"))
def meter():
    #k=int(input("enter value in kilometers"))
    m=k*1000
    return m
#print("kilometer to meter:",meter())

def centimeter():
    #k=int(input("Enter value in meters:"))
    c=k*100
    return c
#print("meter to centimeter:",centimeter())

def milimeter():
    #k=int(input("enter value in centimeter:"))
    m=k*10
    return m
#print("centimeter to milimeter:",milimeter())

def feet():
    #k=int(input("enter value in feets:"))
    i=k*12
    return i
#print("feets to inches:",feet())

def inches():
   # k=int(input("enter value in inches:"))
    c=k*2.54
    return c
#print("inches to centimeter:",inches())

def distance_converter(kilometer,meter,conversion):
    result=conversion(kilometer,meter)
    return result

print("kilometer to meter:",meter())
print("meter to centimeter:",centimeter())
print("centimeter to milimeter:",milimeter())
print("feets to inches:",feet())
print("inches to centimeter:",inches())