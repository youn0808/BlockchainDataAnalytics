import os.path
from multiprocessing import Pool
import sys
import time

def process_file(name):
    ''' Process one file: count number of lines and words '''
    linecount=0
    wordcount=0
    with open(name, 'r') as inp:
        for line in inp:
            linecount+=1
            wordcount+=len(line.split(' '))
    return name, linecount, wordcount
    

def process_files_parallel(arg, dirname, names):
    ''' Process each file in parallel via Poll.map() '''
    pool=Pool()
    results=pool.map(process_file, [os.path.join(dirname, name) for name in names])

#def process_files(arg, dirname, names):
 #   ''' Process each file in via map() '''
  #  results=map(process_file, [os.path.join(dirname, name) for name in names])

if __name__ == '__main__':
    start=time.time()
    os.path.walk('"F:/UofM/MS/Blockchain/project/inputs2010_1.txt", "r"/', process_files_parallel, None)
    print "process_files_parallel()", time.time()-start