import math

def main(y, x):
	a = ((1 + x + 42 * (y ** 3)) ** 3) - 76 * math.floor(x)
	b = (math.atan(42 + 53 * x + (y ** 3)) ** 3)  - 67 * (y ** 4)
	c = a / b
	d = 81 * ((x + (y ** 3)) ** 3) + (math.log(x, 2)) ** 5
	e = 30 * ((x ** 3) + 34 * (y ** 2)) + (y ** 6)
	f = d / e
	g = c + f
	return g

print(main(0.16, 0.66))