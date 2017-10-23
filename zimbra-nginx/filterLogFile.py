def writeToFile(data):
  with open('final-log.txt', 'a') as file:
    file.write(data+'\n')
    file.close()

def closeFile(fileName):
	with open(fileName,'a') as file:
		file.close();

###########################################################################

def readFile(fileName):
	f = open(fileName);
  for line in f:
		words=line.split();
		date = words[0];
		time = words[1];
		type_log = words[2][1:-1];
		session_id = words[4][1:];
		if (('logged' in line) or ('proxied' in line)):
			client_ip = words[9].split(':')[0];
			login_name = words[13][:-1][1:-1]
		elif ('connected' in line):
			client_ip = words[6].split(':')[0];
			login_name = 'null'
		elif (type_log == 'error' and 'zm' in line):
			client_ip = words[24].split(':')[0];
			login_name = words[28][1:-1]
		else:
			client_ip = words[20].split(':')[0];
			login_name = words[24][1:-1]

		message = date + ' ' + time + ' ' + type_log + ' ' + session_id + ' ' + client_ip + ' ' + login_name;
		writeToFile(message);

readFile('zimbra-nginx.txt');
closeFile('final-log.txt');
