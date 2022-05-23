import mysql.connector
from ui import *
from PyQt5.QtWidgets import QMessageBox
from mysql.connector import Error


def connect(host, database, user, password):
    connector = mysql.connector.connect(host=host,
                                        database=database,
                                        user=user,
                                        password=password)
    if connector.is_connected():
        print('Connection to MySQL database is successful')

    selector = "SELECT type,value FROM primtable WHERE value > 100"
    with connector.cursor() as cursor:
        cursor.execute(selector)
        result = cursor.fetchall()
        for row in result:
            print(row)
    value_catch = row[1]
    name_catch = row[0]
    #alerter(value_catch, name_catch)
    #QMessageBox.critical(self, "Обнаружено превышение значения на датчике", "Датчик", name_catch, " - ", value_catch)
    return value_catch, name_catch


if __name__ == '__main__':
    connect()
