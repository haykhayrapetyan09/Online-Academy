import psycopg2
from config.config import configure
from datetime import datetime


class ConnectionManager:
    def __init__(self, configpath="../config/database.ini"):
        print('Connecting to the PostgreSQL database...')
        try:
            self.params = configure(filename=configpath)
            self.conn = psycopg2.connect(**self.params)
            self.cur = self.conn.cursor()
            print("Successful connect")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        print("Closing connection...")
        if self.conn is not None:
            self.conn.close()
        print("Have a nice day :)")

    def db_info(self):
        try:
            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')
            db_version = self.cur.fetchone()
            print(db_version)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def execute(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert(self, table, columns, values, return_id="", add_creation_date=False):
        if add_creation_date:
            current_datetime = datetime.now().replace(microsecond=0)
            values = values + (current_datetime, current_datetime)
        attributes = ("%s,"*len(columns))[:-1]
        columns = ", ".join(columns)
        sql = "INSERT INTO "+table+"("+columns+") VALUES("+attributes+")"
        if return_id:
            sql += " RETURNING "+return_id+";"
        try:
            self.cur.execute(sql, values)
            self.conn.commit()
            if return_id:
                return self.cur.fetchone()[0]
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_list(self, table, columns, values):
        attributes = ("%s," * len(columns))[:-1]
        columns = ", ".join(columns)
        sql = "INSERT INTO " + table + "(" + columns + ") VALUES(" + attributes + ")"
        try:
            self.cur.executemany(sql, values)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_column_names(self, table):
        try:
            self.cur.execute("Select * FROM "+table+" LIMIT 0")
            colnames = [desc[0] for desc in self.cur.description]
            return colnames
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_columns(self, needed_cols, table, condition=""):
        if needed_cols != "*":
            needed_cols = ", ".join(needed_cols)
        sql = "SELECT " + needed_cols + " FROM "+table
        if condition:
            sql += " " + condition
        try:
            self.cur.execute(sql)
            received_columns = self.cur.fetchall()
            return received_columns
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == '__main__':
    connector = ConnectionManager(configpath="config/database.ini")
    connector.db_info()
    connector.close()
