#!/usr/bin/env python

import os
import sys
import glob
import time
import shutil
import datetime


# this is the mountpoint where memory card will be mounted
cfolder = "/run/media/bjoern/EOS_DIGITAL/DCIM/100EOS5D"

# this is the folder where your pictures are stored locally
lfolder = "/home/bjoern/Bilder"

# this will be prefixed to the outputfolder
today = datetime.date.today()
now = today.strftime("%Y_%m_%d")

# outputfolder
try:
    ofolder=(f"{lfolder}/{now}_{sys.argv[1]}")
except IndexError:
    print("Please give local folder as argument")
    print(f"{sys.argv[0]} <foldername>")
    exit(-1)

t1 = "/run/media/bjoern/EOS_DIGITAL/DCIM/100EOS5D"
t2 = "/home/bjoern/Bilder"

if cfolder == t1 or lfolder == t2:
    print("Warning: cfolder or lfolder have not been adjusted")
    print("Warning: If you are not me, than you should do this.")
    time.sleep(2)

lfiles = []
for filename in glob.iglob(f'{lfolder}/**/*', recursive=True):
    lfiles.append(os.path.basename(filename))

cfiles = [] 
for filename in glob.iglob(f'{cfolder}/**/*', recursive=True):
    cfiles.append(os.path.basename(filename))

if len(cfiles) == 0:
    print("Error: No files found on external device")
    print("Error: Maybe the device is not mounted")
    exit(-2)
    
nfiles=set(cfiles) - set(lfiles)
if len(nfiles) == 0:
    print("No new files found")
    exit(0)

if not os.path.exists(ofolder):
    os.mkdir(ofolder)

for x in nfiles:
    i = f"{cfolder}/{x}"
    o = f"{ofolder}/{x}"
    
    print(f"cp {i} --> {o}")
    shutil.copy2(i, o)
    
print("Finished")
exit(0)
