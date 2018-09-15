from unittest import TestCase
from unittest.mock import patch

from freezegun import freeze_time

from get_random import get_random


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
