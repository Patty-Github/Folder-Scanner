import os

'''
Assignment
'''

# 3 things per item in list. name of file format, number of that format, size of that format.
formatInfo = []
#specify root path
rootPath = 'C:\\'
# how many folders scanning
numOfFolders = 25
# open txt file
outputFile = open("info.txt", "w")

'''
Calcs
'''


# get and return the size of folder
def get_folder_size(folder):
    folder_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        #print("dirpath:", dirpath, "filenames:", filenames)

        for g in filenames:
            fullPath = os.path.join(dirpath, g)
            print(f"Full Path: {fullPath}, Size: {os.path.getsize(fullPath)}")
            outputFile.write(f"Full Path: {fullPath}, Size: {os.path.getsize(fullPath)} \n \n")
            #print(f"Filename is {g} size is {os.path.getsize(fullPath)}, dirpath is {dirpath}, "
            #      f"maybe size is {os.path.getsize(dirpath)}")
            fileType = g[g.rfind('.'):]
            # if format isn't in list, add format to list, add 1 to format's quantNum, add fileSize
            if not any(fileType in g for g in formatInfo):
                #print("format is not in")
                formatInfo.append((fileType, 1, os.path.getsize(fullPath)))

            else:
                # add 1 to format's quantNum, add size to fileSize

                indexOfFileType = 0
                # get index of fileType
                for index, l in enumerate(formatInfo):
                    if fileType in l:
                        indexOfFileType = index
                        #print(fileType, index, l)

                # convert to list when needed
                # create list from info so it can be modified
                formatInfoList = list(formatInfo)
                formatInfoListInner = list(formatInfoList[indexOfFileType])
                # add num of format
                formatInfoListInner[1] += 1
                # add format size
                formatInfoListInner[2] += os.path.getsize(fullPath)
                # save to list
                formatInfoList[indexOfFileType] = tuple(formatInfoListInner)
                # clear current info, replace with new info
                formatInfo.clear()
                formatInfo.extend(tuple(formatInfoList))

            #print("G", g[g.rfind('.'):])
            #formatInfo.append(f"{g[g.rfind('.'):]}")

        for f in filenames:
            fullPath = os.path.join(dirpath, f)
            #print(f"fullPath {fullPath}")
            if not os.path.islink(fullPath):
                folder_size += os.path.getsize(fullPath)

    #print("NUM OF FORMAT", formatInfo)
    return folder_size


# get name of all folders in C:\, put them in a list
allFolders = [name for name in os.listdir(rootPath)
              if os.path.isdir(os.path.join(rootPath, name))]

print("All Folders:", allFolders)
outputFile.write(f"All Folders:, {allFolders} \n \n")

# # of files scanned
numScanned = 0
# list of folder name and sizes
print("Folder Name and Sizes")
outputFile.write("Folder Name and Sizes \n \n")
allFolderNamesAndSizes = []
for i in allFolders:
    # current folder name
    currentDir = f"{rootPath}{i}"
    # get size of this folder
    thisFolderSizeMB = get_folder_size(currentDir) / 1000000
    # remove cents and print this folder
    dotPos = str(thisFolderSizeMB).find('.')
    print(currentDir, str(thisFolderSizeMB)[:dotPos], "MB")
    outputFile.write(f"{currentDir} {str(thisFolderSizeMB)[:dotPos]} MB \n \n")
    allFolderNamesAndSizes.append((currentDir, str(thisFolderSizeMB)[:dotPos]))
    #limit number of folders scanned
    numScanned = numScanned + 1
    if numScanned >= numOfFolders:
        #print("Scan Finished")
        break


# convert format info from bytes to GB
formatInfoMB = []

for count, (i, j, k) in enumerate(formatInfo):
    # convert to list to make changeable
    iList = list((i, j, k))

    # convert to MB, then cut off past 3 cents
    convertedSize = k / 1000000
    dotPos = str(convertedSize).rfind('.')
    #convertedSize = str(convertedSize)[:dotPos + 4]
    convertedSize = f"{convertedSize:.3f}"
    convertedSize = float(convertedSize)

    iList[2] = convertedSize

    formatInfoMB.append(iList)


'''
Sorting
'''

# sort folders from biggest to smallest
sortedFolders = sorted(allFolderNamesAndSizes, key=lambda x: int(x[1]), reverse=True)

# sort format info
sortedFormatInfo = sorted(formatInfoMB, key=lambda x: float(x[2]), reverse=True)
#print(f"sorted info {sortedFormatInfo}")

# calculate sum of folders scanned
totalMB = 0
for i in sortedFolders:
    #print('I', i[1])
    totalMB = totalMB + int(i[1])

'''
Output
'''

# print folders and  their size in order
for item in sortedFolders:
    print(str(item).replace('(', '').replace(')', '').replace("'", ''), "MB")
    outputFile.write(f"""{str(item).replace('(', '').replace(')', '').replace("'", '')} "MB" \n \n""")


for item in sortedFormatInfo:
    #print(str(item).replace('[', '').replace(']', '').replace("'", ''))
    print(f"{item[0]} Appeared {item[1]} Times, Totaling {item[2]}MB")
    outputFile.write(f"{item[0]} Appeared {item[1]} Times, Totaling {item[2]}MB \n \n")

print(f"Scanned {totalMB}MB or {totalMB / 1000}GB")
outputFile.write(f"Scanned {totalMB}MB or {totalMB / 1000}GB \n \n")

print(f"length of format info sorted {len(sortedFormatInfo)}, length of format info mb {len(formatInfoMB)}")
outputFile.write(f"length of format info sorted {len(sortedFormatInfo)}, length of format info mb {len(formatInfoMB)} \n \n")
#

# close file
outputFile.close()
#outputFile.write()



'''

order of operations:

1. scan folders
2. get info from folders
3. sort info from folders
4. output info from folders

TO DO 



old code

#folderSizeMB = get_folder_size('C:\\Blender Addons') / 1000000
#dotPos = str(folderSizeMB).find('.')

#print("Folder size: ", str(folderSizeMB)[:dotPos], "MB")

#print(get_folder_size('C:\\test'))

#fileSizeMB = os.path.getsize("folderer") / 1000000

#os.walk()

#print(str(fileSizeMB), " MB")




'''