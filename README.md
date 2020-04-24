#Tree Research

Requirements:
  Python 2.7 with the following modules:
    tlseparate
    open3d
    numpy
    pandas
    
  Matlab 2019 or newer:
    The matlab executable must be in the PATH for some of the scripts to work


The PLY2TXT.py contains a class that can convert ply files to txt. You just have to give it the folder where 
all the ply files are in. Preferrably only ply files should be within the folder. 
The class will create a new folder within the one given by the user where all the txt files are going to be saved.

THE WOOD_LEAVE_SEPARATOR HAS ERROR, DON'T USE YET
The Wood_leave_separator contains a class that will read the txt files created by PLY2TXT and seperate the wood from the leaves. It will then try to save the wood points to another txt file in a directory it will create. All it requires is the path to the folder where all the txt files from PLY2TXT are located. 

Optqsm and TreeQSM have their own instructions but if you want to get it up running as fast as possible, here is the recap. 
Optqsm uses TreeQSM to automate the qsm construction from the pointclouds. Optqsm uses .txt files that contain ONLY the xyz coordinates. If you have PLY files and need to convert them to .txt, use the PLY2TXT.py to do so. It will output the xyz .txt files needed for Optqsm. After that, you need to run the commnand. 
               
               matlab --nodisplay -r "runqsm("path_to_files", "simple", 1)"
               cd ../
               matlab --nodisplay -r "runopt("path_to_intermediate/*/*/.mat", "simple")"
     
from the terminal. HOWEVER, you need to create two directories called models and intermediate. Look at the optqsm README file to learn more.

TreeQSM can be run from within matlab. This scripts can be used with the PLY files directly to build the QSM object. 

              inputs = create_input;
              data = pcread("file"); % read in all the data form ply file
              points = data.Location; % this will get the points 
              treeqsm(points, inputs);
       
This will also display bring a display with the cylinders around the branches and trunk while doing its best to get rid of leaves and other unecessary points. 
