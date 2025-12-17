
import operations.arithmatic as ar
import operations.string_ops as st

a=int(input("Enter first no:"))
b=int(input("Enter second no:"))

add=ar.add(a,b)
print("Addition:",add)
mul=ar.mul(a,b)
print("Multiplication:",mul)

str=input("Enter string:")
rev=st.revstr(str)

s=input("Enter string:")
cnt=st.count_vowels(s)
print("Vowels:" ,cnt)
