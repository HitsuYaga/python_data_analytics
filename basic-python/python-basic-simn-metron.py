import MySQLdb

# Open database connection
db = MySQLdb.connect("222.255.102.137","simn","simn@vnptdata","testdb")

def queryRuleDB():
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM Apply_Rule \
       WHERE (Rule like '%A%' OR Rule like '%B%' OR Rule like '%C%')"
    try:
    # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        return results

    except:
        print "Error: unable to fecth data"

def queryResultDB(rule):
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM Apply_Rule \
       WHERE Rule = '%s'" % (rule)
    try:
    # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        return results[0][0]

    except:
        print "Can not fetch any data"

def compareWithRule(A, B, C, conditions):
    for condition in conditions:
        rule_tmp = condition[1]
        rule = rule_tmp.replace(", ", " & ")
        if eval(rule):
            result = queryResultDB(rule_tmp)
            return result
    return -1

def writeToCSV(data):
    with open('result.csv','a') as file:
        file.write(data+'\n')
        file.close()

###########################################################################
# Query conditional in MySQL
conditions = queryRuleDB();

f = open('log.txt');
for line in f:
    words=line.split()
    A = words[1].split(',')[0];
    B = words[2].split(',')[0];
    C = words[3];

    result = compareWithRule(int(A), int(B), int(C), conditions)
    message = A + ' ' + B + ' ' + C + ' ' + str(result);
    writeToCSV(message);

# disconnect from server
db.close()