import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)   # start,stop,step
y = 0.1*np.sin(x)
#print(x)
#print("------------------")
#print(y)
plt.plot(x,y, "-")


def gradient(x, y):
	#TODO: compute the gradient
	gradients = []
	for i in range(0,len(x) - 1):
	
		largerX = x[i + 1]
		smallerX = x[i]
		#print(largerX)
		changeInX = largerX - smallerX
	
		largerY = y[i + 1]
		smallerY = y[i]
		changeInY = largerY - smallerY

		gradient1 = changeInY / changeInX
		gradients.append(gradient1)

	return gradients

gradient = gradient(x, y)	
print(gradient)
x = np.delete(x,-1)
plt.plot(x,gradient, "*")
plt.show()
