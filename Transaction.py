import time
import numpy as np


class Transaction:
    """
      create a new transaction
      hash_of_transaction : Hash of transaction
      amount :<float> amount to be transferred
      sender_add :<string>  sender transaction adderes
      reciver_add : <string> reciver transaction address
      timestamp : unix time code
      """

    def __init__(self, unix_time_transaction, hash_of_tran):
        self.unix_time_transaction = unix_time_transaction
        self.hash_of_transaction = hash_of_tran  # id
        self.sender_addressess = []  # list of input transaction hashes with index [(hash_of_prev_tran,index)]
        self.reciver_addressess = []  # list of output transaction hashes with index [(hash_of_output,bitcoin)]
        self.totalamount = 0
        self.totaloutgoingamount = 0
        self.index = 0


    def get_hash(self):
        return self.hash_of_transaction

    def get_input(self, index):
        return self.sender_addressess[index]

    def get_output(self, index):
        return self.reciver_addressess[index]

    def current_transaction_sender_addressess_and_amounts(self, next_hash_of_transaction, bitcoin):
        # if self.totaloutgoingamount<self.totalamount:
        if(next_hash_of_transaction!='',bitcoin!=''):

            self.sender_addressess.insert(self.index, [next_hash_of_transaction,bitcoin])
            self.index += 1
        # else:
        #     print("Error")


    def current_transaction_reciver_address_and_amount(self, bitcoins):
        self.totalamount += bitcoins

    def reciving_from(self, hash_of_previous_transaction, index):

        return self.current_transaction_reciver_address_and_amount(hash_of_previous_transaction.sender_addresses[index][1])
