import os.path
import sys
print(sys.argv)
args = sys.argv

filepath = args[1]


print(sys.argv[2])	


p=int(args[2])

num_lines = sum(1 for line in open(args[1]))

a_file = open(filepath)	
number_of_lines = p

if p < 0:
	p=-p

if os.path.exists(args[1]) == False:
	print("File does not exist...")
	quit()


if int(args[2]) > num_lines:
	print('Not enough lines in the file, exiting.... ')
	quit()


else:

	for p in range(number_of_lines):
		line = a_file.readline()
		print(line)