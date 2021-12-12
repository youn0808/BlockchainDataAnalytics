# BlockchainDataAnalytics

This project is link the output data(given in the link http://chartalist.org/BitcoinData.html) 
and create a blockchain trnasaction network.


## Usage

```python
python main.py
```



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



