###### Haseeb Qureshi 2024/09/06 v0.41

###### changing suffix is not sufficient so switching to pandas to open xls into dataframe and save as csv

import os
import shutil
import pandas as pd


asksource= input('insert source path: ') #input full source directory path when prompted
askdest=input('insert destination path: ') #input full output path

print(asksource)

source_directory = os.chdir(asksource) #change current working directory to source directory

listdirectory = os.listdir()

print(listdirectory)

dest_dir = askdest

for a in listdirectory:
    print('current item is {}'.format(a))
    if os.path.isdir(a) is True:
        print('{} is directory'.format(a))
        continue
    prefix,extension = os.path.splitext(a)
    
    csvextension = '.csv'
    if extension=='.xls':
        newfilename=dest_dir+prefix+csvextension
        print('1: ', newfilename)
        
        read_df=pd.read_excel(a,sep='\s+')
        read_df.to_csv(newfilename)
        

        print('{} converted succesfully'.format(a))
  
    

print('copy complete!')
