from datetime import datetime
from secrets import token_hex

import requests


def get_random(id):
    random = token_hex(16)
    current_time = datetime.now().isoformat()
    return f'{id} - {random} - {current_time}'


def get_person():
    url = 'https://swapi.co/api/people/1/'
    response = requests.get(url)

    # try response.ok naja
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def get_starship():
    url1 = 'https://swapi.co/api/starships/1/'
    url2 = 'https://swapi.co/api/starships/2/'

    st_1 = requests.get(url1)
    st_2 = requests.get(url2)

    return st_1, st_2


def create_planet():
    url = 'https://swapi.co/api/planets/'
    planets = [
        {'name': 'Tatooin'},
        {'name': 'Naboo'}
    ]

    created = []
    for planet in planets:
        response = requests.post(url, json=planet)
        created.append(response)

    return created
