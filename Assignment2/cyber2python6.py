def palindrome(str):
   st=str[(x-1)::-1]
   if str==st :
           return("yes palindrome")
   else :
           return("no,not a palindrome")
str=input("enter the string")
x=len(str)
print(palindrome(str))
