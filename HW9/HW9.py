"""Rupprecht_HMWK9_v1.0."""
# Import OS Module
import os


# Define a function called process directory with values 'p' and 'indent'.
# 'p' is for the path while 'indent' is for the base number of indentations.
def process_dir(p, indent):
    """
    Search through directories. Establish files vs. other directories.
    Print them out in a tree format using indents.
    """
    # for the list of items in the directory gven by the user
    for item in os.listdir(p):
        # if the item in the list is a file,
        # '0' being the path, '1' being the file:
        if os.path.isfile("{0}/{1}".format(p, item)):
            # print the item with the default indent level
            print("\t"*indent, item)
        # if the item in the list is a directory,
        # '0' being the path, '1' being the directory:
        elif os.path.isdir("{0}/{1}".format(p, item)):
            # print the item in red with the default indent level
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            # since there are more directories, repeat the process with
            # the other directories and increase the indent size by 1, giving a
            # tree like output of the system path.
            process_dir("{0}/{1}".format(p, item), indent+1)
        # if the item is not a file or a directory:
        else:
            # inform the user that it is not a file or directory
            print("Not a file or directory")


# ask the user for system path and save their awnser to the variable 'path'
path = input("Enter a valid system path: ")
# print the path given in red
print("\x1b[1;31m{}\x1b[0;0m".format(path))
# input the path in the function process directory with a base indentation of 1
process_dir(path, 1)
