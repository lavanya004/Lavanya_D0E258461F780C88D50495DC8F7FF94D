def factorial(n):
  if n==0 or n==1:
     return 1
  else:
      return n*factorial(n-1) 
number=int(input("enter the number"))
fact=factorial(number) 
print(" THE FACTORIAL OF",number, "IS",fact)


   
