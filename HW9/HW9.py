
#import the operating system module
import os

#function definition to process a directory and list its content 
def process_dir(p, indent):
    for item in os.listdir(path):
        #Run if "item" is a file and print it out with some indentation 
        if os.path.isfile("{0}/{1}".format(path, item)):
            print("\t"*indent, item)
        #Run if "item" is a directory and print it out with some indentation
        elif os.path.isdir("{0}/{1}".format(path, item)):
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            #process_dir("{0}/{1}".format(path, item), indent+1) commented out recursion error
        else:
            print("Not a file or directory")

path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)
