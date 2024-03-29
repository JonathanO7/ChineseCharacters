#this algorithm is only suitable for numbers 11 times 11 to 19 times 19. It is not easily expandable so not recommended

def SquareRootByLongDivision(a):
#1. Separate your square root base into pairs. Starting from the right, group the number into pairs. 
#In our example, 361 would be 3 61.

	stringA = str(a)
	listA = [c for c in stringA]
	lenOfA = len(listA)
	numOfModule = 10**lenOfA/10

	remainder = a % numOfModule
	firstDigit = (a - remainder) / numOfModule
	firstDigit = int(firstDigit)
	print(firstDigit)
	print(remainder)
	print("-------------------------------")
	
#2. Find the largest number that when squared it is smaller or equal to the first number or pair. 
#This will give you the first number in your answer. 
#The first number on the left is 3. The highest square that goes into it is one because 1 x 1 = 1, while 2 x 2 = 4.
	listOfSquares = []
	for i in range(0,firstDigit + 1):
		if i*i <= firstDigit + 0.0001:
			listOfSquares.append(i)
	Jangelo = max(listOfSquares) #Jangelo, the largest number that when squared it is smaller or equal to the first number or pair
	print(Jangelo)

	#3. Subtract the square from the first number or pair. 
	#Subtracting the square from the first number will give you a remainder, 
	#which will be included in the next step. In this example, 3 - 1 = 2.
	subtractedFirstDigit = firstDigit - Jangelo
	print(subtractedFirstDigit)
	print("-------------------------------")
	#4. Drop down the next pair. 
	#The next number you will work with will be the combination of the subtracted square and the next pair.
	#In this case, they would make a three-digit number. 
	#When you bring 61 down, the number you will use for finding the next digit in the square root is 261.
	newNumber = str(subtractedFirstDigit) + str(remainder)
	combinedNum = float(newNumber)
	print(combinedNum)
	print("-------------------------------")

	'''
	5. Multiply the first digit of the square by two. 
	This will be the first digit in the factor for finding the second digit of the square root.
	In the example, the first digit of the square root is one. 1 x 2 = 2.
	'''
	firstDigitx2 = Jangelo*2
	

	'''
	6. Set up the next factor equation(No need to do anything here). 
	The equation for the next step is based on the digit from step five and the number from step four. 
	The first factor will be a two-digit number, where the first digit is the number from step five. 
	The equation will look like 2_ x _.
	'''
	

	'''
	7. Find the number that fills the blanks. 
	This number will be the next digit in the solution for √361. 
	The number that will fill the blanks will be the same, 
	and it will be the highest digit where the factors are less than or equal to the number in step four. 
	In this example, the goal number is 261. We will start with 9, so the equation will look like 29 x 9 = 261.

	'''

	for i in range(0,int(combinedNum + 1)):
		firstFactor = str(firstDigitx2) + str(i)
		firstFactor = float(firstFactor)

		if int(firstFactor*i) == int(combinedNum):

			#8. Put the number next to the first digit. In this example, the square is 19.
			finalAnswer = str(Jangelo) + str(i)
			finalAnswer = float(finalAnswer)
			

			return finalAnswer

#not working num: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 400, 441
#working num: (121, 144, 169, 196, 225, 256, 289, 324, 361) 11 to 19 squared

a = 5*5
finalAnswer = SquareRootByLongDivision(a)
print(finalAnswer)		
