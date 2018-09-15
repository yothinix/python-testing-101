from contextlib import ExitStack
from unittest import TestCase
from unittest.mock import patch, Mock, call

from freezegun import freeze_time

from get_random import get_person, get_random, get_starship, create_planet


class TestGetRandom(TestCase):

    @freeze_time('2018-09-15')
    @patch('get_random.token_hex', return_value='random')
    def test_get_random_should_return_id_and_random_and_current_time(
        self,
        mock_random
    ):
        id = 1
        actual = get_random(id)
        self.assertEqual(actual, '1 - random - 2018-09-15T00:00:00')

    def test_get_random_with_context(self):
        id = 1

        with patch('get_random.token_hex', return_value='random'):
            with freeze_time('2018-09-15'):
                actual = get_random(id)

        self.assertEqual(actual, '1 - random - 2018-09-15T00:00:00')

    def test_get_random_with_exit_stack(self):
        id = 1

        with ExitStack() as stack:
            stack.enter_context(patch('get_random.token_hex', return_value='random'))
            stack.enter_context(freeze_time('2018-09-15'))

            actual = get_random(id)

        self.assertEqual(actual, '1 - random - 2018-09-15T00:00:00')

    def test_get_random_with_exit_stack_complex(self):
        id = 1
        mock_list = [
            patch('get_random.token_hex', return_value='random'),
            freeze_time('2018-09-15')
        ]

        with ExitStack() as stack:
            [stack.enter_context(mock) for mock in mock_list]

            actual = get_random(id)

        self.assertEqual(actual, '1 - random - 2018-09-15T00:00:00')

    def test_get_random_should_call_token_hex_with_16(self):
        id = 1

        with ExitStack() as stack:
            mock_token_hex = stack.enter_context(
                patch('get_random.token_hex', return_value='random')
            )
            stack.enter_context(freeze_time('2018-09-15'))

            get_random(id)

        mock_token_hex.assert_called_once_with(16)


class TestGetPerson(TestCase):
    def mock_response(self, status_code=200, json={}):
        return Mock(
            status_code=status_code,
            json=Mock(
                return_value=json
            )
        )

    def test_get_person_should_return_person(self):
        expected = {
            'name': 'Luke Skywalker'
        }

        with patch('get_random.requests.get') as mock_request:
            mock_request.return_value = self.mock_response(json=expected)
            actual = get_person()

        self.assertEqual(actual, expected)

    def test_get_person_shoud_return_empty_dict_when_status_code_is_not_ok(self):
        expected = {}

        with patch('get_random.requests.get') as mock_request:
            mock_request.return_value = self.mock_response(status_code=400)
            actual = get_person()

        self.assertEqual(actual, expected)

    def test_get_person_should_make_request_with_url(self):
        url = 'https://swapi.co/api/people/1/'

        with patch('get_random.requests.get') as mock_request:
            mock_request.return_value = self.mock_response(status_code=400)
            get_person()

        mock_request.assert_called_once_with(url)


class TestGetStarship(TestCase):
    def mock_response(self, status_code=200, json={}):
        return Mock(
            status_code=status_code,
            json=Mock(
                return_value=json
            )
        )

    def test_get_starship_should_make_2_request(self):
        url1 = 'https://swapi.co/api/starships/1/'
        url2 = 'https://swapi.co/api/starships/2/'

        with patch('get_random.requests.get') as mock_request:
            mock_request.return_value = self.mock_response()
            get_starship()

        mock_request.assert_has_calls([
            call(url1),
            call(url2),
        ], any_order=False)


class TestCreatePlanet(TestCase):
    def test_create_planet_should_create_two_planet(self):
        url = 'https://swapi.co/api/planets/'
        planets = [
            {'name': 'Tatooin'},
            {'name': 'Naboo'}
        ]
        expected = [
            {'id': 1, 'name': 'Tatooin'},
            {'id': 2, 'name': 'Naboo'}
        ]

        with patch('get_random.requests.post') as mock_request:
            mock_request.side_effect = expected
            actual = create_planet()

        self.assertEqual(actual, expected)
        mock_request.assert_has_calls([
            call(url, json=planets[0]),
            call(url, json=planets[1])
        ])
