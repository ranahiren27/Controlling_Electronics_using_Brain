from flask import Flask, redirect, url_for, request, render_template
from sklearn.externals import joblib
from numpy import genfromtxt
import numpy as np
import requests
from random import random
import math
# app = Flask(__name__)
predector = joblib.load("SVC_model.joblib")
# @app.route("/")
# def index():
# 	return render_template('index.html')

# @app.route("/predection", methods = ['POST', 'GET'])
def predect(data):
	# data = [request.form[str(0)], request.form[str(1)], request.form[str(2)], request.form[str(3)], request.form[str(4)], request.form[str(5)], request.form[str(6)], request.form[str(7)], request.form[str(8)], request.form[str(9)]]
	# for i in range(5):
	# 	data.append(request.form[str(i)])
	y = predector.predict(data)
	commander(y)
	return str(y[0])

def commander(y):
	if y == 1:
		print("1")
		req = requests.get('http://192.168.43.243/on')
	elif y == 2:
		print("2")
		req = requests.get('http://192.168.43.243/off')
	else:
		print("None")
		req = requests.get('http://192.168.43.243/none')

if __name__ == '__main__':
   # app.run(debug = True)
   	data = genfromtxt('data.csv', delimiter=',')

	y_train = []
	# print(data[4][0:10])
	for i in range(len(data)):
		y_train.append(data[i][10])
	x_train = np.delete(data, 10, 1)
	flag = 1
	while flag:
		predect([x_train[int(math.floor(random()*100))]])
		flag = input("Enter 0 to exit: ")