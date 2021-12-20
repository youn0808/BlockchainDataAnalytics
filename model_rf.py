import numpy as np
import pandas as pd
import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

# this method loads the feature dataset and convert into 80% vs 20% train and test dataset
def buildModel():
	# set parameters range for random search of hyper parameters
	n_estimators = [5, 10, 15, 20]
	max_depth = [int(x) for x in np.linspace(4, 17, num = 4)]
	min_samples_split = [2, 5, 10]
	min_samples_leaf = [2, 4]
	bootstrap = [True, False]
	criterion = ['entropy']

	#create the radom grid
	random_grid = {'n_estimators': n_estimators,
	'max_depth': max_depth,
	'min_samples_split': min_samples_split,
	'min_samples_leaf': min_samples_leaf,
	'bootstrap': bootstrap,
	'criterion': criterion}

	# create random forest model class
	rf = RandomForestClassifier()
	rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, cv = 2, random_state = 42, n_jobs = 5)

	return rf_random

# this method trains the model on the parameters for random search and returns the best model
def trainModel(modelRf, trainX, trainY):
	modelRf.fit(trainX, trainY)
	print("Best Model Parameters:", modelRf.best_params_)
	return modelRf.best_estimator_

# evaluate the best random forest model with unseen data
def testModel(modelRf, testX, testY):
	predictions = modelRf.predict(testX)

	# save the predictions of random forest model
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

	# build the random forest classifier model
	rf_random = buildModel()

	# train the model and get the one with best parameters
	start = time.time()
	modelRf = trainModel(rf_random, trainX, trainY)
	end = time.time()
	print("Total training time for random forest:", (end - start), "seconds")

	# evaluate the model
	start = time.time()
	testModel(modelRf, testX, testY)
	end = time.time()
	print("Total evaluation time for random forest:", (end - start), "seconds")
