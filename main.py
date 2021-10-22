import os
import time

from Blockchain import Blockchain
from Transaction import Transaction
from TransactionList import Transaction_List
import glob
import errno
from re import search
from Block import Block



def main():
    #create genesis block in blockchain
    block_list = Blockchain()


    new_transaction_list = Block(0, [], time.time(), 0)

    path = 'OutputFile/*.txt'
    files = glob.glob(path)
    for name in files:
        try:
            with open(name) as f:
                inp = open(name, "r")
                for line in inp.readlines():
                    x = line.split()
                    size = len(x)
                    next_value = 2
                    if (new_transaction_list.get_MBsize()<1): # if size of block is less than 1 MB then keep add transactions into the block.
                            actingtransaction = new_transaction_list.get_corrrect_element(x[1])

                    else: # create new block

                        block_list.add_block(new_transaction_list,new_transaction_list.compute_hash()) #add
                        new_transaction_list = Block(0, [], time.time(), 0)

                    if actingtransaction == False:  # if the transaction does not exist before, create new Transaction
                        new_transaction = Transaction(x[0], x[1])  # x[0] unix_time_transaction, x[1] hash_of_tran,
                        new_transaction_list.add_element(new_transaction)
                        # next_value = 2

                    else:
                        # if the transaction already exists
                        new_transaction = actingtransaction


                    while next_value != size: #upodating
                        new_transaction.current_transaction_sender_addressess_and_amounts(x[next_value], x[next_value+1])
                        next_value+=2


                inp.close()
        except IOError as exc:
            print('Output file error')

#
# #read input file
#
#     path = 'InputFile/*.txt'
#     input_files = glob.glob(path)
#     for name in input_files:
#         try:
#             with open(name) as f:
#                 inp2 = open(name, "r")
#                 for line in inp2.readlines():
#                     x = line.split()
#                     size = len(x)
#                     next_value = 2
#                     if (new_transaction_list.get_MBsize()<1): # if size of block is less than 1 MB then keep add transactions into the block.
#                             actingtransaction = new_transaction_list.get_corrrect_element(x[1])
#
#                     else: # create new block
#
#                         block_list.add_block(new_transaction_list,new_transaction_list.compute_hash()) #add
#                         new_transaction_list = Block(0, [], time.time(), 0)
#
#                     if actingtransaction == False:  # if the transaction does not exist before, create new Transaction
#                         new_transaction = Transaction(x[0], x[1])  # x[0] unix_time_transaction, x[1] hash_of_tran,
#                         new_transaction_list.add_element(new_transaction)
#
#
#                     else:
#                         # if the transaction already exists
#                         new_transaction = actingtransaction
#
#                     while next_value != size: #upodating
#                         new_transaction_list.reciving_from(x[next_value],x[next_value+1],new_transaction) # pass hash_of_trnasaction, index of output from the input transaction untill the end of line
#                         next_value += 2
#
#                 inp2.close()
#         except IOError as exc:
#             print('Input file error')
#
#
#


if __name__ == "__main__":
    main()

