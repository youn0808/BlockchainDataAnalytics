from collections import defaultdict
import time
import igraph
import pickle


def loadData():
	#data_dir = "edges2010/"
	data_dir= "/home/ashraf/blockchain/data2015/"
	input_files = ["inputs2015_1.txt", "inputs2015_2.txt", "inputs2015_3.txt", "inputs2015_4.txt", "inputs2015_5.txt", "inputs2015_6.txt", 
	"inputs2015_7.txt", "inputs2015_8.txt", "inputs2015_9.txt", "inputs2015_10.txt", "inputs2015_11.txt", "inputs2015_12.txt"]
	output_files = ["outputs2015_1.txt", "outputs2015_2.txt", "outputs2015_3.txt", "outputs2015_4.txt", "outputs2015_5.txt", "outputs2015_6.txt", 
	"outputs2015_7.txt", "outputs2015_8.txt", "outputs2015_9.txt", "outputs2015_10.txt", "outputs2015_11.txt", "outputs2015_12.txt"]

	transCount = 0
	addrCount = 0
	transactions = defaultdict(lambda: -1)
	addressDict = defaultdict(lambda: -1)
	inTransaction = defaultdict(lambda: [])
	inAddress = defaultdict(lambda: [])
	addressList = []
	outAddress = []
	outWeight = []

	for filename in output_files:
		outputData = open(data_dir + filename)
		for line in outputData:
			values = line.split("\t")
			if transactions[values[1]] == -1:
				transactions[values[1]] = transCount
				transCount += 1

			tempAddress = []
			tempWeight = []
			for i in range(2, len(values), 2):
				if addressDict[values[i]] == -1:
					addressDict[values[i]] = addrCount
					addressList.append(values[i])
					addrCount += 1
				tempAddress.append(addressDict[values[i]])
				tempWeight.append(values[i + 1])
			outAddress.append(tempAddress)
			outWeight.append(tempWeight)

	for filename in input_files:
		inputData = open(data_dir + filename)
		for line in inputData:
			values = line.split("\t")
			if transactions[values[1]] != -1:
				tempTrans = []
				tempAddr = []
				for i in range(2, len(values), 2):
					if transactions[values[i]] != -1:
						tempTrans.append(transactions[values[i]])
						tempAddr.append(values[i + 1])
				inTransaction[transactions[values[1]]] = tempTrans
				inAddress[transactions[values[1]]] = tempAddr
	return transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList


def generateGraph(transCount, transactions, outAddress, outWeight, inTransaction, inAddress, addressDict, addressList):
	edge_list = []
	input_addr_index = []
	output_addr_list = []
	output_bitcoin_amount = []

	for i in range(transCount):

		for j in range(len(inTransaction[i])):
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
