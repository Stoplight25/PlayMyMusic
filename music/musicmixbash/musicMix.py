#!/usr/bin/env python
import random, os, subprocess, sys, inspect
platform = sys.platform
myDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) #path normalization, get local paths as variables
os.chdir(myDir)
os.chdir('..')
musicDir = os.getcwd()
musSong = os.path.join(musicDir, 'addSong')
os.chdir(musSong)
addSongDir = os.getcwd()
os.chdir('..')
os.chdir(myDir)
musicmixbashlen = int(len(os.listdir(myDir)))
x  = int(random.randint(1,(musicmixbashlen - 1)))
file = str(x) + '.bat'
subprocess.call(os.path.join(myDir, file))
