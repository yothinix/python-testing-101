from unittest import TestCase


def fizzbuzz(number):
    if type(number) != int:
        return 'Not a number.'
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number


class TestFizzbuzz(TestCase):
    def test_one_should_return_one(self):
        number = 1
        actual = fizzbuzz(number)
        self.assertEqual(actual, number)

    def test_two_should_return_two(self):
        number = 2
        actual = fizzbuzz(number)
        self.assertEqual(actual, number)

    def test_three_should_return_fizz(self):
        number = 3
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Fizz')

    def test_six_should_return_fizz(self):
        number = 6
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Fizz')

    def test_five_should_return_buzz(self):
        number = 5
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Buzz')

    def test_ten_should_return_ten(self):
        number = 10
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Buzz')

    def test_fifteen_should_return_fizzbuzz(self):
        number = 15
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'FizzBuzz')

    def test_thirty_should_return_fizzbuzz(self):
        number = 30
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'FizzBuzz')

    def test_enter_string_should_return_error_message(self):
        number = 'Some string'
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Not a number.')

    def test_enter_bool_should_return_error_message(self):
        number = True
        actual = fizzbuzz(number)
        self.assertEqual(actual, 'Not a number.')
