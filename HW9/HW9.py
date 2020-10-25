import os

def process_dir(p, indent):
    for item in os.listdir(path):
        if os.path.isfile("{0}/{1}".format(path, item)):
            print("\t"*indent, item)
        elif os.path.isdir("{0}/{1}".format(path, item)):
            print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
            process_dir("{0}/{1}".format(path, item), indent+1)
        else:
            print("Not a file or directory")

path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)