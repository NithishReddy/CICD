
from unittest import TestCase
import unittest
from unittest.mock import MagicMock
from exceptions import InvalidInput, DivisionByZero

class Calculator:
    
    @staticmethod
    def addition(var1, var2):
        return var1 + var2

    @staticmethod
    def subtraction(var1, var2):
        return var1 - var2
    
    @staticmethod
    def multiplication(var1, var2):
        return var1 * var2
    
    @staticmethod
    def division(var1, var2):
        
        if var2 == 0:
            raise DivisionByZero(message = 'Division with Zero')
        
        return var1/var2
    
    @staticmethod
    def perform_operation(operator, var1, var2):
        if var1 is None or var2 is None or type(var1) == str or type(var2) == str:
            raise InvalidInput(message = "please enter valid values")

        if operator == '+':
            return Calculator.addition(var1, var2)
        elif operator == '-':
            return Calculator.subtraction(var1, var2)
        elif operator == '*':
            return Calculator.multiplication(var1, var2)
        elif operator == '/':
            return Calculator.division(var1, var2)
        else:
            raise InvalidInput(message = "Dont support other calculations")

