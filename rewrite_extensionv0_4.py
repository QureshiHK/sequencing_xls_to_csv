###### Haseeb Qureshi 2024/09/05 v0.3

###### changing suffix is not sufficient so switching to pandas to open xls into dataframe and save as csv

import os
import shutil
import xlrd

import pandas as pd


asksource= input('insert source path: ')
askdest=input('insert destination path: ')

print(asksource)

source_directory = os.chdir(asksource)
#current_dir = os.getcwd
listdirectory = os.listdir()

print(listdirectory)
#print('current directory is {} and listdir = {}'.format(current_dir,listdirectory))
dest_dir = askdest

for a in listdirectory:
    print('current item is {}'.format(a))
    if os.path.isdir(a) is True:
        print('{} is directory'.format(a))
        continue
    prefix,extension = os.path.splitext(a)
    #print(prefix,'+++',extension)
    csvextension = '.csv'
    if extension=='.xls':
        newfilename=dest_dir+prefix+csvextension
        print('1: ', newfilename)
        
        readxls=pd.read_excel(a,sheet_name='bmper_M1_INDEL')
        readxls.to_csv(newfilename)
        
        '''        
        shutil.copy2(a,dest_dir)
        print('2, shutil complete')
        
        os.rename(newfilename,dest_dir+prefix+csvextension)
        print('3,')
        '''
        print('{} converted succesfully'.format(a))
    #shutil.copy2(a,'dest_folder/')
    
    

print('copy complete!')