def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter number"))
print("Factorial :", factorial(num)) 


#power
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
a=int(input("Enter number one:"))
b=int(input("Enter number two:"))
result=power(a,b)
print("result:",result) 
