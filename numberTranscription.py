import os.path
import sys
from traceback import format_tb
import re
args = sys.argv
nums20 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 100: 'One-Hundred'}

numtens = {2:'Twenty',3: 'Thirty',4: 'Forty',5: 'Fifty',6: 'Sixty',7: 'Seventy',8: 'Eighty',9: 'Ninety'}
numstens = {20:'Twenty',30: 'Thirty',40: 'Forty',50: 'Fifty',60: 'Sixty',70: 'Seventy',80: 'Eighty',90: 'Ninety'}
n = int(args[1])
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
    nint = int(n)
    nums = [int(d) for d in str(n)]
    if int(n) > 100:
        print('Number is out of range')
        quit()
    if n == 0:
        print("Only print from numbers 1 to 100 please")
        quit()
    if (n >= 1) and (n < 20) or (n == 100) or (n == 10):
        print('Your number converted is' + ' ' + (nums20[n]))
    elif nums[1] == 0 and int(n) != 10:
        print('Your number converted is:' + numstens[n])
    elif (n > 20) and (n < 99):
        n1 = nums[0]
        n2 = nums[1]
        print('Your number converted is:' + numtens[n1] +" " + nums20[n2].lower())
conv_to_words(n)