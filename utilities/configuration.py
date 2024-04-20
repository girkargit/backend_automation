import configparser
import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


connect_config = {"user": getconfig()["sql"]["user"],
                  "database": getconfig()["sql"]["database"],
                  "host": getconfig()["sql"]["host"],
                  "password": getconfig()["sql"]["password"]
                  }


def get_connection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection succesfull.")
            return conn
    except Error as e:
        print(e)


def get_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)
    conn.close()
    return row
