def fileRead():

    file = open("Test.txt", "r")
    lines = file.readlines()
    file.close()

    fileTokens = ""
    for line in lines:
        fileTokens += line

    return fileTokens

#print(fileRead())