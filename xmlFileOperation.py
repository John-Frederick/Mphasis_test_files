from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

def ReadWriteXML(x,y):
    FilePath = "C:\\Test\\Updated_Python_exercises_QA_Engr"
    xmlFile = ET.parse(FilePath + "\\test_payload1.xml")
    root = xmlFile.getroot()

    for depart in root.iter('DEPART'):
        depart.text = (datetime.today() + timedelta(days=x)).strftime('%Y%m%d')
        print("Updated Departure date is: ",depart.text)
    for retrn in root.iter('RETURN'):
        retrn.text = (datetime.today() + timedelta(days=y)).strftime('%Y%m%d')
        print("Updated Return date is: ",retrn.text)
    xmlFile.write(FilePath + "\\output_payload.xml")

    print("***This program is developed by John Frederick*** ")

if __name__ == '__main__':
    ReadWriteXML(5,10)
