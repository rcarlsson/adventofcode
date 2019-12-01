import sys
import os
from shutil import copyfile

day = sys.argv[1]

if (os.path.isdir(day)):
    print("Folder already exists, do nothing.")
    sys.exit(0)

os.mkdir(day)
copyfile("template.py", day+"/"+day+".py")
