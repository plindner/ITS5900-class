import os
 
def custom_listdir(path):
    """
    Returns the content of a directory by showing directories first and then
    files in alphabetical order
    """
 
    dirs = sorted([d for d in os.listdir(path) if os.path.isdir(path + os.path.sep + d)])
    dirs.extend(sorted([f for f in os.listdir(path) if os.path.isfile(path + os.path.sep + f)]))
 
    return dirs
 
def process_dir(path, indent, f):
    """
    Returns a list of directories and files for the provided path
    """
 
    # loop over items in directory
    for item in custom_listdir(path):
        itempath = os.path.join(path, item)
        itempathbase = os.path.basename(itempath)
 
        # skip hidden directories
        if itempathbase[0] == '.' or itempath == '..':
            continue
 
        # append directory to list
        if os.path.isdir(itempath):
            f += "\t"*indent + "\x1b[1;31m{}\x1b[0;0m".format(itempathbase) + "\n"
 
            # get next indent data
            f = process_dir(itempath, indent+1, f)
 
        # append file to list
        if os.path.isfile(itempath):
            f += "\t"*indent + item + "\n"
 
    return f
 
# accept user input
path=input("Enter a valid system path: ")

# print colored input path
print("\x1b[1;31m{}\x1b[0;0m".format(path))

# invoke process_dir function
data = process_dir(path, indent=1, f="")

print(data)