
def revstr(str):
   s=str[::-1]
   print(s)

def count_vowels(s):
   vowels='aeiouAEIOU'
   count=0
   for ch in s:
        if ch in vowels:
         count+=1
         
   return count
      




