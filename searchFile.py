import os.path
import sys
import re

args = sys.argv

filename = (args[1])

search_item = (args[2])

search_item = search_item.rjust(2)
f = open(filename, "r")

lines = f.readlines()
res = list(filter(lambda x: search_item in x, lines))
print(str(res))

new_list = [item for item in lines if all((w in item) for w in search_item.rjust(1))]

if len(new_list) !=0:
	print(new_list)
else:
	print('No matches')