import os.path
import sys
from traceback import format_tb


print(sys.argv)
args = sys.argv
a_file = open(args[1])


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False



print(sys.argv)

args = sys.argv

filename = (args[1])

number_of_lines = (args[2])




if isInt(number_of_lines) == False:
	print('n must be an integer')
	quit()

number_of_lines = int(number_of_lines)

#If the file doesn't exist, it should exit and print:
if os.path.exists(filename) == False:
	print("File does not exist...")
	quit()


f = open(filename, "r")



lines = f.readlines()

filelength=len(lines)



if int(number_of_lines) > filelength:
	print('Not enough lines in the file, exiting.... ')
	quit()

print(f"filelength = {filelength}")
print(f"number_of_lines = {number_of_lines}")


#If the argument n is negative e.g. -10, it should print out the last 10 lines .
if number_of_lines < 0:
	start = filelength+number_of_lines
	end=filelength
	print(f"start = {start}")
	print(f"end = {end}")
else:
	start = 0
	end=number_of_lines




#If the number of lines to print n, is more than the total number of lines in the file, it should exit and print

for i in range(start,end):
	print(lines[i])