import shutil,os
import pathlib
from shutil import copytree, ignore_patterns
print(dir(shutil))
user_input=input("please enter the name folder name:")
shutil.copytree(r"\\fr02391vma\share\pythagorus", "sarika")

path, dirs, files = next(os.walk("sarika"))
file_count = len(files)
path_count = len(path)
dirs_count=len(dirs)

print("file_count",file_count)
print("path_count",path_count)
print ("dirs_counts",dirs_count)
for i in dirs:
    a,b,c =(next(os.walk("sarika\\"+i)))
    print (len(a))





