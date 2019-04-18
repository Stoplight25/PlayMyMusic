#!/usr/bin/env python
#the infastructure to play new songs
import shutil, os, subprocess, inspect
myDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) #pth normalization, get local paths as variables
os.chdir(myDir)
os.chdir('..')
musicDir = os.getcwd()
os.chdir(os.path.join(musicDir, 'musicmixbash'))
musicMixDir = os.getcwd()
os.chdir('..')
os.chdir(os.path.join(musicDir, 'addSong'))
musicmixbashlen = int(len(os.listdir(musicMixDir)))
newSongslen = int(len(os.listdir(myDir))) - 2 #subtract 1 to ignore this python file and bash file
for filename in os.listdir(myDir):
    if filename != 'addSongs.py':
        if filename != 'addSongs.bat':
           newbashnum = str(len(os.listdir(musicMixDir)))
           bashName = newbashnum + '.bat'
           newbash = open(bashName,'w')
           musFile = os.path.join(musicDir, filename)
           newbash.write('mplayer '+ musFile +'\nexit 0')
           command = 'chmod u+x '+ os.path.join(myDir, bashName)
           process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
           output, error = process.communicate()
           shutil.move( os.path.join(myDir, filename), musicDir)
           shutil.move( os.path.join(myDir, bashName), musicMixDir)
           newbash.close()
