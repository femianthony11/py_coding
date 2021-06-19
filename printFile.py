import os.path
import sys
print(sys.argv)
args = sys.argv

filepath = args[1]
p=int(args[2])

a_file = open(filepath)

number_of_lines = p

for p in range(number_of_lines):
	line = a_file.readline()
	print(line)
