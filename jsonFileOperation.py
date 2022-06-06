import json
filedir = "C:\\Test\\Updated_Python_exercises_QA_Engr"
inputJsonFile = "\\test_payload.json"
outputJsonFile = "\\output_payload.json"

def jsonFileOperation(nest_key_appdate, key_outParams):
    with open(filedir + inputJsonFile, 'r+') as File:
        jsonobject = json.load(File)
        try:
            mylist = [key_outParams,nest_key_appdate]
            for char in mylist:
                if char in jsonobject.keys():
                    print(f"Delete root dictinary key is : {char}")
                    del jsonobject[char]
                else:
                    for key, value in jsonobject.items():
                        if type(value) == dict:
                            if char in value.keys():
                                print(f"Deleted nested dictionary key is : {char}")
                                del value[char]
                        elif type(value) == list:
                            listitem = value
                            for item in range(len(listitem)):
                                try:
                                    if listitem[item] == nest_key_appdate:
                                        listitem.remove(nest_key_appdate)
                                        print("Deleted list value is : ",nest_key_appdate)
                                except IndexError as IE:
                                    pass
                                    # print(IE)
                with open(filedir + outputJsonFile, 'w') as OutFile:
                    OutFile.seek(0)
                    json.dump(jsonobject, OutFile)
                    OutFile.truncate()
            print("Changes are updated in the new json file :", jsonobject)

        except  RuntimeError as RE:
            pass
            # print("------------->[Info]Exception thrown while deleting dictionary and the message is : ", RE)
    print("***This program is developed by John Frederick*** ")
if __name__ == '__main__':
    nest_key_appdate = 'appdate'
    key_outParams = 'outParams'
    jsonFileOperation(nest_key_appdate, key_outParams)
