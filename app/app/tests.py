"""
Sample test file for the app.
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test that the add function adds numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that the subtract function subtracts numbers together."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, -5)