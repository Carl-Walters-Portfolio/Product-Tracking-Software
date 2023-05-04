
import os
import io
from schema import Schema, And, Use, Regex
import datetime


class SeverSideValidation:
    """
    Provides methods to perform server-side validation on user input.

    This class is used to ensure that user input meets the expected format and data type requirements,
    and to provide feedback to the user when their input does not meet these requirements. And is used by the
    controller WriteController to proivde this class side validatoin

    Methods:
        - nameValidation(name): Validates that the provided name consists only of alphabetical letters and spaces.
        - sellByDateValidation(date): Validates that the provided date is in the format 'day-month-year' and is a valid date.
        - recordIdentifierValidation(recordIdentifier): Validates that the provided record identifier is a whole number.
    """
    def nameValidation(self, name):
        """
        Validates that the provided name consists only of alphabetical letters and spaces.

        This method uses regular expressions to validate that the input consists only of alphabetical letters and spaces.

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
            print("Name: must be alphabetical letters only")
            return False
        
    def sellByDateValidation(self, date):
        """
        Validates that the provided date is in the format 'day-month-year' and is a valid date.

        This method uses the `datetime` module to validate that the input is in the format 'day-month-year'
        and is a valid date.

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
        Validates that the provided record identifier is a whole number.

        This method validates that the input is a whole number.

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
        
# sv = SeverSideValidation()

# name = sv.nameValidation("dddidkd")
# date = sv.sellByDateValidation("2033-03-02")
# riv = sv.recordIdentifierValidation(1)
