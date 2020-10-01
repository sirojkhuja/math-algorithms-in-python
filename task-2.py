import sys

def binToDec(bin_num):
	sum = 0
	num_len = len(bin_num)
	for item in range(num_len):
		sum = sum + (int(bin_num[item]) * (2**(num_len - item - 1)))
	return sum

def binToOct(bin_num):
	return str(oct(binToDec(bin_num)))[2:]

def binToHex(bin_num):
	return str(hex(binToDec(bin_num)))[2:].upper()

print(sys.argv[1], " in dec: ", binToDec(sys.argv[1]))
print(sys.argv[1], " in oct: ", binToOct(sys.argv[1]))
print(sys.argv[1], " in hex: ", binToHex(sys.argv[1]))
