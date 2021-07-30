def factorial(num):
   if num == 1:
       return num
   else:
       return num*factorial(num-1)

n = 10

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", n, "is", factorial(n))