import os.path
import sys
from traceback import format_tb
import re
# Need to pip install tabulate
from tabulate import tabulate
import numpy

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# Counts items in lsit
def countlist(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

#Splits list evenly in pairs
def split_list(lst, n):  
    for i in range(0, len(lst), n):
        yield lst[i:i + n] 



def main():
    #Sets Continue InputS
    yn = input('Continue (Y/N)')
    #Creates empty list for later
    lst = []

    #While loop to check and evaluate what letter grade each input is and add it to the empty list 
    while yn == 'Y':
        sub = input('Enter Subject:')

        per = input('Enter Percentage:')

        yn = input('Continue (Y/N)')
        if isInt(per) == False:
            print("Percentage must be Int")
            quit()
        if int(per) > 89.5:
            per = 'A'
        elif int(per) > 79.5:
            per = 'B'
        elif int(per) > 69.5:
            per = 'C'
        elif int(per) > 59.5:
            per = 'D'
        elif int(per) < 50.5:
            per = 'F'
        lst.append(sub)
        lst.append(per)
        #Checks when someone says to stop 
        if yn == 'N':
            print('Quitting Loop...')
            break

    print(countlist(lst,'A'))

    n = 2
    outlist = list(split_list(lst, n)) 

    print(outlist)
    print('Marking Period Grades:')
    #Makes Table
    print(tabulate(outlist))
    # Sets A var equal to the length of the amount of times each letter comes up in the list
    A = int(countlist(lst,'A'))
    B = int(countlist(lst,'B'))
    C = int(countlist(lst,'C'))
    D = int(countlist(lst,'D'))
    F = int(countlist(lst,'F'))
    listlen = len(lst)
    hflistlen = 1/2 * listlen
    DF = int(D) +int(F)
    #Checks that there are more than 1 class
    if len(lst) == 2:
        print('Not enought Input items')
        quit()
    #Checks what level of Marking period someone achieves by the amount of every certain letter grade
    if B <= 1 and A >= 1 and C == 0 and D == 0 and F == 0:
        Achieve = ' High Honors - at most 1B, A for rest'
        print(Achieve)
        quit()

    if A >= 1 and B <= 2 and C <= 1 and D == 0 and F == 0:
        Achieve = ' Honors  -  at most 2Bs or 1C, A for rest'
        print(Achieve)
        quit()
    if hflistlen >= C and B >= 1 and F == 0:
        Achieve = ' Pass   - less than 50% of letter grades are C, but Not HH or H'
        print(Achieve)
        quit()

    if hflistlen == C:
        Achieve = ' Needs Improvement - 50% of letter grades are C'
        print(Achieve)
        quit()

    if hflistlen == D and F>=1 and C == 0 and A == 0 and B == 0:
        Achieve = 'Fail - > 50%  of letter grades are D or less'
        print(Achieve)
        quit()

if __name__ == "__main__":
    main()