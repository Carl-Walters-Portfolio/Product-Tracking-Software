import sys
import os

# Add the parent directory of the 'controller' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'model' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model import dbConnection, QueryDB

class ReadController():
    """
    The ReadController class handles the communication between the view and model components of the
    application. It provides methods for retrieving and sorting data from the database using the QueryDB
    class from within the model 
    
    Communication with the View component:
        - The ReadController communicate directly with the View component. Providing
          methods for retrieving and sorting data from the database that can be used by the View component
          to display the data to the user.

    Communication with the controller component:
        - The ReadController does not need to communicate directly directly with any other components within 
        the controller
          
    Communication with the Model component:
        - The ReadController initializes an instance of the QueryDB model component in its constructor.
        - The ReadController calls the following methods on the QueryDB instance to retrieve data from
          the database:
            - getAllColumns(): returns a list of all columns in the database
            - getRecordIdentifier(): returns a list of all record identifiers in the database
            - getAllNames(): returns a list of all names in the database
            - getAllUseByDate(): returns a list of all use by dates in the database
            - getAllDateCreated(): returns a list of all dates created in the database
            - sortByIdentifier(order): returns a list of all records sorted by record identifier in ascending
              or descending order based on the 'order' parameter
            - sortByName(order): returns a list of all records sorted by name in ascending or descending order
              based on the 'order' parameter
            - sortByUseByDate(order): returns a list of all records sorted by use by date in ascending or
              descending order based on the 'order' parameter
            - sortByDateCreated(order): returns a list of all records sorted by date created in ascending or
              descending order based on the 'order' parameter
    """
    
    def __init__(self):
        """
        Initializes an instance of the QueryDB model component.
        """
        self.queryDb = QueryDB()

    def getAllColumns(self):
        """
        Returns a list of all columns in the database.

        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Returns:
            A list of strings representing the names of all columns in the database.
        """
        return self.queryDb.getAllColumns()
        
    def getAllRecordIdentifiers(self):
        """
        Returns a tuple of all record identifiers in the database.

        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Returns:
            A tuple of strings representing the record identifiers of all records in the database.
        """
        return self.queryDb.getRecordIdentifier()
        
    def getAllNames(self):
        """
        Returns a tuple of all names in the database.

        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Returns:
            A tuple of strings representing the names of all records in the database.
        """
        return self.queryDb.getAllNames()

    def getAllUseByDate(self):
        """
        Returns a tuple of all use-by dates in the database.

        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Returns:
            A tuple of strings representing the use-by dates of all records in the database.
        """
        return self.queryDb.getAllUseByDate()

    def getAllDateCreated(self):
        """
        Returns a tuple of all dates created in the database.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Returns:
            A tuple of strings representing the dates created of all records in the database.
        """
        return self.queryDb.getAllDateCreated()
    
    def sortByIdentifier(self, order):
        """
        Returns a tuple of all records sorted by record identifier.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Args:
            order (str): A string representing the order in which to sort the records. Must be either 'asc' or 'desc'.

       Returns:
            A tuple of dictionaries representing the sorted records by identifiers, with each dictionary containing the following keys:
            - id (int): The unique identifier for the record.
            - name (str): The name of the product.
            - use_by_date (str): The use-by date of the product.
            - date_created (str): The date the record was created.
        """
        return self.queryDb.sortByIdentifier(order)
            
    def sortByName(self, order):
        """
        Returns a tuple of all records sorted by name.

        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        
        
        Args:
            order (str): A string representing the order in which to sort the records. Must be either 'asc' or 'desc'.

        Returns:
            A tuple of dictionaries representing the sorted records by name, with each dictionary containing the following keys:
            - id (int): The unique identifier for the record.
            - name (str): The name of the product.
            - use_by_date (str): The use-by date of the product.
            - date_created (str): The date the record was created.
        """
        return self.queryDb.sortByName(order)
    
    def sortByUseByDate(self, order):
        """
        Returns a tuple of all records sorted by use-by date.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Args:
            order (str): A string representing the order in which to sort the records. Must be either 'asc' or 'desc'.

        Returns:
            A tuple of dictionaries representing the sorted records by use by date, with each dictionary containing the following keys:
            - id (int): The unique identifier for the record.
            - name (str): The name of the product.
            - use_by_date (str): The use-by date of the product.
            - date_created (str): The date the record was created.
        """
        return self.queryDb.sortByUseByDate(order)

    def sortByDateCreated(self, order):
        """
        Returns a tuple of all records sorted by date created.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Args:
            order (str): A string representing the order in which to sort the records. Must be either 'asc' or 'desc'.

        Returns:
            A tuple of dictionaries representing the sorted records by date created, with each dictionary containing the following keys:
            - id (int): The unique identifier for the record.
            - name (str): The name of the product.
            - use_by_date (str): The use-by date of the product.
            - date_created (str): The date the record was created.
        """
        return self.queryDb.sortByDateCreated(order)
                          
# read = ReadController()
# x = read.getAllColumns()

