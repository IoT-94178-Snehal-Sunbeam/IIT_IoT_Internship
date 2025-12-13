n=int(input("enter number"))
temp=n
rev=0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

if temp==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")

