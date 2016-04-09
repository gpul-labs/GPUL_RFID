import pymysql


class LoggerDAO(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306,
                                  user='rfid', passwd='rfid_gpul', db='rfid',
                                  cursorclass=pymysql.cursors.DictCursor)
        self.db.autocommit(True)

    def log_entry(self, event):
        with self.db.cursor() as c:
            c.execute("INSERT INTO logger SET event=%s", [event])

    def get_entries(self):
        with self.db.cursor() as c:
            c.execute("SELECT * FROM logger order by moment DESC")
            return c.fetchall()
