# secureerase.py
# Andrew, 12/12/2017 (Last Revision)
# Description of intent: Simple script to run a secure erase on a Mac OS X - in order to reclaim "purgeable space" 
# NOTE:Erasing freespace only works on mounted and writable volumes

import subprocess

subprocess.call('df -h', shell=True)
subprocess.call('diskutil list', shell=True)
wone = str(input("What disk do want to secure erase?(i.e. disk0s2): "))
           
ques = str(input("Do you want to secure erase freespace data in " + wone + "?(Y/N): "))
if ques in ["Y","y"]:
    subprocess.call('diskutil secureerase freespace 0 ' + wone, shell=True)
    subprocess.call('df -h', shell=True)
    print('Exiting...')
    exit()
else:
    print("Exiting...")
    exit()