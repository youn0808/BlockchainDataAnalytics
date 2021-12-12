import os
import gc
import datetime as dt
import numpy as np

year = 2015
data_dir = "data/edges" + str(year) + "/"
intermediate_dir = "data/intermediate_data/"
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
output_files = []

# automatically generate names of output files
def generateOutputFileNames():
	for i in range(12):
		output_files.append("outputs" + str(year) + "_" + str(i + 1) + ".txt")

# Convert the given timestamp into a readable format
def convertTime(input_time):
	return dt.datetime.utcfromtimestamp(input_time).strftime("%Y/%m/%d %H:%M")

# this method reads data in a month by month basis
def readNetworkData(month):
	month_dir = intermediate_dir + "month_" + str(month + 1)
	os.mkdir(month_dir)

	# initialize empty data dictionaries
	tx_times = {}
	addr_counts = {}
	avg_prices = {}
	addr_prices = {}
	addr_tx_index = {}
	addr_hashes = {}

	# initialize each day of data dictionary with empty lists
	for day in range(1, month_days[month] + 1):
		tx_times[day] = []
		addr_counts[day] = []
		avg_prices[day] = []
		addr_prices[day] = []
		addr_tx_index[day] = []
		addr_hashes[day] = []

	# Open output file
	outputData = open(data_dir + output_files[month])

	# iterate every line of output file
	for line in outputData:
		# spliting words in a line
		values = line.split("\t")
		cur_tx_time = convertTime(int(values[0]))
		day = int(cur_tx_time[8:10])

		# setting data to the appropriate dictionary
		temp_total_price = 0
		temp_addr_count = 0
		for i in range(2, len(values), 2):
			addr_tx_index[day].append(len(tx_times[day]))
			addr_hashes[day].append(values[i])
			addr_prices[day].append(int(values[i + 1]))
			temp_addr_count += 1
			temp_total_price += int(values[i + 1])
		if temp_addr_count > 0:
			tx_times[day].append(values[0])
			addr_counts[day].append(temp_addr_count)
			avg_prices[day].append(temp_total_price//temp_addr_count)

	# initialize data directory names
	tx_times_dir = month_dir + "/tx_times"
	addr_counts_dir = month_dir + "/addr_counts"
	avg_prices_dir = month_dir + "/avg_prices"
	addr_prices_dir = month_dir + "/addr_prices"
	addr_tx_index_dir = month_dir + "/addr_tx_index"
	addr_hashes_dir = month_dir + "/addr_hashes"
	os.mkdir(tx_times_dir)
	os.mkdir(addr_counts_dir)
	os.mkdir(avg_prices_dir)
	os.mkdir(addr_prices_dir)
	os.mkdir(addr_tx_index_dir)
	os.mkdir(addr_hashes_dir)

	# saving data into files in a day by day basis
	for day in range(1, month_days[month] + 1):
		with open(tx_times_dir + "/tx_times_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(tx_times[day]))
			tx_times[day] = None

		with open(addr_counts_dir + "/addr_counts_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(addr_counts[day]))
			addr_counts[day] = None

		with open(avg_prices_dir + "/avg_prices_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(avg_prices[day]))
			avg_prices[day] = None

		with open(addr_prices_dir + "/addr_prices_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(addr_prices[day]))
			addr_prices[day] = None

		with open(addr_tx_index_dir + "/addr_tx_index_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(addr_tx_index[day]))
			addr_tx_index[day] = None

		with open(addr_hashes_dir + "/addr_hashes_" + str(day) + ".npy", "wb") as f:
			np.save(f, np.array(addr_hashes[day]))
			addr_hashes[day] = None

	# clearing dictionaries as inside data no longer required
	tx_times.clear()
	addr_counts.clear()
	avg_prices.clear()
	addr_prices.clear()
	addr_tx_index.clear()
	addr_hashes.clear()


if __name__ == '__main__':
	generateOutputFileNames()

	# load data and generate network in a month basis
	for i in range(12):
		print("Loading month " + str(i + 1) + " data ...")
		readNetworkData(i)
		# clearing cach after reading and saving each month data
		gc.collect()

	print("Network data loading finished.")


