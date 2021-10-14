from typing import List, Any


class Block:
    blockheight=0
    previous_blockhash=0
    nonce=0
    time=0
    transactionlist=[]

class Transaction:
    hash_of_transaction=0
    sender_addressess=[] #type address
    reciever_addressess=[] #type address
    time_stamp_of_linking = 0 #UNIXTIMECODE

    def total_input(self):
        return sum(Transaction.input_trans)

    def total_output(self):
        return Transaction.output_trans

    def verify_linked_input_transactions(self):



    def input_of_current_transaction_address(self,previous_transaction):
        if(previous_transaction.outputs_trans)


class ouput:
    adresses=[]             #The array should contain all the sent out addresses of a previous transaction
    amount = 0
    releasingtime=0

    def __init__(self,amount_in,time):
        self.amount = amount_in
        self.releasingtime=time

    def totalamount(self,transaction):
        return sum(addresss[transaction.inputs_trans])


    def specific_output(self,input_address):
        return self.adresses.index(input_address)


class intput:
    amount = 0;            #This is for current trnsaction

class address:  #each address
    Bitcoin_amount=0
    address=""
    def getamount(self): return self.Bitcoin_amount;












