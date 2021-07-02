import os.path
import sys
import re
import math
from math import sqrt

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

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


def main():
	#Setting the variable args equal to the arguments passed in terminal
	args = sys.argv
	#Checking if each argument is an integer and quitting if not
	if isInt(args[1]) == False:
		print('n must be an integer')
		quit()
	elif isInt(args[2]) == False:
		print('n must be an integer')
		quit()
	elif isInt(args[3]) == False:
		print('n must be an integer')
		quit()


	#Setting variables equal to the indexes of the arguments inputted at the terminal
	A = int(args[1])
	B = int(args[2])
	C = int(args[3])
	#Setting the discriminant equal to the A,B and C values passed in the function used to find the discriminant
	discriminant = (calculate_discriminant(A,B,C))
	print(discriminant)
	#Checking if the discriminant is greater than zero to figure out whether to run the function solve, which is used to do the quadratic formula
	if discriminant >= 0:
		solve(A,B,discriminant)
	else:
		print("No solution")



if __name__ == "__main__":
    main()

