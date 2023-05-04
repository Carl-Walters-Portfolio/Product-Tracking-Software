from db_connection import dbConnection

class WriteToDb:
    """
    The WriteToDb class provides methods for adding new products and deleting existing products from the database. It
    uses the dbConnection class to interact with the database.
    
    Communication with the View component:
        - The WriteToDb class does not communicate directly with the View component. Instead, it provides methods for
          modifying the data in the database, which can be used by the controller component to update the data.
          
    Communication with the Controller component:
    - The WriteController calls the following methods on the WriteToDb instance to retrieve or delete data from the database:
        - addOneNewProduct(): Adds a new product to the database.
        - deleteBySingleRecordIdentifier():  Deletes a product from the database based on its record identifier.
          
    Communication with the Model component:
        - WriteToDb uses dbConnection to pass its SQL queries to be executed in a safe environment.

    """
    def __init__(self):
        """
        Initializes the WriteToDb object with an instance of the dbConnection class.
        """
        self.db = dbConnection()
        
    def addOneNewProduct(self, name, useByDate):
        """
        Adds a new product to the database.

        Args:
            name (str): The name of the new product.
            useByDate (str): The use-by date of the new product.
        """
        data = (name, useByDate)

        sql = "INSERT INTO product (name, use_by_date) VALUES (?, ?)"
        
        x = self.db.set(sql, data)
        print(x, "x")
        return x

    def deleteBySingleRecordIdentifier(self, recordIdentifier):
        """
        Deletes a product from the database based on its record identifier.

        Args:
            recordIdentifier (str): The record identifier of the product to be deleted.
        """
        data = "DELETE FROM product WHERE record_identifier = ?"
        sql = (recordIdentifier,)
        y = self.db.set(data, sql)
        
        print(y, "y")
        return y
        
# cursor.execute())


# w = WriteToDb()
# w.addNewProduct("food item", "2024-02-11")
# w.deleteByID(1)