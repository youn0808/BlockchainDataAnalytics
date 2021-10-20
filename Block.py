from hashlib import sha256
import json
import sys

class Block:
    #def __init__(self, index, listoftransactions, timestamp, previous_hash, nonce=0):
    # def __init__(self, Index, timestamp, previous_hash, nonce):
    def __init__(self, Index, list_of_transactions, time_stamp, previous_hash):
        self.index = Index
        self.list_of_transactions = list_of_transactions
        self.timestamp = time_stamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def get_MBsize(self):

        value= sys.getsizeof(self.list_of_transactions)/(1024*1024)
        return value

    def add_element(self, Transaction):
        if(self.get_corrrect_element(Transaction.get_hash())==False):
            self.list_of_transactions.append(Transaction)
            return True
        else:
            return False

    def get_corrrect_element(self, hash):
        if(len(self.list_of_transactions)!=0):

            for i in self.list_of_transactions: #searching trnasaction list
                if i.get_hash() == hash:    # if there is already existing transaction, we just need to update the trans
                    return i
                else:
                    break# i is trnasaction
        else:
            return False
