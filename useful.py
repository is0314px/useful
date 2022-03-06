#coding:utf-8
import os
import sys
import numpy as np
import glob
import pandas as pd

def make_files():
    dir = 'new_file/'
    iter = 10
    for id in range(iter):
        with open(dir + 'test_'+str(id)+'.csv', 'w') as file:
            file.write("hoge\n")
            file.write("hogehoge\n")
            file.write("hogehogehoge\n")

def read_files():
    dir = 'new_file/'
    files = glob.glob(dir+'*')
    files = np.sort(files)
    for file in files:
        print(file)
    
    return files

def rename_files():
    dir = 'new_file/'

    print('Before rename -----')
    files = read_files() #before rename

    for id, old_file in enumerate(files):
        new_file = dir+'new_'+str(id)+'.csv'
        os.rename(old_file, new_file)
    
    print('After remove -----')
    files = read_files() #after rename

def remove_files():
    print('Before remove -----')
    files = read_files() #before remove

    for old_file in files:
        os.remove(old_file)
    
    print('After remove -----')
    files = read_files() #after remove

def csv_to_excel():
    dir = 'new_file/'

    print('Before csv_to_excel -----')
    files = read_files() #before rename

    for id, old_file in enumerate(files):
        read_file = pd.read_csv(old_file)
        new_file = dir+'conv_'+str(id)+'.xlsx'
        read_file.to_excel(new_file, index = None, header=True)
    
    print('After csv_to_excel -----')
    files = read_files() #after rename

if __name__ ==  '__main__':
    if sys.argv[1] == 'makedir':
        os.mkdir('new_file')
    elif sys.argv[1] == 'makefile':
        make_files()
    elif sys.argv[1] == 'readfile':
        read_files()
    elif sys.argv[1] == 'renamefile':
        rename_files()
    elif sys.argv[1] == 'removefile':
        remove_files()
    elif sys.argv[1] == 'csv-excel':
        csv_to_excel()
    else:
        print("ERROR: Check argument")