
import os

 #takes the path (changed from p) and the indentation level
def process_dir(path, indent):
    
    #checks out every item in path
    for item in os.listdir(path): 
        
        #prints if the path is just a file
        if os.path.isfile("{0}/{1}".format(path, item)):
            print("\t"*indent, item)
        
        #re runs the process_dir() function if the path is a directory
        elif os.path.isdir("{0}/{1}".format(path, item)):
            #prints the directory name
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            #checks inside the directory
            process_dir("{0}/{1}".format(path, item), indent+1)
        
        #
        else:
            print("Not a file or directory")

#asks user for path
path=input("Enter a valid system path: ")
#prints the path
print("\x1b[1;31m{}\x1b[0;0m".format(path))

#error checking try/except
try:
    process_dir(path, 1)
except:
    print("Please try again")