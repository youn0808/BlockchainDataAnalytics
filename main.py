from typing import List, Any


class Block:
    time_of_transactions = 0
    hash_transactions=[]
    address=[]
    transaction_id=[]
    def len_of_transaction(self):
        return len(Block.transaction_id)

class list_of_transaction:


class Transaction:

    inputs_trans =[] # type input
    outputs_trans=[] # type input
    total_input_amount = 0
    total_output_amount = 0

    def total_input(self):
        return sum(Transaction.input_trans)

    def total_output(self):
        return sum(Transaction.output_trans)

    def verify_linked_input_transactions(self):



    def input_of_current_transaction_address(self,previous_transaction):
        if(previous_transaction.outputs_trans)




class ouput:
    adresses=[] # hashes
    amount = 0

    def __init__(self,amount_in):
        self.amount = amount_in

    def specific_output(self,input_address):
        return self.adresses.index(input_address)


class intput:
    amount = 0;












