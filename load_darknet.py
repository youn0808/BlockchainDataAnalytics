import os
import shutil
import gc
import numpy as np
import pandas as pd
import datetime as dt

intermediate_dir = "data/intermediate_data/"
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
bad_times = {}
bad_prices = {}

# Convert the given timestamp into a readable format
def convertTime(input_time):
	return dt.datetime.utcfromtimestamp(input_time).strftime("%Y/%m/%d %H:%M")

# this method reads prices and times of darknet address in a specific darknet file
def readDarknetData(file_path):
	market_data = pd.read_csv(file_path)
	# separating arrays of prices and times
	addr_prices = market_data['price']
	addr_times = market_data['add_time']
	market_data = None

	# iterating over all darknet addresses
	for i in range(len(addr_times)):
		# extracting month and day of the darknet address
		cur_tx_time = convertTime(int(addr_times[i]))
		month = int(cur_tx_time[5:7])
		day = int(cur_tx_time[8:10])

		# storing address times and prices into dictionaries of corresponding day
		bad_times[str(month) + "-" + str(day)].append(addr_times[i])
		bad_prices[str(month) + "-" + str(day)].append(addr_prices[i])

	# clearing unnecessary variables
	addr_times = None
	addr_prices = None
	
	

if __name__ == '__main__':
	print("Reading Darknet market data...")

	# initializing data holder dictionaries
	for i in range(12):
		for j in range(1, month_days[i] + 1):
			bad_times[str(i + 1) + "-" + str(j)] = []
			bad_prices[str(i + 1) + "-" + str(j)] = []

	# reading darket data of all folders
	folders = os.listdir('data/grams/')

	for folder in folders:
		files = os.listdir('data/grams/' + folder)

		#uncomment below code if you want want to work on a specific file such as Agora.csv
		'''if 'Agora.csv' not in files:
			continue
		readDarknetData('data/grams/' + folder + "/" + 'Agora.csv')
		gc.collect()'''

		#comment below code if you want want to work on a specific file such as Agora.csv
		for fname in files:
			readDarknetData('data/grams/' + folder + "/" + fname)
			gc.collect()

	# after loading folder data into dictionaries, save dictionaries into files
	# iterate month by month
	for i in range(12):
		# initializing folder names
		month = i + 1
		month_dir = intermediate_dir + "month_" + str(month)
		bad_times_dir = month_dir + "/bad_times"
		bad_prices_dir = month_dir + "/bad_prices"

		# check if folder exists. If exists delete and create new
		if os.path.exists(bad_times_dir) and os.path.isdir(bad_times_dir):
			shutil.rmtree(bad_times_dir)
		if os.path.exists(bad_prices_dir) and os.path.isdir(bad_prices_dir):
			shutil.rmtree(bad_prices_dir)

		os.mkdir(bad_times_dir)
		os.mkdir(bad_prices_dir)

		# iterate day by day
		for day in range(1, month_days[i] + 1):
			if len(bad_times[str(month) + "-" + str(day)]) == 0:
				continue
			with open(bad_times_dir + "/bad_times_" + str(day) + ".npy", "wb") as f:
				np.save(f, np.array(bad_times[str(month) + "-" + str(day)]))
				bad_times[str(month) + "-" + str(day)] = None

			with open(bad_prices_dir + "/bad_prices_" + str(day) + ".npy", "wb") as f:
				np.save(f, np.array(bad_prices[str(month) + "-" + str(day)]))
				bad_prices[str(month) + "-" + str(day)] = None

	print("Darknet data reading finished.")
