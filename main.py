from datetime import datetime

class Blockchain:
    Blockchain_size=0;
    timestamp=0

    def create_new_block(self,nonce_x,previous_blockhash_y,hash_z):
        m= Block(nonce_x,previous_blockhash_y,hash_z)
        self.Blockchain_size+=1
        self.timestamp=datetime.now()



class Block:
    blockheight=0
    previous_blockhash=0
    nonce=0
    timestamp = 0
    transactionlist=[]


    def __init__(self,nonce,previous_blockhash, hash):
        self.nonce=nonce
        self.previous_blockhash=previous_blockhash
        self.hash=hash
        self.timestamp = datetime.now()



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












