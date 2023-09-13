import json
import requests

URL = "http://127.0.0.1:8000/create/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)

    r = requests.get(url=URL, data=json_data)

    data = r.json()

    print(data)

# get_data(1)


def post_data():
    data = {
        'name': 'Anamika',
        'roll': 105,
        'city': 'Derhadoon',
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id':  5,
        'name': 'raja',
        'city': 'monishco',

    }

    json_data = json.dumps(data)

    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)

update_data()