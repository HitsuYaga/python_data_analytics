import os;

def readAllFile(path):
  with open('log-final.txt','a') as finalfile:
    # Duyet toan bo files trong folder
    for file in os.listdir(path):
      print file;
      # Doc tung file
      f = open(path + file);
      # Doc tung line trong 1 file
      for line in f:
        # Xu ly cac line not comment
        if ('#' not in line):
          # Ghi line hop le vao file log tong hop
          finalfile.write(line+'\n');
      f.close();
    finalfile.close();

readAllFile("log-file/");