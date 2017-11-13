import MySQLdb


class Database(object):

    @staticmethod
    def initializeDB():
        db = MySQLdb.connect("222.255.102.149", "metronapi",
                             "simn_metron", "metron")
        return db.cursor()

    @staticmethod
    def queryUsernameAndPassword(username, password):
        cursor = Database.initializeDB()
        sql = "SELECT * FROM users \
            WHERE USERNAME='%s' AND PASSWORD='%s'" % (username, password)
        try:
            results = cursor.execute(sql)
            if results == 1:
                return True
            else:
                return False
        except:
            return "Error Connection"
