import os.path
import sys
from traceback import format_tb
import re


def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def zodiac_identifier(day, month):
	# checks month and date depending on the day to calculate the zodiac sign 
    if month == '12': 
        zod_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
          
    elif month == '01': 
        zod_sign = 'Capricorn' if (day < 20) else 'Aquarius'
          
    elif month == '02': 
        zod_sign = 'Aquarius' if (day < 19) else 'Pisces'
          
    elif month == '03': 
        zod_sign = 'Pisces' if (day < 21)  else 'Aries'
          
    elif month == '04': 
        zod_sign = 'Aries' if (day < 20) else 'Taurus'
          
    elif month == '05': 
        zod_sign = 'Taurus' if (day < 21) else 'Gemini'
          
    elif month == '06': 
        zod_sign = 'Gemini' if (day < 21) else 'Cancer'
          
    elif month == '07': 
        zod_sign = 'Cancer' if (day < 23) else 'Leo'
          
    elif month == '08': 
        zod_sign = 'Leo' if (day < 23) else 'Virgo'
          
    elif month == '09': 
        zod_sign = 'Virgo' if (day < 23) else 'Libra'
          
    elif month == '10': 
        zod_sign = 'Libra' if (day < 23) else 'Scorpio'
          
    elif month == '11': 
        zod_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    print(zod_sign)




def main():
	args = sys.argv
	Date = args[1]
	Date = Date.split('-')
	print(Date)
	print(type(Date))
	Month = Date[0]
	Day  = int(Date[1])
	print(Month)
	print(Day)
	#Setting the variable args equal to the arguments passed in terminal
	args = sys.argv
	#Checking if each argument is an integer and quitting if not
	if isInt(Date[0]) == False:
		print('arg must be an integer')
		quit()
	elif isInt(Date[1]) == False:
		print('arg must be an integer')
		quit()
	elif isInt(Date[2]) == False:
		print('arg must be an integer')
		quit()
	zodiac_identifier(Day,Month)

if __name__ == "__main__":
    main()