import mysql.connector
from mysql.connector import Error
from config.config import DB_DATABASE,DB_HOSTNAME,DB_PASSWORD,DB_PORT,DB_USERNAME


class DbConnection:
    def __init__(self):
        self.__connection = None
        self.__cursor = None
        print("Trying to connnect")
        try:
            self.__connection = mysql.connector.connect(
                host = DB_HOSTNAME,
                database =DB_DATABASE,
                user = DB_USERNAME,
                password = DB_PASSWORD,
                port = DB_PORT
            )
        except Error as err:
            print("Error Connection",err)
        except Exception as err:
            print('!! Error', err)
        else:
            if self.__connection.is_connected():
                print('Connected')
                print(self.__connection.get_server_info())
                self.__cursor = self.__connection.cursor()
                
                
    def get_cursor(self):
        if self.__cursor is not None:
            return self.__cursor
        else:
            print('No db connection found')
            return None
        
        
    def close_connection(self):
        if self.__connection is not None:
            if self.__cursor is not None:
                self.__cursor.close()
            self.__connection.close()
            print('Conn close successfully')

            
            