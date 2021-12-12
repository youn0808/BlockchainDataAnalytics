import os
import gc
import numpy as np
from csv import writer

year = 2015
intermediate_dir = "data/intermediate_data/"
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
featureNames = ["address_hash", "price", "no_transaction", "no_neighbor", "avg_price_neighbors", "month", "day", "is_bad_address"]

month_dir = None
bad_times_dir = None
bad_prices_dir = None
tx_times_dir = None
addr_counts_dir = None
avg_prices_dir = None
addr_prices_dir = None
addr_tx_index_dir = None
addr_hashes_dir = None

# this method extract address features of a given day and write into a csv file
def getFeaturesOfDay(month, day, isBadAddrAvailable, csvWriter):
	# initiazing intermediate data files
	tx_times = np.load(tx_times_dir + "/tx_times_" + str(day) + ".npy")
	addr_counts = np.load(addr_counts_dir + "/addr_counts_" + str(day) + ".npy")
	avg_prices = np.load(avg_prices_dir + "/avg_prices_" + str(day) + ".npy")
	addr_prices = np.load(addr_prices_dir + "/addr_prices_" + str(day) + ".npy")
	addr_tx_index = np.load(addr_tx_index_dir + "/addr_tx_index_" + str(day) + ".npy")
	addr_hashes = np.load(addr_hashes_dir + "/addr_hashes_" + str(day) + ".npy")

	bad_times = None
	bad_prices = None
	# keeping track of which addresses are already added
	added_addrs = [False] * len(addr_prices)

	# check if bad addresses are available for the corresponding day
	if isBadAddrAvailable:
		# open numpy files lisitng bad address times and prices on the corresponding day
		bad_times = np.load(bad_times_dir + "/bad_times_" + str(day) + ".npy")
		bad_prices = np.load(bad_prices_dir + "/bad_prices_" + str(day) + ".npy")

		for i in range(len(bad_prices)):
			# convert darknet price into original price
			price_in_darknet = int(round(float(bad_prices[i]) * 10 ** 8))
			if price_in_darknet == 0:
				continue

			# check if the bad address price matches with address prices of the same day
			indices = np.where(addr_prices == price_in_darknet)[0]
			if len(indices) > 0:
				# iterate over all price matches to find matches in timestamp
				for j in indices:
					index = addr_tx_index[j]
					if added_addrs[j] == False: #tx_times[index] == bad_times[i]:
						# There is a match. Write all features into csv file
						features_row = []
						features_row.append(addr_hashes[j])
						features_row.append(addr_prices[j])
						features_row.append(len(tx_times))
						features_row.append(addr_counts[index] - 1)
						features_row.append(avg_prices[index])
						features_row.append(month)
						features_row.append(day)
						features_row.append(True)
						csvWriter.writerow(features_row)
						added_addrs[j] = True

	# adding 1k good addresses
	good_count = 0
	for i in range(len(addr_prices)):
		if int(addr_prices[i]) == 0 or added_addrs[i] == True:
			continue

		index = addr_tx_index[i]

		features_row = []
		features_row.append(addr_hashes[i])
		features_row.append(addr_prices[i])
		features_row.append(len(tx_times))
		features_row.append(addr_counts[index] - 1)
		features_row.append(avg_prices[index])
		features_row.append(month)
		features_row.append(day)
		features_row.append(False)
		csvWriter.writerow(features_row)
		added_addrs[i] = True

		good_count += 1
		if good_count > 1000:
			break

	# clearing unnecessary data variables
	tx_times = None
	addr_counts = None
	avg_prices = None
	addr_prices = None
	addr_tx_index = None
	addr_hashes = None
	bad_times = None
	bad_prices = None


if __name__ == '__main__':
	print("Extracting features...")
	f_csv = open("data/output_features.csv", "a", encoding='UTF8', newline='')
	csvWriter = writer(f_csv)
	csvWriter.writerow(featureNames)

	for i in range(12):
		month = i + 1
		# initializing data directories for the given month
		month_dir = intermediate_dir + "month_" + str(month) + "/"

		#initializing data directories of darknet data for the given month
		bad_times_dir = month_dir + "bad_times/"
		bad_prices_dir = month_dir + "bad_prices/"

		#initializing data directories of network data for the given month
		tx_times_dir = month_dir + "tx_times/"
		addr_counts_dir = month_dir + "addr_counts/"
		avg_prices_dir = month_dir + "avg_prices/"
		addr_prices_dir = month_dir + "addr_prices/"
		addr_tx_index_dir = month_dir + "addr_tx_index/"
		addr_hashes_dir = month_dir + "addr_hashes/"

		#getting bad file names under current month directory
		fnames_bad_times = os.listdir(bad_times_dir)
		fnames_bad_prices = os.listdir(bad_prices_dir)

		for day in range(1, month_days[i] + 1):
			if "bad_times_" + str(day) + ".npy" in fnames_bad_times:
				isBadAddrAvailable = True
			else:
				isBadAddrAvailable = False

			# calling appropriate function to extract features
			getFeaturesOfDay(month, day, isBadAddrAvailable, csvWriter)
			gc.collect()

	#closing the CSV file after writing all features
	f_csv.close()
	print("Feature extraction finished.")




