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

    def __init__(self,unix_time_transaction, hash_of_tran, inputs, outputs, amount):
        self.unix_time_transaction = unix_time_transaction
        self.hash_of_transaction = hash_of_tran
        self.hash_of_inputs = inputs
        self.hash_of_outputs = outputs
        self.amount = amount


    class Input:
        def __init__(self,prev_hash=None, index=None):
            self.prev_hash = prev_hash
            self.index = index
            #self.signature = None
            #

    class Output:
       def __init__(self, amount = None):
           self.amount = amount


    def add_input(self,prev_hash,index):
        input = Transaction.Input(prev_hash,index) # get input address
        self.sender_addressess.append(input)

    def add_output(self,amount):
        output = Transaction.Output(amount)

    def get_raw_transaction(selfself):
        raw_transaction=""
        for input in self.hash_of_inputs is not None:
            raw_transaction+= str(input.prev_hash)



