import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def train_model(
        model, x_matrix: np.array, y_matrix: np.array, test_size: float = 0.2, random_state: int = 42,
) -> tuple:
    x_train, x_test, y_train, y_test = train_test_split(
        x_matrix, y_matrix, test_size=test_size, random_state=random_state
    )
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    scores = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }

    print(f"Model: {model}")
    print(f'Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}')

    return model, scores


if __name__ == "__main__":
    import json
    from pathlib import Path
    from joblib import dump

    from src.data import data, target
    from src.models import tree, svc, svc_linear

    output_dirpath = Path(__file__).parent.parent.parent / 'models'

    output_models_dirpath = output_dirpath / 'models'
    output_models_dirpath.mkdir(exist_ok=True, parents=True)

    output_scores_dirpath = output_dirpath / 'scores'
    output_scores_dirpath.mkdir(exist_ok=True, parents=True)

    models = [(svc, 'svc'), (svc_linear, 'svc_linear'), (tree, 'tree')]
    for model, model_name in models:
        model_trained, score = train_model(model, data, target)

        output_model_filepath = output_models_dirpath / f'{model_name}.joblib'
        dump(model_trained, output_model_filepath)

        output_score_filepath = output_scores_dirpath / f'{model_name}.json'
        with open(output_score_filepath, 'w') as ff:
            json.dump(score, ff, indent=4)
