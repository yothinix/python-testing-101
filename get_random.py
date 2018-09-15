from datetime import datetime
from secrets import token_hex


def get_random(id):
    random = token_hex(16)
    current_time = datetime.now().isoformat()
    return f'{id} - {random} - {current_time}'
