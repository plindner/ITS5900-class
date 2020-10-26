#Importing a module
import os

#Defining a function with the file path, and an indent 
def process_dir(p, indent):
    #For loop in a file path you are directing
    for item in os.listdir(path):
#If statement to identify the file
        if os.path.isfile("{0}/{1}".format(path, item)):
            print("\t"*indent, item)
#Elif statement to identify the directory 
        elif os.path.isdir("{0}/{1}".format(path, item)):
#Color code the output
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
#Infinite loop for indenting files; commented out because it is not needed
#            process_dir("{0}/{1}".format(path, item), indent+1)
#Else statement for an invalid path 
        else:
            print("Not a file or directory")
#input for a system path
path=input("Enter a valid system path: ")
#print the files, with color showing the directories
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)
