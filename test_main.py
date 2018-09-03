from unittest import TestCase

from main import app, hello


class TestHello(TestCase):
    def test_hello_should_return_message(self):
        expected = 'Hello World!'
        actual = hello()
        self.assertEqual(actual, expected)


class TestCreateBudgetView(TestCase):
    def test_create_budget_should_return_data(self):
        expected = {'amount': 123, 'date': '2018-09-03T00:00:00'}
        budget = {'amount': 123, 'date': '2018-09-03T00:00:00'}

        with app.test_client() as client:
            response = client.post('/create', json=budget)
            actual = response.get_json()

        self.assertDictEqual(actual, expected)
