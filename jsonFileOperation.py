
import json
filepath = "C:\\Test\\Updated_Python_exercises_QA_Engr\\test_payload.json"

def jsonFileOperation(key_appdate,key_outParams):
    with open(filepath,'r+') as File:
        jsonobject = json.load(File)
        try:
            for key, val in jsonobject.items():
                try:
                    if type(val) == dict:
                        for key1, val1 in val.items():
                            del jsonobject[key][key_appdate]
                            print(f"Result after removing [{key_appdate}] from [{key}] : ", jsonobject[key])
                    else:
                        if key == key_outParams:
                            print(key)
                            del jsonobject[key]
                            print(f"Result after removing from [{key}] : ", jsonobject)

                    File.seek(0)
                    json.dump(jsonobject, File)
                    File.truncate()

                except  RuntimeError as RE:
                    print("------------->[Info]Exception thrown while deleting dictionary and the message is : ", RE)
        except  RuntimeError as RE:
            print("------------->[Info]Exception thrown while deleting dictionary and the message is : ", RE)
    print("***This program is developed by John Frederick*** ")
if __name__ == '__main__':
    key_appdate = 'appdate'
    key_outParams = 'outParams'
    jsonFileOperation(key_appdate,key_outParams)



