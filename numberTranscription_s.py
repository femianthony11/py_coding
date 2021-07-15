import os.path
import sys
from traceback import format_tb
import re
args = sys.argv
n = args[1]
n = int(n)
nums20 = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 100: 'One-Hundred'}
numtens = {0: 'Zero', 2:'Twenty',3: 'Thirty',4: 'Forty',5: 'Fifty',6: 'Sixty',7: 'Seventy',8: 'Eighty',9: 'Ninety'}
numstens = {0: 'Zero',20:'Twenty',30: 'Thirty',40: 'Forty',50: 'Fifty',60: 'Sixty',70: 'Seventy',80: 'Eighty',90: 'Ninety'}
numconv = 'Your number converted is:'
nums = [int(d) for d in str(n)]

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if isInt(n) == False:
    print('Please enter a number')
    quit()

def conv_to_words(n):
    if n > 100:
        print('Number is out of range')
        quit()
    if n % 10 == 0:
        print(numconv + ' ' + numstens[n].lower())
    elif (n >=0) and (n<=19):
        print(numconv + nums20[n])
    else:
        n1 = nums[0]
        n2 = nums[1]
        print(numconv +numtens[n1] + ' ' + nums20[n2].lower())
conv_to_words(n)