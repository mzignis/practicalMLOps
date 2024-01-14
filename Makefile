install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest -vv test_main.py

docker-build:
	docker build -t practical-mlops .

docker-run:
	docker run -p 8000:8000 practical-mlops