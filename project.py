import math

def get_values():
	print "Enter the values \n"
	n = int(raw_input("Enter the value of n: "))
	a = float(raw_input("Enter the value of A: "))
	i_raw = float(raw_input("Enter the value of i (in percentage): "))

	# Converting i value to decimal for calculation purposes
	i = (i_raw/100)

	p = float(raw_input("Enter the value of P: "))

	f_values = list()

	for index in range(0, n):
		print "\nGetting the value for F" + str(index + 1)
		val = float(raw_input("Enter the value: "))
		f_values.append(val)

	sv = float(raw_input("\nEnter the value of Salvage Value: "))

	return (n, a, i, p, f_values, sv)


def part1(f_values, i, n):
	res = 0
	for index in range(0, n - 1):
		f = f_values[index]
		res += f * math.pow((1 + i), (-(index + 1)))
	return res

def part2(f_n, sv, i, n):
	res = (f_n + sv) * math.pow((1+i), -n)
	return res

def part3(a, i, n):
	x = math.pow((1+i), n)
	res = (x - 1) / (i * x)
	res = a * res
	return res 

def part4(p, pe1, pe2, pe3):
	res = -p + pe1 + pe2 + pe3
	return res
	

if __name__ == "__main__":
	print "Program to calculate the Present Equivalent value \n"

	(n, a, i, p, f_values, sv) = get_values()
	pe1 = part1(f_values, i, n)
	pe2 = part2(f_values[-1], sv, i, n)
	pe3 = part3(a, i, n)
	pe = part4(p, pe1, pe2, pe3)

	print "\nThe Present Equivalent is ", pe