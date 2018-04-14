import os
import sys
import re

#rootdir = sys.argv[1]
rootdir = 'C:\\Users\\i\\Google Drive\\Honours\\COS720\\Assignment\\maildir\\'
file = open('C:\\Users\\i\\Desktop\\Enron emails.txt','w')
for folder, subs, files in os.walk(rootdir):
    #with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:
        for filename in files:
            #with open(os.path.join(folder, filename), 'r') as src:
            curFile =  open(os.path.join(folder, filename), 'r')
            #dest.write(src.read())
            for line in curFile:
                file.write(line)
                if re.match("(.*)(X|x)-FileName:(.*)", line):
                    file.write("\n")
                    file.write("\n")
                    break