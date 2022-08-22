def test():
	print("hello world! changed")
	return
test()

def IsFromLowToHigh(aList):
	for i in range(0,len(aList) -1):
		element = aList[i]
		nextElement = aList[i + 1]
		if element > nextElement:
			return 0
	return 1

aList = [1,0,0,0,0,0,0,0]
def SortFromLowToHigh(aList):
	while IsFromLowToHigh(aList) != 1:
		for i in range(0,len(aList) - 1):
			element = aList[i]
			nextElement = aList[i+1]
			if element > nextElement:
				aList[i+1] = element
				aList[i] = nextElement
		#print(aList)
	return aList
aList = SortFromLowToHigh(aList)
#print(aList)

def IsFromHighToLow(bList):
	for i in range(0,len(bList) -1):
		element = bList[i]
		nextElement = bList[i + 1]
		if element < nextElement:
			return 0
	return 1


bList = [5,3,6,7,3,2,8,7,2,1]
def SortFromHighToLow(bList):
	while IsFromHighToLow(bList) != 1:
		for i in range(0,len(bList) - 1):
			element = bList[i]
			nextElement = bList[i+1]
			if element < nextElement:
				bList[i+1] = element
				bList[i] = nextElement
		print(bList)
	return bList
bList = SortFromHighToLow(bList)
print(bList)

