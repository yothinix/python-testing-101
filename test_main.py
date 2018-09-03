from unittest import TestCase

from main import hello


class TestHello(TestCase):
    def test_hello_should_return_message(self):
        expected = 'Hello World!'
        actual = hello()
        self.assertEqual(actual, expected)
