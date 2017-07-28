"""
Create a script that merges the three text files into a new text file containing the text of all three files. The filename of the merged text file should contain the current timestamp down to the millisecond level. E.g. "2016-06-01-13-57-39-170965.txt".
1. Consider using the glob2 third-party library to generate a list of filenames to iterate through.

2. Use a "with" statement to create a new text file and then iterate through the file list inside that "with" statement and open and read existing file contents in each iteration and write them to new text file.

"""

import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")



"""
 some alternative methods:
 
file = open("file1.txt", 'r')
content = file.readlines()
file.close()
content1 = [i.rstrip("\n") for i in content]

"""
