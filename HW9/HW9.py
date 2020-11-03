import os   #import os module
def process_dir(newpath, indent):   #define recursive function
    try:    #test the block for errors
        for newitem in os.listdir(newpath):     #loop through the path enteries
            if os.path.isfile("{0}/{1}".format(newpath, newitem)):  #base case
                print("\t"*indent, newitem)
            elif os.path.isdir("{0}/{1}".format(newpath, newitem)) and indent:  #recursive case
                print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(newitem))
                newpath1 = '{}/{}'.format(newpath,newitem)  #assign new path to new vaiable in the execution context to prevent stack overflow error
                process_dir(newpath1, indent + 1)   #call the function
            else:
                print("Not a file or directory")
    except: #handle errors
        print("What you entered is not valid directory")
path=input("Enter a valid system path: ")
print("\x1b[1;31m{}\x1b[0;0m".format(path))
process_dir(path, 1)