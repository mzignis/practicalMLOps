from pathlib import Path
from joblib import load
import numpy as np

from flask import Flask, render_template, redirect, request, url_for


# -------------- library code -------------- #
def say_hello(username: str = "World"):
    return f'<p>Hello {username}!</p>\n'


# -------------- application code -------------- #
application = Flask(__name__)


@application.route('/')
def index():
    return say_hello()


@application.route('/<model_name>')
def model(model_name: str):
    models_dirpath = Path('models') / 'models'
    models = [model.name.split('.')[0] for model in models_dirpath.iterdir()]
    if model_name not in models:
        return f'<p>Model "{model_name}" not found. Available models: {", ".join(models)}</p>\n'
    else:
        model = load(models_dirpath / f'{model_name}.joblib')
        return say_hello(f"{model}")


@application.route('/<model_name>/predict', methods=['GET'])
def model_predict_get(model_name: str):
    models_dirpath = Path('models') / 'models'
    models = [model.name.split('.')[0] for model in models_dirpath.iterdir()]
    if model_name not in models:
        return f'<p>Model "{model_name}" not found. Available models: {", ".join(models)}</p>\n'

    return render_template('predict.html', model_name=model_name)


@application.route('/<model_name>/predict', methods=['POST'])
def predict(model_name: str):

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    ds = np.array([data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']])
    models_dirpath = Path('models') / 'models'
    model = load(models_dirpath / f'{model_name}.joblib')
    prediction_result = {
        'model_name': model_name,
        'output': model.predict(ds.reshape(1, -1))[0]
    }
    return redirect(url_for('results', model_name=model_name, result=prediction_result['output']))


@application.route('/<model_name>/results')
def results(model_name):
    result = request.args.get('result')
    return render_template('results.html', model_name=model_name, result=result)


# -------------- main -------------- #
if __name__ == "__main__":
    import os
    host = os.environ.get('HOST', '127.0.0.1')
    application.run(host=host)
