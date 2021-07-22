import os.path
import sys
from traceback import format_tb
import re
args = sys.argv

n = args[1]

def isInt(n):
    try: 
        int(n)
        return True
    except ValueError:
        return False

if isInt(n) == False:
    print('Please enter a number')
    quit()
nint = int(n)
n0 = n[0]
n1 = n[1]


def oned(n):
    return (nums20[n])
def twod(n):
    n0 = n[0]
    n1 = n[1]
    if (int(n) >= 0) and (int(n) < 20):
        return (nums20[n])
    elif (int(n) < 101) and (int(n) % 10 ==0):
        return (numstens[n])
    else:
        return (numtens[n0] + ' ' + oned(n1))
def threed(n):
    n0 = n[0]
    n1 = n[1]
    n3 = n[2]
    n23 = n[1:]
    print(n23)
    print(n0)
    if (int(n[1]) == 0) and (int(n[2]) == 0):
        return (numshunds[n0])
    elif (int(n[1]) == 0):
        return (numshunds[n0] + ' and ' + nums20[n3])
    else:
        print(n23)
        return (numshunds[n0] + ' and ' + twod(n23))
def fourd(n):
    n0 = n[0]
    n1 = n[1]
    n23 = n[1:]
    n34 = n[2:]
    n1m = n[-1]
    n0m = n[0:]
    if (int(n[1]) == 0) and (int(n[2]) == 0) and (int(n[3]) == 0):
        print('hi1')
        return numsthous[n0]
    elif (int(n[1]) ==0) and (int(n[2]) == 0):
        print('hi2')
        return (numsthous[n0] +' and '+ nums20[n1m])
    elif (int(n[1]) == 0) and (int(n[3]) == 0):
        print('hi3')
        return (numsthous[n0]+' ' +twod(n34))
    elif (int(n[1]) == 0):
        return (numsthous[n0] + ' ' +(twod(n34)))
    else:
        print(threed(n23))
        return (numsthous[n0] +' ' + threed(n23))


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
nums = [int(d) for d in str(n)]

if (nint < 0) or (len(n) > 4):
    print('Input out of range, please input numbers between 0 and 9999')
    quit()

if len(n) == 1:
    print(oned(n))
elif len(n) == 2:
    print(twod(n))
elif len(n) == 3:
    print(threed(n))
elif len(n) == 4:
    print(fourd(n))





