
"""
This program downloads the 1st 100 stories of The Brother's Grimm and saves it in your working folder.
"""

import os
import requests


def download(url: str, dest_folder: str):

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # creates "stories" directory if it does not exist


    for i in range(1, 101): #repeats download 100 times
        num = f"{i:03}" #converts iteration into triple digits to match website
        filename = url + str(num) + ".txt" # 
        save_location = dest_folder + str(num) + ".txt"
        r = requests.get(filename, stream=True) #makes download request with converted url w/ filename
        if r.ok:
            print("saving to", os.path.abspath(save_location))
            with open(save_location, 'wb') as f: #saving file to hdd.
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))


download("https://www.cs.cmu.edu/~spok/grimmtmp/", dest_folder="stories/")