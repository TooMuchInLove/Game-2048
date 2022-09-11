# -*- coding: utf-8 -*-

# import modules
from sqlite3 import connect


class DataBase:
    def __init__(self):
        self.conn_db = connect('GAME2048.db')
        self.curs_db = self.conn_db.cursor()
        self.curs_db.execute('''
            CREATE TABLE IF NOT EXISTS GAME2048 (id integer primary key, score integer)
        ''')
        self.conn_db.commit()

    def add_data(self, score):
        self.curs_db.execute('''
            INSERT INTO GAME2048 (score) VALUES (?)
        ''', (score,))
        self.conn_db.commit()

    def __del__(self):
        self.conn_db.close()
