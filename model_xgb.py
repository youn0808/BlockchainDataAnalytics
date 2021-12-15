import numpy as np
import pandas as pd
import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier


def buildModel():
	# set parameters range for random search of hyper parameters
	learning_rate = [0.01, 0.05, 0.1, 0.2, 0.3]
	max_depth = [2, 5, 6, 8, 9, 10]
	colsample_bytree = [0.5, 0.75]
	subsample = [0.6, 0.7, 0.8]
	n_estimators = [10, 30, 50, 70, 100, 150, 200, 250]
	objective = ['binary:logistic']
	eval_metric = ['logloss']


	random_grid = {'learning_rate': learning_rate,
	'max_depth': max_depth,
	'colsample_bytree': colsample_bytree,
	'n_estimators': n_estimators,
	'objective': objective,
	'eval_metric': eval_metric}

	model_xgb = XGBClassifier()
	xgb_random = RandomizedSearchCV(estimator = model_xgb, param_distributions = random_grid, n_jobs = 5)

	return xgb_random

def trainModel(modelXgb, trainX, trainY):
	modelXgb.fit(trainX, trainY)
	print("Best Model Parameters:", modelXgb.best_params_)
	return modelXgb.best_estimator_


def testModel(modelXgb, testX, testY):
	y_pred = modelXgb.predict(testX)
	predictions = [round(value) for value in y_pred]


	with open('data/model_data/predictions_xgb.npy', 'wb') as f:
		np.save(f, np.array(predictions))

	print('Accuracy:', accuracy_score(testY, predictions))
	print('Precision:', precision_score(testY, predictions))
	print('Recall:', recall_score(testY, predictions))
	print('F1 Score:', f1_score(testY, predictions))


if __name__ == '__main__':


	trainX = np.load('data/model_data/trainX.npy')
	trainY = np.load('data/model_data/trainY.npy')
	testX = np.load('data/model_data/testX.npy')
	testY = np.load('data/model_data/testY.npy')


	xgb_random = buildModel()


	start = time.time()
	modelXgb = trainModel(xgb_random, trainX, trainY)
	end = time.time()
	print("Total training time for XGBoost:", (end - start), "seconds")

	start = time.time()
	testModel(modelXgb, testX, testY)
	end = time.time()
	print("Total evaluation time for XGBoost:", (end - start), "seconds")

