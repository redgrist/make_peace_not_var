#!/usr/bin/python3
import psutil
import os
import shutil
# java kill
PROCNAME = "java"
#move files
source1 = '/var/services/'
dest1 = '/home/gemini/services'
#start gemini
polnoc = '/etc/init.d/gemini-polnoc start'
warszawa = '/etc/init.d/gemini-warszawa start'

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()

if not os.path.exists('/home/gemini/services'):
    os.makedirs('/home/gemini/services')

files = os.listdir(source1)
for f in files:
    shutil.move(source1+f, dest1)

os.rename('/var/services', '/var/services_OLD')

os.symlink('/home/gemini/services', '/var/services')

os.system(polnoc)
os.system(warszawa)