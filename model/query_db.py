from db_connection import dbConnection

import os

class QueryDB:
    """
    The QueryDB class provides methods for querying data from the database using the dbConnection model component.
    However it does not directly access the database instead that is left to the dbconnection class that this 
    class utilizes.

    Communication with the View component:
        - The QueryDB class does not communicate directly with the View component. Instead, it provides methods for 
        querying data from the database that can be used by the controller layer where ReadController to retrieve 
        data for display to the user.
        
    Communication with the Controller component:
        - The QueryDB class is used by the ReadController to interact with the database.
        - The ReadController calls the following methods on the QueryDB instance to retrieve data from the database:
            - getAllColumns(): returns a tuple of all columns in the database
            - getAllRecordIdentifiers(): returns a tuple of all record identifiers in the database
            - getAllNames(): returns a tuple of all names in the database
            - getAllUseByDate(): returns a tuple of all use by dates in the database
            - getAllDateCreated(): returns a tuple of all dates created in the database
            - sortByIdentifier(order): returns a tuple of all records sorted by record identifier in ascending or 
              descending order based on the 'order' parameter
            - sortByName(order): returns a tuple of all records sorted by name in ascending or descending order 
              based on the 'order' parameter
            - sortByUseByDate(order): returns a tuple of all records sorted by use by date in ascending or descending 
              order based on the 'order' parameter
            - sortByDateCreated(order): returns a tuple of all records sorted by date created in ascending or descending 
              order based on the 'order' parameter

        Communication with the Model component:
            - QueryDB uses dbConnection to pass its SQL queries to be executed in a safe environment.
    """

    def __init__(self):
        self.db = dbConnection()
    def getAllColumns(self):
        """
        Returns a tuple of all columns in the database.

        Returns:
            A tuple of strings representing the names of all columns in the database.
        """
        return self.db.get("SELECT * FROM product")
        
    def getAllRecordIdentifiers(self):
        """
        Returns a tuple of all record identifiers in the database.

        Returns:
            A tuple of strings representing the record identifiers of all records in the database.
        """
        return self.db.get("SELECT record_identifier FROM product")
    
    def getAllNames(self):
        """
        Returns a tuple of all names in the database.

        Returns:
            A tuple of strings representing the names of all records in the database.
        """
        return self.db.get("SELECT name FROM product")

    def getAllUseByDate(self):
        """
        Returns a tuple of all use by dates in the database.

        Returns:
            A tuple of strings representing the use by dates of all records in the database.
        """
        return self.db.get("SELECT use_by_date FROM product")

    def getAllDateCreated(self):
        """
        Returns a tuple of all dates created in the database.

        Returns:
            A tuple of strings representing the dates created of all records in the database.
        """        
        return self.db.get("SELECT date_created FROM product")
    
    def sortByIdentifier(self, order):
        """
        Returns a tuple of all records sorted by record identifier.

        Args:
            order (str): A string representing the order in which to sort the records. Must be either 'asc' or 'desc'.

        Returns:
            A tuple of dictionaries representing the sorted records, with each dictionary containing the data for a
            single record.
        """
        try:
            if order.lower() == "desc":
                return self.db.get("SELECT * FROM product ORDER BY record_identifier DESC")
            elif order.lower() == "asc":
                return self.db.get("SELECT * FROM product ORDER BY record_identifier;")
            else:
                raise ValueError("Invalid order value. Must be 'asc' or 'desc'.")
        except ValueError as ve:
            print("Error: please only provide desc or asc for order", ve)
            
    def sortByName(self, order):
        """
        Sorts the products in the database by name in ascending or descending order.

        Args:
            order (str): The order in which to sort the products. Must be "asc" or "desc".

        Returns:
            tuple: A tuple of dictionaries representing the sorted products.

        Raises:
            ValueError: If order is not "asc" or "desc".
        """
        try:
            if order.lower() == "desc":
                return self.db.get("SELECT * FROM product ORDER BY name DESC")
            elif order.lower() == "asc":
                return self.db.get("SELECT * FROM product ORDER BY name;")
            else:
                raise ValueError("Invalid order value. Must be 'asc' or 'desc'.")
        except ValueError as ve:
            print("Error: please only provide desc or asc for order", ve)
            
    def sortByUseByDate(self, order):
        """
        Sorts the products in the database by use-by date in ascending or descending order.

        Args:
            order (str): The order in which to sort the products. Must be "asc" or "desc".

        Returns:
            tuple: A tuple of dictionaries representing the sorted products.

        Raises:
            ValueError: If order is not "asc" or "desc".
        """
        try:
            if order.lower() == "desc":
                return self.db.get("SELECT * FROM product ORDER BY use_by_date DESC")
            elif order.lower() == "asc":
                return self.db.get("SELECT * FROM product ORDER BY use_by_date;")
            else:
                raise ValueError("Invalid order value. Must be 'asc' or 'desc'.")
        except ValueError as ve:
            print("Error: please only provide desc or asc for order", ve)

    def sortByDateCreated(self, order):
        """
        Sorts the products in the database by creation date in ascending or descending order.

        Args:
            order (str): The order in which to sort the products. Must be "asc" or "desc".

        Returns:
            tuple: A tuple of dictionaries representing the sorted products.

        Raises:
            ValueError: If order is not "asc" or "desc".
        """
        try:
            if order.lower() == "desc":
                return self.db.get("SELECT * FROM product ORDER BY date_created DESC")
            elif order.lower() == "asc":
                return self.db.get("SELECT * FROM product ORDER BY date_created;")
            else:
                raise ValueError("Invalid order value. Must be 'asc' or 'desc'.")
        except ValueError as ve:
            print("Error: please only provide desc or asc for order", ve)
                        
