from src.datasource.mysql import MysqlSource


class LoggerDAO(object):
    def __init__(self):
        self.db = MysqlSource()

    def log_entry(self, event):
        with self.db.get_cursor() as c:
            c.execute("INSERT INTO logger SET event=%s", [event])

    def get_entries(self):
        with self.db.get_cursor() as c:
            c.execute("SELECT * FROM logger order by moment DESC")
            return c.fetchall()
