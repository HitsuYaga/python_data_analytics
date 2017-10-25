import pandas as pdp
import numpy as np
import matplotlib.pyplot as plt
import datetime
# import matplotlib.style as style

# style.use('fivethirtyeight')

# plt.figure();

# %matplotlib inline

# Set gia tri hien thi graph
pdp.set_option('display.height', 1000)
pdp.set_option('display.max_rows', 500)
pdp.set_option('display.max_columns', 500)
pdp.set_option('display.width', 1000)

# Tao DataFrame tu file
def makeDataFramefromFile(file):
  # Lay du lieu tu file log.csv
  df = pdp.read_csv(file, sep=",", header=None)
  # Thiet lap ten cua cac columns trong Data Frame
  df.columns = ['DateTime', 'SessionID', 'LogType', 'ClientIP', 'LoggedUser', 'FullLog', 'Timestamp']
  return df

def caculateMeanAndSTD(data):
  # Tinh gia tri trung binh cua du lieu
  mean = data.mean()
  # Tinh do lech chuan cua du lieu
  std = data.std()
  return mean, std

def convertUnixTimetoHumanTime(unixTime):
  return datetime.datetime.utcfromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S')

def countConnectionPerUser(data):
  df1 = data[['LogType', 'LoggedUser', 'Timestamp']].copy()
  # Chia khoang thoi gian 1h
  df1['Timestamp'] = df1['Timestamp'].apply(lambda x: x / 3600)
  # Dem tong so luot ket noi theo tung user theo khoang thoi gian (1h)
  df2 = df1.groupby(['Timestamp', 'LoggedUser']).size().reset_index(name="ConnectCount")
  # Dem tong so ket noi loi theo tung user theo khoang thoi gian (1h)
  df3 = df1.groupby(['Timestamp', 'LoggedUser']).LogType.apply(lambda x: (x == 'error').sum()).reset_index(name="ErrorCount")
  df4 = df2
  # Add cot ErrorCount tu df3 sang df4
  df4['ErrorCount'] = df3['ErrorCount']
  # Tinh gia tri trung binh va do lech chua cua tong so ket noi
  mean, std = caculateMeanAndSTD(df4['ConnectCount'])
  # Gia tri nguong cua tong so ket noi
  noiseLimit = mean + std*2
  # Dua vao gia tri nguong tim ra gia tri co the tin tuong va gia tri nhieu cua truong ConnectionCount
  df4['StatusConnectCount'] = df4['ConnectCount'].apply(lambda x: 1 if x >= noiseLimit else 0)
  print df4

def countConnectionPerHour(data):
  df1 = data[['Timestamp']].copy();
  # Convert Unix timestamp sang human readable timestamp
  df1['Timestamp'] = df1['Timestamp'].apply(lambda x: convertUnixTimetoHumanTime(x))
  # Chuyen kieu du lieu cua field Timestamp tu string sang dang datetime
  df1['Timestamp'] = pdp.to_datetime(df1['Timestamp']);
  # Trich xuat ngay gio trong chuoi datetime
  df1['Hour'] = df1['Timestamp'].dt.hour;
  df1['Day'] = df1['Timestamp'].dt.day;
  # Tao DataFrame moi voi cot Hour va Day
  df2 = df1[['Day', 'Hour']]
  # Tinh tan suat xuat hien cac gia tri trong tung gio ung voi tung ngay
  df3 = df2.groupby(['Day', 'Hour']).size().reset_index(name="Count");
  # Tao Paviot table
  df3 = pdp.pivot_table(df3, index='Hour', columns='Day', values='Count');
  # Ve cac do thi lien quan
  df3.plot.bar()
  # Hien thi graph khi dung CMD
  plt.show();

def countConnectionPerIP(data):
  df1 = data[['ClientIP', 'LoggedUser', 'Timestamp', 'SessionID']]
  df1['Timestamp'] = df1['Timestamp'].apply(lambda x: x / 3600)
  df2 = df1.groupby(['Timestamp', 'LoggedUser', 'ClientIP']).size().reset_index(name="ConnectCount")

df = makeDataFramefromFile('log.csv')
# countConnectionPerUser(df)
countConnectionPerHour(df)

