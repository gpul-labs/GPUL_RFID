import pymysql

class MysqlSource(object):

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306,
                                  user='rfid', passwd='rfid_gpul', db='rfid',
                                  cursorclass=pymysql.cursors.DictCursor)
        self.db.autocommit(True)

    def get_db(self):

        return self.db
