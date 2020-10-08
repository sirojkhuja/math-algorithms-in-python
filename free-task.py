"""
	This project was written to calculate certain power of certain numbers
"""

# Import sys to work with console args
import sys

base_number = sys.argv[1]
power = sys.argv[2]

print(power + " power of " + base_number + " is " + str(int(base_number)**int(power)))
