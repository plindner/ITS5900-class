

###### Name: Prajakta Badhan ######
# I have referred to the https://docs.python.org/2/tutorial/errors.html for try and except method.
# 3rd requirement: Bug detection and adding meaningful comments
# variable path is already declared outside on line 28
# the code is trying to print all the files from the directory and its subdirectory using the path given by the user. 
#  Identified Bug: in the def function below, the path is defined as p and to call it in the os.listdir & os.path.isfile it should be p instead of path in the complete loop from for loop till elif loop.
# variable p is the path in my code, I have replaced variable "path" with "p" wherever it was declared in the code to fix the bug.



import os # importing the module os

 
def process_dir(p, indent): # defining a function (process_dir) with two arguments p and indent.
    
    
    for item in os.listdir(p): # checks for item in the path given by user.
        
        if os.path.isfile("{0}/{1}".format(p, item)):# checks whether the specified path is an existing regular file or not, if it is then it checks the item from the given path.
            print("\t"*indent, item) # prints the item from the folder: HW9
            
        elif os.path.isdir("{0}/{1}".format(p, item)): # checks whether the specified path is an existing directory or not, if it is then it checks the item from that given directory.
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))  # it prints the item using ANSI color code in python
            process_dir("{0}/{1}".format(p, item), indent+1) # calling a function process_dir and {0}/{1} is the sequence in which we want the output to be displayed(path and item).
            
        else:
            print("Not a file or directory") # if in the path, the item is not a file or directory then it prints the output as Not a file or directory.




p=input("Enter a valid system path: ") # asks user for the input.
print("\x1b[1;31m{}\x1b[0;0m".format(p)) # prints the path in red color using ANSI color code in python.
process_dir(p, 1) # calling the function (process_dir) to check for the files from the given path by the user by going through the def function and for loop under it.

