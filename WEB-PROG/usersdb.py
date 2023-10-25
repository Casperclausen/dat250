"""
Example SQLite usage using PySQLite Connector/Python

https://www.sqlitetutorial.net/sqlite-python/
"""

import sqlite3
from sqlite3 import Error
from werkzeug.security import generate_password_hash


def drop_table(conn):
    """Drop table."""
    cur = conn.cursor()
    try:
        sql = "DROP TABLE users"
        cur.execute(sql)
    except Error as err:
        # if err.errno == errorcode.ER_BAD_TABLE_ERROR:
        #     print("Error: Table does not exist.")
        # else:
        print("Error: {}".format(err))
    else:
        print("Table dropped.")
    finally:
        cur.close()


def create_table(conn):
    """Create table."""
    cur = conn.cursor()
    try:
        sql = ("CREATE TABLE users ("
               "username TEXT NOT NULL UNIQUE, "
               'role TEXT,'
               "password TEXT NOT NULL); "
               )
        cur.execute(sql)
    except Error as err:
        print("Error: {}".format(err))
    else:
        print("Table created.")
    finally:
        cur.close()


def insert_admin(conn, username, password):
    return insert_account(conn, username, password, 'admin')
        
def insert_user(conn, username, password):
    return insert_account(conn, username, password, 'user')

def insert_account(conn, username, password, role):
    cur = conn.cursor()
    sql = "INSERT INTO users(username, password, role) VALUES (?, ?, ?)"
    try:
        cur.execute(sql, (username, password, role))
        conn.commit()
        return True
    except Error as err:
        print("Error: {}".format(err))
        return False
    finally:
        cur.close()
        
  
def get_users(conn, username):
    """Querying data."""
    cur = conn.cursor()
    try:
        sql = ("SELECT username, password, role FROM users "
               "WHERE username = ?")

        cur.execute(sql, (username,))
        for (name,pw, role) in cur:
            return{
                "username": name,
                "password": pw,
                "role": role
            }
        else:
            return None
    except Error as err:
        print("Error: {}".format(err))
    finally:
        cur.close()
       



if __name__ == "__main__":

    try:
        conn = sqlite3.connect("database.db")
    except Error as err:
        print(err)
    else:
        drop_table(conn)
        create_table(conn)
        insert_admin(conn,"admin", generate_password_hash("1234"))
        conn.close()