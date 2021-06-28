import os.path
import sys
import re

args = sys.argv

filename = (args[1])

search_item = (args[2])

search_item = search_item.rjust(2)
f = open(filename, "r")

lines = f.readlines()
#Function to search for a string in the file
def search_string_in_file(filename, str):
    line_number = 0
    list_of_results = []
    with open(filename, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if str in line:
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results
#setting a variable equal to the result(or calling) of the function
results=search_string_in_file(filename,search_item)

#If statement to check whether the file even contains our keyword
if len(results) != 0:
	print(*results, sep="\n")
else:
	print('No matches')