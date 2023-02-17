#Refer README.md to have a brief overlook of the way this script works...

#A script to trim the end of a WAV audo file upto a given duration
#The script operates on all the files in the specified folder
#It searches for all the files with the extension ".wav" and adds it to the list of files to operate on
#Finally the trimmed filenames are stored into a subdirectory(named "auto_trimmed") within the specified directory

import scipy.io.wavfile as wavfile
import numpy as np
from matplotlib import pyplot as plt
import os
import seaborn as sns

#Preconfiguration variables
#Variables to configure the trimming operation

t = 10  #seconds upto which the wav file to be trimmedf

master_dir = ""  #location of your directory

filenames = []  #empty list to store wav file names
for f in os.listdir(master_dir): #loop to store compatible file names
    name, ext = os.path.splitext(f)
    if ext == '.wav':
        filenames.append(f)

#storage directory creation
stor_dir = os.path.join(dir,'auto_trimmed')
os.makedirs(stor_dir,777)

#Trimming function definition

for filename in filenames:
  #FILENAME STRING MANIPULATION
  file_dir = os.path.join(dir,filename) #full directory name
  sr, data=wavfile.read(file_dir) #read wavfile to gather data, sr = <Sampling Rate>; data = <numpy array of wavfile>
  filename = file_dir.rsplit('/', 1)[1] #extracting filename
  write_directory = os.path.join(stor_dir,filename) #compose write directory string

  #SAMPLE TRIMMING
  sample_no = sr*10 #Number of samples for a 10s sample extraction
  data_new = data[0:sample_no]  #Using numpy array slicing to trim the audio to 10s sample

  #WRITING TO DIRECTORY
  wavfile.write(write_directory,sr,data_new.astype(np.int16))

def tail_trim(data): #Tail trimming function
  sample_no = sr*10 #Number of samples for a 10s sample extraction
  data_new = data[0:sample_no]  #Using numpy array slicing to trim the audio to 10s sample
  return data_new