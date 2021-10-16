import sys

class UTXO:
    def __init__(self, transaction_hash,index):
        self.transaction_hash=transaction_hash
        self.index = index
