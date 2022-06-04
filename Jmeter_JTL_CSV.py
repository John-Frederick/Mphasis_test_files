import pandas as pd
import csv
from os.path import exists
from datetime import datetime
import pytz
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def jtlToCsvFileIO(Filepath,jtlfile1,jtlfile2):
    try:
        dataframe1 = pd.read_csv(Filepath + jtlfile1,delimiter=',')
        dataframe1.to_csv(Filepath + "\\Jmeter_log1.csv",index=None)
        dataframe2 = pd.read_csv(Filepath + jtlfile2,delimiter=',')
        dataframe2.to_csv(Filepath + "\\Jmeter_log1.csv" ,mode='a',header=False,index=None)
    except NameError as NE:
        print(NE)
    except FileNotFoundError as FnF:
        print(FnF)
    try:
        with open(Filepath + "\\Jmeter_log1.csv",'r+') as updateDateFormat:
            header = ['timeStamp', 'label', 'responseCode', 'responseMessage', 'failureMessage']
            df1 = pd.read_csv(updateDateFormat,usecols=header)
            date_time = df1['timeStamp']
            for date in range(len(date_time)):
                # date_utctime = datetime.utcfromtimestamp(int(date_time[date]) / 1000)
                datetandtime = datetime.fromtimestamp((int(date_time[date]) / 1000))
                my_datetime_pst = datetandtime.astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%d %H:%M:%S %Z')
                df1.loc[date,'timeStamp'] = my_datetime_pst
            df2 = df1[df1.responseCode != 200]
            print(df2.head(10))
    except ValueError as VE:
        print(VE)
    except KeyError as KE:
        print(KE)
    print("***This program is developed by John Frederick*** ")
if __name__ == '__main__':
    Filepath = "C:\\Test\\Updated_Python_exercises_QA_Engr"
    jtlfile1 = "\\Jmeter_log1.jtl"
    jtlfile2 = "\\Jmeter_log2.jtl"
    jtlToCsvFileIO(Filepath,jtlfile1,jtlfile2)
