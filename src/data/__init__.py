from sklearn.datasets import load_iris

dataset = load_iris()

data = dataset.data
target = dataset.target
names = dataset.target_names
feature_names = dataset.feature_names
print(feature_names)
