#author
#ychadetc
import time 
from subprocess import call
import subprocess
from shutil import copyfile
import os
x = os.getcwd()
src = x+"\doctor"
dest = x+"\medrecs"
print(type(src))
print(type(dest))
while True:
 time.sleep(20)
 subprocess.call('copy'+" "+src+" "+dest, shell=True)
