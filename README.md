A Python script to segment a WAV file according to a timestamps list. The script scrapes the specified folder for wav files to operate on. The script works as follows - 

1. Specify the directory to scrape the wave files from.
2. Specify the timestamps to segment with as a list - 't'
3. Segmented files are stored into a subdirectory of the specified folder named 'auto_trimmed'

There are two inputs needed - 
1. dir = directory to scrape the wav files from
2. t = timestamps to split the wav files with
