import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

def plotRocCurve(testY, predY, modelName, figName):
	# get the roc_curve values for XGboost model
	fpr, tpr, thresh = roc_curve(testY, predY)
	auc = roc_auc_score(testY, predY)


	fig = plt.figure()
	plt.plot(fpr, tpr, label="AUC={}".format(str(auc)))

	# set labels
	plt.xlabel("False Positive Rate")
	plt.ylabel("True Positive Rate")
	plt.title("Test data ROC Curve for " + modelName)
	plt.legend(loc=0)


	plt.show()
	fig.savefig(figName)


if __name__ == '__main__':
	# load test actual labels and predicted labels
	testY = np.load('data/model_data/testY.npy')
	predRf = np.load('data/model_data/predictions_rf.npy')
	predXgb = np.load('data/model_data/predictions_xgb.npy')

	# call plotRocCurve() method to curve plots
	# plot for XGboost model
	plotRocCurve(testY, predXgb, "XGBoost Model", "data/roc_xgboost.png")

	# plot for random Forest model
	plotRocCurve(testY, predRf, "Random Forest Model", "data/roc_rf.png")


