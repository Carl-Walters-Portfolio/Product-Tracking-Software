import os
import io
from schema import Schema, And, Use, Regex
import datetime


class ClientSideValidation:
    """
    Provides methods to perform client-side validation on user input.

    This class is used to ensure that user input meets the expected format and data type requirements,
    and to provide feedback to the user when their input does not meet these requirements.

    Attributes:
        None

    Methods:
        nameValidation(name): Validates that the provided name consists only of alphabetical letters and spaces.
        sellByDateValidation(date): Validates that the provided date is in the format 'day-month-year' and can be parsed as a date.
        recordIdentifierValidation(recordIdentifier): Validates that the provided record identifier is an integer.
    """
    
    def nameValidation(self, name):
        """
        Validates that the provided name consists only of alphabetical letters and spaces.

        This method uses the `Schema` class from the `schema` module to define a validation schema
        that requires the input to be a string containing only alphabetical letters and spaces.

        Args:
            name (str): The name to validate.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        try:
            schema = Schema(And(str, Regex(r'^[a-zA-Z\s]+$')))
            schema.validate(name)
            return True
        except:
            print("Name: must be alphabetical letters only.")
            return False
        
    def sellByDateValidation(self, date):
        """
        Validates that the provided date is in the format 'day-month-year' and can be parsed as a date.

        This method uses the `Schema` class from the `schema` module to define a validation schema
        that requires the input to be a string containing a date in the format 'day-month-year',
        which can be parsed as a date using the `datetime` module.

        Args:
            date (str): The date to validate.

        Returns:
            bool: True if the date is valid, False otherwise.
        """
        try:
            schema = Schema(And(str, Use(lambda s: datetime.datetime.strptime(s, '%d-%m-%Y').date())))
            schema.validate(date)
            return True
        except:
            print("Date: must be in year-month-day format for exmaple '10-20-2033'")
            return False
        
        
        
    def recordIdentifierValidation(self, recordIdentifier):
        """
        Validates that the provided record identifier is an integer.

        This method uses the `Schema` class from the `schema` module to define a validation schema
        that requires the input to be an integer.

        Args:
            recordIdentifier (int): The record identifier to validate.

        Returns:
            bool: True if the record identifier is valid, False otherwise.
        """
        try:
            schema = Schema(int)
            schema.validate(recordIdentifier)
            return True
        except:
            print("Record Identifier: must be a whole number")
            return False