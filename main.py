import uuid
from _sha256 import sha256
from datetime import datetime


class Transaction:
    hash_of_transaction = 0
    sender_addressess = "" #type address
    receiver_addressees = "" #type address
    time_stamp_of_linking = 0 #UNIXTIMECODE
    ID=""


    def __init__(self,hash_of_tran,sender_add,reciever_addr,id):
        self.hash_of_transaction=hash_of_tran
        self.sender_addressess=sender_add
        self.receiver_addressees=reciever_addr
        ID=id



    def total_input(self):
        return sum(Transaction.input_trans)

    def total_output(self):
        return Transaction.output_trans

    #def verify_linked_input_transactions(self):



   # def input_of_current_transaction_address(self,previous_transaction):





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












