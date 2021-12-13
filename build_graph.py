from collections import defaultdict
import time
import igraph
import pickle


def loadData():
	data_dir = "edges2010/"
	# data_dir= "data/edges2015/"
	# input_files = ["inputs2015_1.txt", "inputs2015_2.txt", "inputs2015_3.txt", "inputs2015_4.txt", "inputs2015_5.txt", "inputs2015_6.txt",
	# "inputs2015_7.txt", "inputs2015_8.txt", "inputs2015_9.txt", "inputs2015_10.txt", "inputs2015_11.txt", "inputs2015_12.txt"]
	# output_files = ["outputs2015_1.txt", "outputs2015_2.txt", "outputs2015_3.txt", "outputs2015_4.txt", "outputs2015_5.txt", "outputs2015_6.txt",
	# "outputs2015_7.txt", "outputs2015_8.txt", "outputs2015_9.txt", "outputs2015_10.txt", "outputs2015_11.txt", "outputs2015_12.txt"]
	# #
	input_files = ["inputs2010_1.txt", "inputs2010_2.txt", "inputs2010_3.txt", "inputs2010_4.txt", "inputs2010_5.txt",
				   "inputs2010_6.txt",
				   "inputs2010_7.txt", "inputs2010_8.txt", "inputs2010_9.txt", "inputs2010_10.txt", "inputs2010_11.txt",
				   "inputs2010_12.txt"]
	output_files = ["outputs2010_1.txt", "outputs2010_2.txt", "outputs2010_3.txt", "outputs2010_4.txt",
					"outputs2010_5.txt", "outputs2010_6.txt",
					"outputs2010_7.txt", "outputs2010_8.txt", "outputs2010_9.txt", "outputs2010_10.txt",
					"outputs2010_11.txt", "outputs2010_12.txt"]
	transCount = 0 #number of transactions
	addrCount = 0 #number of address
	transactions = defaultdict(lambda: -1) #using defaultdict to handling missing key
	addressDict = defaultdict(lambda: -1)
	inTransaction = defaultdict(lambda: []) #Intrnasction store list of {txn_ID:[all_incomming_txnID]}
	inAddress = defaultdict(lambda: [])  #InAddress store list of {txn_ID:[all incomming address's index]}

	addressList = []
	outAddress = []
	outWeight = []

	# read output file
	for filename in output_files:
		outputData = open(data_dir + filename)
		# read data line by line
		for line in outputData:
			# split data by tab
			values = line.split("\t")
			if transactions[values[1]] == -1: # if hash of transaction does not exist, add it into the transactions
				transactions[values[1]] = transCount # set key is txn_hash value: count
				transCount += 1

			tempAddress = []
			tempWeight = []
			for i in range(2, len(values), 2):
				if addressDict[values[i]] == -1: # if the address does not exist
					addressDict[values[i]] = addrCount # address dict store hash of output address and count number (hashMap)
					addressList.append(values[i])
					addrCount += 1
				tempAddress.append(addressDict[values[i]]) #values[i] return hash_address, addressDict[val[i]]= Addr_ID, tempAddre store the specific hash_txns's addressess IDs.
				tempWeight.append(values[i + 1])
			outAddress.append(tempAddress)
			outWeight.append(tempWeight)

	for filename in input_files:
		inputData = open(data_dir + filename)
		for line in inputData:
			#seperate by tab
			values = line.split("\t")
			if transactions[values[1]] != -1: # if target trasn does exist move in
				tempTrans = []
				tempAddr = []
				for i in range(2, len(values), 2):
					if transactions[values[i]] != -1:
						tempTrans.append(transactions[values[i]]) # get the transaction(ID) from the list of transactions and store the ID into the tempTransaction.
						tempAddr.append(values[i + 1]) # get the given transaction's (i)'th index's of address
				inTransaction[transactions[values[1]]] = tempTrans # transactions[values[1]] is the current transaction , temo trans we need to look up
				inAddress[transactions[values[1]]] = tempAddr
	return transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList


def generateGraph(transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList):
	edge_list = [] #edge_list contains list of [from_txn_ID, to_txn_ID]
	input_addr_index = [] #contains list of incomming txn's address index
	output_addr_list = []
	output_bitcoin_amount = []

	# linking edges
	for i in range(transCount): #loop all transactionns

		for j in range(len(inTransaction[i])): # len(inTransation[i]) will return the number of previous transactions
			edge_list.append([inTransaction[i][j], i])
			input_addr_index.append(inAddress[i][j])
	
	bitcoin_graph = igraph.Graph(n = transCount, 
		edges = edge_list, 
		edge_attrs = {'input_addr_index': input_addr_index},
		vertex_attrs = {'output_addr_list': outAddress, 'output_bitcoin_amount': outWeight},
		directed = True)
	return bitcoin_graph


# Call load data and graph generation functions here
t_start = time.time()
transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList = loadData()
t_end = time.time()
print("Data loading time: " + str((t_end - t_start) * 1000) + " milliseconds")
#print("Number of transactions: " + str(transCount))


t_start = time.time()
bitcoin_graph = generateGraph(transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList)
t_end = time.time()
print("\nGraph generation time: " + str((t_end - t_start) * 1000) + " milliseconds")
#print("Number of vertices: " + str(bitcoin_graph.vcount()))
#print("Number of edges: " + str(bitcoin_graph.ecount()))

#bitcoin_graph.write_svg("bitcoin_graph.svg")
with open('address_list.pickle', 'wb') as file_addr_list:
	pickle.dump(addressList, file_addr_list)

with open('bitcoin_graph.pickle', 'wb') as file_graph:
	pickle.dump(bitcoin_graph, file_graph)
