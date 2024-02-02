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

docker-ecr-push:
	aws ecr get-login-password --region eu-north-1 --profile marek.zalecki.256 | docker login --username AWS --password-stdin 211125791844.dkr.ecr.eu-north-1.amazonaws.com
	docker build -t practical-mlops .
	docker tag practical-mlops:latest 211125791844.dkr.ecr.eu-north-1.amazonaws.com/practical-mlops:latest
	docker push 211125791844.dkr.ecr.eu-north-1.amazonaws.com/practical-mlops:latest
