"""
	This project was written to calculate certain power of certain numbers
"""

# Import sys to work with console args
import sys

base_number = sys.argv[1]
power = sys.argv[2]
result = int(base_number)**int(power);


print(power + " power of " + base_number + " is " + str(result))
