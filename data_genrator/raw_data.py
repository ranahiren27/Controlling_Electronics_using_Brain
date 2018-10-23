from random import random
import math
import numpy as np
import matplotlib.pyplot as plt 

def get_number(n):
	temp = []
	for i in range(n):
		temp.append(random())
	arr = np.array(temp,dtype='float')
	return arr

def class_1_data(data, qunt):
	newdata = []
	for j in range(qunt):
		temp = random()
		for i in data:
			newdata.append(i*temp)
	return newdata

def class_2_data(data, qunt):
	newdata = []
	for j in range(qunt):
		temp = random()
		for i in data:
			newdata.append(i*temp)
	return newdata

if __name__ == "__main__":

	class1 = get_number(10)
	class2 = get_number(10)

	class1 = class_1_data(class1,100)
	class2 = class_2_data(class2,100)
	nones = []
	for i in range(1000):
		nones.append(random())
	plt.plot(class1)
	plt.show()
	# print(len(class1))
	# print("\n")
	# print(len(class2))
	# print("\n")
	# print(len(nones))

	class1.append(1)
	class2.append(2)
	nones.append(0)

	data = np.array([class1, class2, nones],dtype='float')
	np.savetxt("raw_data.csv", data, delimiter=",")