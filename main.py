import os


def get_folder_size(folder):
    folder_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        #print("dirpath:", dirpath, "filenames:", filenames)
        for f in filenames:
            fullPath = os.path.join(dirpath, f)
            if not os.path.islink(fullPath):
                folder_size += os.path.getsize(fullPath)

    return folder_size


# get name of all folders in C:\, put them in a list

#specify root path
rootPath = 'C:\\'

#get all folder names in drive
allFolders = [name for name in os.listdir(rootPath)
              if os.path.isdir(os.path.join(rootPath, name))]

print("All Folders:", allFolders)

# # of files scanned
numScanned = 0
# list of folder name and sizes
allFolderNamesAndSizes = []
for i in allFolders:
    # current folder name
    currentDir = f"C:\\{i}"
    # get size of this folder
    thisFolderSizeMB = get_folder_size(currentDir) / 1000000
    # remove cents and print this folder
    dotPos = str(thisFolderSizeMB).find('.')
    print(currentDir, str(thisFolderSizeMB)[:dotPos], "MB")
    allFolderNamesAndSizes.append((currentDir, str(thisFolderSizeMB)[:dotPos]))
    #limit number of folders scanned
    numScanned = numScanned + 1
    if numScanned >= 24:
        print("Scan Finished")
        break

#print(allFolderNamesAndSizes)
# sort folders from biggest to smallest
sortedFolders = sorted(allFolderNamesAndSizes, key=lambda x: int(x[1]), reverse=True)

# calculate sum of folders scanned
totalMB = 0
for i in sortedFolders:
    #print('I', i[1])
    totalMB = totalMB + int(i[1])

for item in sortedFolders:
    print(str(item).replace('(', '').replace(')', '').replace("'", ''), "MB")

print(f"Scanned {totalMB}MB or {totalMB / 1000}GB")

# get size of all folders in C drive


'''

old code

#folderSizeMB = get_folder_size('C:\\Blender Addons') / 1000000
#dotPos = str(folderSizeMB).find('.')

#print("Folder size: ", str(folderSizeMB)[:dotPos], "MB")

#print(get_folder_size('C:\\test'))

#fileSizeMB = os.path.getsize("folderer") / 1000000

#os.walk()

#print(str(fileSizeMB), " MB")




'''