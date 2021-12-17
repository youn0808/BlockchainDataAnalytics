import os
import shutil
import gc
import numpy as np
import pandas as pd
import datetime as dt
import time

intermediate_dir = "data/intermediate_data/"
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 2015
bad_times = {}
bad_prices = {}

# Convert the given timestamp into a readable format as example: 2015/07/27 08:58
def convertTime(input_time):
	return dt.datetime.utcfromtimestamp(input_time).strftime("%Y/%m/%d %H:%M")


# this method reads prices and times of darknet address in a specific darknet file
'''
It takes the path of a darknet file, converts it into a pandas dataframe and reads all rows.
For each row, it parses the timestamp and extract year, month and date.
Then, it adds the timestamp and price of the row into the dictionary of the corresponding day
The purpose is to store all addresses of this file into a dictionary against transaction dates 
'''
def readDarknetData(file_path):
	# read the darknet file
	try:
		market_data = pd.read_csv(file_path)
	except Exception as e:
		return

	# separating arrays of prices and times
	addr_prices = market_data['price']
	addr_times = market_data['add_time']
	market_data = None

	# iterating over all rows in this file
	for i in range(len(addr_times)):
		# convert the timestamp into year-month-day hour:minute format
		cur_tx_time = convertTime(int(addr_times[i]))

		# extracting year, month and day of the darknet address
		yr = int(cur_tx_time[0:4])
		month = int(cur_tx_time[5:7])
		day = int(cur_tx_time[8:10])

		# if current address is not for the year we are working, skip
		if yr != year:
			continue

		# storing address times and prices into dictionaries of corresponding day
		bad_times[str(month) + "-" + str(day)].append(addr_times[i])
		bad_prices[str(month) + "-" + str(day)].append(addr_prices[i])

	# clearing unnecessary variables
	addr_times = None
	addr_prices = None
	
	

if __name__ == '__main__':
	'''
	Here, we store time stamps and prices of all darknet files into two files: one for times which we call
	bad times, and another for prices which we call bad prices
	'''

	print("Reading Darknet market data...")
	t_start = time.time()

	# initializing data holder dictionaries for 12 months
	for i in range(12):
		for j in range(1, month_days[i] + 1):
			bad_times[str(i + 1) + "-" + str(j)] = []
			bad_prices[str(i + 1) + "-" + str(j)] = []

	# reading darket data of all folders
	folders = os.listdir('data/grams/')

	for folder in folders:
		# get a list of all files within each folder
		files = os.listdir('data/grams/' + folder)

		#uncomment below code if you want want to work on a specific file such as Agora.csv
		'''if 'Agora.csv' not in files:
			continue
		readDarknetData('data/grams/' + folder + "/" + 'Agora.csv')
		gc.collect()'''

		#comment below code if you want want to work on a specific file such as Agora.csv
		# read all files under current folder
		for fname in files:
			# call the method we initialized earlier, it stores info of this file into dictionaries
			readDarknetData('data/grams/' + folder + "/" + fname)
			# clear unnecessary caches
			gc.collect()

	# after loading folder data into dictionaries, save dictionaries into files
	# iterate month by month from 1 to 12
	for i in range(12):
		# initializing folder names of bad times and bad prices for each month
		month = i + 1
		month_dir = intermediate_dir + "month_" + str(month)
		bad_times_dir = month_dir + "/bad_times"
		bad_prices_dir = month_dir + "/bad_prices"

		# check if folder exists. If exists delete them
		if os.path.exists(bad_times_dir) and os.path.isdir(bad_times_dir):
			shutil.rmtree(bad_times_dir)
		if os.path.exists(bad_prices_dir) and os.path.isdir(bad_prices_dir):
			shutil.rmtree(bad_prices_dir)

		# create folders
		os.mkdir(bad_times_dir)
		os.mkdir(bad_prices_dir)

		# iterate day by day and save the data of each day as numpy array files
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
	t_end = time.time()
	print("Darknet data loading time:", str(t_end - t_start), "seconds")
