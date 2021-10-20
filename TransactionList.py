import numpy as np
import Transaction


class Transaction_List:
    def __init__(self):
        self.listoftransaction = np.array()

    def add_element(self, Transaction):
        if(self.get_corrrect_element(Transaction.get_hash())==False):
            self.listoftransaction = np.append(Transaction)
        else:
            return False

    def get_corrrect_element(self, hash):
        for i in self.listoftransaction:
            if i.get_hash == hash:
                return i
            else:
                return False# i is trnasaction

