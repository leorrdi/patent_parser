from getpass import getpass
from mysql.connector import connect, Error
from datetime import datetime

host = "localhost"
user = "root"
password="2296"
database="new_schema"


def insertIntoTable(title, date, descriprion, link, source, nameTable = ''):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""INSERT INTO `{nameTable}` (name,date,description,link,source, recordingDate) VALUES (%s, %s, %s, %s, %s, %s)"""
            val = (title, date, descriprion, link, source, datetime.now().date())
            with connection.cursor() as cursor:
                cursor.execute(query, val)
                connection.commit()
    except Error as e:
        print(e)


def selectFromTable(nameTable):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""SELECT * FROM `{nameTable}`"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
    except Error as e:
        print(e)
    return result


def SelectFromTableSource(nameTable, source):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""SELECT * FROM `{nameTable}` WHERE source = %s"""
            val = (source,)
            with connection.cursor() as cursor:
                cursor.execute(query, val)
                result = cursor.fetchall()
    except Error as e:
        print(e)
    return result


def createTable(nameTable = ''):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""CREATE TABLE `{nameTable}` (
                    `id` int NOT NULL AUTO_INCREMENT,
                    `name` longtext,
                    `date` date,
                    `description` longtext,
                    `link` mediumtext,
                    `source` mediumtext,
                    `recordingDate` date DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    )"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
    except Error as e:
        print(e)


def showTables():
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = """SHOW FULL TABLES"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Error as e:
        print(e)


def deletingTable(nameTable):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""DROP TABLE IF EXISTS `{nameTable}` """
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Error as e:
        print(e)


def deleteEntry(nameTable, link):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""DELETE FROM `{nameTable}`
            WHERE link = '{link}'"""
            with connection.cursor() as cursor:
                cursor.execute(query)
                return connection.commit()
    except Error as e:
        print(e)


def insertAllIntoTable(nameTable, objects):
    try:
        with connect(
            host= host,
            user=user,
            password=password,
            database=database
        ) as connection:
            query = f"""INSERT INTO `{nameTable}` (name,date,description,link,source) VALUES (%s, %s, %s, %s, %s)"""
            with connection.cursor() as cursor:
                cursor.executemany(query, objects)
                return connection.commit()
    except Error as e:
        print(e)