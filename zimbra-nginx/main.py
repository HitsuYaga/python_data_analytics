import pandas as pdp
import numpy as np
import matplotlib.pyplot as plt

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
  mean = data.mean()
  std = data.std()
  return mean, std

def CountConnectionPerUser(data):
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

def CountConnectionPerIP(data):
  df1 = data[['ClientIP', 'LoggedUser', 'Timestamp', 'SessionID']]
  df1['Timestamp'] = df1['Timestamp'].apply(lambda x: x / 86400)
  df2 = df1.groupby(['Timestamp', 'LoggedUser', 'ClientIP']).size().reset_index(name="ConnectCount")

df = makeDataFramefromFile('log.csv')
CountConnectionPerUser(df)

