import os
files = os.listdir('.')
natsort(files)
index = 0
for filename in files:
    os.rename(filename, str(index).zfill(7)+'.png')
    index += 1
