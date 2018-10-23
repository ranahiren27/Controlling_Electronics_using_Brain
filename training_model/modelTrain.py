from sklearn.externals import joblib
import numpy as np
from numpy import genfromtxt
from sklearn.svm import NuSVC
from sklearn import svm
if __name__ == "__main__":
	
	data = genfromtxt('data.csv', delimiter=',')

	y_train = []
	# print(data[4][0:10])
	for i in range(len(data)):
		y_train.append(data[i][10])
	x_train = np.delete(data, 10, 1)

	test_data = genfromtxt('test_data.csv', delimiter=',')

	y_test = []
	# print(test_data[4][0:10])
	for i in range(len(test_data)):
		y_test.append(test_data[i][10])
	x_test = np.delete(test_data, 10, 1)

	# ## NuSVC classification model
	# clf1 = NuSVC(gamma='scale', decision_function_shape='ovo')
	# clf1.fit(x_train, y_train)

	# print(clf1.score(x_test, y_test))
	# print(clf1.get_params(deep=True))

	## SVC classification model

	clf2 = svm.SVC(gamma='scale', decision_function_shape='ovo')
	clf2.fit(x_train, y_train)

	print(clf2.score(x_test, y_test))
	print(clf2.get_params(deep=True))


	##saving model
	# joblib.dump(clf1,"NuSVC_model.joblib")
	joblib.dump(clf2,"SVC_model.joblib")