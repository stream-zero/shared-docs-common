import os
import shutil

dir_path = '/Users/balajibal/Documents/workspace/streamzero-site/static/images/connectors'
file_list = os.listdir(dir_path)

for file_name in file_list:
    #print(file_name)
    if '.svg' in file_name:
       print(f'<div class="slide"><button class="image-button"><img src="/images/connectors/{file_name}" alt="Image"><span>{file_name.split(".")[0]}</span></button></div>')