#Refer README.md to have a brief overlook of the way this script works...

#A script to trim the end of a WAV audo file upto a given duration
#The script operates on all the files in the specified folder
#It searches for all the files with the extension ".wav" and adds it to the list of files to operate on
#Finally the trimmed filenames are stored into a subdirectory(named "auto_trimmed") within the specified directory

import numpy as np
import platform
import os
import seaborn as sns
import soundfile as sf

#Preconfiguration variables
#Variables to configure the trimming operation

t = [0,15,30,60]  #timestamps onto which the file to be split

dir = r'' #location of your directory to be scraped

master_dir = ""  

filenames = []
for f in os.listdir(dir): #loop to store compatible file names
    name, ext = os.path.splitext(f)
    if ext == '.wav':
        filenames.append(f)

#creating a subdirectory to store the operated files
stor_dir = os.path.join(dir,'auto_trimmed')
try:
  os.makedirs(stor_dir,777)
except:
  print('Directory already exists')

#storage directory creation
stor_dir = os.path.join(dir,'auto_trimmed')
os.makedirs(stor_dir,777)

for filename in filenames:
  #To store new write directories for different filenames
  file_dir = os.path.join(dir,filename)
  data, sr = sf.read(file_dir)
  
  #Splitting the ndarray into segments according to timestamps
  for i in range(len(t[:-1])):
    data_new = []
    write_directory = []
    
    data_new = data[sr*t[i] : sr*t[i+1]]


    if platform.system() == 'Windows':
      a = '\\'
    else:
      a = '/'

    filename = file_dir.rsplit(a, 1)[1][:-4] + '_' + str(i) + '.wav'
    write_directory = os.path.join(stor_dir,filename)

    sf.write(write_directory, data_new, sr)
    print(write_directory + '  --> written')