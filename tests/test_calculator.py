from unittest import TestCase
import unittest
from unittest.mock import MagicMock
from example import Calculator
from exceptions import InvalidInput, DivisionByZero

class CalculatorTest(TestCase):
    def setUp(self):
        pass

        """ 
        We are using mocking function to mock the response of the addition function in Calculator
        """
    def test_perform_operation1(self):
        Calculator.addition = MagicMock(return_value=6)
        self.assertEqual(Calculator.perform_operation('+', 3, 3), 6)
    
    def test_perform_operation2(self):
        Calculator.subtraction = MagicMock(return_value=6)
        self.assertEqual(Calculator.perform_operation('-', 9, 3), 6)
        
    def test_perform_operation3(self):
        self.assertEqual(Calculator.perform_operation('*', 9, 3), 27)
    
    def test_perform_operation4(self):
        with self.assertRaises(DivisionByZero):
            Calculator.perform_operation('/', 9, 0)
    
    def test_perform_operation5(self):
        self.assertEqual(Calculator.perform_operation('/', 9, 3), 3)
        
    def test_perform_operation6(self):
        with self.assertRaises(InvalidInput):
            Calculator.perform_operation('%', 9, 3)