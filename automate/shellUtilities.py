import shutil, os, send2trash

# shell utilities

# Copying
# shutil.copy(source, destination)
# shutil.copytree(source, destination) # copies a folder and all content

# Moving and renaming
# shutil.move(source, destination)
# shutil.move(source, sameDirectoryNewFilename)

# Permanently Deleting
# os.unlink(single file)
# os.rmdir(empty directory)

# shutil.rmtree(full directory you want to delete)

# A safer way
# send2trash.send2trash(path to file you want to send to trash)

# Walk
# Use os.walk in a for loop, with three results folderName, subfolders, filenames
for folderName, subfolders, filenames in os.walk(os.getcwd()):
	print('the folder is ' + folderName)
	print('the subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('the filenames in ' + folderName + ' are: ' + str(filenames))

	for subfolder in subfolders:
		if 'fish' in subfolder:
			os.rmdir(subfolder)

	for file in filenames:
		if file.endswith('.py'):
			shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))

