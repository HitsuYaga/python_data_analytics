import MySQLdb
def queryResultDB(rule):
    db = MySQLdb.connect("222.255.102.137","simn","simn@vnptdata","testdb")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT * FROM Apply_Rule \
       WHERE Rule = '%s'" % (rule)
    try:
    # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        print results
        return results

    except:
        print "Error: unable to fecth data"

    # disconnect from server
    db.close()

queryResultDB('A>10, B<10, C>5')
