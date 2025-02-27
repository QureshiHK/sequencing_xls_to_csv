#2025-02-27: HQ program to copy files containing particular string and extension to a designated location, a problem involving copying from network drives. deploy this script via jupyter or windows command line
import os
import shutil
#########REMEMBER TO END FILE PATHS IN THE SLASHES! replace the following 3 variables with your paths and search string of choice#########
currdir='Z:/Whitfield_lab/Shared/Haseeb/csvfind_/' #parent directory to recirsively search to copy files from
newdir='C:/Users/hkqur/Documents/python_A/' #destination directory to copy files to
search_string = 'a' #search substring in filename to match on


matches = []
for root, dirnames, filenames in os.walk(currdir):
    for filename in filenames:
        if filename.endswith(('.xls','.xlsx','.csv')) and search_string in filename: #can modify file extensions to limit search to here if you wish, just replace the or remove the extensions in the endswith function
            print(filename)
            newfilename=newdir+filename
            print('newfilename: ', newfilename)
            shutil.copy2(os.path.join(root,filename),newfilename)
            matches.append(os.path.join(root,filename))

#print(matches)
print('copy complete')
