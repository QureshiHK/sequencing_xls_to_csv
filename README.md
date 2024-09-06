# sequencing_xls_to_csv
corrupted xls outputs from gene sequencing being properly cast as csv files so R can read them


I think Novogene intended to output some of its sequencing outputs as csv but instead output a wonky .xls file that nothing wanted to read properly. This should fix that.

prereqs: pandas

Upon running script, paste in full path of directory with files to convert when prompted for a source. THen paste/type in the full path (with the slash at the end of the path) of the directory  you wish to save your outputs to. I recommend creating a new folder for this.
