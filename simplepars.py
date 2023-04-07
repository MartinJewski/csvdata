import sys
import os
import replacer

def parse(filePath, fileObj):
    mycsv = open(filePath, "r")
    print("PATH:", filePath)

    counter = 0
    while True:
        line = mycsv.readline().strip()
        if line == '':
            print("break")
            break

        if counter == 0:
            newLine = line.replace(" ", ",").replace("┬", ",").replace(";", ",")
            newLine = newLine + "\n"
            print(newLine, end=" ")
            fileObj.write(newLine)
            counter += 1
            continue
            
        
        if counter == 1:
            newLine = line.replace(" ", ",").replace("│", ",").replace(",,,", ",").replace(",,",",").replace(",,",",")
            newLine = newLine + "\n"
            print(newLine, end=" ")
            fileObj.write(newLine)
            counter += 1
            continue
            
        
        if counter > 1:
            newLine = line.replace(" ", ",").replace("┊",",").replace("│", ",").replace(",,,", ",").replace(",,", ",").replace("│,", ",").replace(",;", ",").replace(",,", ",")
            newLine = replacer.monitoringLineConvert(newLine) + "\n"
            print(newLine, end=" ")
            fileObj.write(newLine)
            counter += 1
            continue
            
    counter = 0


directory = sys.argv[1]


for filename in os.listdir(directory):
    filePath = os.path.join(directory, filename)
    newFilePath = os.path.join(directory, "CSV_" + filename)

    newCSV = open(newFilePath, "w+")


    if os.path.isfile(filePath):
        print(filePath)
        print(newFilePath)
        parse(filePath, newCSV)

