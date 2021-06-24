import os.path
import sys
from traceback import format_tb

print(sys.argv)
args = sys.argv

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if isInt(args[2]) == False:
	print('n must be an integer')
	quit()

number_of_lines = (args[2])
z = number_of_lines
z = int(number_of_lines)


#If the file doesn't exist, it should exit and print:
if os.path.exists(args[1]) == False:
	print("File does not exist...")
	quit()
print(int(args[2]))




f = open("notes.txt", "r")

num_lines = sum(1 for line in open(args[1]))



xs = f.readlines()




#If the argument n is negative e.g. -10, it should print out the last 10 lines .
if z < 0:
	print(xs[z:])
	quit()




#If the number of lines to print n, is more than the total number of lines in the file, it should exit and print
if int(args[2]) > num_lines:
	print('Not enough lines in the file, exiting.... ')
	quit()


else:

	for i in range(z):
		line = a_file.readline()
		print(line)