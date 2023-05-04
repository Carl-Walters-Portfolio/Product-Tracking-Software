import sys
import os

# Add the parent directory of the 'controller' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the 'model' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model import dbConnection, WriteToDb
from server_side_validation import SeverSideValidation

class WriteController():

    """
    The WriteController class handles the communication between the Model and View components. 
    It provides methods for adding and deleting records from the database, and utilizes server-side validation 
    using the ServerSideValidation module.

    Communication with the View component:
        - The WriteController communicates directly with the View component by providing 
        methods for adding and deleting records from the database that can be used by the View 
        component. This allows the user to use the add and delete .ui interface.

    Communication with the controller component:
        - The WriteController communicates directly and implements the ServerSideValidation class to check user input 
        that came from the view layer.
          
    Communication with the Model component:
        - The WriteController class initializes an instance of the WriteToDb model component and the SeverSideValidation
          component in its constructor.
        - The class provides the following methods to interact with the WriteToDb model component:
            - addOneNewProduct(name, useByDate): Adds a new product to the database, if the server-side validation
            using the SeverSideValidation component passes. Returns the result of the writeToDb.addOneNewProduct()
            method.
            - deleteBySingleRecordIdentifier(recordIdentifier): Deletes a product from the database based on the
            record identifier, if the server-side validation using the SeverSideValidation component passes. Returns
            the result of the writeToDb.deleteBySingleRecordIdentifier() method.
    """
    
    def __init__(self):
        """
        Initializes an instance of the WriteToDb model component and the SeverSideValidation component.
        """
        self.writeToDb = WriteToDb()
        self.serverSideValidation = SeverSideValidation()
        
    def addOneNewProduct(self, name, useByDate):
        """
        Adds a new product to the database, if the server-side validation using the SeverSideValidation component
        passes.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Args:
            name (str): The name of the product to be added to the database.
            useByDate (str): The use-by date of the product to be added to the database.

        """
        
        if self.serverSideValidation.nameValidation(name) == True and self.serverSideValidation.sellByDateValidation(useByDate) == True:
            self.writeToDb.addOneNewProduct(name, useByDate)
            
        else:
            print("Sorry, your request to add a product could not be processed please see information on correct formatting above this message.")

    def deleteBySingleRecordIdentifier(self, recordIdentifier):
        """
        Deletes a product from the database based on the record identifier, if the server-side validation using the
        SeverSideValidation component passes.
        
        Business logic could also be placed here, which sets it apart from the queryDb in the model layer.        

        Args:
            recordIdentifier (str): The record identifier of the product to be deleted from the database.
        """
        if self.serverSideValidation.recordIdentifierValidation(recordIdentifier):
            self.writeToDb.deleteBySingleRecordIdentifier(recordIdentifier)
        else:
            print("Sorry, your request to delete a product could not be processed please see information on correct formatting above this message.")
        