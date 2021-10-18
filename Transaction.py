import time


class Transaction:
    """
      create a new transaction
      hash_of_transaction : Hash of transaction
      amount :<float> amount to be transferred
      sender_add :<string>  sender transaction adderes
      reciver_add : <string> reciver transaction address
      timestamp : unix time code
      """

    def __init__(self, unix_time_transaction, hash_of_tran, amount = 0):
        self.unix_time_transaction = unix_time_transaction
        self.hash_of_transaction = hash_of_tran
        self.sender_addressess = []     # list of input transaction hashes with index
        self.reciver_addressess = []    #list of output transaction hashes with index
        self.amount = amount

    class Input:
        def __init__(self, prev_hash=None, index=None):
            self.prev_hash = prev_hash
            self.index = index

    class Output:
        def __init__(self, hash_of_output, amount=None):
            self.amount = amount
            self.hash_of_output = hash_of_output

    def add_input(self, prev_hash, index):
        sender_addr = Transaction.Input(prev_hash, index)  # get input address
        self.sender_addressess.append(sender_addr)

    def add_output(self, hash_of_output, amount):
        reciver_addr = Transaction.Output(hash_of_output, amount)
        self.reciver_addressess.append(reciver_addr)

    def get_hash(self):
        return self.hash_of_transaction

    def get_input(self, index):
        return self.inputs[index]

    def get_output(self, index):
        return self.outputs[index]
