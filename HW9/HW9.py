import os #import os module

def process_dir(p, indent): #function that processes input path and output content folders and files
    try:
        for item in os.listdir(p): #loop through the items in the directory
            if os.path.isfile("{0}/{1}".format(p, item)): #condition to check if current item is an existing file
                print("\t"*indent, item) #print item if it is a file and uses number tabs depending on indent number
            elif os.path.isdir("{0}/{1}".format(p, item)): #condition to check if item is an existing path/directory
                print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item)) #print name of folder in redcolor
                #calls the function, process_dir, to process current folder content and increase indent by one
                process_dir("{0}/{1}".format(p, item), indent+1) 
            else:
                print("Not a file or directory") #print when input is not file or directory
    except Exception: #catch errors of invalid/inaccessible path or directory
        print('Error! File/Directory cannot be found') #print this error message to user

path=input("Enter a valid system path: ") #accepting path input from user and assigning to a variable
print("\x1b[1;31m{}\x1b[0;0m".format(path)) #print path/directory inputed in red color
process_dir(path, 1) #calls function to process the input path
