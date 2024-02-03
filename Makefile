install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C application.py

test:
	python -m pytest -vv test_main.py

docker-build:
	docker build -t practical-mlops .

docker-run:
	docker run -p 127.0.0.1:5000:5000 -e HOST=0.0.0.0 practical-mlops

docker-ecr-push:
	aws ecr get-login-password --region eu-north-1 --profile marek.zalecki.256 | docker login --username AWS --password-stdin 211125791844.dkr.ecr.eu-north-1.amazonaws.com
	docker build -t practical-mlops .
	docker tag practical-mlops:latest 211125791844.dkr.ecr.eu-north-1.amazonaws.com/practical-mlops:latest
	docker push 211125791844.dkr.ecr.eu-north-1.amazonaws.com/practical-mlops:latest

eb-init:
	eb init -p python-3.11 practocal-mlops-flask-hello-world --profile marek.zalecki.256 --region eu-north-1

eb-create:
	eb create practocal-mlops-flask --region eu-north-1 --profile marek.zalecki.256

eb-deploy:
	eb deploy practocal-mlops-flask --region eu-north-1 --profile marek.zalecki.256
