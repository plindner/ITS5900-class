
import os

# creating a function that reads the contents of a given filepath
# with different behavior if it is a file or directory
# it indents and prints the content of the file/directory
# it will continue expanding the contents of a directory if it finds
# another

# the {0}/{1}s exist as placeholders to be replaced by the format's
# arguments

# "\x1b[1;31m{}\x1b[0;0m" is just formatting used to define color in the output.
# Directories and file paths show up in red, files in white.


def process_dir(p, indent):
    try:
        for item in os.listdir(p): 
            if os.path.isfile("{0}\{1}".format(p, item)):
                print("\t"*indent, item)
            elif os.path.isdir("{0}\{1}".format(p, item)):
                print("\t"*(indent+1), "\x1b[1;31m{}\x1b[0;0m".format(item))
                process_dir("{0}\{1}".format(p, item), indent+1)
            else:
                print("Not a file or directory")
                return
    except:
        print("Invalid input.")
path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)
