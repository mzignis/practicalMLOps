# practicalMLOps

## Setup environment

### Install and activate venv
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install requirements
```bash
make install
```

## ssh-key agent
```bash
eval "$(ssh-agent -s)" 
ssh-add ~/.ssh/id_rsa_priv
```

## Docker
Build and run the docker container
```bash
make docker-build
make docker-run
```

Push docker to ECR
```bash
make docker-ecr-push
```
