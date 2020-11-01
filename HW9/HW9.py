
##3a.
 ## This  program is trying to print files in a given path going through all the 
 ##subdirectories of that location.
 
 ## 3b. The error is that the inside the def function, the program is using "path" declared outside
 ## has a value of original path which causes the recursive error beause the same path has been called over and over again. 
 
 ## To correct that the local path "p"' of the directory is rather used 

### 4. To prevent the program from crashing, I used the try and except

import os ## using os module on a system file 

def process_dir(p, indent):## defining a function process_dir
        try:
         #for item in os.listdir(path): ## using for loop to go through the path
            for item in os.listdir(p): 
                if os.path.isfile("{0}/{1}".format(p, item)): ## in a subdirectory or path, listing all regular files- the path comes on top followed by the items 
        
                    print("\t"*indent, item)
                elif os.path.isdir("{0}/{1}".format(p, item)): ### To check if a particular directory exists 
                    print("\t"*indent, "\x1b[1;31m{}\x1b[0;0m".format(item))
                    process_dir("{0}/{1}".format(p, item), indent+1) ###  Retriving the function def
                else:
                    print("Not a file or directory")### prints "Not a file or directory" if there is no file or directory on the path selected 
        except Exception as Error:
            print("The program exits with the following message:\n"+str(Error))

path=input("Enter a valid system path: ") ## taking input from the user 
print("\x1b[1;31m{}\x1b[0;0m".format(path)) ## Prints the path in color 
process_dir(path, 1) ## Retrieving or printing the files or directories going or looping through the def function 
