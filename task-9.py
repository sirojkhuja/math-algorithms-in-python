"""
	This file calculates continued fractions
"""

# import sys library to work with console arguments
import sys

# Get two numbers from console arguments
a = int(sys.argv[1])
b = int(sys.argv[2])

def GCD(first, second):
        """
                This function takes two numbers
                and calculates GCD (greatest common divider) of them
        """
        # Initial values
        u2, u1, v2, v1 = 1, 0, 0, 1

        # if a is less than b need to swap the values
        if first < second: first, second = second, first

        # calculates until second (minimum) number becomes zero
        while(second > 0):
                q = first//second
                r = first - q * second
                u = u2 - q * u1
                v = v2 - q * v1
                first = second
                second = r
                u2 = u1
                u1 = u
                v2 = v1
                v1 = v
        return first, u2, v2

gcd = GCD(a,b)[0]
a = a//gcd
b = b//gcd

q_values = []
r = b

while(r > 0):
	q_values.append(a//b)
	r = a%b
	a = b
	b = r

capP, capQ, capP1, capQ1 = 1, 0, q_values[0], 1
sym = capP1//capQ1

print(q_values)
