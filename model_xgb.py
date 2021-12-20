import numpy as np
import pandas as pd
import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier

# this method loads the feature dataset and convert into 80% vs 20% train and test dataset
def buildModel():
	# set parameters range for random search of hyper parameters
	learning_rate = [0.01, 0.05, 0.1, 0.2, 0.3]
	max_depth = [2, 5, 6, 8, 9]
	colsample_bytree = [0.4, 0.5, 0.6]
	subsample = [0.5, 0.6, 0.7]
	n_estimators = [10, 20, 30]
	objective = ['binary:logistic']
	eval_metric = ['logloss']

	#create the radom grid
	random_grid = {'learning_rate': learning_rate,
	'max_depth': max_depth,
	'colsample_bytree': colsample_bytree,
	'n_estimators': n_estimators,
	'objective': objective,
	'eval_metric': eval_metric}

	# create XGBoost model class
	model_xgb = XGBClassifier()
	xgb_random = RandomizedSearchCV(estimator = model_xgb, param_distributions = random_grid, n_jobs = 5)

	return xgb_random

# this method trains the model on the parameters for random search and returns the best model
def trainModel(modelXgb, trainX, trainY):
	modelXgb.fit(trainX, trainY)
	print("Best Model Parameters:", modelXgb.best_params_)
	return modelXgb.best_estimator_

# evaluate the best XGBoostmodel with unseen data
def testModel(modelXgb, testX, testY):
	y_pred = modelXgb.predict(testX)
	predictions = [round(value) for value in y_pred]

	# save the predictions of XGBoost model
	with open('data/model_data/predictions_xgb.npy', 'wb') as f:
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

	# build the random forest classifier model
	xgb_random = buildModel()

	# train the model and get the one with best parameters
	start = time.time()
	modelXgb = trainModel(xgb_random, trainX, trainY)
	end = time.time()
	print("Total training time for XGBoost:", (end - start), "seconds")

	# evaluate the model
	start = time.time()
	testModel(modelXgb, testX, testY)
	end = time.time()
	print("Total evaluation time for XGBoost:", (end - start), "seconds")
