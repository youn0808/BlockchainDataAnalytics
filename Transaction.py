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
        self.sender_addressess = []
        self.reciver_addressess = []
        self.amount = amount

    class Input:
        def __init__(self, prev_hash=None, index=None):
            self.prev_hash = prev_hash
            self.index = index

    class Output:
        def __init__(self, amount=None):
            self.amount = amount

    def add_input(self, prev_hash, index):
        sender_addr = Transaction.Input(prev_hash, index)  # get input address
        self.sender_addressess.append(sender_addr)

    def add_output(self, amount):
        reciver_addr = Transaction.Output(amount)
        self.reciver_addressess.append(reciver_addr)

    def get_hash(self):
        return self.hash_of_transaction

    def get_input(self, index):
        return self.inputs[index]

    def get_output(self, index):
        return self.outputs[index]
