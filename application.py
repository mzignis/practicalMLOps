from flask import Flask


# -------------- library code -------------- #
def say_hello(username: str = "World"):
    return f'<p>Hello {username}! It is a new version</p>\n'


# -------------- application code -------------- #
application = Flask(__name__)


@application.route('/')
def index():
    return say_hello()


# -------------- main -------------- #
if __name__ == "__main__":
    import os
    host = os.environ.get('HOST', '127.0.0.1')
    application.run(host=host)
