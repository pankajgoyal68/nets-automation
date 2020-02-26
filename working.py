import fnmatch

def moveFilesByMatchingPattern(dirPath, pattern):
    listOfFilesWithError = []
    for parentDir, dirnames, filenames in os.walk(dirPath):
        for filename in fnmatch.filter(filenames, failure):
            try:
                os.move(os.path.join(parentDir, filename))
            except:
                print("Error while moving file : ", os.path.join(parentDir, filename))
                listOfFilesWithError.append(os.path.join(parentDir, filename))
 
    return listOfFilesWithError
