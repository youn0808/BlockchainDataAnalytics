# BlockchainDataAnalytics

This project is link the output data(given in the link http://chartalist.org/BitcoinData.html) 
and create a blockchain trnasaction network.

### Check our presentation file https://youn0808.github.io/BlockchainDataAnalytics/. 

## Usage

```python
python main.py
```

# Instructions to run the code:
...............................

Data Organization:
..................
1. A data folder exists in the same directory where Python files are located
2. Put edges2015 folder inside data directory. All input and output files should be under edges2015 folder.
3. For the darknet data, put the unzipped grams folder inside data directory
4. There should be a folder named intermediate_data inside data directory which is initially empty

Running Python Files:
....................
1. At first, run load_network.py file. It should write some file inside intermediate_data directory. Don't delete those files.
2. Secondly, run load_darknet.py file. It should also write some file inside intermediate_data directory. Don't delete those files.
3. At last, run get_features.py file. It will extract necessary features and write to a CSV file named output_features.csv. This csv file will be availabel inside data directory.

## Features:
........
1. address_hash: Unique ID of the address
2. price: Bitcoin amount for the address
3. no_transaction: No of transactions in the 24 hour window of the address
4. no_neighbor: No of extra output addresses of the transaction where this address is also an output
5. avg_price_neighbors: Average price/bitcoin amount of the neighbors of this address
6. month: month when the transaction of this address happened
7. day: day when the transaction of this address happened
8. is_bad_address: True if this address is a darknet address, False otherwise



