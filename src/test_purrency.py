"""
Tests for the parser
"""

from unittest import TestCase
from purrency import Purrency
from decimal import Decimal


class TestPurrency(TestCase):

    def setUp(self):
        self.expected_test_dollar = {'amount': Decimal(200.0), 'symbol': '$'}
        test_dollar = '$200.00'

        self.purr = Purrency(test_dollar)
        self.parsed_dollar = self.purr.parse()

    def test_dollar(self):
        """
        Parse USD
        """
        self.assertEqual(self.expected_test_dollar, self.parsed_dollar)
