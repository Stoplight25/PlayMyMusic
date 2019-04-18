#!/usr/bin/env python
#create the bash file that runs the program
import shutil, os, subprocess, inspect
myDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(os.path.join(myDir, 'musicmixbash'))
musicMixDir = os.getcwd()
os.chdir('..')
finPath = os.path.join(musicMixDir, 'musicMix.py')
startBash = open('playMusic.bat','w')
startBash.write('#!/bin/bash\npython3 '+ finPath +'\nexit 0')
command = 'chmod u+x '+ os.path.join(myDir, 'playMusic.bat')
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
startBash.close()
