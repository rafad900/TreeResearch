import os
import open3d as o3d
import numpy as np

class WoodLeafSeparator:
    def __init__(self):
        self.path_to_ply = 0
        self.new_directory = 0
        self.run()
    
    def run(self):
        self.get_paths()
        self.create_directory()
        self.convert_ply()

    def return_ply_path(self):
        return self.path_to_ply

    def return_new_directory(self):
        return self.new_directory

    def create_directory(self):
        try:
            os.mkdir(self.path_to_ply + '/' + self.new_directory)
        except(OSError) as e:
            print "\n\n{} \nDid you give a valid subfolder for the txt files?\n\n".format(type(e))
            self.get_paths()
        else:
            print("\n\nSuccesfully created new directory\n\n")

    def convert_ply(self):
        for file in os.listdir(self.path_to_ply):
            if (file == '.DS_Store' or file == self.new_directory):    # ADD ANY OTHER HIDDEN FOLDERS OR ANYTHING THAT ISNT A PLY FILE
                continue
            print("Processing: " + file)
            pcd_load = o3d.io.read_point_cloud(self.path_to_ply + '/' + file)
            xyz_load = np.asarray(pcd_load.points)
            txt_file_name = self.path_to_ply + '/' + self.new_directory + '/' + file[:-4] + '_xyz_points.txt'
            np.savetxt(txt_file_name, xyz_load, fmt="%f")
        
    def get_paths(self):
        self.path_to_ply = 0
        self.new_directory = 0
        self.path_to_ply = raw_input("Path to the ply files: ")
        self.new_directory = raw_input("Folders to place txt files (default is in 'txt_tree_files'): ") or "txt_tree_files"

if __name__=='__main__':
    sep = WoodLeafSeparator()