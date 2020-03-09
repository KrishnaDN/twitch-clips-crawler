
import os
import glob

all_files=sorted(glob.glob('links/*.txt'))
for filepath in all_files:
    download = 'python batchloader.py '+filepath
    os.system(download)

