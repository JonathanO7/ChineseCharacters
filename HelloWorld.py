def test():
	print("hello world! changed")
	return
test()
aList = [3, 6, 1, 3, 1, 4, 1, 5, 6]
bList = []
def SortFromLowToHigh(aList):
	for i in range(0, len(aList)):
		
			
			bList.append(aList[i])
			
	return bList
bList = SortFromLowToHigh(aList)
print(bList)