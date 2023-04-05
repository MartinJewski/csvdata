import sys
import os

def parse(filePath, fileObj):
    mycsv = open(filePath, "r")
    print("PATH:", filePath)

    while True:
        line = mycsv.readline().strip()
        if line == '':
            print("break")
            break
        newLine = line.replace(" ", ",").replace("┊","│").replace("│", ";").replace(",,,", ",").replace(",,", "").replace("│,", "|").replace(";,", ",").replace(",;", ";").replace(",,", ",")
        print(newLine)
        fileObj.write(newLine)




directory = sys.argv[1]


for filename in os.listdir(directory):
    filePath = os.path.join(directory, filename)
    newFilePath = os.path.join(directory, "CSV_" + filename)

    newCSV = open(newFilePath, "w+")


    if os.path.isfile(filePath):
        print(filePath)
        print(newFilePath)
        parse(filePath, newCSV)

