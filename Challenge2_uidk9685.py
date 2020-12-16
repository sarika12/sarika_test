import shutil, os
import pathlib
import collections
from shutil import copytree, ignore_patterns

# Creating dir in same location
# user_input=input("please enter the name folder name:")
shutil.copytree(r"\\fr02391vma\share\pythagorus", "sarika")
# count all the dirs and file name and type
dirs_count = 0
file_count = 0
count_png = 0
count_jpg = 0
count_txt = 0
count_pdf = 0
count_svg = 0
count_db = 0
for root, dirs, files in os.walk("sarika", topdown=True):
    # print ("++++",root,dirs,files)
    dirs_count = dirs_count + int(len(dirs))
    file_count = file_count + int(len(files))

    for files in files:

        if files.endswith(".PNG"):
            count_png += 1
        if files.endswith(".txt"):
            count_txt += 1
        if files.endswith(".jpg"):
            count_jpg += 1
        if files.endswith(".pdf"):
            count_pdf += 1
        if files.endswith(".svg"):
            count_svg += 1
        if files.endswith(".db"):
            count_db += 1
        if files == "readme.txt":
            pass
print("dirs_count", dirs_count)
print("file_count", file_count)

print("count_txt", count_txt)
print("count_png", count_png)
print("count_pdf", count_pdf)
print("count_svg", count_svg)
print("count_jpg", count_jpg)
print("count_db", count_db)
# Counting the "will "
file_pt = os.getcwd()

with open(file_pt + "\\sarika\\readme.txt", "r+", encoding="utf-8") as file:
    file_open = file.read()
    print("Count of will", file_open.count("will"))
