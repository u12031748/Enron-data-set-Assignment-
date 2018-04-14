import os
from shutil import copyfile

# The top argument for name in files
topdir = 'C:\\Users\\i\\Google Drive\\Honours\\COS720\\Assignment\\maildir\\'
dest = 'C:\\Users\\i\\Desktop\\Enron emails'

extens = ['txt', 'pdf', 'doc']  # the extensions to search for

found = {x: [] for x in extens}  # lists of found files



logname = "findfiletypes.log"
print('Beginning search for files in %s' % os.path.realpath(topdir))

# Walk the tree
for dirpath, dirnames, files in os.walk(topdir):


    # Loop through the file names for the current step
    for name in files:
        # Split the name by '.' & get the last element
       pathX = os.path.realpath(name)
       print(pathX)
