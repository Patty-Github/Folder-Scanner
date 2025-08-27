import os

# 3 things per item in list. name of file format, number of that format, size of that format.
formatInfo = []


def get_folder_size(folder):
    folder_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        #print("dirpath:", dirpath, "filenames:", filenames)

        for g in filenames:
            fileType = g[g.rfind('.'):]
            # if format isn't in list, add format to list, add 1 to format's quantNum, add fileSize
            if not any(fileType in g for g in formatInfo):
                print("format is not in")
                formatInfo.append((fileType, 1, os.path.getsize(dirpath)))

            else:
                # add 1 to format's quantNum, add size to fileSize

                indexOfFileType = 0
                # get index of fileType
                for index, l in enumerate(formatInfo):
                    if fileType in l:
                        indexOfFileType = index
                        print(fileType, index, l)

                # convert to list when needed
                print("formatinfo", formatInfo)
                formatInfoList = list(formatInfo)
                formatInfoListInner = list(formatInfoList[indexOfFileType])
                formatInfoListInner[1] += 1
                formatInfoList[indexOfFileType] = tuple(formatInfoListInner)
                formatInfo = tuple(formatInfoList)

                # find fileType in list, then add 1 to index 1



            #print("G", g[g.rfind('.'):])
            #formatInfo.append(f"{g[g.rfind('.'):]}")

        for f in filenames:
            fullPath = os.path.join(dirpath, f)
            if not os.path.islink(fullPath):
                folder_size += os.path.getsize(fullPath)

    print("NUM OF FORMAT", formatInfo)
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
    if numScanned >= 9:
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

#

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