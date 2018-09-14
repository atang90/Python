# secureerase.py
# Andrew, 09/13/2018 (Last Revision)
# Description of intent: Simple script to run a secure erase on a Mac OS X - in order to reclaim "purgeable space"
# NOTE:Erasing freespace only works on mounted and writable volumes

import subprocess

subprocess.call('df -h', shell=True)
subprocess.call('diskutil list', shell=True)
wone = str(input("What disk do want to secure erase?[i.e. disk0s2]: "))
           
ques = str(input(("Secure erase freespace will run on ""'" + wone + "'"", do you want to continue?(Y/N): "))
if ques in ["Y","y"]:
    print("diskutil secureerase freespace 0 " + wone + "........")
    subprocess.call('diskutil secureerase freespace 0 ' + wone, shell=True)
    subprocess.call('df -h', shell=True)
    print('Exiting...')
    exit()
else:
    print("Exiting...")
    exit()
