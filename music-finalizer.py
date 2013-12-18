import os
import sys
import mutagen
from mutagen.mp3 import MP3 
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3

# Change this path to the folder that is denotated by the artists name
# which should be applied to all the files under that directory 
directory = '/media/iamnotus/FreeAgent\ Drive/Music/Music-new-allocation/python-fixed/Jimi\ Hendrix/'

exts = ['.mp3']


class Song:

    def __init__(self,path,fullPath):
        self.path = path
        self.fullPath = fullPath


#iterate through each directory from root
for root, dirs, files in os.walk(directory):
    i=0
    dirCurrent = ''
    s = []

    #iterate through each file in the directory 
    for file in files:
        #iterate through each possible extenstion type
        for ext in exts:
            if file.endswith(ext):
                # set the directory name
                if i==0:
                    dirCurrent = os.path.join(root) 
                    i = 1
                song = Song(file,os.path.join(root,file))
                s.append(song)


    #print the folder and songs contained within 
    if dirCurrent != '':
        print '-'*15,dirCurrent,' has ',len(s),' songs','-'*15


    for index,song in enumerate(s):
        fullPath = getattr(song,'fullPath')
        path = getattr(song,'path')

        audio = mutagen.File(fullPath,easy=True)
        print '-'*15,path,'-'*15
        print fullPath

        last = fullPath.rindex('/')
        second = fullPath.rindex('/',0,last-1)
        name = fullPath[second+1:last]

        audio['artist'] = name

        print audio.pprint()


        audio.save()

