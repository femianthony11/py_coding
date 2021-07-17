import os.path
import sys
from traceback import format_tb
import re
args = sys.argv
n = args[1]
n = int(n)
ntr = str(n)
nums20 = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', \
            '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten', \
            '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', \
            '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen', '100': 'One-Hundred'}
numtens = {'0': 'Zero', '2':'Twenty','3': 'Thirty','4': 'Forty','5': 'Fifty','6': 'Sixty','7': 'Seventy','8': 'Eighty','9': 'Ninety'}
numstens = {'0': 'Zero','20':'Twenty','30': 'Thirty','40': 'Forty','50': 'Fifty','60': 'Sixty','70': 'Seventy','80': 'Eighty','90': 'Ninety'}
numshunds = {'1': 'One Hundred', '2': 'Two Hundred', '3': 'Three Hundred', '4': 'Four Hundred', '5': 'Five Hundred', \
            '6': 'Six Hundred', '7': 'Seven Hundred', '8': 'Eight Hundred', '9': 'Nine Hundred'}
numsthous = {'1': 'One Thousand', '2': 'Two Thousand', '3': 'Three Thousand', '4': 'Four Thousand', '5': 'Five Thousand', \
            '6': 'Six Thousand', '7': 'Seven Thousand', '8': 'Eight Thousand', '9': 'Nine Thousand'}
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
    ntr = str(n)
    n1 = nums[0]
    n2 = nums[1]
    if len(str(n)) == 3:
        n3 = nums[1]
        n4 = nums[2]
        if (int(ntr[1]) == 0) and (int(ntr[2]) == 0):
            print(numshunds[ntr[0]])
        else:
            print(numshunds[ntr[0]] + ' and ' + numtens[str(n3)] + ' ' + nums20[str(n4)].lower())
    elif len(str(n)) == 4:
        if (int(ntr[1]) == 0) and (int(ntr[2]) == 0) and (int(ntr[3]) == 0):
            print(numsthous[ntr[0]])
        elif (int(ntr[2]) == 0) and (int(ntr[3]) == 0):
            print(numsthous[ntr[0]] + ' ' + numshunds[ntr[1]].lower())
        elif (int(ntr[3]) == 0):
            print(numsthous[ntr[0]] +' ' + numshunds[ntr[1]].lower() + ' and ' + numtens[str(nums[2])].lower())
        else:
            print(numsthous[ntr[0]] +' ' + numshunds[ntr[1]].lower() + ' and ' + numtens[str(nums[2])].lower() + ' ' + nums20[str(nums[3])].lower())


    elif (n >=0) and (n<=19):
        print(numconv + nums20[n])
    elif n % 10 == 0:
        print(numconv + ' ' + numstens[n].lower())
    else:

        print(numconv + numtens[n1] + ' ' + nums20[n2].lower())
conv_to_words(n)