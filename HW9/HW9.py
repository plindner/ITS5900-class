# importing os module
import os


# defining a function with two arguments
def process_dir(p, indent):
    try:
    #loop through a file path
        for item in os.listdir(path):
            # identifying a file
            if os.path.isfile("{0}/{1}".format(path, item)):
                print("\t"*indent, item)
            # identifying a directory as alternate loop
            elif os.path.isdir("{0}/{1}".format(path, item)):
                # indent and apply color to output
                print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
                # this code is redundant so i commented it out
                '''process_dir("{0}/{1}".format(path, item), indent+1)'''
                # else statement when a path is not a directory
            else:
                print("Not a file or directory")
    except:
        print("your input does not exist")

path=input("Enter a valid system path: ")
#print files in color
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)
