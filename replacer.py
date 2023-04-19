
def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def convertUnit(num, unit):
    parsedValue = 0
    if unit == "B":
        if isInt(num):
            parsedValue = int(num) * 8 #giga
        elif isFloat(num):
            parsedValue = round(float(num) * 8) #giga
    elif unit == "K":
        if isInt(num):
            parsedValue = int(num) * pow(10, 3) #kilo
        elif isFloat(num):
            parsedValue = round(float(num) * pow(10, 3)) #kilo
    elif unit == "M":
        if isInt(num):
            parsedValue = int(num) * pow(10, 6) #mega
        elif isFloat(num):
            parsedValue = round(float(num) * pow(10, 6)) #mega
    elif unit == "G":
        if isInt(num):
            parsedValue = int(num) * pow(10, 9) #giga
        elif isFloat(num):
            parsedValue = round(float(num) * pow(10, 9)) #giga
    else:
        if isInt(num):
            parsedValue = int(num) #giga
        elif isFloat(num):
            parsedValue = round(float(num)) #giga

    return parsedValue
    

def monitoringLineConvert(stringVal: str):
    #csvFile = open(filePath, "w+")
    stringList = stringVal.split(",")
    units = ["B", "K", "M", "G", "NONE"]
    finalString = ""
    
    for ele in range(stringList.__len__()):
        for i in units:
            if stringList[ele].__contains__(i):
                print("1", ele)
                print("2", stringList[ele], i)                
                print("3", convertUnit(stringList[ele].replace(i, ""), i))
                stringList[ele] = str(convertUnit(stringList[ele].replace(i, ""), i))
            if stringList[ele].__contains__("."):
                print("1", ele)
                print("2", stringList[ele], i)                
                print("3", convertUnit(stringList[ele], "NONE"))
                stringList[ele] = str(convertUnit(stringList[ele], "NONE"))



    for ele in range(stringList.__len__()):
        if ele == stringList.__len__()-1:
            finalString += stringList[ele]
        else:
            finalString += stringList[ele] + ","

    return finalString





mystring = "l:2,45,1,54,0,0,1419K,3263K,0,0,0,0,13B,63B,26.96G,41.231G,81.5G,123G,5108,3943,0,0,5.6,0.08,0.09,0.09,Apr-07,14:18:32,node24-012.cm.cluster,07-04-2023,14:18:32"

monitoringLineConvert(mystring)

#convert_to_byte(mystring)