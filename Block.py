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
        '''
        :return: hash of the block
        '''
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def get_MBsize(self):
        '''
        :return: value: return size of block
        '''
        value= sys.getsizeof(self.list_of_transactions)/(1024*1024)
        return value

    def add_element(self, Transaction):
        '''
        :param Transaction:
        :return: if we can find exist transaction hash, then add the transaction into the block. and return T/F
        '''
        if(self.get_corrrect_element(Transaction.get_hash())==False):
            self.list_of_transactions.append(Transaction)
            return True
        else:
            return False

    def get_corrrect_element(self, hash):
        '''
        search transaction list and if the list of trnasaction has the hash(parameter) then update the transaction
        '''
        if(len(self.list_of_transactions)!=0):

            for i in self.list_of_transactions: #searching trnasaction list
                print('working')
                if i.get_hash() == hash:    # if there is already existing transaction, we just need to update the trans
                    return i

        return False

    def reciving_from(self, hash_of_previous_transaction, index ,Current_Transaction):
            Transaction=self.get_corrrect_element(hash_of_previous_transaction)
            if(Transaction!=False):
                return Current_Transaction.current_transaction_reciver_address_and_amount(self.get_corrrect_element(hash_of_previous_transaction).sender_addresses[index][1])
            else:
                print ("Transaction is not found")