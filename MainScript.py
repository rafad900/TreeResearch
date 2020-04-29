import sys, os, subprocess
from PLY2TXT import WoodLeafSeparator

# Read the names of the functions, it will help understand what they do
def find_in_path():
    print "\nChecking for matlab executable in PATH\n"
    raw_input("Press Enter:")
    found_in_path = False
    PATH = os.environ["PATH"]
    PATH_DIRECTORIES = PATH.split(':')
    for d in PATH_DIRECTORIES:
        if d.find("MATLAB") != -1 or d.find("matlab") != -1:
            print d
            found_in_path = True
    if found_in_path:
        print "Done searching PATH. The matlab executable was found in the PATH\n"
    else:
        print "Done searching PATH. The matlab executable was not found it the PATH\n"
    return found_in_path

def find_in_dir():
    print "\nChecking for matlab in /usr/bin/ directory\n"
    raw_input("Press Enter:")
    EXECUTABLES = os.listdir("/usr/bin/")
    found_in_usrbin = False
    for e in EXECUTABLES:
        if e == "matlab":
            print e
            found_in_usrbin = True
    if found_in_usrbin:
        print "Done searching /usr/bin/. The matlab executable was found in the /usr/bin directory"
    else:
        print "Done searching /usr/bin/. The matlab executable was not found in the /usr/bin/directory"
    return found_in_usrbin

def find_in_apps():
    print "\nChecking for matlab executable in Applications folder for both all users and only this user.\n"
    raw_input("Press Enter:")
    path_to_executable = ""
    found_in_globalapps = False
    found_in_userapps = False
    APPS = os.listdir("/Applications/")
    for a in APPS:
        if a.find("MATLAB") != -1:
            found_in_globalapps = True
            path_to_executable = "/Applications/" + a + "/bin/matlab"
            print a
    if not found_in_globalapps:
        print "Matlab executable not found in the all users application folder. Searching in this user only applications folder.\n"
        USER_APPS = os.listdir("/Users/rafaeldiaz/Applications")
        for a in USER_APPS:
            if a.find("MATLAB") != -1:
                found_in_userapps = True
                path_to_executable = "/Users/rafaeldiaz/Applications" + a + "/bin/matlab"
                print a
    else: 
        print "Matlab executable found in all users Application folder\n"
    return path_to_executable
            
        
    print path_to_executable

if __name__=='__main__':
    path = ""
    found = find_in_dir()
    if not found:
        found = find_in_path()
    if not found:
        path = find_in_apps()
    
    separator = WoodLeafSeparator()
    path_to_ply = separator.return_ply_path()
    path_to_txt = separator.return_new_directory()

    try:
        os.mkdir(path_to_ply + "/models")
        os.mkdir(path_to_ply + "/models/intermediate")
    except(OSError) as e:
        print "\n\n{} \nThere was a problem creating the subfolder for the .mat files\n\n".format(type(e))
    else:
        print("\n\nSuccesfully created new directory for the .mat files\n\n")

    if found:
        print "Beginning the matlab process. Part 1 of 2. This can take a while. \n"
        os.chdir(path_to_ply + "/models/intermediate")
        subprocess.call(['matlab', '-nodisplay', '-r', 'runqsm(\'../../' + path_to_txt + '/*.txt\', \'simple\', 10)'])
        print "\nFinished Part 1. Starting Part 2. This will hopefully be much faster. \n"
        os.chdir("..")
        subprocess.call(['matlab' ,'-nodisplay', '-r', 'runopt(\'./intermediate/*/*.mat\', \'simple\')'])
    else: 
        print "Beginning the matlab process. Part 1 of 2. This can take a while. \n"
        os.chdir(path_to_ply + "/models/intermediate")
        subprocess.call([path, '-nodisplay', '-r', 'runqsm(\'../../' + path_to_txt + '/*.txt\', \'simple\', 10)'])
        print "\nFinished Part 1. Starting Part 2. This will hopefully be much faster. \n"
        os.chdir("..")
        subprocess.call([path ,'-nodisplay', '-r', 'runopt(\'./intermediate/*/*.mat\', \'simple\')'])

    print("It has created the models in the /" + path_to_ply + "/models folder")
