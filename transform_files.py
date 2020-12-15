"""
File: transform_files.py 
-------------------
This program is used to transform the data points from mp3 to wav format.  
"""

import os
from glob import glob
from pydub import AudioSegment

DATA_DIRECTORY = 'raw_data'


master_dict = {}
for subdir in os.listdir(DATA_DIRECTORY):
    path = DATA_DIRECTORY + "/" + subdir
    d = glob(path + '/*.mp3')
    master_dict[subdir] = d


for key in master_dict:
    print(key)


for key in master_dict:
	if key == 'neg' or key == 'pos':
		class_name = key
		class_list = master_dict[key]
		count = 0
		for file in class_list:
			count += 1
			sound = AudioSegment.from_mp3(file)
			name_path = "mod_data/" + str(class_name) + "/" + str(count) + ".wav"
			sound.export(name_path, format="wav")  



