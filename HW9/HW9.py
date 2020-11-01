
import os

# process_dir funciton definition
# process list files/directory of a given path, p
# with depth of the directory structure, indent 
def process_dir(p, indent):

    # loop through list of items (files/directory) for given path
    for item in os.listdir(path):
        
        # check if item is a file given the path and item name
        if os.path.isfile("{0}/{1}".format(path, item)):

            # print file with tabs of the indentation
            print("\t"*indent, item)

        # check if item is a folder given the path and item name when file test fails
        elif os.path.isdir("{0}/{1}".format(path, item)):

            # print directory name with tabs of the indentation and color (orange/red)
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))

            # repeat the process for current item  
            process_dir("{0}/{1}".format(path, item), indent+1)
        else:
            # print message when both test fails
            print("Not a file or directory")

# accept user input
path=input("Enter a valid system path: ")

# print colored input path
print("\x1b[1;31m{}\x1b[0;0m".format(path))

# invoke process_dir function
process_dir(path, 1)