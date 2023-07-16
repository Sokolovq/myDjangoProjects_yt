from django.test import TestCase
from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(5, 15, '+')
        self.assertEqual(result, 20)

    def test_minus(self):
        result = operations(5, 15, '-')
        self.assertEqual(result, -10)

    def test_multiply(self):
        result = operations(5, 15, '*')
        self.assertEqual(result, 75)
