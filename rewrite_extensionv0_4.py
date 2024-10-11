###### Haseeb Qureshi 2024/10/11 v0.6

###### changing suffix is not sufficient so switching to pandas to open xls into dataframe and save as csv

import os
import shutil
import xlrd
import platform
import pandas as pd


asksource= input('insert source path: ')
askdest=input('insert destination path: ')

#check operating system, check if user destination input contains slash at end of path for smooth destination file name append. if no slash on end (os dependent, then append one here, otherwise continue)
if platform.system()=='Linux':
    if askdest[len(askdest)-1]!='/':
        askdest=askdest+'/'
else:
    if askdest[len(askdest)-1]!='\\':
        askdest=askdest+'\\'


print(asksource)

source_directory = os.chdir(asksource) #change current working directory to source folder
listdirectory = os.listdir() #create list of source folder contents

print(listdirectory)
dest_dir = askdest #redundant process at this point but it's from a legacy version of this script and it was simpler just to rename the variable than running find/replace

for a in listdirectory:
    print('current item is {}'.format(a)) #iterate through source folder contents and check if files meet criteria. if directory then pass. otherwise, the script is currently hardcoded to seek out .xls files that have csv-like behaviour.
    if os.path.isdir(a) is True:
        print('{} is directory'.format(a))
        continue
    prefix,extension = os.path.splitext(a)
    
    csvextension = '.csv'
    extension_list = ['.xls','.csv','.xlsx']
    if extension in extension_list: #coutnerintuitive to treat excel .xls files as csv but that seems to be the nature of thse novogene outputs for now. should add option to change file type, make it more dynamic.
        newfilename=dest_dir+prefix+csvextension #create file path for converted xls file
        print('1: ', newfilename) #sanity check
        
        ###find delimiter and declare as string to pass to sep argument in read_df
        ###assuming the delimiters are either space and tab so try one or the other. If delimiter isn't either then it will just error out I guess.
        try:
            read_df=pd.read_csv(a,sep='\t') #read weird .xls using space(s) as separator and create dataframe
            read_df.to_csv(newfilename) #write new csv file (properly) from imported dataframe
        except:
            read_df=pd.read_csv(a,sep='\s+') #read weird .xls using space(s) as separator and create dataframe
            read_df.to_csv(newfilename) #write new csv file (properly) from imported dataframe            
        print('{} converted succesfully'.format(a))
    
    
    

print('copy complete!')
