import os.path
import sys
import re
import math
from math import sqrt
args = sys.argv

A = int(args[1])
B = int(args[2])
C = int(args[3])
#Defining function to calculate the Discriminant
def calculate_discriminant(a,b,c):
	#Making the parameters integer versions of themselves
	a = int(a)
	b = int(b)
	c=int(c)
	#Setting Discriminant Formula to a variable
	disc = (b**2-4*a*c)
	#Returning the Discriminant
	return disc

discriminant = (calculate_discriminant(A,B,C))
print(discriminant)

#Definining function to solve the quadratic formula
def solve(a,b,d):
	# Setting the quadratic formula's values to variables
	quad = (-b+sqrt(d))/2*(a)
	quadneg = (-b-sqrt(d))/2*(a)
	#If statement to check how many solutions and how many times to print an answer
	if d == 0:
		print('One Solution')
		print(quad)
	else:
		print('Two Solutions')
		print(quad)
		print(quadneg)


if discriminant >= 0:
	solve(A,B,discriminant)
else:
	print("No solution")