import os.path
import sys
from traceback import format_tb
import re
nums20 = {1: ' One', 2: ' Two', 3: ' Three', 4: 'Four', 5: ' Five', \
            6: ' Six', 7: ' Seven', 8: ' Eight', 9: 'Nine', 10: ' Ten', \
            11: ' Eleven', 12: ' Twelve', 13: ' Thirteen', 14: ' Fourteen', \
            15: ' Fifteen', 16: ' Sixteen', 17: ' Seventeen', 18: ' Eighteen', 19: ' Nineteen', 100: ' One-Hundred'}

numtens = {2:' Twenty',3: ' Thirty',4: ' Forty',5: ' Fifty',6: ' Sixty',7: ' Seventy',8: ' Eighty',9: ' Ninety'}
n = input('Enter a number between 0 and 100:')
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
    n = int(n)
    nums = [int(d) for d in str(n)]
    if int(n) > 100:
        print('Number is out of range')
        quit()
    if (n > 1) and (n < 20) or (n == 100):
        print((nums20[n]))
    elif (n > 20) or (n < 99):
        n1 = nums[0]
        n2 = nums[1]
        print('Your number converted is:' + numtens[n1] +" " + nums20[n2].lower())
conv_to_words(n)