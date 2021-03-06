# filefinddel.py
# Andrew, 12/12/2017 (Last Revision)
# Description of intent: Recursively lists all specified files in a specified directory and gives the user the option to delete the files

import glob, os
from pathlib import Path

nexans = True
while True:

    sdir = str(input("Specify full directory path: "))
    sfile = str(input("Specify file type: "))
    dpath = sdir + '**/*' + sfile
    print(dpath)

    if os.path.isdir(sdir):
        file = [os.path.basename(x) for x in glob.glob(dpath, recursive=True)]
        print(file)

        ans = str(input("Do you want to delete all [" + sfile + "] files in this directory?(Y/N): "))
        if ans in ["Y","y"]:
            print('Removing files...')
            for z in glob.glob(dpath, recursive=True):
                os.remove(z)
            print('[' + sfile + '] files have been removed...')
            finans1 = str(input("Do you want to continue searching for file types?(Y/N): "))
            if finans1 in ["Y","y"]:
                nexans = True
            else:
                nexans = False
                print("Exiting...")
                break
                exit() 
        else:
            finans2 = str(input("Do you want to continue searching for file types?(Y/N): "))
            if finans2 in ["Y","y"]:
                nexans = True
            else:
                nexans = False
                print("Exiting...")
                break
                exit()       
    else:
        print('Specified path ' + dpath + ' does not exist! \nExiting...')
        nexans = False
        break
        exit()


#/Users/Andrew/Sites/Projects/wordpress/wp-content/plugins/polylang/flags/

