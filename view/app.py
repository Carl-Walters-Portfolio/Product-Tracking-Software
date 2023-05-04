from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtWidgets, QtGui, QtCore

from PyQt6.QtGui import  *
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtMultimedia import *
from PyQt6 import QtMultimedia
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets

from PyQt6.QtWidgets import (QWidget, QTabWidget, QGridLayout, QApplication, QMainWindow, QStatusBar, QTableView)
from PyQt6.QtCore import (Qt, QTimer, QAbstractTableModel, QThread, QVariant, QObject, QRect, pyqtSlot, pyqtSignal)

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import *

import os

# x = json.loads(document_name)

import time
import random
import datetime
import json


state = True
import sys

# Add the parent directory of the 'controller' and 'model folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'controller')))

from controller.read_controller import ReadController
from controller.write_controller import WriteController

from client_side_validation import ClientSideValidation
from PyQt6.QtGui import QStandardItemModel, QStandardItem



class MainWindow(QMainWindow):
    """
    A class that implerments 'view/GUI/mainwindow.ui' and represents this .ui in a main window of the product tracker app 
    using PyQt6.
    
    Communication with the View component:
        - ClientSideValidation is utilised to check suer input
        - 'view/GUI/mainwindow.ui' is loaded into this MainWindow
          
    Communication with the Controller component:
        - The controller allows business logic to be added such that UI concerns are loosely coupled.
        - The class provides the following methods within the controller 
            - addOneNewProduct(name, useByDate): Adds a new product to the database, if the server-side validation
            using the SeverSideValidation component passes. Returns the result of the writeToDb.addOneNewProduct()
            method.
            - deleteBySingleRecordIdentifier(recordIdentifier): Deletes a product from the database based on the
            record identifier, if the server-side validation using the SeverSideValidation component passes. Returns
            the result of the writeToDb.deleteBySingleRecordIdentifier() method.
          
    Communication with the Model component:
        -The view layer and, by extension, this MainWindow has no direct communication with the model layer component.   
                 
    Attributes from view and controller:
        clientSideValidation (ClientSideValidation): An instance of the ClientSideValidation class.
        readController (ReadController): An instance of the ReadController class.
        writeController (WriteController): An instance of the WriteController class.
        sortByThis (str): The current sorting criteria.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the MainWindow class."""

        super(MainWindow, self).__init__(*args, **kwargs)
        # from within view module
        self.clientSideValidation = ClientSideValidation()
        
        # Controller
        self.readController = ReadController()
        self.writeController = WriteController()
        
        # Load GUI file
        uic.loadUi('view/GUI/mainwindow.ui', self)
        
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        
        self.productMenu.setCurrentIndex(0)

        self.setWindowTitle("Product tracker")
        
        self.addNewProductButton.pressed.connect(lambda: self.addNewProduct())
        self.removeByRecordIdentifierButton.pressed.connect(lambda: self.deleteProductByRecordIdentifier())
        self.sortByXDropdown.currentTextChanged.connect(self.sortBy)
        
        self.sortByThis = "Use by date"

        self.loadTableView()
        
    def addNewProduct(self):
        """
        Adds a new product to the database.

        Raises:
            ValueError: If there is an issue with the user input.
        """
        # get user input
        try:
            name = str(self.nameLineEdit.text()).strip()
            useByDate = str(self.useByDateLineEdit.text()).strip()

                
            # name error user feedback
            if self.clientSideValidation.nameValidation(name) == False:
                self.customUiError("Please try letters and\n spaces only.", "nameError")

            # use by date error user feedback
            if self.clientSideValidation.sellByDateValidation(useByDate) == False:
                self.customUiError("year-month-day format for exmaple\n'25-05-2033' including hyphens", "useByDateError")
                
            # controller takes care of addeding new product to .db
            if self.clientSideValidation.nameValidation(name) == True and self.clientSideValidation.sellByDateValidation(useByDate) == True:
                self.writeController.addOneNewProduct(name, useByDate)
                self.customUiError("", "nameError")
                self.customUiError("", "useByDateError")

                self.loadTableView()
            else:
                # self.customUiError("The client validation is looking\nfor only alphabetical letters only.")
                print("The client validation is looking\nfor only alphabetical letters only.")
                
        except ValueError:
            print(ValueError)
            

    def deleteProductByRecordIdentifier(self):
        """
        Deletes a product from the database by its record identifier.

        Raises:
            ValueError: If there is an issue with the user input.
        """
        try:
            recordIdentifier = int(self.recordIdentifierError.text())
            
            if self.clientSideValidation.recordIdentifierValidation(recordIdentifier) == False:
                self.customUiError("Please enter numbers only.", "ridError")
            
            # controller takes care of addeding new product to .db
            if self.clientSideValidation.recordIdentifierValidation(recordIdentifier) == True:
                self.writeController.deleteBySingleRecordIdentifier(recordIdentifier)
                self.customUiError("", "ridError")

                self.loadTableView()
            else:
                print("not work")
        
        except ValueError:
            print(ValueError)
            # int to str may create an error before customUiError method could be used above
            self.customUiError("Please enter numbers only.", "ridError")

        
    def sortBy(self, sortingCriteria):
        """
        Sorts the table view by the specified criteria.

        Args:
            sortingCriteria (str): The sorting criteria selected by the user.
        """
        if sortingCriteria == "Use by date (ASC)":
            self.sortByThis = "Use by date (ASC)"
        elif sortingCriteria == "Date created (ASC)":
            self.sortByThis = "Date created (ASC)"
        elif sortingCriteria == "Name(ASC)":
            self.sortByThis = "Name(ASC)"
        elif sortingCriteria == "Use by date (DESC)":
            self.sortByThis = "Use by date (DESC)"
        elif sortingCriteria == "Date created (DESC)":
            self.sortByThis = "Date created (DESC)"
        elif sortingCriteria == "Name(DESC)":
            self.sortByThis = "Name(DESC)"

        print("Sorted by: {sortingCriteriaText}".format(sortingCriteriaText=sortingCriteria))

        self.loadTableView()
        
    def loadTableView(self):
        """
        Loads the data into the table view and applies any sorting criteria.

        Retrieves the data from the database and populates the table view accordingly.
        """
        qItem = QStandardItemModel()
        self.tableView.setModel(qItem)

        headers = ["Record Identifier (RID)", "Name", "Use By Date", "Date Created"]
        qItem.setHorizontalHeaderLabels(headers)
        
        if self.sortByThis == "Use by date (ASC)":
            allColumns = self.readController.sortByUseByDate("asc")
        elif self.sortByThis == "Date created (ASC)":
            allColumns = self.readController.sortByDateCreated("asc")
        elif self.sortByThis == "Name(ASC)":
            allColumns = self.readController.sortByName("asc")
        elif self.sortByThis == "Use by date (DESC)":
            allColumns = self.readController.sortByUseByDate("desc")
        elif self.sortByThis == "Date created (DESC)":
            allColumns = self.readController.sortByDateCreated("desc")
        elif self.sortByThis == "Name(DESC)":
            allColumns = self.readController.sortByName("desc")
        else:
            # makes sure table view has values even if sorting failed
            allColumns = self.readController.getAllColumns()
            print("Sorting Failed")

         # Populate table view with retrieved data from database/products.db
        for row in allColumns:
            record_identifier = QStandardItem(str(row[0]))
            name_item = QStandardItem(str(row[1]))
            use_by_date_item = QStandardItem(row[2])
            date_created_item = QStandardItem(row[3])
            qItem.appendRow([record_identifier, name_item, use_by_date_item, date_created_item])
            
        # Resize columns and rows to fit the data
        self.tableView.resizeColumnsToContents()
        self.tableView.resizeRowsToContents()

    def customUiError(self, message, location):
        """
        Displays an error message in the appropriate location on the UI.

        Args:
            message (str): The error message to display.
            location (str): The location on the UI where the error message should be displayed.
                Can be one of "nameError", "useByDateError", or "ridError".
        """
        if location == "nameError":
            self.nameError.setText(message)
        elif location == "useByDateError":
            self.useByDateError.setText(message)
        elif location == "ridError":
            self.ridError.setText(message)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
state = False
