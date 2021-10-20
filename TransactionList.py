import numpy as np
import Transaction


class Transaction_List:
    def __init__(self):
        self.listoftransaction = []

    def add_element(self, Transaction):
        if(self.get_corrrect_element(Transaction.get_hash())==False):
            self.listoftransaction.append(Transaction)
            return True
        else:
            return False

    def get_corrrect_element(self, hash):
        if(len(self.listoftransaction)!=0):

            for i in self.listoftransaction: #searching trnasaction list
                if i.get_hash() == hash:    # if there is already existing transaction, we just need to update the trans
                    return i
                else:
                    break# i is trnasaction
        else:
            return False

