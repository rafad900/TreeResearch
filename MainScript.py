import os, sys
import open3d as o3d
import numpy as np

stream1 = open("PLY2TXT.py")
py2txt_script = stream1.read()
exec(py2txt_script)

#stream2 = open("Wood_Leaf_Separator.py")
#wood2leaf_script = stream2.read()
#exec(wood2leaf_script)