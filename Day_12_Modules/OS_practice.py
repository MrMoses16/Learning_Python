import os
from datetime import datetime

# print the current directory
print(os.getcwd(), end='\n\n')

# change directory to 30_Day_Python and list file name(s)
os.chdir(r"C:\Users\02kmt\Downloads\30_Day_Python")
print(os.listdir(), end='\n\n')

# create new directory using: os.mkdir() and os.makedirs()
# then delete directory using: os.rmdir() and os.makedirs()
# The difference is os.makedirs() will make the intermediate directories for a multi-level directories
# same principle for os.removedirs() for deleting multi-level directories
    # Below creates error messages when creating a sub_directory within OS_Practice
    # os.mkdir('OS_Practice/Sub_Dir_1')
    # first must create main directory before creating sub-levels
os.mkdir('OS_Practice')
os.mkdir('OS_Practice/Sub_Dir_1')
os.rmdir('OS_Practice/Sub_Dir_1')
os.rmdir('OS_Practice')
    # makedirs() and removedirs() can make one call for main directory and sub-levels
os.makedirs('OS_Practice/Sub_Dir_1/Sub_Dir_2')
os.removedirs('OS_Practice/Sub_Dir_1/Sub_Dir_2')

# create a directory and change its name
os.mkdir('OS_Practice')
    # os.rename(current name, new name)
os.rename('OS_Practice', 'OS_Master')
os.rmdir('OS_Master')

# print the stats with a directory
    # os.stat give the following info: (st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime)
    # can use the dot operator to get specific info
print(os.stat('Day_12_Modules'))
print(os.stat('Day_12_Modules').st_size)

# print the date of a directory last edit
print(datetime.fromtimestamp(os.stat('Day_1_Intro').st_mtime), end='\n\n')

# print all pathes, directories, and files within current directory
# use os.walk(directory name)
for dirpath, dirnames, filenames in os.walk(r"C:\Users\02kmt\Downloads\30_Day_Python"):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames, end='\n\n')

# To change current directory use os.chdir(new directory)
os.chdir(r'C:\Users\02kmt\Downloads')

# get environment variables, there are many envirment variables so only look at HOME
print(os.environ.get('HOMEPATH'))

# to join two pathes use os.path.join(Base, Extension)
new_file = 'test.txt'
file_path = os.path.join(os.environ.get('HOMEPATH'), new_file)
print(file_path)

# os.path has other features: os.path.basename, os.path.dirname, os.path.split, os.path.exists, os.path.isdir, os.path.isfile, os.path.splitext
# for all feactures print(dir(os.path))
new_file = '/tmp/test.txt'
print(os.path.basename(new_file)) # output: test.txt

print(os.path.dirname(new_file)) # output: /tmp

print(os.path.split(new_file)) # output: ('/tmp', 'test.txt')

print(os.path.exists(new_file)) # output: False

print(os.path.isdir(new_file)) # output: False

print(os.path.isfile(new_file)) # output: False

print(os.path.splitext(new_file)) # output: ('/tmp/test', '.txt')