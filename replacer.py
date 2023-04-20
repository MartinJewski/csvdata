
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
    
def unitInString(unitList, String):
    contains = False
    for unit in unitList:
        if unit in String:
            contains = True
            break
    return contains

    

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
    stringList = str(stringVal).split(",")
    print("PREPARE: ", stringList)
    units = ["B", "K", "M", "G", "NONE"]
    finalString = ""
    
    for ele in range(stringList.__len__()):
        for i in units:
            if stringList[ele].find(i) != -1 and stringList[ele].find(".") == -1:
                #print("---------")
                #print("01", i)
                #print("11", ele)
                #print("21", stringList[ele], i)                
                #print("31", convertUnit(stringList[ele].replace(i, ""), i))
                #print("41", stringList[ele].replace(i, ""))
                #print("51", isFloat(stringList[ele].replace(i, "")))
                stringList[ele] = str(convertUnit(stringList[ele].replace(i, ""), i))
                #print("---------")

            if stringList[ele].find(i) != -1 and unitInString(units, stringList[ele]) and (stringList[ele].count('.') == 1):
                #print("---------")
               #print("02", i)
               # rint("12", ele)
               #print("22", stringList[ele], i)                
               #print("32", convertUnit(stringList[ele].replace(i, ""), i))
                #print("42", stringList[ele].replace(i, ""))
                #print("52", isFloat(stringList[ele].replace(i, "")))
                stringList[ele] = str(convertUnit(stringList[ele].replace(i, ""), i))
                #print("---------")

            if not unitInString(units, stringList[ele]) and (stringList[ele].count('.') == 1):
                #print("---------")
                #print("03", "NONE")
                #print("13", ele)
                #print("23", stringList[ele], "<<< POINT")                
                #rint("33", convertUnit(stringList[ele], "NONE"))
                #print("44", stringList[ele].replace(i, ""))
                #print("43", isFloat(stringList[ele].replace(i, "")))
                #print("---------")
                stringList[ele] = str(convertUnit(stringList[ele], "NONE"))




    for ele in range(stringList.__len__()):
        if ele == stringList.__len__()-1:
            finalString += stringList[ele]
        else:
            finalString += stringList[ele] + ","

    return finalString





#mystring = "l:2,45,1,54,0,0,1419K,3263K,0,0,0,0,1.3B,6.3B,26.96G,41.231G,81.5G,12.3G,5108,3943,0,0,5.6,0.08,0.09,0.09,Apr-07,14:18:32,node24-012.cm.cluster,07-04-2023,14:18:32"

print(unitInString(["G"], "19.1G"))

#print("3.0.0".count('.'))

#monitoringLineConvert(mystring)

#convert_to_byte(mystring)