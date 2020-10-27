# Fmporting module type os
import os 

# Function with two arguments
def process_dir(p, indent):
    # Looping through the given file path  
    for item in os.listdir(path): 
        # Condition for checking the file
        if os.path.isfile("{0}/{1}".format(path, item)): 
            # printing out the indented format of the indent from file call item
            print("\t"*indent, item)  
        # Condition for checking the file path
        elif os.path.isdir("{0}/{1}".format(path, item)):
            # Using ANSI color code to color the output
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            # Processing the directory incrementally, causing the program to run continously,
            # Hence the code is commented
            #process_dir("{0}/{1}".format(path, item), indent+1)
        # Else condition for wrong file directory
        else:
            print("Not a file or directory")
# Prompting user for input file path
path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)