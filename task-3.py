# import sys library to work with console arguments
import sys

# Get n and m values from arguments
n = int(sys.argv[1])
m = int(sys.argv[2])

# h - number for base
h = int(sys.argv[3])

# Print n and m values
print("n =", n, " m =", m)

def decToAnyBase(num, base):
	"""
		This function get decimal number 
		and converts it to any base number
		and returns it
	"""
	i = r = 0

	q = a = num

	h_based_num = []
	while(q > 0):
		r = a%base
		# print("r =", r, "q =", q)

		h_based_num.append(str(r))
		q = (a - r)//base

		i = i + 1
		a = q
	return "".join(h_based_num[::-1])

print("Decimal:", n, " -> ", h, " - based number: ", decToAnyBase(n, h))
print("Decimal:", m, " -> ", h, " - based number: ", decToAnyBase(m, h))
