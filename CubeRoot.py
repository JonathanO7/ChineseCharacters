print("Please Enter A Number")
a = -0.1


def cbrt(a):
	#if a < 0:
		#print("You must input a positive number")
		#return None

	if type(a) == str:
		print("Please enter a number")
		return None

	
	a = float(a)
	threshold = 0.000001
	lowerlimit = 0
	upperlimit = a

	if 0 < a < 1:
			upperlimit = 1

	if -1 < a < 0:
			upperlimit = -1

	
	if a > 2**63:
			print("number is too large")
			return None
	initialguess = lowerlimit + (upperlimit - lowerlimit)/2       
	
	error = abs(initialguess**3 - a)

	count = 0
	while error > threshold:
		
		count = count + 1

		if count > 5000:
			return initialguess
			
		if a < 0:

			if initialguess**3 > a:
				lowerlimit = initialguess
			else:
				upperlimit = initialguess
			
		else:

			if initialguess**3 > a:
				upperlimit = initialguess
			else:
				lowerlimit = initialguess

		initialguess = lowerlimit + (upperlimit - lowerlimit)/2
		error = abs(initialguess**3 - a)
	
		if error < threshold:
			return initialguess


cbrt = cbrt(a)
print(cbrt)