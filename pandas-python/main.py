import pandas as pdp;
import numpy as np;
import matplotlib.pyplot as plt;

# plt.figure();

# %matplotlib inline

# Set gia tri hien thi graph
pdp.set_option('display.height', 1000)
pdp.set_option('display.max_rows', 500)
pdp.set_option('display.max_columns', 500)
pdp.set_option('display.width', 1000)

# Tao DataFrame tu file
def makeDataFramefromFile(file):
  # Lay du lieu tu file log-final.txt
  df = pdp.read_csv(file, sep=" ", header=None);
  # Thiet lap ten cua cac columns trong Data Frame
  df.columns = ['date', 'time', 's_ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port', 'cs-username', 'c_ip', 'cs(User-Agent)', 'cs(Referer)', 'sc-status', 'sc-substatus', 'sc-win32-status', 'time-taken']
  return df;

# Ham ve bar chart
def drawBarChart(data, title):
  data.plot(kind='bar', title=title);
  # Hien thi graph khi dung CMD
  plt.show();

# Ham ve Sdatter Chart
def drawScatterChart(data, x_field, y_field, title):
  data.plot(kind='scatter', x=x_field, y=y_field, title=title);
  # Hien thi graph khi dung CMD
  plt.show();

# Phan tich va ve do thi tan suat truy cap theo gio
def countLogInFreqPerHour(df):
  # Tao DataFrame moi bang cach trich xuat 2 cot date va time tren DataFrame cha
  df1 = df[['date', 'time']].copy();
  # Tao 1 cot moi
  df1['timestamp'] = df1['date'] + ' ' + df1['time'];
  # Chuyen type tu object ve thanh datetime (chuyen xu ly cac kieu thoi gian)
  df1['timestamp'] = pdp.to_datetime(df1['timestamp']);
  # Lay ra gia tri gio trong timestamp
  df1['hour'] = df1['timestamp'].dt.hour;
  # Tao DataFrame moi voi cot hour
  df2 = df1[['hour']].copy();
  # Tinh tan suat xuat hien cac gia tri trong cot hour
  df3 = df2.hour.value_counts().sort_values(ascending=False).reset_index(name="count").rename(columns={'index': 'hour'});
  # Chon cot hour lam index cho DataFrame
  df4 = df3.set_index(['hour']);
  # Ve cac do thi lien quan
  drawBarChart(df4, 'Tan suat truy cap theo gio');
  drawScatterChart(df3, 'hour', 'count', 'Tan suat truy cap theo gio')

# Phan tich va ve do thi tan suat truy cap theo IP
def countLogInFreqPerIP(df):
  # Tao DataFrame moi bang cach trich xuat 1 cot s_ip cua DataFrame cha
  df1 = df[['s_ip']].copy();
  # Tinh tan suat xuat hien cac gia tri trong cot s_ip
  df2 = df1.s_ip.value_counts().sort_values(ascending=False).reset_index(name="count").rename(columns={'index': 's_ip'});
  # Chon cot s_ip lam index cho DataFrame
  df3 = df2.set_index(['s_ip']);
  # Thay doi tat ca gia tri cua cot s_ip thanh 1
  df2['s_ip'] = df2['s_ip'].apply(lambda x: 1)
  # Ve cac do thi lien quan
  drawBarChart(df3, 'Tan suat truy cap theo IP');
  drawScatterChart(df2, 's_ip', 'count', 'Tan suat truy cap theo IP')

# Phan tich va ve do thi tan suat truy cap theo IP va ngay
def countLogInFreqPerIPandDate(df):
  # Tao DataFrame moi bang cach trich xuat 2 cot s_ip va date cua DataFrame cha
  df1 = df[['s_ip', 'date']].copy();
  # Groupby theo 2 field theo dang count va them cot moi voi ten count
  df2 = df1.groupby(['date', 's_ip']).size().reset_index(name="count");
  # Tao Pivot Tables
  df3 = pdp.pivot_table(df2, index='date', columns='s_ip', values='count');
  drawBarChart(df3, 'Tan suat truy cap theo IP va ngay');
  df3.plot(title="Tan suat truy cap theo IP va ngay");plt.show();

df = makeDataFramefromFile('log-final.txt');
countLogInFreqPerHour(df);
countLogInFreqPerIP(df);
countLogInFreqPerIPandDate(df);