#Tree Research

The PLY2TXT.py contains a class that can convert ply files to txt. You just have to give it the folder where 
all the ply files are in. Preferrably only ply files should be within the folder. 
The class will create a new folder within the one given by the user where all the txt files are going to be saved.

The Wood_leave_separator contains a class that will read the txt files created by PLY2TXT and seperate the wood from the leaves. It will then try to save the wood points to another txt file in a directory it will create. All it requires is the path to the folder where all the txt files from PLY2TXT are located. 


