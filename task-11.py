"""
	This project was created to solve 11th task of Questions Book I provided in the same folder
"""

# Import sys to get console arguments
import sys

# Get base_number, power and mod from console arguments, ex. python task-11.py 5 596 1234
base_number = sys.argv[1]
power = sys.argv[2]
mod = sys.argv[3]

k_arr = list(str(bin(int(power))))[2:]
k_arr.reverse()
cap_A = []
b_arr = []

def solve():
	if(power == 0): 
		return 1
	else:
		cap_A.append(int(base_number))

		if(k_arr[0] == '1'):
			b_arr.append(int(base_number))
		else:
			b_arr.append(1)

		for i in range(1,10):
			cap_A.append((cap_A[i-1]**2) % int(mod))

			if(k_arr[i] == '0'):
				b_arr.append(b_arr[i-1])
			elif(k_arr[i] == '1'):
				b_arr.append((b_arr[i-1] * cap_A[i]) % int(mod))

def display_table():
	print("i  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
	print(k_arr)
	print(cap_A)
	print(b_arr)

if(solve() != 1):
	display_table()
