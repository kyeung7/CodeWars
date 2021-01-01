def to_jaden_case(string):
    returnStr = ""
    list = string.split(" ")
    for element in list:
        element = element[0].upper() + element[1:] + " "
        returnStr += element
        
    return returnStr[:-1]
