import os

os.sep # the separator between directory names, '//' for Windows

os.path.join('folder1', 'folder2', 'folder3', 'file.png')

os.getcwd()
os.chdir('c:\\')  # change directory

os.path.abspath('nameOfFileInDirectory') # essentially prepends filename with getcwd()

# . this directory
# .. the parent folder

os.path.isabs('path to test if it begins with the root folder')

os.path.relpath('absoulte path name', 'directory you want to be the parent in the relative path')

os.path.dirname('path name to pull out directory name')
os.path.basename('path name to pull out folder or file name')

os.path.exists()
# tests if a pathname actually exists

os.path.isfile()
# tests to see if it's a file

os.path.isdir()
# tests to see if it is a directory

os.path.getsize()
# returns the number of bytes

os.listdir()
# returns a list of files in that directory


totalSize = 0
for filename in os.listdir(os.getcwd()):
	if not os.path.isfile(os.path.join(os.getcwd(), filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))

print(totalSize)

os.makedirs('C:\\newdir\\newdir2\\yeah')

