from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

def ReadWriteXML(x,y):
    FilePath = "C:\\Test\\Updated_Python_exercises_QA_Engr"
    xmlFile = ET.parse(FilePath + "\\test_payload1.xml")
    root = xmlFile.getroot()

    for depart in root.iter('DEPART'):
        depart.text = str(x)
        print("Updated Departure date is: ",depart.text)
    for retrn in root.iter('RETURN'):
        retrn.text = str(y)
        print("Updated Return date is: ",retrn.text)
    xmlFile.write(FilePath + "\\output_payload.xml")

    print("***This program is developed by John Frederick*** ")

if __name__ == '__main__':
    x = int((datetime.today() + timedelta(days=3)).strftime('%Y%m%d'))
    y = int((datetime.today() + timedelta(days=5)).strftime('%Y%m%d'))
    ReadWriteXML(x,y)











