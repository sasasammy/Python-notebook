#
# Src: FileCount.py
#

import os

import time
start = time.time()


# Path IN which we have to count files and directories
LOCPATH = '/tmp/'   # Give your path here

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(LOCPATH):
    print('Checking in location:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

end = time.time()
print('Total time spent:', end - start)

print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total:',(dirCount + fileCount))
