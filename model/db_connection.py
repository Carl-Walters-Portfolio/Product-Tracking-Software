import sqlite3

class dbConnection:
        """
        The dbConnection class provides methods for interacting with a sqlite3 database. It includes methods for executing
        SELECT and INSERT statements, as well as for connecting to and closing the database connection.
        
        Communication with the View component:
            - The dbConnection class does not communicate directly with the View component.
            
        Communication with the controller:
            - The dbConnection class does not communicate directly with the View component.

        Communication with the Model component:
            - The dbConnection class provides methods for interacting with the database, which can be used by the 
              Model components to perform create, read, update, and delete operations on the products.db.
              It is the only file in the Model layer that is able to directly connect to the database.
              query_db.py and write_to_db.py send dbConnection SQL code which dbConnection executes on their behalf.
        """

        def __init__(self):
            """
            Initializes the dbConnection object with default database name and no connection or cursor.
            """
            self.dbName = "model/products.db"
            self.connection = None
            self.cursor = None
            
        def get(self, query):
            """
            Executes a SELECT statement on the database and returns the result.

            Args:
                query (str): The SELECT statement to execute on the database.

            Returns:
                The result of the SELECT statement as a tuple.
            """
            try:
                self.connect()
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                self.close()
            
                return result
            
            except sqlite3.Error as e:
                print(f"Error executing query: {e}")
                return None
        
        def set(self, sql, data):
            """
            Executes an INSERT statement on the database.

            Args:
                sql (str): The INSERT statement to execute on the database.
                data (tuple): The data to be inserted into the database.

            Returns:
                None.
            """
            try:
                self.connect()
                self.cursor.execute(sql, data)
                self.closeCommit()
            except sqlite3.Error as e:
                print(f"Could not be added to database {e}")

        def connect(self):
            """
            Connects to the database and returns the connection object.

            Returns:
                The connection object.
            """
            try:
                self.connection = sqlite3.connect(self.dbName)
                self.cursor = self.connection.cursor()
                return self.connection

            except sqlite3.Error as e:
                print(f"Could not connect: {e}")
        
        def close(self):
            """
            Closes the connection and cursor to the database.

            """
            self.cursor.close()
            self.connection.close()

        def closeCommit(self):
            """
            Commits the changes made to the database, and then closes the connection and cursor.

            """            
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            
        def setDatabaseName(self, dbName_):
            """
            Sets the database name to be used by the dbConnection object.

            Args:
                dbName_ (str): The name of the database to be used.

            """
            self.dbName = dbName_

