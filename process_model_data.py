import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# this method loads the feature dataset and convert into 80% vs 20% train and test dataset
'''
It splits the total data into 80% training data and 20% test data. It creates a balanced dataset where
ratio of good address and bad address will be same in training data and test data.
For that purpose, it first splits rows with good address and bad address.
Then splits both good and bad data into train and test set with 80% x 20% ratio
It generates training data by concatenating good and bad training data. generates test data similarly.
After shuffling train and test data, it separates features and labels of training data and test data.
labels indicate whether good adrdress or bad address. 1 indicates bad address and 0 indicates good address.
Train feature, train labels, test features and test labels are saved as numpy arrays.
'''
def loadAndProcessData(data_path):
	# load features csv file
	data = pd.read_csv(data_path)

	# drop address serial column as it is not a feature
	data = data.drop(columns = ['address_hash'])

	# replace true and false values of the column 'is_bad_address' with 1 and 0
	data["is_bad_address"].replace({True: 1, False: 0}, inplace = True)

	# splitting good addresses and bad address
	good_data = data[data['is_bad_address'] == 0]
	bad_data = data[data['is_bad_address'] == 1]
	data = None

	# splitting both good and bad data into train and test set
	train_good, test_good = train_test_split(good_data, test_size=0.2, shuffle=True)
	train_bad, test_bad = train_test_split(bad_data, test_size=0.2, shuffle=True)
	good_data = None
	bad_data = None

	# generate training data by concatenating good and bad training data
	train_data = pd.concat([train_good, train_bad])
	# generate test data by concatenating good and bad training data
	test_data = pd.concat([test_good, test_bad])

	# set unnecessary data to None
	train_good = None
	train_bad = None
	test_good = None
	test_bad = None

	# shuffle train and test data
	train_data = train_data.sample(frac=1).reset_index(drop=True)
	test_data = test_data.sample(frac=1).reset_index(drop=True)
	# specifying drop=True prevents reset_index from creating a column containing the old index entries.

	#convert train data and test data into numpy arrays
	train_data = np.array(train_data)
	test_data = np.array(test_data)

	# convert data types of features and labels into int
	train_data = train_data.astype('int')
	test_data = test_data.astype('int')

	# Splitting train and test data into features and labels
	trainY = train_data[:, 6]
	testY = test_data[:, 6]
	trainX = np.delete(train_data, 6, 1)
	testX = np.delete(test_data, 6, 1)

	# create directory to save train and test data
	os.mkdir('data/model_data')

	# save train and test data
	with open('data/model_data/trainX.npy', 'wb') as f:
		np.save(f, trainX)
	with open('data/model_data/trainY.npy', 'wb') as f:
		np.save(f, trainY)
	with open('data/model_data/testX.npy', 'wb') as f:
		np.save(f, testX)
	with open('data/model_data/testY.npy', 'wb') as f:
		np.save(f, testY)


if __name__ == '__main__':

	# call the loadAndProcessData function to generate train and test data and save as numpy array
	loadAndProcessData("data/output_features.csv")




