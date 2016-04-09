from src.datasource.mysql import MysqlSource


class LoggerDAO(object):
    def __init__(self):
        self.db = MysqlSource().get_db()
        self.table_name = 'logger'

    def log_entry(self, event):
        with self.db.cursor() as c:
            c.execute("INSERT INTO "+self.table_name+" SET event=%s", [event])

    def get_entries(self):
        with self.db.cursor() as c:
            c.execute("SELECT * FROM "+self.table_name+" order by moment DESC")
            return c.fetchall()
