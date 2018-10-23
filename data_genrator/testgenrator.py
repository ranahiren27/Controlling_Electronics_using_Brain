from numpy import genfromtxt
import numpy as np
from random import random
if __name__ == "__main__":
	raw_data = genfromtxt('data.csv', delimiter=',')
	for i in range(len(raw_data)):
		temp = random()*0.001
		for j in range(len(raw_data[i])-1):
			if j!=0:
				if i%j == 0:
					raw_data[i][j] += temp
				else:
					raw_data[i][j] -= temp
			else:
					raw_data[i][j] += temp
	np.savetxt("test_data.csv", raw_data, delimiter=",")