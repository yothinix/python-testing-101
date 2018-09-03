from datetime import datetime

from flask import jsonify, Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/create')
def create_budget():
    data = request.get_json()
    amount = data['amount']
    date = data.get('date', datetime.now())

    return jsonify(
        dict(
            amount=amount,
            date=date
        )
    )
