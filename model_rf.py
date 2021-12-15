import numpy as np
import pandas as pd
import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV


def buildModel():
	n_estimators = [100, 150, 200, 250]
	max_depth = [int(x) for x in np.linspace(60, 100, num = 20)]
	min_samples_split = [2, 5, 10]
	min_samples_leaf = [1, 2, 4]
	bootstrap = [True, False]
	criterion = ['entropy']


	random_grid = {'n_estimators': n_estimators,
	'max_depth': max_depth,
	'min_samples_split': min_samples_split,
	'min_samples_leaf': min_samples_leaf,
	'bootstrap': bootstrap,
	'criterion': criterion}

	rf = RandomForestClassifier()
	rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, cv = 2, random_state = 42, n_jobs = 5)

	return rf_random


def trainModel(modelRf, trainX, trainY):
	modelRf.fit(trainX, trainY)
	print("Best Model Parameters:", modelRf.best_params_)
	return modelRf.best_estimator_


def testModel(modelRf, testX, testY):
	predictions = modelRf.predict(testX)

	with open('data/model_data/predictions_rf.npy', 'wb') as f:
		np.save(f, np.array(predictions))

	print('Accuracy:', accuracy_score(testY, predictions))
	print('Precision:', precision_score(testY, predictions))
	print('Recall:', recall_score(testY, predictions))
	print('F1 Score:', f1_score(testY, predictions))


if __name__ == '__main__':

	# load previously processed train and test data
	trainX = np.load('data/model_data/trainX.npy')
	trainY = np.load('data/model_data/trainY.npy')
	testX = np.load('data/model_data/testX.npy')
	testY = np.load('data/model_data/testY.npy')


	rf_random = buildModel()

	start = time.time()
	modelRf = trainModel(rf_random, trainX, trainY)
	end = time.time()
	print("Total training time for random forest:", (end - start), "seconds")


	start = time.time()
	testModel(modelRf, testX, testY)
	end = time.time()
	print("Total evaluation time for random forest:", (end - start), "seconds")

