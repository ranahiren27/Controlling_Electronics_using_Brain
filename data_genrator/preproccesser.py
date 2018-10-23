from numpy import genfromtxt
import numpy as np
def slicer(data):
	newData = np.zeros((100,10), dtype='float')
	for i in range((len(data)-1)/10):
		for j in range(10):
			newData[i][j] = data[(i*10)+j]
			# print(str(newData[i])+" : "+str((i*10)+j))
	return newData

if __name__ == "__main__":
	raw_data = genfromtxt('raw_data.csv', delimiter=',')
	class1, class2, nones = raw_data

	class1 = slicer(class1)
	class2 = slicer(class2)
	nones = slicer(nones)
	class1 = np.append(class1, np.ones((100,1), dtype='float')*1, axis=1)
	class2 = np.append(class2, np.ones((100,1), dtype='float')*2, axis=1)
	nones = np.append(nones, np.ones((100,1), dtype='float')*0, axis=1)

	# print(len(class1[0]))
	# print("\n")
	# print(len(class2[0]))
	# print("\n")
	# print(len(nones[0]))

	data = np.concatenate([class1, class2, nones])
	np.random.shuffle(data)
	np.savetxt("data.csv", data, delimiter=",")