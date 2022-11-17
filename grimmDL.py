import os

#create a directory if needed

dir_name = "stories"
url = "https://www.cs.cmu.edu/~spok/grimmtmp/"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    def maybe_download(filename):
        """Download a file if not present"""
        print("Downloading file: ", dir_name+ os.sep+filename)
if not os.path.exists(dir_name+os.sep+filename):
    filename, _ = urlretrieve(url + filename, dir_name+os.sep+filename)
else:
    print("File ", filename, "already exists.")


num_files = 100

filenames = [format(i, '03d')+'.txt' for i in range(1,101)]

for fn in filenames:

maybe_download(fn)