
a = 25

def sqrt(a):
	if a < 0:
		print("You must input a positive number")
		return None
	threshold = 0.000001
	lowerlimit = 0
	upperlimit = a
	initialguess = lowerlimit + (upperlimit - lowerlimit)/2
	error = abs(initialguess**2 - a)

	while error > threshold:
		if initialguess**2 > a:
			upperlimit = initialguess
		else:
			lowerlimit = initialguess
		initialguess = lowerlimit + (upperlimit - lowerlimit)/2
		error = abs(initialguess**2 - a)
		if error < threshold:
			return initialguess

sqrt = sqrt(a)
print(sqrt)