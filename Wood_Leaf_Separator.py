import os, sys
import numpy as np
import open3d as o3d


''' DONT USE THIS FILE FOR FILTRATION YET, IT HAS PROBLEMS '''

try: 
    from tlseparation.scripts.automated_separation import generic_tree
except ( ImportError) as e:
    print("\n\n{} Are you using python2... ? \nDid you pip install tlseparation ? \nYou can check what you have installed with \"pip list -v\" \n".format(type(e)))
    exit(1)
else:
    print("\n\nThe packages were imported succesfully")

class Wood_Leaf_Separator:
    def __init__(self):
        self.new_directory = 'wood_only_txt/'
        self.path_to_TXT = 0
        self.run()
    
    def get_paths(self):
        self.path_to_TXT = 0
        self.path_to_TXT = raw_input("Path to the txt files (--help for options): ")
        while (self.path_to_TXT == '--help'):
            self.display_help()
            self.path_to_TXT = raw_input("Path to the txt files (--help for options): ")
    
    def display_help(self):
        print("The path to the txt should be the folder created by PLY2TXT")
        print("If the files were not created by PLY2TXT, then the folder given")
        print("should contain .txt files that only contain the 'x y z' float numbers.\n\n")

    def read_values(self, file):
        data = []
        for row in file:
            values = row.split(' ')
            data.append([float(values[0]), float(values[1]), float(values[2])])
        points = np.array(data)
        return points

    def open_files(self):
        self.create_directory()
        print
        for file in os.listdir(self.path_to_TXT):       # Maybe add some kind of progress bar here so that the users know that its working, cuz generic_tree() on line 45 takes a long time to process the trees
            if (file == '.DS_Store' or file[-4:] != '.txt'): # if the file is the DS_STORE directory or the file does NOT end with .txt, continue
                print(file[-4])
                continue
            print("\nOpening: " + file)
            txt_file = open(self.path_to_TXT + '/' + file, 'r')
            data = self.read_values(txt_file)
            print("Processing: " + file)
            wood, leaves = generic_tree(data)
            self.write_save_file(wood, file)        # Only the wood is necessary, we removing leaves
        
    def write_save_file(self, wood, file):
        txt_file_name = self.new_directory + file[:-4] + '_xyz_points_wood.txt'
        print "Saved to: " + txt_file_name
        np.savetxt(txt_file_name, wood, fmt="%f")

    def create_directory(self):
        try:
            os.mkdir(self.new_directory)
        except(OSError) as e:
            self.get_paths()
        else:
            print("\n\nSuccesfully created new directory: {}\n\n".format(self.new_directory))

    def run(self):
        self.get_paths()
        self.open_files()


if __name__=='__main__':
    WLS = Wood_Leaf_Separator()