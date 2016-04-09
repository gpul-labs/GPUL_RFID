from src.datasource.mysql import MysqlSource

class CardsDAO(object):
    def __init__(self):
        self.db = MysqlSource().get_db()
        self.table_name = "cards"

    def create_card(self, username, num0, num1, num2, num3, num4):
        with self.db.cursor() as c:
            c.execute("INSERT INTO "+self.table_name+" SET username=%s, num0=%s, num1=%s, num2=%s, num3=%s, num4=%s",
                      [username, num0, num1, num2, num3, num4])

    def get_cards(self):
        with self.db.cursor() as c:
            c.execute("SELECT * FROM "+self.table_name+" order by create_time DESC")
            return c.fetchall()

    def get_card(self, num0, num1, num2, num3, num4):
        with self.db.cursor() as c:
            c.execute("SELECT * FROM "+self.table_name+" WHERE num0=%s and num1=%s and num2=%s and num3=%s and num4=%s",
                      [num0, num1, num2, num3, num4])
            return c.fetchone()