#pixelise an image. turning image into numbers in list

import cv2
import numpy as np

img_path = 'onechinese.png'
img = cv2.imread(img_path, 0)
img_reverted = cv2.bitwise_not(img) #255 is black and 0 is white as it is inverted
#print(img[50])


    
s = 1
ws = 4
p = 2

from matplotlib import pyplot as plt
plt.imshow(img_reverted, interpolation='nearest')
plt.show()

#force images of different resolutions into the same resolution


def compress(img_reverted, s, ws):
    compressedList = []

    lenImg = len(img_reverted)
    #print("////////////////")
    #print(lenImg)
    for j in range(0,lenImg -ws, s):
        listOfRow = []
        
        for i in range(0,lenImg-ws, s):
            sumOfPixels = 0
            for k in range(i,i + ws):
                for x in range(j,j + ws):
                    sumOfPixels = sumOfPixels + img_reverted[x][k]
                         
            avg = sumOfPixels/(ws**2)
            listOfRow.append(avg)
            #print(len(img_reverted))
        
        compressedList.append(listOfRow)       
        
    return compressedList

#print(compress(img_reverted, s, ws))
s = 4
ws = 8
compressedImg = compress(img_reverted, s, ws)


def compressMaxPooling(img_reverted, s, ws):
    compressedList = []

    lenImg = len(img_reverted)
    #print("////////////////")
    #print(lenImg)
    for j in range(0,lenImg -ws, s):
        listOfRow = []
        
        for i in range(0,lenImg-ws, s):
            sumOfPixels = 0
            for k in range(i,i + ws):
                for x in range(j,j + ws):
                    sumOfPixels = sumOfPixels + img_reverted[x][k]
                    value = [] 
                    value.append(img_reverted[x][k])
                    max1 = 0
                    lenIMG = len(value)
                    for i in range(0,lenIMG):
                        if max1 < value[i]:
                            max1 = value[i]
                        
                         
           
            listOfRow.append(max1)
            #print(len(img_reverted))
        
        compressedList.append(listOfRow)       
        
    return compressedList

compressMaxPooling = compressMaxPooling(img_reverted, s, ws)
print(compressMaxPooling)


def padding(img_reverted, p):
    
    
    paddedList = []
    listOfZeros = []
    for b in range(0,len(img_reverted) + 2*p):
        listOfZeros.append(0)
    for g in range(0,len(img_reverted)):
        newList = img_reverted[g]
        for pi in range(0,p):
            newList = np.insert(newList,0,0)
            newList = np.append(newList, 0)
        newList = newList.tolist()
        paddedList.append(newList)
        
        
    for pi in range(0,p):
        paddedList.insert(0,listOfZeros)
        paddedList.append(listOfZeros)
        
    return paddedList




def paddingHorizontally(img_reverted, p):
    
    paddedList = []
    for g in range(0,len(img_reverted)):
        newList = img_reverted[g]
        for pi in range(0,p):
            newList = np.insert(newList,0,0)
            newList = np.append(newList, 0)
        newList = newList.tolist()
        paddedList.append(newList)
        
    return paddedList

def paddingVertically(img_reverted, p):
    
    paddedList = []
    listOfZeros = []
    for b in range(0,len(img_reverted)):
        listOfZeros.append(0)
    
    for pi in range(0,p):
        paddedList.insert(0,listOfZeros)
        paddedList.append(listOfZeros)
        
    return paddedList

def paddingHorizontallyLeft(img_reverted, p):
    
    paddedList = []
    for g in range(0,len(img_reverted)):
        newList = img_reverted[g]
        for pi in range(0,p):
            newList = np.insert(newList,0,0)
            
        newList = newList.tolist()
        paddedList.append(newList)
        
    return paddedList

def paddingHorizontallyRight(img_reverted, p):
    
    paddedList = []
    for g in range(0,len(img_reverted)):
        newList = img_reverted[g]
        for pi in range(0,p):
            
            newList = np.append(newList, 0)
        newList = newList.tolist()
        paddedList.append(newList)
        
    return paddedList

def paddingVerticallyTop(img_reverted, p):
    
    paddedList = []
    listOfZeros = []
    for b in range(0,len(img_reverted)):
        listOfZeros.append(0)
    
    for pi in range(0,p):
        paddedList.insert(0,listOfZeros)
        
        
    return paddedList

def paddingVerticallyBottom(img_reverted, p):
    
    paddedList = []
    listOfZeros = []
    for b in range(0,len(img_reverted)):
        listOfZeros.append(0)
    
    for pi in range(0,p):
        
        paddedList.append(listOfZeros)
        
    return paddedList





def SquaringImage(img_reverted):
    horizontalResolution = len(img_reverted[0])
    verticalResolution = len(img_reverted)
    
    if horizontalResolution == verticalResolution:
        return img_reverted
    else:
        if abs(horizontalResolution - verticalResolution) % 2 == 0:
            #eg. 8 by 10 img, we know how to pad
            
            if horizontalResolution > verticalResolution:
                difference = horizontalResolution - verticalResolution
                pad = difference / 2
                p = int(pad)
                return paddingVertically(img_reverted, p)
            
            elif verticalResolution > horizontalResolution:
                difference = verticalResolution - horizontalResolution
                pad = difference / 2
                p = int(pad)
                return paddingHorizontally(img_reverted, p)
            
            
        else:
            #eg. 7 by 10 img, tricky to pad
            
            if horizontalResolution > verticalResolution:    
                difference = horizontalResolution - verticalResolution
                pad = difference / 2
                largeP = int(pad)
                smallP = difference - largeP
                img_reverted = paddingVerticallyTop(img_reverted, largeP)
                img_reverted = paddingVerticallyBottom(img_reverted, smallP)
                return img_reverted
                    
            elif horizontalResolution < verticalResolution:    
                difference = verticalResolution - horizontalResolution
                pad = difference / 2
                largeP = int(pad)
                smallP = difference - largeP
                img_reverted = paddingHorizontallyLeft(img_reverted, largeP)
                img_reverted = paddingHorizontallyRight(img_reverted, smallP)
                return img_reverted
            
       
        

paddedImg = padding(img_reverted, p)
lenPadded = len(paddedImg)
lenPaddedX = len(paddedImg[0])
#print(lenPadded)
#print(lenPaddedX)
for v in range(0,lenPadded):
    for w in range(0,lenPaddedX):
        paddedImg[v][w] = np.float64(paddedImg[v][w])
       



plt.imshow(compressedImg, interpolation='nearest')
plt.show()

#print(type(paddedImg[0][0]))


plt.imshow(paddedImg, interpolation='nearest')
plt.show()

"""Make image of any size into a square image of a particular size"""
resolutionNew = 100
def resize(img_reverted, resolutionNew = 100):
    
 
    
    #pad first
    img_squared = SquaringImage(img_reverted)
    
    widthOfImg = len(img_squared)
    print(widthOfImg)
    #width is 81
    lengthOfImg = len(img_squared[0])
    print(lengthOfImg)
    #length is 101
    
    if lengthOfImg != widthOfImg:
        print("Error! Lenght of image does not equal to width of image")
    else:
        #50 = 101 - ws / s  +1
    
        #rn = ro - ws +2p/s +1
        
        #ws = -(rn - 1)*s + Ro
        
        s = 1
      
        ws = -(resolutionNew - 1)*s + lengthOfImg
        ws = int(ws)
        print("/////////////////////////////////////////////")  
        print(ws)
        resizedList = []
             
        resizedList = compress(img_squared, s, ws)
        
        return resizedList
    
resizedList = resize(img_reverted, resolutionNew)
#print(resizedList)
    

lenResized = len(resizedList)
lenResizedX = len(resizedList[0])
print("/////////////////////////////////////////////")    
print(lenResized)
print(lenResizedX)
print("/////////////////////////////////////////////")      
for v in range(0,lenResized):
    for w in range(0,lenResizedX):
        resizedList[v][w] = np.float64(resizedList[v][w])

plt.imshow(resizedList, interpolation='nearest')
plt.show()
