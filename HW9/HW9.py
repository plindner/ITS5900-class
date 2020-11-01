#the OS module is imported so as to use some functions to be able to work on file paths
import os


#a function named process_dir is created and has 2 arguments, p and indent
def process_dir(p, indent):
    #the function loops through a path named p that the user will provide
    for item in os.listdir(p):
        # if the item is a file, an output of the file name is printed
        if os.path.isfile("{0}/{1}".format(p, item)):
            print("\t" * indent, item)
           # else if the item is a directory, a recurssion is used which means the function calls itself
        elif os.path.isdir("{0}/{1}".format(p, item)):
            print("\t" * indent, "\x1b[1;31m{}{}\x1b[0;0m".format(p,item))
            process_dir("{0}{1}".format(p, item), indent+1)
        #output no directory when there is no item in the directory
        else:
            print("Not a file or directory")


#the user provides an input of the file path
path=input("Enter a valid system path: ")
#an output of the file path is printed with ANSI colour red
print("\x1b[1;31m{}\x1b[0;0m".format(path))
#the function is called to process the input the user gives
process_dir(path, 1)