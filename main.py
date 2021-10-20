import os
from Transaction import Transaction
import TransactionList
import glob
import errno
from re import search

def main():


    Transactionlist=0

    path = 'OutputFile/*.txt'
    files = glob.glob(path)
    for name in files:
        try:
            with open(name) as f:
                inp = open(name, "r")
                for line in inp.readlines():
                    x = line.split()
                    new_transaction = Transaction(x[0], x[1])  # x[0] unix_time_transaction, x[1] hash_of_tran,
                    next_value = 2
                    while x[next_value] != '\n':
                        # new_transaction.reciving_from(x[next_value],x[next_value+1])
                        next_value+=1
  #                      new_transaction.current_transaction_sender_addressess_and_amounts(x[next_value], x[next_value])
                        # create new transaction

                        next_value += 1
                    Transactionlist.add_element(new_transaction)
                inp.close()
        except IOError as exc:
            print('error')






# #read output file
#
#     inp = open("InputFile\inputs2010_1.txt" "r")
#     for line in inp.readlines():
#         for i in line:
#             x = line.split()
#             desired_transaction=Transactionlist.get_corrrect_element(x[1])
#             next_value=2
#             while x[next_value] != '\n':
#                 desired_transaction.reciving_from(x[next_value],x[next_value+1])
#                 next_value += 1
#















if __name__ == "__main__":
    main()











