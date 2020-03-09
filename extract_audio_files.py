#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:34:16 2020

@author: Krishna
"""

import os
import glob

mp4_root = '/mnt/archive/Twitch_clips/downloads/'
save_root = '/mnt/archive/Twitch_clips/audio_files/'

all_folders = sorted(glob.glob(mp4_root+'/*/'))
for folderpath in all_folders:
    create_store = save_root+'/'+folderpath.split('/')[-2]
    if not os.path.exists(create_store):
        os.makedirs(create_store)
    all_files = sorted(glob.glob(folderpath+'/*.mp4'))
    
    for filepath in all_files:
        save_path = create_store+'/'+filepath.split('/')[-1][:-4]+'.wav'
        extract_audio='ffmpeg -i '+filepath +' -f wav '+save_path
        try:
            os.system(extract_audio)
        except:
            print('Could not process {}'.format(filepath))
