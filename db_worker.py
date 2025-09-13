import sqlite3

class BazaDBAsync():
    cache = dict()

    def __init__(self):
        self.connection = sqlite3.connect('baza.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

        with open('init_db.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            self.cursor.executescript(sql_script)



    async def get_roles(self):
        self.cursor.execute("SELECT * FROM roles;")
        res = self.cursor.fetchall()
        return res

    async def get_users(self):
        pass
