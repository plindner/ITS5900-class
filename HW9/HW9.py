
import os

 
def process_dir(path, indent):
    try :
        for item in os.listdir(path): #loop through the items in the directory
        
            if os.path.isfile("{0}/{1}".format(path, item)): #check if item is a file
                print("\t"*indent, item) #print the item in the directory 
            if os.path.isdir("{0}/{1}".format(path, item)):#check if item is a subfolder
                print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item)) #print the subfolder
                process_dir("{0}/{1}".format(path, item), indent+1) #call the method to process the path of the directory   
    except Exception:
             print("Not a file or directory") #print it's not a file or directory

path=input("Enter a valid system path: ") #allowing user to print path
print("\x1b[1;31m{}\x1b[0;0m".format(path)) #print path in red 
process_dir(path, 1) #call the method process directory
