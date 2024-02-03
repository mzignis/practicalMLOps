import requests


def test_add():
    assert requests.get('http://127.0.0.1:5000').status_code == 200
    assert requests.get('http://127.0.0.1:5000').text == 'Hello world!'
